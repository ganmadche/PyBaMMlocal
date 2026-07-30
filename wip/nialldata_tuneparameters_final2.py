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
parameter_values.update({"SEI kinetic rate constant [m.s-1]": 2*1e-12*0.002*0.5}) 
parameter_values.update({"SEI growth activation energy [J.mol-1]": 42000.0,
                         "SEI partial molar volume [m3.mol-1]": 9.585e-05*0.25,
                         "SEI resistivity [Ohm.m]": 200000.0
                         })  
# LAM parameters update

parameter_values.update({"Positive electrode LAM constant proportional term [s-1]": 2*0.25*0.5*1.5*0.1/3600,
                         "Negative electrode LAM constant proportional term [s-1]": 2*0.13*0.5*1.5*0.1/3600,
                         
                         "Positive electrode LAM constant exponential term": 2.3,
                         "Negative electrode LAM constant exponential term": 2.3,
                         
                         })






#Plating paremeters update
parameter_values.update({
                        "Lithium plating kinetic rate constant [m.s-1]": 300*5*1e-09*0.001,
                        "Lithium plating transfer coefficient": 0.65,
                        "Dead lithium decay constant [s-1]": 4e-05,
                        
                        })