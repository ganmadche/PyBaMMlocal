#
# Base class for active material volume fraction
#
import pybamm


class BaseModel(pybamm.BaseSubModel):
    """Base class for active material volume fraction

    Parameters
    ----------
    param : parameter class
        The parameters to use for this submodel
    domain : str
        The domain of the model either 'Negative' or 'Positive'
    options : dict
        Additional options to pass to the model

    **Extends:** :class:`pybamm.BaseSubModel`
    """

    def __init__(self, param, domain, options):
        super().__init__(param, domain, options=options)

    def _get_standard_active_material_variables(self, eps_solid):
        param = self.param
        eps_solid_av = pybamm.x_average(eps_solid)

        variables = {
            self.domain + " electrode active material volume fraction": eps_solid,
            "X-averaged "
            + self.domain.lower()
            + " electrode active material volume fraction": eps_solid_av,
        }

        # Update electrode capacity variables
        if self.domain == "Negative":
            L = param.L_n
            c_s_max = param.c_n_max
        elif self.domain == "Positive":
            L = param.L_p
            c_s_max = param.c_p_max

        C = eps_solid_av * L * param.A_cc * c_s_max * param.F / 3600
        variables.update({self.domain + " electrode capacity [A.h]": C})

        # Update other microstructure variables
        # some models (e.g. lead-acid) do not have particles
        if self.options["particle shape"] == "no particles":
            if self.domain == "Negative":
                x = pybamm.standard_spatial_vars.x_n
                a = self.param.a_n(x)
                a_typ = self.param.a_n_typ
            elif self.domain == "Positive":
                x = pybamm.standard_spatial_vars.x_p
                a = self.param.a_p(x)
                a_typ = self.param.a_p_typ
            variables.update(
                {
                    self.domain + " electrode surface area to volume ratio": a,
                    self.domain
                    + " electrode surface area to volume ratio [m-1]": a * a_typ,
                }
            )
            return variables

        else:
            if self.domain == "Negative":
                x = pybamm.standard_spatial_vars.x_n
                R = self.param.R_n(x)
                R_dim = self.param.R_n_dimensional(x * self.param.L_x)
                a_typ = self.param.a_n_typ
            elif self.domain == "Positive":
                x = pybamm.standard_spatial_vars.x_p
                R = self.param.R_p(x)
                R_dim = self.param.R_p_dimensional(x * self.param.L_x)
                a_typ = self.param.a_p_typ

            # Compute dimensional particle shape
            if self.options["particle shape"] == "spherical":
                a_dim = 3 * eps_solid / R_dim
            elif self.options["particle shape"] == "user":
                if self.domain == "Negative":
                    # give dimensional x as an input
                    inputs = {"Through-cell distance (x_n) [m]": x * self.param.L_x}
                    a_dim = pybamm.FunctionParameter(
                        "Negative electrode surface area to volume ratio [m-1]", inputs
                    )
                if self.domain == "Positive":
                    # give dimensional x as an input
                    inputs = {"Through-cell distance (x_p) [m]": x * self.param.L_x}
                    a_dim = pybamm.FunctionParameter(
                        "Positive electrode surface area to volume ratio [m-1]", inputs
                    )

            # Surface area to volume ratio is scaled with a_typ, so that it is equal to
            # 1 when eps_solid and R are uniform in space and time
            a = a_dim / a_typ
            variables.update(
                {
                    self.domain + " particle radius": R,
                    self.domain + " particle radius [m]": R_dim,
                    self.domain + " electrode surface area to volume ratio": a,
                    self.domain
                    + " electrode surface area to volume ratio [m-1]": a_dim,
                }
            )

            return variables

    def _get_standard_active_material_change_variables(self, deps_solid_dt):

        deps_solid_dt_av = pybamm.x_average(deps_solid_dt)

        variables = {
            self.domain
            + " electrode active material volume fraction change": deps_solid_dt,
            "X-averaged "
            + self.domain.lower()
            + " electrode active material volume fraction change": deps_solid_dt_av,
        }

        return variables
