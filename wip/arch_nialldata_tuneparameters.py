
#For tuning with base heat cooling for Niall data only
parameter_values.update({"Total heat transfer coefficient [W.m-2.K-1]": 10.0,})
#thermal parameters update
parameter_values.update({"Negative electrode OCP entropic change [V.K-1]": -0.0002,
                         "Positive electrode OCP entropic change [V.K-1]": -0.0004,
                         "Contact resistance [Ohm]": 0.001,
                         
                        })
def ec_diffusivity(T_amb):
    D_sj = 2.5e-22*4*10*3
    EaD = 10000
    arrhenius = np.exp(EaD / pybamm.constants.R *(1/ 298.15 - 1/ T_amb))
    return D_sj * arrhenius
parameter_values.update({"EC diffusivity [m2.s-1]": ec_diffusivity})
#sei parameters update
parameter_values.update({"SEI kinetic rate constant [m.s-1]": 1e-12*0.002*0.5}) 
parameter_values.update({"SEI growth activation energy [J.mol-1]": 42000.0,
                         "SEI partial molar volume [m3.mol-1]": 9.585e-05*0.4,
                         "SEI resistivity [Ohm.m]": 200000.0
                         })  
# LAM parameters update

parameter_values.update({"Positive electrode LAM constant proportional term [s-1]": 0.25*0.5*1.5*0.1/3600,
                         "Negative electrode LAM constant proportional term [s-1]": 0.13*0.5*1.5*0.1/3600,
                         
                         "Positive electrode LAM constant exponential term": 2.3,
                         "Negative electrode LAM constant exponential term": 2.3,
                         
                         })






#Plating paremeters update
parameter_values.update({
                        "Lithium plating kinetic rate constant [m.s-1]": 1e-09*0.001,
                        "Lithium plating transfer coefficient": 0.65,
                        
                        })

# def graphite_LGM50_diffusivity_Chen2020(sto, T):
#     """
#     LG M50 Graphite diffusivity as a function of stoichiometry, in this case the
#     diffusivity is taken to be a constant. The value is taken from [1].

#     References
#     ----------
#     .. [1] Chang-Hui Chen, Ferran Brosa Planella, Kieran O’Regan, Dominika Gastol, W.
#     Dhammika Widanage, and Emma Kendrick. "Development of Experimental Techniques for
#     Parameterization of Multi-scale Lithium-ion Battery Models." Journal of the
#     Electrochemical Society 167 (2020): 080534.

#     Parameters
#     ----------
#     sto: :class:`pybamm.Symbol`
#        Electrode stoichiometry
#     T: :class:`pybamm.Symbol`
#        Dimensional temperature

#     Returns
#     -------
#     :class:`pybamm.Symbol`
#        Solid diffusivity
#     """

#     D_ref = 3.3e-14
#     E_D_s = 3.03e4
#     # E_D_s not given by Chen et al (2020), so taken from Ecker et al. (2015) instead
#     arrhenius = np.exp(E_D_s / pybamm.constants.R * (1 / 298.15 - 1 / T))

#     return D_ref * arrhenius


# parameter_values.update({
#                         "Negative particle diffusivity [m2.s-1]": graphite_LGM50_diffusivity_Chen2020,
                        
#                         })

