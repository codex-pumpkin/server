### **Chapter 3**

# **Carrying On**

In this chapter, we introduce the different element and control statement lines that Spice allows you to
use, starting with the different types of circuit elements. In particular we discuss inductors, active elements
(diodes and transistors), and transmission lines. We then cover the different types of analyses you can do
with Spice, starting with the most common, the transient analysis, which is introduced in Chapter 2. The
main role of the control statements is to specify these analyses.
Each implementation of Spice differs in the range of elements and control statements used. In this
chapter, we describe those elements and control statements found in all versions of Spice, i.e. those found
in Spice2g6.

##### **3.1 Elements**


Resistors and capacitors are described briefly in Chapter 2. We now look at the other elements, both passive
and active. The most common form of the element is described only. For example, we do not describe how
a temperature dependency could be specified. That sort of detail is found in the reference section (chapters
6 and 7).


**3.1.1** **Inductors and Mutual Inductors**


An example showing an inductor and a mutual inductor is shown below:






#### _5_ _4_









L1 1 2 20nH
13


14 _CHAPTER 3. CARRYING ON_


L2 3 2 40nH
L3 4 5 40nH
K L1 L2 0.90


Note how the ‘dot’ is placed on the first node of each inductor.


**3.1.2** **Active Devices**


Unlike passive devices, such as resistors, active, or semiconductor, devices can not be specified by one or a
few parameter values. To save typing effort a separate .model line is created for every semiconductor device
type that might appear in the circuit. In this part of the tutorial, we do not describe the meaning of the
parameters in the model line. That can be found in the Reference section (chapters 6 and 7). Instead, we
give examples showing how semiconductor devices are inserted into a Spice circuit. We only describe the
bipolar junction diode, bipolar junction transistor, and the MOS field effect transistor. Spice can also be
used to describe junction field effect transistors and Gallium Arsenide but the process is the same.


**Diodes and Bipolar Transistors**


The schematic and partial Spice net-list for a simple TTL inverter is shown in Figure 3.1. Note the following
features in this circuit description:


_•_ The format for bipolar junction transistors is:
Q _name NCollector NBase NEmitter_ [ _NSubstrate_ ] _ModelName_ [ _Area_ ] [OFF]
+ [IC= _Vbe,Vce_ ]
specifying a three terminal device.


_•_ The format for diodes is: D _name n_ 1 _n_ 2 _ModelName_ [ _Area_ ] [OFF] [IC _=VD_ ]
specifying a two terminal device.


_•_ The use of ‘+’s in the model lines to ‘join’ different lines in the file into one line for Spice.


It is also possible to have an ‘area’ parameter in the diode and bipolar transistor element line. This area
parameter is a scale factor, not an absolute measure. An area of ‘1.0’ (which is the default) specifies that the
model parameters are used unchanged. Specifying another area factor causes Spice to change some of the
model parameters to reflect a larger or smaller transistor. An area of ‘2.0’ specifies a situation equivalent to
two transistors operating in parallel.


**MOSFETs**


The MOSFET element line looks quite different than the element line for a bipolar transistor. There are
two major differences. First, the MOSFET is a four terminal device. Three of the terminals (source, drain,
gate) have analogous functions to the three terminals in a bipolar transistor. The current passes between
the drain to the source (analogous to the emitter and collector) and is controlled by the voltage on the gate
(analogous to the base). The fourth terminal is the ‘substrate’ referring to the bulk silicon in which the
transistor sits. For correct functioning, the substrate must be connected to the ground or Vcc node, for
n-channel and p-channel transistors respectively.
The second major difference is that the physical dimensions of the transistor are specified in the model line.
Specifically, the channel length and width, and source and drain perimeters and areas are specified. These are
the actual dimensions, as they appear on the chip. An example is shown in Figure 3.2. This example matches
the usual general model format: M _name NDrain NGate NSsource NBulk ModelName_ [L _=Length_ ] [W _=Width_ ]
+ [AD _=DrainDiffusionArea_ ] [AS _=SourceDiffusionArea_ ]
+ [PD _=DrainPerimeter_ ] [PS _=SourcePerimeter_ ]
+ [OFF] [IC= _VDS, VGS, VBS_ ]


_3.1. ELEMENTS_ 15













**OUT**













Q3 7 4 0 NQ1A
D1 8 7 DPN
Q4 6 3 8 NQ1A
R4 5 6 100


- Model element for NPN Transistor type NQ1A (courtesy Signetics)
.MODEL NQ1A NPN IS= 1.95E-17 BF= 7.03E+01 VAF= 1.80E+01 IKF= 1.80E-02


_(Remainder of model deleted)_


- Model for diode type DPN
.MODEL DPN D(IS= 8.17E-17 RS= 2.85E+01 N= 9.99E-01 CJO= 1.65E-13
+ VJ= 8.01E-01 M= 4.61E-01 EG= 7.99E-01 XTI= 4.00E+00)


Figure 3.1: TTL Circuit Description.


16 _CHAPTER 3. CARRYING ON_

###### **Drain Gate Source**


###### Area = 3.2 pm (‘ad’ and ‘as’)


###### 2


###### 2 micron


###### 0.8 micron



M1 0 1 2 0 nenh l=0.8u w=1.6u ad=3.2p as=3.2p pd=5.2u ad=5.2u


Figure 3.2: Example of a MOSFET element specification.


where [] indicates optional parameters. PSpice supports additional element parameters. (For the full
general format please see the reference catalog.)
Note that though the _drain_ and _source_ have different physical meanings (the _source_ is the source of the
majority carrier – electrons for an n-channel [nmos] device and holes for a p-channel [pmos] device), no error
is produced if they are interchanged in the Spice circuit description. For example, in figure 3.2, using M1 2
1 0 0, produces the same simulation results as using M1 0 1 2 0.
An example of a CMOS digital inverter circuit, together with its Spice model is given in Figure 3.3.
Note the use of the .option line in this example to fix circuit-wide default values for L, W, AD, and AS.


**3.1.3** **Transmission Lines**


Though a transmission line is a four terminal device, two of the terminals are normally set to a common
reference node, an example of which is shown in Figure 3.4. This lossless transmission line model supports
only a single mode of propagation. If the two ‘reference’ terminals (nodes 0 in this example) correspond to
two electrically different nodes in the physical circuit then two modes are excited and two transmission lines
are required in the corresponding Spice description.
If quick simulation times are important then it is necessary to limit the use of small transmission lines.
In a transient simulation the minimum time step does not exceed half the propagation delay of the line.
Smaller time steps result in longer simulation times. If this is a problem, remember that a transmission line
can be safely replaced by the equivalent lumped inductor and capacitor if the length of the line is smaller
than 1/10th of the shortest signal wavelength of interest.


**3.1.4** **Voltage and Current Sources**


**Independent Sources**


Spice supplies a number of independent voltage and current source types. As many of the source’s features
only make sense in the context of the analysis to be used, only some of the source’s features are discussed


_3.1. ELEMENTS_ 17


here. In particular, we present those features that might be used in a transient analysis (see Chapter 2 and
Section 3.2.1).
Voltage supplies are specified using DC independent sources, for example:


VCC 5 0 DC 5


for a 5 V DC power supply between nodes 5 and 0.
Any repeating non-sinusoidal waveform can be specified using the pulse waveform specification, an
example of which was given in Chapter 2. pulse is often used to describe digital clocks, for example.
Non-repeating non-sinusoidal waveforms are specified using the piece-wise linear (pwl) waveform function.
One period of the pulse example presented in Chapter 2 is shown below in the piece-wise linear format:


###### (0ns, 0V)


###### (14ns, 0V)



vin 1 0 pwl (0ns 0V 4ns 0V 7ns 1.5V 12ns 1.5V 14ns 0V 17ns 0V)


18 _CHAPTER 3. CARRYING ON_


Sinusoidal and decaying sinusoidal waveforms are specified using the SIN function, for example:


Vin 4 0 sin(2.5 1 100meg 10ns)

#### _Voltage_


#### _3.5_ _2.5_ _1.5_




#### _10 ns_

Spice also allows you to specify exponential and single-frequency FM signals. Please see the reference catalog
for details.


**Dependent Sources**


These are the most overlooked elements Spice provides. Four different types of linear dependent sources
can be specified in Spice:


_•_ Voltage-controlled voltage source and current-controlled current source:





E1 4 3 2 1 3.3 _A voltage gain of 3.3._
F1 6 5 Va 1.7 _A current gain of 1.7_




###### 6 5 6 5




_•_ Voltage-controlled current source and current-controlled voltage source:
















_3.1. ELEMENTS_ 19


G1 4 3 2 1 15mmho _A transconductance of 15×_ 10 _[−]_ [3] _mho (_ Ω _[−]_ [1] _)._
H1 6 5 Va 0.5k _A transresistance of 500 Ohms_


The above are linear sources. Non-linear sources can also be specified. For example, the following voltagecontrolled current source actually specifies a non-linear resistance that could be used as part of a non-linear
Thevenin equivalent circuit:





Gout 2 1 2 0 0 1m -0.6m


The format used in this example is:


G _xxx node1 node2 ref-node1 ref-node2 C0 C1 C2_


to produce a dependent source that obeys the equation:


_I_ = _C_ 0 + _C_ 1( _V_ ( _ref −_ _node_ 2) _−_ _V_ ( _ref −_ _node_ 1)) + _C_ 2( _V_ ( _ref −_ _node_ 2) _−_ _V_ ( _ref −_ _node_ 1)) [2] _._


In this case, the equation specifying the current is:


_I_ = 0 + 1 _×_ 10 _[−]_ [3] _Vout −_ 0 _._ 6 _×_ 10 _[−]_ [3] _Vout_ [2]


The above non-linear source is quadratic and dependent on only one other variable. The same format can
be used to specify higher order polynomials. A source dependent on the voltages/currents on/in ND other
nodes/branches can be specified by including a poly(nd) statement in the element line. For example, the
following linear voltage-controlled voltage source specifies a gated sinusoidal source:

###### 0


Vsine 1 0 sin (0 0.5 100k 5us)
Vpulse 2 0 pwl (0ns 0V 14us 0V 15us 1V 65us 1V 66us 0V)
Egate 3 0 poly(2) 1 0 2 0 0 0 0 1


i.e. This source specifies a voltage,


Vgate = 0 + 0 _×_ Vsine + 0 _×_ Vpulse + 1 _×_ Vpulse _×_ Vpulse


20 _CHAPTER 3. CARRYING ON_


which has the following waveform:


In its general form, a polynomial of any complexity can be specified. e.g. The generalized voltage controlled
voltage source,


EX <node> <node> poly(2) V1 V2 k0 k1 k2 k3 k4 k5 k6 k7


specifies a controlled voltage of the form


_EX_ = _k_ 1 + _k_ 2 _× V_ 1 + _k_ 3 _× V_ 2 + _k_ 4 _× V_ 1 _× V_ 2 + _k_ 5 _V_ 1 [2] + _k_ 6 _V_ 2 [2] + _k_ 7 _V_ 1 [2] _V_ 2 [2]


This could be extended to create polynomials as a function of 3, 4, etc. variables. However, as a practical
matter, it is very difficult to read and understand non-linear polynomials with more than two inputs. It is
easier to create two-input polynomials separately and combine them with another polynomial.

##### **3.2 Analyses**


**3.2.1** **Transient Analysis**


In the transient analysis response is observed with one or more time-varying inputs. A simple example is
given in Chapter 2.
The first step performed by Spice in a transient analysis is to compute the initial DC or bias point
condition. During this computation it is assumed that the voltage across capacitors is zero, the current
through inductors is zero, and the value for dependent sources is zero. Spice then conducts the transient
simulation by calculating all of the voltages and currents at a set of points in time. In the rest of this section,
we discuss a number of issues related to transient analyses, starting with a treatment of convergence.


**DC Convergence**


During both the DC analysis and the following transient analysis iterative numerical techniques are used
to obtain a solution. The objective of these techniques is to iterate on the value of the node voltages and
branch currents until successive iterations only bring very small changes in their values, i.e. Spice _converges_
on a solution in the DC analysis and at every time step.
Sometimes Spice can not converge on a solution. If this occurs during the DC analysis it will report
this problem in the output file with a ‘convergence problem’ message like. Failure to converge in the DC
analysis is usually due to an error in specifying node numbers, circuit values or model parameter values.
These should be checked carefully before proceeding further. However, sometimes Spice is having a genuine
problem in converging and you might have to help it find a solution.
In many bistable circuits (e.g. flip-flops) and positive feedback circuits, Spice will not converge in the
DC analysis or will converge to an undesirable value (e.g. midway between logic-0 and logic-1 in a latch).
One way to help Spice converge to the correct value is to use the off option to turn off devices in the
feedback path, e.g.,


M0 0 1 2 0 pd=5.2u ad=5.2u off


allowing Spice to find a DC solution. Spice turns the devices back on during the transient analysis. Another
approach is to use nodeset to provide ‘hints’ to Spice or to specify initial conditions that force a solution.


_3.2. ANALYSES_ 21


**Nodeset and Initial Conditions**


The basic difference between using nodeset and specifying initial conditions is that the latter forces nodes
to the specified voltage while nodeset only provides hints. The values specified by the nodeset line are only
used during the first part of the DC solution procedure and then ignored in the later parts. Thus if they are
incorrect, or inconsistent, convergence is not prevented. As an example of nodeset, ts use as follows in the
the simple latch, will result in the output (node 2) converging to 5 V (assuming a CMOS latch):


.nodeset V(1)=0V


When initial conditions are set, they are used through the entire DC solution right to the start of the
transient analysis. For example in the circuit above, the use of .IC V(1)=1V will result in V(1) starting at
1 V in the transient analysis while the use of .nodeset V(1)=1V would result in V(1) starting at 0 V. An
error or inconsistency in specifying initial conditions with .IC might prevent Spice from converging.
A second way to specify initial conditions is to specify them in the element lines. For example, the
statement,


C1 6 0 IC=3.1


initializes the voltage across capacitor C1 to 3.1 V. For an inductor, the following statement will set the
initial current flowing through it to 4.3 mA:


L3 4 5 IC=4.3m


If IC= statements are used then it is necessary to include a “Use IC=” (UIC) statement in the .tran statement,
e.g.


.tran 200ps 34ns UIC


Specifying UIC commands Spice to skip the DC bias calculation, making it is necessary for the initial
conditions to be completely specified through a combination of IC= and .IC statements. Be careful.


**Simulation Time Step Size**


Using a smaller time step increases both the results accuracy and computer run-time of the simulation. One
thing to be very aware of is if short transmission lines or very fast edges are specified then the simulation
time step will be very short. For example, trying to obtain a ‘step response’ with a waveform/statement


22 _CHAPTER 3. CARRYING ON_


such as the following will greatly increase rise time (and also quite likely lead to convergence problems).

###### 1 ps

|Col1|Col2|
|---|---|
|||



.Vin 4 0 PWL 0ns 0V 1ps 5V 40ns 5V


It is also possible to change the time step, and other step-related parameters, in the .options statement.
Please see the reference catalog for details.


**Transient Analysis Convergence Problems**


Spice might report a transient analysis convergence problem with a message like the following:


*ERROR*: Convergence problem in Transient Analysis at


TIME =


_etc._


Sometimes Spice is not so hopeful and just ‘dumps’ you part way through the analysis, e.g. part way into
a 40 ns analysis Spice might suddenly stop the analysis at 34 ns and end with:


3.400E-09 5.452E+00 6.602E+00 6.892E+00
Y
0 ***** JOB ABORTED


In this case, the problem was a too-short implicit time step caused by a very short (62.3 ps delay) transmission
line:


Tline3 10 0 11 0 z0=60 td=62.3ps


Replacing the line with its equivalent lumped circuit,


Lline3 10 11 7.48nH
Cline3a 10 0 1.03pF
Cline3b 11 0 1.03pF


solved the problem.
If your transient analysis convergence problem is not being caused by a too short a time step, then it
is most likely caused by an error in specifying a circuit node number or parameter value. Your circuit and
.model lines should be checked carefully. Often looking at the circuit description as specified in the output
listing is more useful than looking at the file you typed in, as the output listing is describing what Spice
‘sees’.
However, Spice is a numerical program and can be quirky. For example, one simulation driven by the
pulse


V2 4 0 Pulse(0V 5V 0n 1.2n 1.2n 20n 40n)


would abort about half way through the simulation. However, turning the pulse ‘up-side-down’ (interchanging
0V and 5V),


V2 4 0 Pulse(5V 0V 0n 1.2n 1.2n 20n 40n)


allowed the simulation to complete.


_3.2. ANALYSES_ 23


**Spectral Analysis – Fourier Transform**


The .Four control statement can be used to find the spectrum of any time-varying signal in a transient
analysis. For example, in Chapter 2, we used the following time-domain signal as the input to an RC circuit:
###### 1.5 V 0 V

|4ns 3ns 5ns 2ns|Col2|
|---|---|
|||
|||



vin 1 0 pulse (0 1.5 4ns 3ns 5ns 2ns 17ns)


The addition of the control statement,


.Four 58.82MegHz V(1) V(2)


to this file, specifies that the spectrum of the input (V(1)) and output (V(2)) voltage waveforms are also
to be obtained. The frequency specified in this statement is the fundamental frequency of the waveform
(1/17 ns = 58.82 MHz). As a result of this statement, the output file reports the magnitude and phase of
the first nine harmonics for each signal. In this case, the output for V(1) is:


0**** FOURIER ANALYSIS TEMPERATURE = 27.000 DEG C


0***********************************************************************


FOURIER COMPONENTS OF TRANSIENT RESPONSE V(1)
0DC COMPONENT = 5.293D-01
0HARMONIC FREQUENCY FOURIER NORMALIZED PHASE NORMALIZED
NO (HZ) COMPONENT COMPONENT (DEG) PHASE (DEG)


1 5.882D+07 7.750D-01 1.000000 -91.352 0.000


2 1.176D+08 2.561D-01 0.330483 99.249 190.601


3 1.765D+08 7.623D-02 0.098364 16.321 107.673


4 2.353D+08 2.980D-02 0.038451 -123.300 -31.947


5 2.941D+08 2.502D-02 0.032282 -167.139 -75.786


6 3.529D+08 6.971D-03 0.008994 -46.439 44.913


7 4.118D+08 9.869D-03 0.012734 81.719 173.071


8 4.706D+08 1.722D-02 0.022225 -9.729 81.623


9 5.294D+08 1.346D-02 0.017363 -169.978 -78.625


A similar table is obtained for V(2).


24 _CHAPTER 3. CARRYING ON_


**3.2.2** **DC Analyses**


Spice enables you to conduct the following DC analyses:


_•_ DC solution for a particular input voltage/current condition (.OP).


_•_ DC solutions over a range of input conditions (.DC).


_•_ Small signal DC transfer functions, including gain, input and output resistance (.TF).


_•_ Sensitivity of the DC value of an output to some set of parametric variations (.SENS).


These are discussed in turn.
The insertion of a line with just


.OP


on it asks Spice to determine the DC bias point of the circuit with inductors shorted and capacitors opened,
just the same as the DC analysis conducted before a transient analysis. It might be used in situations where
you wish to know the DC bias point but the analysis you are doing does not request it (e.g. such as when
determining a frequency response).
A command line beginning with .DC instructs Spice to sweep the specified voltage source over the
specified range, reporting the DC bias point for each combination of input conditions. If more than one
source is specified in the .DC statement, then the first source will be swept over its entire range for every
value of the second source. An example is given in Figure 3.5 in which two analyses alternatives are presented
at the bottom. The left hand alternative instructs Spice to plot the transfer characteristics of the CMOS
inverter, the right hand example instructs Spice to plot the output V-I characteristics for when Vin is 5 V.
Both examples specify that the voltage sweep is to be from 0 to 5 V in 0.1 V increments. The resulting
output V-I characteristic (obtained using the statements on the right hand side of the Figure 3.5) is plotted
in Figure 3.6.
Now, if you wish to find the small signal output resistance at say Vout = _X_ V,



_rout_ = _[∂v]_

_∂i_



����
_Vout_ = _X V_



then one way to obtain this would be to measure the slope of the plot shown in Figure 3.6 at Vout = 0 _._ 5 V.
However, Spice provides an easier way to get this result as a transfer function .TF:


.TF I(vout) Vout


There is no need for a .print statement with .TF. Running this produces the output:


OUTPUT RESISTANCE AT I(VOUT) = 2.247D+03


A DC sweep can also be done by specifying a slow moving input and a conducting a transient analysis.
Sometimes this is necessary, for example in circuits with hysteresis, such as a Schmitt Trigger.
Sometimes we wish to know the sensitivities of various output parameters with respect to variations in
circuit parameters. For example, we might wish to know whether to specify resistors to +/-10% or +/-1%
in order to guarantee a certain bias point in a transistor amplifier. This is done with the .sens statement.
The following example determines the sensitivity of the bias point of an amplifier to variations in resistance


_3.2. ANALYSES_ 25


values:



















_Extract from input file:_


Common-Emitter Amplifier


R1 2 5 40k
R2 2 0 40k

- Measure the Base current
Vbase 3 2
Q1 4 3 6 NQ1A
RC1 5 4 4k
RE1 6 0 100


- AC source with unity magnitude and AC buffered
Vin 1 0 AC
Cbuff 1 2 100u


Vcc 5 0 5V


- Find the bias point
.OP


*Find the sensitivity of the bias voltage at the collector
.sens V(4)


_Extracts from output file reporting DC bias point and the sensitivity analysis:_


NODE VOLTAGE NODE VOLTAGE NODE VOLTAGE NODE VOLTAGE
NODE VOLTAGE NODE VOLTAGE


26 _CHAPTER 3. CARRYING ON_


( 1) 0.0000 ( 2) 1.1432 ( 3) 1.1432 ( 4) 0.3220 (
5) 5.0000 ( 6) 0.1237


0DC SENSITIVITIES OF OUTPUT V(4)
0 ELEMENT ELEMENT ELEMENT NORMALIZED
NAME VALUE SENSITIVITY SENSITIVITY
(VOLTS/UNIT) (VOLTS/PERCENT)


R1 4.000D+04 1.114D-06 4.457D-04
R2 4.000D+04 -3.303D-07 -1.321D-04
RC1 4.000D+03 -7.010D-05 -2.804D-03
RE1 1.000D+02 1.192D-03 1.192D-03


In this case, if the value for RE1 changed by 100% the collector voltage would only change by only 119 mV.


**3.2.3** **Small Signal AC Analysis**


Analog circuits are often analyzed in terms of their frequency response to steady-state, sinusoidal, smallvoltage, input signals. With small voltage swing signals, all of the circuit elements can be treated as being
linear around some bias point. Three types of AC analysis can be done:


1. Obtain circuit response(s) as a function of frequency using the .AC analysis.


2. Conduct a noise analysis as a function of frequency using a .NOISE element together with a .AC element.


3. Analyze the circuit for harmonic distortion using the .DISTO element together with the .AC element.


In this section, we discuss the first two types of analysis only. The distortion analysis capability provided in
Spice2g6is somewhat limited and so is not presented.
Consider the frequency response of the LC filter described, with its Spice file, in Figure 3.7. There are
several features in this file that differentiate it from a file specifying a transient analysis. First the signal
source Vin is specified as an AC source, not a source in the time domain. Here it specifies a sinusoid with
a magnitude of 1 Volt. The .AC control statement specifies that we wish the frequency range to be swept
over a frequency range of 100 Hz to 10 kHz in decade (dec) increments with 20 points per decade. i.e. The
output contains a total of 40 frequency points, 20 between 100 Hz and 1 kHz and 20 between 1 KHz and
10 Hz. The .print statement specifies that this is an AC analysis and specifies that the magnitude of the
voltage (VM) of node 3 with respect to node 0 be printed at each frequency point. Examples of other results
that can also be obtained include:


**Control statement Example** **Meaning**
.print AC VR V(2,3) _Real part of the voltage across the inductor_
.print AC VI V(2,3) _Imaginary part of the voltage across the inductor_
.print AC VP I(Vin) _Phase of current through the voltage source_
.print AC VDB(3) _Voltage in dB,_ 10 _× log_ 10( _magnitude_ )


The results obtained by running the Spice file specified in Figure 3.7 are shown in Figure 3.8. Note again
that a DC analysis is carried out before the AC analysis so as to obtain the bias point (this is not shown).
In Section 3.2.2, we show how to obtain the (non-linear) output impedance as a function of the output
voltage. For small voltage swing signals, all impedances are linear, so we are interested in input and output
impedance as a function of frequency. For example, we could plot the output impedance of the LCR circuit
above using the following Spice file:


_3.2. ANALYSES_ 27


RLC filter


- ‘Short’ input so that it does not form

- part of the output impedance
Vin 1 0 AC 0V

R1 1 2 15Ohm
L1 2 3 50mH
C1 3 0 1.5uF

.AC dec 20 100Hz 10kHz


- Measure output impedance with a current source
Iout 0 3 AC 1


- Measure Zout:
.print AC VM(3)
.end


The output impedance is plotted in Figure 3.9.
Spice is also capable of conducting a noise analysis as part of the AC analysis. This analysis is often
useful as an aid to the design of analog circuits. For full details please see the .NOISE and .PRINT control
statement descriptions in the reference catalog (Part III).


**3.2.4** **Monte Carlo Analysis**


The Monte Carlo analysis is a statistical analysis of the circuit causing the circuit to be analyzed many
times with a random change of model parameters (parameters in a .MODEL statement). It is available in the
PSpice version only.
The form on the Monte Carlo analysis is
PSpice _Form_


.MC _NumberOfRuns AnalysisType OutputSpecification OutputFunction_ [LIST]
+ [OUTPUT( _OutputSampleType_ )] [RANGE( _LowValue_, _HighValue_ )]
+ [SEED= _SeedValue_ ]


Monte Carlo analysis repeates DC analysis as specified by the .DC statement, AC small-signal analysis as
specified by the .AC statement, or transient analysis as specified by the .TRAN statement. In the .MC statement
the way in which the results of the multiple runs are interested is controlled by the _OutputSpecification_ ] and
_OutputFunction_ parameters.
A typical use of Monte Carlo analysis is to predict yield of a circuit by examining the effect of process
variations such as length and width of transistors. As well the effect of temperature on circuit performance
can be investigated.
The initial run uses the nominal parameter values given in the NETLIST. Subsequent runs statistically
vary model parameters indicated as having either lot or device tolerances. These tolerances are specified in
a .MODEL statement.


**3.2.5** **Transfer Function Specification**


The transfer function specifies a small-signal DC analysis from which a small-signal transfer function and
input and output resistances are computed. The transfer function computed is the ratio of the DC value
of the output quantity to the input quantity. In the above examples the following transfer functions are


28 _CHAPTER 3. CARRYING ON_


computed:


EXAMPLE Transfer Function


V(10)
.TF V(10) VINPUT
VINPUT


V(10 _,_ 2)
.TF V(10,2) ISOURCE
ISOURCE


I(VLOAD)
.TF I(VLOAD) ISOURCE

ISOURCE


**3.2.6** **Parameteric Analysis**


**3.2.7** **Sensistivity and Worst Case Analysis**


_3.2. ANALYSES_ 29





CMOS Inverter Example

M0 0 1 2 0 nenh l=0.8u w=1.6u ad=3.2p as=3.2p pd=5.2u ad=5.2u
M1 5 1 2 5 penh l=0.8u w=1.6u ad=3.2p as=3.2p pd=5.2u ad=5.2u
Vcc 5 0 DC 5V


- following option line fixes transistor length and width, and

- drain/source area defaults

.options defl=0.8u defw=1.6u defad=3.2p defas=3.2p


.model nenh nmos
+ Level=2 Ld=4.000e-8 Tox=1.750000e-08
+ Nsub=1.506725e+17 Vto=0.59073 Kp=6.124495e-05


_(Remainder of model omitted.)_


.model penh pmos
+ Level=2 Ld=4.000000e-08 Tox=1.750000e-08


_(Remainder of model omitted.)_


Figure 3.3: A CMOS inverter.


30 _CHAPTER 3. CARRYING ON_

###### 8 v = 3 x 10  m/s Characteristic Impedance = 50 Ohms


T1 1 0 2 0 Z0=50 TD=333ps


Figure 3.4: Example of a transmission line.





MOS Inverter

M0 0 1 2 0 nenh l=0.8u w=1.6u ad=3.2p as=3.2p pd=5.2u ad=5.2u
M1 2 1 5 5 penh l=0.8u w=1.6u ad=3.2p as=3.2p pd=5.2u ad=5.2u
Vcc 5 0 DC 5V


Vin 1 0 Vin 1 0 5V
Vout 2 0
.DC Vin 0 5 0.1 .DC Vout 0 5 0.1
.print DC V(2) .print DC I(Vout)


Figure 3.5: DC response example. Two alternative analyses are presented at the bottom and are described
in the text.


_3.2. ANALYSES_ 31


0.0001


0


-0.0001


-0.0002


-0.0003


-0.0004


-0.0005


-0.0006


-0.0007

0 0.5 1 1.5 2 2.5 3 3.5 4 4.5 5

Vout (V)


Figure 3.6: Output V-I characteristics for CMOS inverter.


###### **R1**


###### 150




###### L1 50mH








###### V(3)



RLC filter

           Vin 1 0 AC 1V _AC signal source_

           R1 1 2 15Ohm
L1 2 3 50mH
C1 3 0 1.5uF

           .AC dec 20 100Hz 10kHz _AC analysis specification_

           .print AC VM(3) _print results of AC analysis_


Figure 3.7: LC filter and the Spice file specifying a frequency response analysis. (Comments in _emphasis_
are not part of the file.)


Figure 3.8: Frequency response of the circuit shown in Figure 3.7.

##### 1800 1600 1400 1200 1000 800 600 400 200 0 100 1000 10000 Frequency (Hz)


Figure 3.9: Output impedance vs. frequency for LC circuit shown in in Figure 3.7.


### **Chapter 4**

# **How Spice Works**

##### **4.1 Introduction**

Spice has three basic analyses: DC analysis — initiated by the .DC statement; AC analysis — initiated by the
.AC statement; and transient analysis — initiated by the .TRAN statement. AC analysis involves incorporating
the relations relating terminal voltages and device currents into a matrix equation This matrix equation is
called the network equation and embodies the topology of the network and the constitutive relations (that is,
device equation) describing individual devices. It derives from a mathematical statement of Kirchoff’s current
law with device currents replaced by node voltages with the substitution achieved by using the constitutive
relations of individual devices. Extensions to this basic form of the network equation (called the modal
formulation of the network equation) is required for elements that can not be mathematicly modeled as a
current or currents in terms of voltages. AC analysis is the appropriate place to begin a technical exposition
of the analysis algorithms in Spice as it illustrates the method of development of network equation is used
by all other analyses.
Transient analysis requires, as well, that a time-stepping numerical integration algorithm be incorporated
into the network equations. A straight forward approach to transient analysis, which was used prior to the
development of the “Spice” approach, is to derive the state equations in state space (that is in differential
form using the _s_ operator) and apply the time discretization of a numerical integration method to the complete
network equation. However, in Spice the time discretization is incorporated in the constitutive relations
before the network equation is developed. The time discretized network equation must be solved iteratively
and the Newton iteration procedure is applied to the device equations along with the time-discretization step.
This has proved to be a particularly robust approach and is the main reason Spice is so widely accepted.
DC analysis is a special case of transient analysis without the time discretization step and so is discussed
after transient analysis.

##### **4.2 AC Small Signal Analysis**


AC small signal analysis is inititated by the .AC statement (see page 53). The aim in AC analysis is to determine
the AC voltage at every node in the circuit which is now linear because of the small-signal approximation.
First of all a matrix equation is developed that relates node voltages to external current sources. Through
Thevenin’s theorem external voltage sources are converted to external current sources and node voltages
are easily related to voltages across elements. This formulation of the network equation is called the nodal
admittance formulation. Unfortunately there are several elements, such as the current controlled voltage
source element, which do not have an admittance description as required in this approach. A method of
circumventing this problem is discussed in section **??** and is a direct extension of the method discussed below.
Consider the general network _N_ in Figure 4.1(a) with _N_ internal nodes in addition to the reference node.
33


34 _CHAPTER 4. HOW SPICE WORKS_
(a) (b)


Figure 4.1: Definition of networks: (a) _N_ ; and (b) _N_ _[′]_ .


In general the reference node is not part of the circuit and the development of the network equations is
simplified by treating all of the nodes (except the external reference node) in the same way.
All of the nodes of the network have external current sources _J_ with _Jn_ being the external current source
between the _n_ th node and the reference node. In practice most of the external current sources, the _J_ ’s, are
zero and those that are not are due to independent sources. The network equations used in Spice relate the
node voltages, the _v_ ’s, and the _J_ ’s. In matrix form


**Yv** _n_ = **J** _n_ (4.1)


where **v** _n_ is the vector of node voltages, and **J** _n_ is the vector of external currents. Solution of equation ( **??** )
enablEs the node voltages to be evaluated given the external current sources.
In Spice the grounded reference node, node “0”, is part of the network and so there is a linear dependence
of the rows of **Y** ( _|_ **Y** _|_ = 0). Hence **Y** is called the indefinite nodal admittance matrix. One row and one
column can be deleted from **Y** without the lossing any information to yield what is called the definite nodal
admittance matrix. For now consider that the reference node is an arbitrary node. The correction required
because the reference node is actually part of the circuit is discussed in section **??** .

##### **4.3 DC Analysis**

DC
The analysis of nonlinear resistive circuits, or equivalently the analysis of circuits at DC is an important first
step in ACand transient analysis. In both cases nonlinear resistive analysis determines the initial starting
point for further analysis incorporating energy storage elements such as capacitors and inductors.
DC analysis is Spice is identical to transient analysis discussed in the previous section except that the
contributions of capacitors and inductors are ignored. DC analysis has better convergence properties ithan
transient analysis since energy storage elements, and thus resonant responses, are eliminated. As well the
analysis is numericly efficient since only a steady-state response is required and calculated.

##### **4.4 Discussion**


Spice supports several analyses other than those discussed above. Essentially these are extensions of the
AC, DC and transient analyses.


_4.5. TO EXPLORE FURTHER_ 35


The transfer function analysis, initiated by the .TF statement, calculates a transfer function as the ratio
of the DC value of an output quantity to the DC value of an input quantity over a range of values of the input
quantity. A DC analysis at each value of the input quantity is performed.
With the .DISTO statement a distortion analysis is performed by dteremining the steady-state harmonic
and intermodulation products for small input signal. Evaluation of the small-signal distortion is based on a
third-order multi-dimensional Volterra series expansion of nonlinearities around their operating point. The
method for calculating of the distortion products parallels AC analysis algorithm.
The sensitivity analysis calculates the DC small-signal sensitivities of each output quantity with respect
to every circuit parameter. It is initiated by the .SENS statement. The transfer function computed is the
sensitivity (or partial derivative) of the DC value of the output quantity with respect to the each and every
circuit parameter.
If the .NOISE statement is included in the input file the noise generated by active devices and resistors
is evaluated. All active devices and some passive devices have noise models consisting of uncorrelated noise
current sources. These noise current sources are used as the external current sources in ACanalysis. One noise
source at a time is considered and the response at the output terminals and sources specified are calculated.
The contributions from each source are added in a root-mean-squared sense as they are uncorrelated. The
noise analysis utilizes the network equation formulated and solved in AC analysis.
A Monte Carlo analysis is performed when the .MC statement is specified. In the Monte Carlo analysis
either a DC, an AC, or a transient analysis is performed multiple times.
An operating point analysis initiated by the .OP statement is just a single DCanalysis.
The Fourier analysis performed when the .FOUR statement is used is not really a separate analysis at all.
Really it is a way of examiing the results of a transient analysis by taking the Fourier transform of a voltage
or current response.

##### **4.5 To Explore Further**


The essential aspects of Spice are the models of devices and the algorithms for formulating and solving the
network equations. The derivation of the AC model of devices is straightforward requiring the _y_ parameters
of the device. These are obtained from the analytic derivatives of the device equations calculated at the
operating point of the circuit as determined from a DC analysis. For transient and DC analysis the associated
discrete circuit model must be calculated from the device equations. The device equations of semiconductor
devices are calculated from knowledge of the device physics. Derivation of the models used for semiconductor
devices in Spice2g6 and Spice3 are described in [2] ( _Semiconductor Device Modeling with SPICE_ edited
by P. Antognetti and G. Massobrio). Without fail the models in Spice2g6 are available in all commercial
versions of Spice. Spice3 and most commercial versions of Spice provide additional or enhanced models.
Derivations of more advanced models are described in [8] ( _Semiconductor Device Modeling for VLSI_ by K.
Lee, M. Shur, T. Fjeldly and T. Ytterdal).
In Spice the network equations are stored in sparse matrices to conserve memory usage. This also results
in much faster solution of the network equations than if regular matrices were used. Greater detail than
that provided in this chapter of the numerical algorithms used in Spice can be found in [1] ( _Fundamentals_
_of Computer-Aided Circuit Simulation,”_ by W. J. McCalla).


36 _CHAPTER 4. HOW SPICE WORKS_


### **Chapter 5**

# **Input File**

##### **5.1 Introduction**

The operation of Spice is controlled by statements which are embedded in an input file which includes as
well descriptions of elements and their topology. The description of the elements and their topology is also
known as a netlist. The output or results of a Spice run are logged in an output file and in more modern
versions of Spice, in a data file for subsequent interactive plotting and analysis. With PSpice the program
for subsequent analysis is probe and with Spice3 the comparable tool is NUTMEG.

##### **5.2 Circuit Model**


The model used by Spice to represent circuits is as shown in Figure 5.1. Spice supports a hierarchical
description of a circuit with subcircuits. A large number of parameters are required for many elements,
especially for active devices, and for these the model concept is introduced where most of the parameters
of active elements can be defined separately from invocation of the element. This permits a single model
description to be used by many elements. A model is specific to a particular element type but not all elements
have models. Mostly models are used to set the parameters describing a semiconductor fabrication process
and so are common to many elements.
When the input file is read subcircuits definitions and models are stored internally separately from the
main circuit. Subcircuit calls are expanded if the subcricuits referenced are already defined and stored
internally. If a referenced subcircuit is not defined then the subcircuit call is flagged as not being expanded
and only when the input file has been completely read (up to the .END statement) is an attempt made to
resolve incomplete expansions. In PSpice library files (described in the .LIB statement discussion on page
68) are checked. The first time a library file is to be searched, an internal table of which subcircuits and
models are available and where they can be found in the library files is constructed. Models are treated in
a similar way, a model is used if it has been defined otherwise resolved references to models are expanded
once the input file has been completely scanned (up to the .END statement). With PSpice evaluation of
expressions in subcircuits and models is only performed when on fully expanded subcircuits. Note that
expressions and libraries are not supported in Spice2g6or in Spice3.

##### **5.3 Input Lines**


The input file of Spice is essentially unstructured. It must begin with a TITLE line and should end in a
.END statement although this is automaticlly assumed if the end of the input file is read. The string on the
TITLE line is used as the banner in the output log file appearing at the top of each page. The .END statement
marks the end of one circuit with the effect that several circuits can be specified in the file (at least for
37


38 _CHAPTER 5. INPUT FILE_








|NETLIST<br>TOP<br>LEVEL CONTROL<br>CIRCUIT STATEMENTS<br>DESCRIPTION<br>SUBCIRCUIT A<br>DESCRIPTION<br>SUBCIRCUIT B<br>DESCRIPTION<br>MODEL 4<br>MODEL 1<br>MODEL 2<br>SUBCIRCUIT C<br>DESCRIPTION<br>MODEL 3|Col2|Col3|INTERNAL CIRCUIT<br>REPRESENTATION<br>A EXPANSION<br>A.B EXPANSION<br>A.B.C EXPANSION<br>A.C EXPANSION<br>C EXPANSION|
|---|---|---|---|
|**TOP**<br>**LEVEL**<br>**CIRCUIT**<br>**DESCRIPTION**<br>**MODEL   1**<br>**MODEL   2**<br>**MODEL   4**<br>**MODEL   3**<br>**SUBCIRCUIT  A**<br>**DESCRIPTION**<br>**SUBCIRCUIT C**<br>**DESCRIPTION**<br>**SUBCIRCUIT  B**<br>**DESCRIPTION**<br>**CONTROL**<br>**STATEMENTS**|**TOP**<br>**LEVEL**<br>**CIRCUIT**<br>**DESCRIPTION**<br>**MODEL   1**<br>**MODEL   2**<br>**MODEL   4**<br>**MODEL   3**<br>**SUBCIRCUIT  A**<br>**DESCRIPTION**<br>**SUBCIRCUIT C**<br>**DESCRIPTION**<br>**SUBCIRCUIT  B**<br>**DESCRIPTION**<br>**CONTROL**<br>**STATEMENTS**|**TOP**<br>**LEVEL**<br>**CIRCUIT**<br>**DESCRIPTION**<br>**MODEL   1**<br>**MODEL   2**<br>**MODEL   4**<br>**MODEL   3**<br>**SUBCIRCUIT  A**<br>**DESCRIPTION**<br>**SUBCIRCUIT C**<br>**DESCRIPTION**<br>**SUBCIRCUIT  B**<br>**DESCRIPTION**<br>**CONTROL**<br>**STATEMENTS**|**TOP**<br>**LEVEL**<br>**CIRCUIT**<br>**DESCRIPTION**<br>**MODEL   1**<br>**MODEL   2**<br>**MODEL   4**<br>**MODEL   3**<br>**SUBCIRCUIT  A**<br>**DESCRIPTION**<br>**SUBCIRCUIT C**<br>**DESCRIPTION**<br>**SUBCIRCUIT  B**<br>**DESCRIPTION**<br>**CONTROL**<br>**STATEMENTS**|
|**TOP**<br>**LEVEL**<br>**CIRCUIT**<br>**DESCRIPTION**<br>**MODEL   1**<br>**MODEL   2**<br>**MODEL   4**<br>**MODEL   3**<br>**SUBCIRCUIT  A**<br>**DESCRIPTION**<br>**SUBCIRCUIT C**<br>**DESCRIPTION**<br>**SUBCIRCUIT  B**<br>**DESCRIPTION**<br>**CONTROL**<br>**STATEMENTS**||||



Figure 5.1: The Spice circuit representation.


_5.3. INPUT LINES_ 39


Spice3 and PSpice). In between the TITLE line and the .END statement can be any mix of statements —
which control the operation of the simulator and the analysis to be performed; optional comment lines —
for documenting the input file; and element lines — which specify the circuit elements. The input file can
in fact contain no statements and the simulator will then perform an operating point .OP analysis. Spice
does not distinguish between upper and lower case characters.
Except for the TITLE line which is the first line of the input file, the type of input lines is distinguished
by the first character on the line: statements begin with a period “.”; element lines begin with an alphabetic
character “A–Z” — with the letter identifying the element type (e.g. R for a resistor); and comment lines
begin with an asterisk “*”. In older terminology, based on the original use of punched cards, statements are
referred to as “ _dot cards_ ” or “ _statement cards_ ”; element lines are referred to as “ _element cards_ ” or “ _device_
_cards_ ”; and comment lines as “ _comment cards_ .”
PSpice allows for in line comments indicated by a semicolon “;”. The semicolon and everything following
it on the same line are ignored except for purpose of echoing the input file in the output log file.


**5.3.1** **Analysis Statements**


An analysis statement identifies the type of analysis to be performed. Any combination of analyses may be
specified. Reporting of the results of an analysis is controlled by the .PRINT, .PLOT and, in with PSpiceby
the .PROBE control statements. If no analysis statement is included in the input file then an operating point
analysis (.OP) is performed by default. A brief description of the analysis options and the page on which a
complete description can be found as follows.


.AC AC Analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . Page 53


Obtains the small-signal circuit response as a function of frequency. The .AC analysis is one of several small
signal AC analyses.


.DC DC Analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . Page 55


DC solutions over a range of input conditions (.DC).


.DISTO Small-Signal Distortion Analysis Spice2g6 and Spice3 Only . . . . . . . . . . . Page 58


Analyze the circuit for harmonic and intermodulation distortion. This analysis is available in Spice2g6 and
Spice3 but is not available in PSpice as it has proved to be unreliable. In Spice2g6 the distortion analysis
must be performed in conjunction with a .AC analysis.


.FOUR Fourier Analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . Page 64


The .FOUR control statement can be used to find the spectrum of any time-varying signal in a (.TRAN)
transient analysis. The .FOUR statement is unlike other analysis statements as it does not initiate a simulation
but interprets the result of a simulation initiated by the .TRAN sattement.


.MC Monte Carlo Analysis (PSpice only) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . Page 69


The Monte Carlo analysis is a statistical analysis of the circuit causing the circuit to be analyzed many times
with a random change of model parameters (parameters in a .MODEL statement). The analyses specified in
the .DC, .AC or .TRAN statements can be simulated multiple times.


.NOISE Small-Signal Noise Analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . Page 77


Conduct a small-signal noise analysis as a function of frequency. In PSpice this statement must be used in
conjunction with a .AC statement.


.OP Operating Point Analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . Page 82


DC solution for a particular input voltage/current condition. This is the default analysis if no analysis is
specified in the input file. This is the default analysis if not analysis type is specified in the input file.


.PZ Pole-Zero Analysis, Spice3 Only . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . Page 99


In this analysis the poles and zeros of the small signal ACtransfer function of a two-port is evaluated.


40 _CHAPTER 5. INPUT FILE_


.SAVEBIAS Save Bias Conditions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . Page 100


.SENS Sensitivity Analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . Page 101


The sensitivity of the DC value of an output to some set of parametric variations is calculated.


.STEP Parameteric Analysis PSpice Only . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . Page 102


.TF Transfer Function Specification PSpice Only . . . . . . . . . . . . . . . . . . . . . . . . . . . Page 107


Small signal DC transfer functions, including gain and input and output resistance are computed


.TRAN Transient Analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . Page 109


In the transient analysis response is observed with one or more time-varying inputs.


.WCASE Sensistivity and Worst Case Analysis PSpice Only . . . . . . . . . . . . . . . . . . . . . Page 112


**5.3.2** **Control Statements**


.DISTRIBUTION Distribution Specification (PSpice only) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . Page 61


This statement specifies the statistical tolerance distribution used in a Monte Carlo analysis (see the .MC
statement on page 69).


.END End Statement . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . Page 62


This statement indicates the end of the input of one circuit.


.ENDS End Subcircuit Statement . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . Page 63


The end subcircuit statement indicates the end of a subcircuit definition.


.FUNC Function Definition PSpiceOnly . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . Page 65


Enables commonly used expressions to be more conveniently defined as functions.


.IC Initial Conditions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . Page 66


This statement is used to set initial conditions for transient analysis. It has no effect on other types of
analyses.


.INC Include Statement, PSpice only . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . Page 67


Specifies the name of a file which is to be treated as part of the input file.


.LIB Library Statement, PSpice only . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . Page 68


Specifies the name of a library file.


.MODEL Model Statement . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . Page 72


Specifies the parameters of elements that either are too numerous to put on the element line or are common
to many elements.


.NODESET Node Voltage Initialization . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . Page 76


Specifies the voltage at one or more nodes to be used as an initial guess.


.OPTIONS Option Specification . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . Page 83


The options specification provides the user control over the program and sets defaults for certain elements
and analyses.


.PARAM Parameter Definition, PSpice Only . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . Page 86


This statement defines parameters that can be used in subsequent statements and element lines.


_5.3. INPUT LINES_ 41


.PLOT Plot Specification . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . Page 88


The plot specification controls the information that is plotted in the output file as a character plot. This is
one way to view the result of various analyses.


.PRINT Print Specification . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . Page 92


The print specification controls the information that is reported as the result of various analyses.


.PROBE Data Output Specification, PSpice Only . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . Page 98


This statement saves the node voltages and device currents in a file for subsequent interactive plotting


.SUBCKT Subcircuit Statement . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . Page 103


Indicates the start of a subcircuit description and describes int interface to the subcircuit.


.TEMP Temperature Specification . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . Page 105


Specifies the temperature(s) to perform the analysis at.


.TEXT Text Parameter Definition, PSpice Only . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . Page 106


.WATCH Watch Analysis Statement PSpice Only . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . Page 111


.WIDTH Width Specification . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . Page 114


Specifies the column width for the output file.


**5.3.3** **Elements**


The general form for elements is device name, followed by a list of nodes, followed by the numeric value of
the element, followed in some cases by the name of a model, and then by other keywords:
_Name Node1 Node2 . . . NodeN NumericValue ModelName_
+ _keyword=NumericValue . . . InitialConditions._
For some elements initial conditions ( _InitialConditions_ ) can also be specified which can be used to ensure
that the desired initial state of astable circuits is obtained and also to aid in convergence. The first letter of
the _Name_ identifies the element. For example, if _Name_ is RTEST then the element is a resistor.
The general form above is not the form for every element. The way in which Spice evolved resulted in
the syntax for element lines not being fully consistent. Commercial extensions, as with PSpice, allowing
alphabetic names for nodes rather than just an integer designation also result in syntaxical problems. With
this extension it is not possible to use the fact that a field was alphabetic to distinguish between a node and
a parameter name. However this change has necessitated no change to the the standard syntax as defined by
Spice2g6. The problem appears in conjunction with other extensions which allow for an arbitrary number
of nodes in some statements. The result is that the syntax can be slightly different than would be expected.
For these reasons the description of the form of a particular element or statement must be consulted to
ensure that the syntax is correct.


**Active Elements**


_Form_


Q _name NCollector NBase NEmitter_ [ _NSubstrate_ ] _ModelName_ [ _Area_ ] [OFF]
+ [IC= _Vbe,Vce_ ]


Unlike passive devices active devices can not be specified by one or a few parameter values. Since many
of the parameter values are the same for many devices it is convenient to specify them in a .MODEL statement
that can be reused many times. All active elements require a .MODEL statement and most allow an optional
substrate node to be used on the element line.
The active devices supported in Spice2g6, Spice3 and PSpice and where their descriptions can be
found are as follows:


**5.3.4** **Distributed Elements**


The distributed devices and where they are described are as follows:
The convolution element enables a linear circuit described by a set of frequency dependent complex _y_
parameters to be included in transient analysis.

##### **5.4 Input Grammar**


Each input line contains fields which are delimited (separated) by one of a number of characters. The most
obvious delimiter is simply a space but other characters are also treated as “ _white space_ ” characters. White
space is defined as one or any combination of the following characters:


“blank” “tab” ( ), =
While the above characters appear in the input file they are ignored except that they are treated as a field
delimiter. The “(”, “)”, “=” and “,” characters are often used in the input file and are included in specifiying
the syntax for elements and statements but they serve only to add visual structure to the input.


Continuation lines begin with a plus “+” in the first column. For example


R1 1 2 1000


and R1 1 2
+1000
are equivalent.


Comment lines begin with an asterisk “*” in the first position. In line comments are supported in
PSpice and these begin with a semicolon “;” and must be contained wholly on one line. For example

            - This just shows off a comment
R1 1 2 1000 ;This shows of an in line comment


44 _CHAPTER 5. INPUT FILE_


In nearly every situation where a numeric value is required in the input an algebraic expression can be
used instead. Everything between a “ _{_ ” character and the matching “ _}_ ” character is treated as an algebraic
expression. The evaluation of algebraic expressions are discussed in the ALgebraic Expressions section on
on page **??** .


**5.4.1** **Prefixes and Units**


Almost-standard metric prefixes are used in Spice, the prefix abbreviation, the full metric name, and the
represented scale factors being as follows:


Spice **Metric** **Scale**
**Prefix** **Name** **Factor**
F femto 10 _[−]_ [15]

P pico 10 _[−]_ [12]

N nano 10 _[−]_ [9]

U micro 10 _[−]_ [6]

M milli 10 _[−]_ [3]

K kilo 10 [+3]

MEG mega 10 [+6]

G giga 10 [+9]

T tera 10 [+12]


As Spice does not differentiate between upper and lower case, ‘MEG’ (or ‘meg’) is used for ‘mega’ instead of
the standard metric upper case ‘M’.

The value of an element is specified in terms of the conventionally accepted units, e.g. resistance in
Ohms, capacitance in Farads, and inductance in Henries. If you wish you can spell it out more fully, e.g.


C1 0 2 5fF or
C1 0 2 5fFarad or even
C1 0 2 5fthingies


The last alternative is allowed as Spice actually ignores whatever follows the ‘f’ and assumes Farads.

##### **5.5 Parameters**


Parameters can be defined in two ways:


_•_ In a parameter definition (.PARAM).


_•_ As a subcircuit parameter in a .SUBCKT statement.


Parameters defined in a .PARAM statement can be used in subsequent statements and element lines by replacing a numeric value by an expression in which the parameter is used. The general form of the .PARAM
statement is


_5.5. PARAMETERS_ 45


.PARAM [ParameterName = NumericValue _. . ._ ]
+ [ParameterName = _{_ Expression _} . . ._ ]
Here the _ParameterName_ is the name of a parameter with the first character being alphabetic (a-zA-Z) and
can be assigned a numeric value _NumericValue_ which may be followed immediately by a spice scale factor.
For example, SMALL=1.E-9, SMALL=+1N, SMALL=1NV and SMALL=1.E-9V are equivalent and all
establish a parameter SMALL with a value of 10 _[−]_ [9] . If _ParameterName_ is the name of a previously defined
parameter at the same level of subcircut expansion then the parameter value is changed. If the .PARAM
statement is is in the top level circuit then the parameter value is global and is available any where in the
netlist. If the .PARAM statement is in a subcircuit then the parameter value is local and can be used at
the current subcircuit expansion level or lower in the subcircuit expansion hierarchy. The same idea applies
to values of a parameter changed in a subcircuit. Value changes are local and are available in the current
subcircuit and lower nested subcircuits. Libraries are searched for parameters not defined in the circuit
NETLIST or in included files. A .PARAM statement does not have to be within a subcircuit in a library.


Instead of a numeric value an algebraic expression can be used to establish the value of the parameter.
The expression is evaluated in the standard way for an algebraic expression replacing numeric values and is
evaluated at the time of expansion rather than as the netlist is read. This ensures the correct hierarchical
interpretation of the netlist. The treatment of expression is discussed in section 5.6 on page 46. Note that
as always the expression must be enclosed in matching braces ( _{ . . . }_ ).


Parameters can be used nearly anywhere a numeric value is expected by including them in an expression
evaluation even if the expression contains a single parameter. For example .PARAM rbig=10MEG
R1 1 2 _{_ RBIG _}_
establishes a resistance R1 between nodes 1 and 2 with a value of 10 [6] Ω.


Several predefined parameters are supported and the user must avoid defining these as unpredictable
results may result. The predefined parameters are


46 _CHAPTER 5. INPUT FILE_


**Name** **Value** **Description**

TEMP not supported Analysis temperature.
Reserved for future expansion


VT not supported Thermal voltage.
Reserved for future expansion

##### **5.6 Expressions**


In PSpice most places where a numeric value is normally used an expression (within braces _{ . . . }_ ) can
be used instead. An expression can contain any supported mathematical operation, constant numeric values
or expressions. Exceptions are


_•_ Polynomial coefficients.


_•_ The values of the transmission line device parameters NL and F.


_•_ The values of the piece-wise linear characteristic in the PWL form of the independent voltage (V) and
current (I) sources.


_•_ The values of the resistor device parameter TC.


_•_ As node numbers.


and


_•_ Values of most statements (such as .TEMP, .AC, .TRAN etc.)


Specifically included are


_•_ The values of all other device parameters.


_•_ The values in .IC and .NODESET statements.


_•_ The values in .SUBCKT statements.


and


_•_ The values of all model parameters. F.


Operators that can be used in expressions are listed in Table 5.1.


_5.6. EXPRESSIONS_ 47


Table 5.1: Expression operators.


**Operator** **Syntax** **Description**
PLUS _x_ + _y_ plus
MINUS _x_        - _y_ minus
UNARY PLUS + _x_ unary plus
UNARY MINUS        - _x_ unary minus
MULTIPLY _x_        - _y_ multiply
DIVIDE _y_ / _x_ divide
POW _x_ ^ _y_ or _x_ ** _y_ raise to a power, _x_ _[y]_

AND _x_ & _y_ AND
OR _x_ | _y_ OR
NOT ! _x_ NOT
XOR _x y_ XOR (exclusive or)
SIN sin( _x_ ) sine, argument in radians
COS cos( _x_ ) cosine, argument in radians
TAN tan( _x_ ) tangent, argument in radians
ASIN asin( _x_ ) arcsine, argument in radians
ACOS acos( _x_ ) arccosine, argument in radians
ATAN atan( _x_ ) arctangent, argument in radians
SINH sinh( _x_ ) hyperbolic sine
COSH cosh( _x_ ) hyperbolic cosine
TANH tanh( _x_ ) hyperbolic tangent
EXP exp( _x_ ) exponentiation, _e_ _[x]_

ASINH asinh( _x_ ) arc-hyberbolic sine
ACOSH acosh( _x_ ) arc-hyberbolic cosine
ATANH atanh( _x_ ) arc-hyberbolic tangent
ABSSQRT abs(sqrt( _x_ ) _x_ ) absolute,square root, _|x|_ _[√]_ _x_


**5.6.1** **Polynomials**


Polynomial expressions can be used with the controlled source elements (E, F, G and H) to realize nonlinear
controlled sources. The specification of the polynomial must be at the end of the input line and has two
forms. The polynomial format for a voltage-controlled current source (the G element) or a voltage-controlled
voltage source (the E element) is


48 _CHAPTER 5. INPUT FILE_


POLY( _N_ ) ( _NC_ 1+, _NC_ 1 _−_ ) _. . ._ ( _NCN_ +, _NCN_ _−_ ) _C_ 0 _C_ 1 _C_ 2 _C_ 3 _. . ._ where


POLY is the keyword indicating that a polynomial description follows.


_N_ is the degree of the polynomial.


_NC_ 1+, _NC_ 1 _−_ The voltage at the node _NC_ 1+ with respect to the voltage at the node _NC_ 1 _−_ is the controlling
voltage _V_ 1.


_NCN_ +, _NCN_ _−_ The voltage at the node _NCN_ + with respect to the voltage at the node _NCN_ _−_ is the controlling voltage _VN_ .


_C_ 0 _C_ 1 _. . ._ are the polynomial coefficients. Not all of the coefficients need be specified as the trailing
coefficients that are not specified are treated as if they are zero.


Note that in spice parentheses, “(” and “)”, and commas, “,”, are treated as if they are spaces. The use of
parentheses and commas serves only to make the netlist more easily read. **The exception to this is their**
**use in expressions (see section 5.6).**


For voltage-controlled elements the output is calculated as


OUTPUT = _C_ 0
+ _C_ 1 _V_ 1 + _. . ._ + _CN_ _VN_
+ _CN_ +1 _V_ 1 _V_ 1 + _CN_ +2 _V_ 1 _V_ 2 + _. . ._ + _CN_ + _N_ _V_ 1 _VN_
+ _C_ 2 _N_ +1 _V_ 2 _V_ 2 + _C_ 2 _N_ +2 _V_ 2 _V_ 3 + _. . ._ + _C_ 2 _N_ + _N_ _−_ 1 _V_ 2 _VN_
...


+ _CN_ ! _/_ (2( _N_ _−_ 2)!)+2 _N_ _VN_ _VN_
+ _CN_ ! _/_ (2( _N_ _−_ 2)!)+2 _N_ +1 _V_ 1 _V_ 1 _V_ 1 + _CN_ ! _/_ (2( _N_ _−_ 2)!)+2 _N_ +2 _V_ 1 _V_ 1 _V_ 2
+ _. . ._ + _CN_ ! _/_ (2( _N_ _−_ 2)!)+2 _N_ + _N_ _−_ 1 _V_ 1 _V_ 1 _VN_
+ _CN_ ! _/_ (2( _N_ _−_ 2)!)+3 _N_ _V_ 1 _V_ 2 _V_ 2 + _. . ._ + _CN_ ! _/_ (2( _N_ _−_ 2)!)+3 _N_ + _N_ _−_ 2 _V_ 1 _V_ 2 _VN_
...


A one dimensional polynomial (with only one pair of controlling nodes) is evaluated as


OUTPUT = _C_ 0 + _C_ 1 _V_ 1 + _C_ 2 _V_ 1 [2] [+] _[ C]_ [3] _[V]_ 1 [ 3] [+] _[ . . . C][N]_ _[V]_ 1 _[ N]_


An example of a voltage-controlled voltage source is


E1 2 3 POLY(2) (10,0) (12,2) 0.5 1 1 0.2 0.3 0.2


and of a voltage-controlled current source is


G1 2 3 POLY(4) (10,0) (12,2) (11,0) (13,0) 0.5 1 1 1 1 0.2 0.3 0.2


The format for a current-controlled current source (the F element) or a current-controlled voltage source
(the H element) is


_5.7._ _FUNCTION DEFINITION .FUNC_ PSPICE _ONLY_ 49


POLY( _N_ ) _VoltageSourceName_ 1 _. . . VoltageSourceNameN C_ 0 _C_ 1 _C_ 2 _C_ 3 _. . ._ where


POLY is the keyword indicating that that a polynomial description follows.


_N_ is the degree of the polynomial.


_VoltageSourceName_ 1 is the name of the voltage source the current through which is control current _I_ 1.


_VoltageSourceNameN_ is the name of the voltage source the current through which is control current _IN_ .


_C_ 0 _C_ 1 _. . ._ are the polynomial coefficients.


For these elements the output is calculated as


OUTPUT = _C_ 0
+ _C_ 1 _V_ 1 + _. . ._ + _CN_ _VN_
+ _CN_ +1 _V_ 1 _V_ 1 + _CN_ +2 _V_ 1 _V_ 2 + _. . ._ + _CN_ + _N_ _V_ 1 _VN_
+ _C_ 2 _N_ +1 _V_ 2 _V_ 2 + _C_ 2 _N_ +2 _V_ 2 _V_ 3 + _. . ._ + _C_ 2 _N_ + _N_ _−_ 1 _V_ 2 _VN_
...


+ _CN_ ! _/_ (2( _N_ _−_ 2)!)+2 _N_ _VN_ _VN_
+ _CN_ ! _/_ (2( _N_ _−_ 2)!)+2 _N_ +1 _V_ 1 _V_ 1 _V_ 1 + _CN_ ! _/_ (2( _N_ _−_ 2)!)+2 _N_ +2 _V_ 1 _V_ 1 _V_ 2 (5.1)

+ _. . ._ + _CN_ ! _/_ (2( _N_ _−_ 2)!)+2 _N_ + _N_ _−_ 1 _V_ 1 _V_ 1 _VN_
+ _CN_ ! _/_ (2( _N_ _−_ 2)!)+3 _N_ _V_ 1 _V_ 2 _V_ 2 + _. . ._ + _CN_ ! _/_ (2( _N_ _−_ 2)!)+3 _N_ + _N_ _−_ 2 _V_ 1 _V_ 2 _VN_
... (5.2)


An example of a current-controlled voltage source is:


H1 2 3 POLY(2) VIN V2 0.5 1 1 0.2 0.3 0.2


and of a current-controlled current source is:


F1 2 3 POLY(4) VIN V2 (11,0) (13,0) 0.5 1 1 1 1 0.2 0.3 0.2


**5.6.2** **Laplace Expressions**


**5.6.3** **Chebyschev**

##### 5.7 Function Definition .FUNC PSpice Only


The .FUNC statement can be used to conveniently define commonly used expressions.
.FUNC FunctionName( [Argument1, Argument2, _. . ._ Argument10] ] ] ) = FunctionDeclaration
_FunctionName_ is the name of the function being defined. It must begin with an alphabetic character
(A-Z).
_Argument1_ is a function argument. There can be from 0 to 10 arguments.
_FunctionDeclaration_ can be any regular algebraic expression (see section **??** on page **??** ) and can use
previously defined functions and the Laplace variable _s_ . The expression delimiters _{_ and _}_ need not be used.
The _FunctionDeclaration_ is automaticly enclosed within the expression delimiters _{_ and _}_ . The function
declaration plus the two delimiters must be no more than 80 characters (one line) long.
The names of predefined functions msut be avoided. The predefined functions are listed in section **??** on
page **??** .


50 _CHAPTER 5. INPUT FILE_


Functions are treated as macros in the C programming language. when user defined functions are
invoked a textual expansion is performed and the resultant expansion is evaluated as a regular expression.
The FunctionDeclaration before and after expansion is enclosed within expression delimiters _{_ and _}_ . This
defines how nested functions are treated.
It is faster to use predefined functions if available. Predefined functions also test the validity of the
arguments and evaluate the correct asymptotic behavior.

##### **5.8 Syntax Variations**


Commercial versions have enhanced the syntax of Berkeley version of Spice. In virtually all cases the
syntax of Spice2g6 and Spice3is a subset of the syntax of commercial versions of Spice. Here we list some
exceptions.


_•_ Units. Spice does not allow units immediately following a quantity. For example, the following is
acceptable in all versions.
VIN 1 0 DC 4
VIN 1 0 DC 4UV
For example, the following is not acceptable in all Spice2g6 and Spice3
VIN 1 0 DC 4V
but is acceptable in HSpice, PSpiceand SomeVersionsOfSpice.


### **Chapter 6**


##### **Conventions**


Square brackets “[ _. . ._ ] ”indicate an optional quantity.
Italics indicate a quantity that is replaced by a specific value.


_AC Analysis_ 53

### .AC AC Analysis


The .AC statement initializes an AC small-signal analysis sweeping the frequency of the independent
voltage and current sources.
_Form_


.AC DEC _FrequenciesPerDecade FStart FStop_
.AC OCT _FrequenciesPerOctave FStart FStop_
.AC LIN _NumberPoints FStart FStop_


DEC is the decade sweep keyword specifying that the frequency _F_ 1 is to be swept logarithmically
by decades.


_FrequenciesPerDecade_ specifies the number of frequencies per decade.


OCT is the octave sweep keyword specifying that the frequency is to be swept logarithmically by
octaves.


_FrequenciesPerOctave_ specifies the number of frequencies per octave.


LIN is the linear sweep keyword specifying that the frequency is to be swept linearly.


_NumberPoints_ specifies the total number of frequencies in a linear sweep.


_FStart_ is the starting frequency of the frequency sweep.
(Units: Hz; Required; _FStart >_ 0)


_FStop_ is the stopping frequency of the frequency sweep.
(Units: Hz; Required; _FStop ≥_ _FStart_ )


_Example_


.AC DEC 10 1kHz 100Mhz
.AC DEC 10 1kHz 100Mhz


_Note_


1. A DC analysis is automatically performed prior to an AC small-signal analysis to find the operating
point. Using the DC values of voltage and current at the operating point the linearized, small-signal
models of nonlinear devices are determined.


2. In AC analysis voltage sources without AC specifications are shorted and current sources without AC
specifications are opened.


54 _CHAPTER 6. STATEMENT CATALOG_

### COMMENT Comment Card


Used to insert a comment in the circuit NETLIST.
_Form_


    - _a comment string_


_Note_


1. A comment line begins with an asterisk “*” in the first position of the line. There can be no leading
white space.


2. Comment lines can appear anywhere in the input file and are ignored except that they are echoed in
the output log file.


3. In PSpicecomments can appear anywhere on following a semicolon “;”. The remainder of the line
(following the “;”) is ignored except for purposes of echoing the input NETLIST in the log file.


_DC Analysis_ 55

### .DC DC Analysis


In DC analysis the DC operating point of a circuit is determined for a range of values of up to two independent voltage or current sources.


_Form_


.DC _SourceName1 StartValue1 StopValue1 ValueIncrement1_
+ [ _SourceName2 StartValue2 StopValue2 ValueIncrement2_ ]


PSpice _Form_


.DC [LIN ] _SweepVariableName1 StartValue1 StopValue1 ValueIncrement1_
+ [ _SourceName2 StartValue2 StopValue2 ValueIncrement2_ ]


.DC OCT _SweepVariableName1 StartValue1 StopValue1 PointsPerOctave1_
+ _SweepVariableName2 StartValue2 StopValue2 PointsPerOctave2_ ]


.DC DEC _SweepVariableName1 StartValue1 StopValue1 PointsPerDecade1_
+ _SweepVariableName2 StartValue2 StopValue2 PointsPerDecade2_ ]


.DC _SweepVariableName1_ LIST _Value_ 1 _,_ 1 [ _Value_ 1 _,_ 2 _. . . Value_ 1 _,N_ ]
+ [ _SweepVariableName2_ LIST _Value_ 2 _,_ 1 ] _Value_ 2 _,_ 2 _. . . Value_ 2 _,N_ ] ]


56 _CHAPTER 6. STATEMENT CATALOG_


_SourceName1_ is the name of the first independent voltage (V element) or current (I element) source the
value of which will be swept.


_StartValue1_ is the starting value of the sweep of the first voltage or current source.


_StopValue1_ is the final value of the sweep of the first voltage or current source.


_ValueIncrement1_ is the increment by which the value of the first voltage or current source is incremented.


_SourceName2_ is the name of the first independent voltage (V element) or current (I element) source the
value of which will be swept.


_StartValue2_ is the starting value of the sweep of the second voltage or current source.


_StopValue2_ is the final value of the sweep of the second voltage or current source.


_ValueIncrement2_ is the increment by which the value of the second voltage or current source is incremented.


LIN is the linear sweep keyword. This is the default sweep type.


OCT is the octave sweep keyword specifying that the sweep variable or variables is to be swept
logarithmically by octaves.


DEC is the decade sweep keyword specifying that the sweep variable or variables is to be swept
logarithmically by decades.


_PointsPerOctave1_ is the number of points per octave in a OCT sweep type for the first sweep.


_PointsPerDecade1_ is the number of points per decade in a DEC sweep type for the first sweep.


_PointsPerOctave2_ is the number of points per octave in a OCT sweep type for the second sweep.


_PointsPerDecade2_ is the number of points per decade in a DEC sweep type for the second sweep.


_SweepVariableName1_ is the name of the first sweep variable. The sweep variable can be:


1. the name of an independent voltage or current source. The _DCvalue_ of the source is
swept.


2. the name of a parameter of a specific model specified in the form _ModelName_ ( _ParameterKeyword_ ).
For example to sweep the IS parameter of an NPN model of name MYNPN the _Sweep-_
_VariableName_ would be MYNPN(IS).

3. the keyword TEMP which indicates that the analysis temperature in _[◦]_ C is swept. The
model parameters are updated for each sweep value.


_SweepVariableName2_ is the name of the second sweep variable. The properties are as for _SweepVariable-_
_Name1_ as described above.


LIST indicates that the value of the _SweepVariable_ will take the values, in order, in the following
list rather than be swept.


_Value i,j_ the _j_ th value to be assigned to the _i_ th sweep variable.


_Example_


.DC VIN 0.25 5.0 0.25
.DC VDS 0 10 .5 VGS 0 5 1
.DC VCE 0 10 .25 IB 0 10U 1U


_DC Analysis_ 57


PSpice _Example_


.DC VIN 0.25 5.0 0.25
.DC VDS 0 10 .5 VGS 0 5 1
.DC VCE 0 10 .25 IB 0 10U 1U
.DC LIN VCE 0 10 .25 IB 0 10U 1U
.DC DEC MYNPN(IS) 1.E-15 1.e-17 3
.DC TEMP -25 0 25 50 75 100 VIN 0.25 5.0 0.25


_Note_


1. The .DC statement initiates a DC operating point analysis.


2. In the DC analysis inductors are shorted and capacitors are open circuited.


3. A DC analysis over a range of source conditions can be used to produce the transfer characteristic of a
circuit or current-voltage characteristics of a semiconductor device such as a transistor. An example of
determining the transfer characteristic of an operational amplifier is given in section 8.5.1. An example
of determining the current-voltage characteristics of a transistor is in section 8.5.1.


3 A DC analysis over a range of source conditions can also be used to provide biasing information in
circuit design.


4 The specified independent voltage or current source or sources are stepped over a user-specified range
and the DC output variables indicated by the .PRINT statement are stored for each source value.


5 When two sources are specified the first source is swept over its range for each value of the second
source. For example, consider
.DC VDS 0 10 5 VGS 0 5 2.5
VGS is swept from 0 to 5V in 2.5V increments. For each value of VGS VDS is swept from 0 to 10V in 5V
increments so that that 9 DC analyses performed are


RUN VDS VGS
1 0 0
2 5 0
3 10 0
4 0 2.5
5 5 2.5
6 10 2.5
7 0 5
8 5 5
9 10 5


6 When the sweep is completed the original values are restored.


7 The sweep can go in either direction. That is, _StartValue_ can be less than or greater than _StopValue_
but _ValueIncrement_ must be positive.


58 _CHAPTER 6. STATEMENT CATALOG_

### .DISTO Small-Signal Distortion Analysis


In distortion analysis the steady-state harmonic and intermodulation products for small input signal are
computed as a part of an AC analysis. One or two excitation frequencies, _F_ 1 and _F_ 2 may be specified. If only
one excitation frequency, _F_ 1, is specified the program evaluates the second and third harmonic distortions. If
a second excitation frequency, _F_ 2, is specified the three lowest order intermodulation distortion components
are evaluated as well.
_Form_


.DISTO _ResistorName_ [ _OutputInterval_ [ _F_ 2 _OverF_ 1 [ _F_ 1 _ReferencePower_
+ [ _F_ 2 _ReferencePower_ ] ] ] ]


Spice3 _Form_


.DISTO DEC _FrequenciesPerDecade F_ 1 _Start F_ 1 _Stop_ [ _F_ 2 _OverF_ 1 ]
.DISTO OCT _FrequenciesPerOctave F_ 1 _Start F_ 1 _Stop_ [ _F_ 2 _OverF_ 1 ]
.DISTO LIN _NumberPoints F_ 1 _Start F_ 1 _Stop_ [ _F_ 2 _OverF_ 1]


_ResistorName_ the name of the output resistor. The power dissipated in this resistor is reported as the
distortion measures. Spice2g6 only.


_OutputInterval_ is the optional output reporting interval at which distortion components produced by all
nonlinear components is reported. By default, or if omitted no detailed output is produced.
Spice2g6 only.


_F_ 1 _ReferencePower_ power level of _F_ 1. Spice2g6 only.
(Units: W; Optional; Default: 1.0E-3 (i.e. 1 mW or 1 dBm))


_F_ 2 _ReferencePower_ power level of _F_ 2. Spice2g6 only.
(Units: W; Optional; Default: 1.0E-3 (i.e. 1 mW or 1 dBm))


DEC is the decade sweep keyword specifying that the frequency _F_ 1 is to be swept logarithmically
by decades.


_FrequenciesPerDecade_ specifies the number of frequencies per decade.


OCT is the octave sweep keyword specifying that the frequency _F_ 1 is to be swept logarithmically
by octaves.


_FrequenciesPerOctave_ specifies the number of frequencies per octave.


LIN is the linear sweep keyword specifying that the frequency _F_ 1 is to be swept linearly.


_NumberPoints_ specifies the total number of frequencies in a linear sweep.


_F_ 1 _Start_ is the starting frequency of the _F_ 1 sweep.


_F_ 1 _Stop_ is the stopping frequency of the _F_ 1 sweep.


_F_ 2 _OverF_ 1 is the ratio of _F_ 2 to _F_ 1.
In Spice3, if _F_ 2 _OverF_ 1 is omitted an harmonic analysis only is reported. Otherwise
_F_ 2 = _F_ 2 _OverF_ 1 _F_ 1 _Start_
In Spice2g6, if _F_ 2 _OverF_ 1 is omitted it defaults to 0.9. _F_ 2 = _F_ 2 _OverF_ 1 _F_ 1


_Small-Signal Distortion Analysis_ 59


_F_ 2 _OverF_ 1 should be an irrational number between 0.0 and 1.0. If it is a rational number the
signals at _F_ 1 and _F_ 2 are harmonically related and the spectral analysis may in error. Since
an irrational number can not actually be specified care should be excercized in choosing
_F_ 2 _OverF_ 1 so that _F_ 1 and _F_ 2 are not simple multiples of each other. For example, use 0.498
instead, if you want to set _F_ 2 _OverF_ 1 to 0.5. The rule to follow is to keep the denominator
in the fractional representation of _F_ 2 _OverF_ 1 as large as possible with at least three digits
for accurate results.


_Example_


.DISTO DEC 10 1kHz 100Mhz
.DISTO DEC 10 1kHz 100Mhz 0.9


_Note_


1. In Spice2g6 the distortion analysis must be performed in conjunction with an AC analysis. The .AC
statement (see page 53) specifies the sweep parameters for _F_ 1.


2. In Spice3 the distortion analysis is also performed in conjunction with the AC analysis specified by the
.AC statement. The amplitudes and relative phases of the input distortion components are specified
in the .AC statement as the arguments of the DISTOF1 keyword for _F_ 1 and of the DISTOF2 keyword
for _F_ 2. This enables several sources to generate components at _F_ 1 and/or _F_ 2. If the DISTOF1 or
DISTOF2 keywords are missing from a source then this source is assumed to have no input at _F_ 1 or
_F_ 2 respectively.


When a spectral analysis is performed (both _F_ 1 and _F_ 2 specified) the circuit is treated as having
sinusoidal inputs at two different frequencies _F_ 1 and _F_ 2. _F_ 1 is swept but _F_ 2 is fixed at _F_ 2 _OverF_ 1 _FStart_ .
Each independent source in the circuit can have two inputs at _F_ 1 and _F_ 2 for distortion analysis.


_Note_


3 Distortion analysis is not valid if switches (if present) change state under the small excitations used
for distortion calculations.


4 Evaluation of the small-signal distortion of a circuit is based on a multi-dimensional Volterra series
analysis. The nonlinearities are expanded in a third order multi-dimensional Taylor series around the
operating point determined from an operating point (DC) analysis. Using this analysis the distortion
components are evaluated symbolically


5 In Spice2g6 the following distortion components are evaluated.


60 _CHAPTER 6. STATEMENT CATALOG_


HD2      - the magnitude of the second harmonic at frequency 2 _F_ 1
assuming that _F_ 2 is not present.
HD3      - the magnitude of the third harmonic at frequency 3 _F_ 1 assuming that _F_ 2 is not present.
SIM2      - the magnitude of the sum frequency _F_ 1 + _F_ 2
DIM2      - the magnitude of the difference frequency _F_ 1 _−_ _F_ 2
DIM3      - the magnitude of the third order intermodulation frequency 2 _F_ 1 _−_ _F_ 2


1. In Spice3 the complex values of the above distortion components are computed at all nodes in the
circuit. The distortion components at any node can be reported using the .PRINT statement (discussed
on page 92) or the .PLOT statement (discussed on page 88). The running variable in the output is the
frequency _F_ 1.


2. The quantities reported are the actual AC voltages and currents and must be normalized by the user
to the sources at _F_ 1 and _F_ 2 to obtain true distortion measures.


_Distribution Specification_ 61

### .DISTRIBUTION Distribution Specification


The .DISTRIBUTION statement specifies the statistical tolerance distribution used in Monte Carlo analysis
(see the .MC statement on page 69).
PSpice _Form_


.DISTRIBUTION _DistributionName_ ( _Deviation1, Probability1_ )
+ ( _Deviation2, Probability2_ ) [( _Deviation3, Probability3_ ) _..._ ]


_DistributionName_ is the name the user assigns to the distribution defined by the succeeding values.


_Deviation_ Relative deviation from nominal value.
( _−_ 1 _≤_ _Deviation ≤_ 1).


_Probability_ Probability of preceding deviation.
( _Probability ≥_ 0)


_Note_


1. Parentheses, ‘(’ and ‘)’, and commas, ‘,’, in the NETLIST are ignored and are generally used to make
the NETLIST more readable.


2. The pairs of values ( _Deviation_, _Probability_ ) define a piecewise linear probability distribution curve used
in calculating the random numbers used in Monte Carlo analysis.


3. The _Deviation_ s must be in ascending order:
_Deviation1 < Deviation2 < Deviation3 < . . ._


4. 100 ( _Deviation_, _Probability_ ) pairs can be specified.


62 _CHAPTER 6. STATEMENT CATALOG_

### .END End Statement


This statement indicates the end of the NETLIST of a circuit. While it is often inserted automatically
by most Spice simulators when the last statement of the NETLIST is read and it is not .END its usage is
recommended as several circuits in one file are supported by some versions of Spice including PSpice.
_Form_


.END


_End Subcircuit Statement_ 63

### .ENDS End Subcircuit Statement


The end subcircuit statement indicates the end of a subcircuit definition.
_Form_


.ENDS [ _SubcircuitName_ ]


_SubcircuitName_ Indicates which subcircuit is being terminated. If omitted, all subcircuits being defined are
terminated. Its use is required when nested subcircuit definitions are being made. It is good
practise to use the full form of .ENDS.


_Example_


.ENDS NAND GATE


_Note_


1. See the definition of .SUBCKT on page 103.


64 _CHAPTER 6. STATEMENT CATALOG_

### .FOUR Fourier Analysis


The Fourier analysis statement initiates a Fourier analysis of the results of a transient analysis.
_Form_


.FOUR _Frequency OutputSpecification_ [ _OutputSpecification . . ._ ]


_Frequency_ specifies the fundamental frequency of the transient waveform to be analyzed. It is used to
determine the period of the waveform.


_OutputSpecification_ specifies the quantity to be reported as the result of the Fourier Analysis. It has the
same format as the _OutputSpecification_ in a .PRINT statement (see page 92).


_Example_


.FOUR 1M V(10,2) V(5) I(VLOAD)


_Note_


1. Fourier analysis uses the transient output waveform in the time interval from TSTOP _−_ _T_ to TSTOP. _T_
is the period of the _Frequency_ parameter ( _T_ = 1 _/Frequency_ ) specified in the .FOUR statement. TSTOP
is the final transient analysis time specified in the .TRAN statement (which is described on page 109.


2. Unlike most other analyses, a .PRINT, .PROBE or .PLOT statement is not required for the data to be
reported.


_Function Definition_ 65

### .FUNC Function Definition


In this statement commonly used expressions can be defined as more convenient functions.
PSpice _Form_


.FUNC _FunctionName_ ( [ _Argument1, Argument2, . . . Argument10_ ] ] ] ) _= Function-_
_Declaration_


_FunctionName_ is the name of the function being defined. It must begin with an alphabetic character (A-Z).


_Argument1_ is a function argument. There can be from 0 to 10 arguments.


_FunctionDeclaration_ can be any regular algebraic expression (see section **??** on page **??** ) and can use previously defined functions and the Laplace variable _s_ . The expression delimiters _{_ and _}_
need not be used. The _FunctionDeclaration_ is automatically enclosed within the expression
delimiters _{_ and _}_ . The function declaration plus the two delimiters must be no more than
80 characters (one line) long.


_Example_


.FUNC


_Note_


1. The names of predefined functions must be avoided. The predefined functions are listed in section **??**
on page **??** .


2. Functions are treated as macros in the C programming language. when user defined functions are
invoked a textual expansion is performed and the resultant expansion is evaluated as a regular expression. The FunctionDeclaration before and after expansion is enclosed within expression delimiters _{_
and _}_ . This defines how nested functions are treated.


3. It is faster to use predefined functions if available. Predefined functions also test the validity of the
arguments and evaluate the correct as asymptotic behavior.


66 _CHAPTER 6. STATEMENT CATALOG_

### .IC Initial Conditions


The .IC statement is used to set initial conditions for transient analysis. It has no effect on other types
of analyses.
_Form_


.IC V( _NodeName1_ ) _=Voltage1_ [ _V(NodeName2_ ) _=Voltage2 . . ._ ]


V is the keyword specifying a node voltage


_NodeName_ is the name of a node. Note that in Spice2g6 and Spice3 _NodeName_ must be an integer.


_Voltage_ is a numeric value.


_Example_


.IC V(11)=4.9 V(2)=2.5


_Note_


1. Initial conditions can be specified for the following elements: B (MESFET), C (capacitor), D (diode), Q
(BJT), M (MOSFET) and J (JFET)


2. The .IC statement has two different effects depending on whether the UIC (use initial conditions)
keyword is present on the .TRAN statement.


(a) If the UIC keyword is specified in the .TRAN statement:
The initial conditions specified in the .IC statement are used to establish the initial conditions.
Initial conditions specified for individual elements using the IC parameter on the element line will
always have precedence over those specified in a .IC statement.
No DC analysis is performed prior to a transient analysis. Thus it is important to establish the
initial conditions at all nodes using the .IC statement or using the IC element parameter.


(b) If the UIC keyword is not specified in the .TRAN statement:
A DC analysis is performed prior to a transient analysis. During the DC analysis the node voltages
indicated in the .IC statement are held constant at the initial condition values. During transient
analysis the nodes are not constrained to the initial condition values.


_Include Statement_ 67

### .INC Include Statement


_Form_


.INC _FileName_


_Filename_ is the name of the file which is to be included.


_Note_


1. The contents of _Filename_ are read as if it were part of the original file.


2. Libraries could be included using the .INC statement or by the .LIB statement discussed on page 68.
The difference is that the .INC statement includes the contents of the library file (except for comments)
in internal data structures. However a .LIB statement causes the library file to be scanned and an
index constructed for model (.MODEL) and subcircuit (.SUBCKT) statements. The models subcircuits
in the library file are included in internal data structures if they are referred to. Thus the use of .LIB
statements is a much more efficient way of using library files leading to both a smaller program and
faster library access, especially for large libraries. Library files can only contain models and subcircuits
so that the type of files that can be incorporated using a .LIB statement is more restricted than the
type of file that can be incorporated using a .INC statement.


68 _CHAPTER 6. STATEMENT CATALOG_

### .LIB Library Statement


The .LIB statement is an efficient way to include .MODEL statements and subcircuits.
_Form_


.LIB [ _FileName_ ]


_Filename_ is the name of the library file. (Optional; Default: NOM.LIB)


_Note_


1. The library file can only contain a restricted set of Spice statements. It must contain only .MODEL
statements, subcircuit definitions (between .SUBCKT and .ENDS statements), and .LIB statements.


2. The library file _Filename_ is searched in the current directory and then in a list of directories specified by
the environment variable PSPICELIB (for compatibility purposes the environment variable PSPICELIB
is also supported).


3. If the DOS operating system is being used the library environment specification has the form


SET PSPICELIB = _Directory1_ [; _Directory2 . . ._ ]


The environment variable may be set in the AUTOEXEC.BAT file in the root DOS directory or before
PSpice is evoked. For example:


SET PSPICELIB = C: _\_ SPICE _\_ MY LIB;D: _\_ SPICE _\_ TI LIB


4. If the UNIX operating system is being used the library environment specification has the form


setenv PSPICELIB = _Directory1_ [; _Directory2 . . ._ ]


For example:


setenv PSPICELIB = /SPICE/MY LIB; /SPICE/TI LIB


5. Libraries could be included using the .INC statement or by the .LIB statement. The difference is that
the .INC statement includes the contents of the library file (except for comments) in internal data
structures. However a .LIB statement causes the library file to be scanned and an index constructed
of model (.MODEL) and subcircuit (.SUBCKT) statements. The models subcircuits in the library file are
included in internal data structures only if they are referred to. Thus the use of .LIB statements is
a much more efficient way of using library files leading to both a smaller program and faster library
access, especially for large libraries.


_Monte Carlo Analysis_ 69

### .MC Monte Carlo Analysis


The Monte Carlo analysis is a statistical analysis of the circuit causing the circuit to be analyzed many
times with a random change of model parameters (parameters in a .MODEL statement).
PSpice _Form_


.MC _NumberOfRuns AnalysisType OutputSpecification OutputFunction_ [LIST]
+ [OUTPUT( _OutputSampleType_ )]


PSpice _Form_


.MC _NumberOfRuns AnalysisType OutputSpecification OutputFunction_ [LIST]
+ [OUTPUT( _OutputSampleType_ )] [RANGE( _LowValue_, _HighValue_ )]
+ [SEED= _SeedValue_ ]


_NumberOfRuns_ is the total number of runs to do. This number includes the initial nominal run.


_AnalysisType_ is the type of analysis to be performed in the Monte Carlo runs after the initial nominal run
(using the nominal values of model parameters). All analyses specified in the NETLIST are
performed in the nominal run. The _AnalysisType_ must be one of the following:


DC is a keyword indicating that the DC analysis as specified by the .DC statement is repeated. The sweep variable used in analyzing the output _Out-_
_putSpecification_ is the value of the independent voltage or current source
specified in the .DC statement (as discussed on page 55).


AC is a keyword indicating that the AC small-signal analysis as specified by the
.AC statement is repeated. The sweep variable used in analyzing the output
_OutputSpecification_ is frequency.


TRAN is a keyword indicating that the transient analysis as specified by the .TRAN
statement is repeated. The sweep variable used in analyzing the output
_OutputSpecification_ is time.


_OutputSpecification_ specifies the quantity to be reported as the result of the Monte Carlo Analysis. It has
the same format as the _OutputSpecification_ in a .PRINT statement (see page 92). The result
is the value of the _OutputSpecification_ with respect to a sweep for DC and AC analysis, and
as a waveform for TRAN analysis.


70 _CHAPTER 6. STATEMENT CATALOG_


_OutputFunction_ indicates the function to be performed on the output indicated by _OutputSpecification_ to reduce the sweep or waveform at each run to a single numeric value. The _OutputSpecification_
must be one of the following keywords:


YMAX which produces the greatest deviation of the sweep or waveform from the
nominal run.


MAX which results in the maximum value in each sweep or waveform.


MIN which results in the minimum value in each sweep or waveform.


RISE EDGE( _Value_ ) which reports as the result the first run when the waveform crosses above
the threshold _Value_ . The algorithm used requires that one point in the
waveform be below _Value_ and the succeeding point be above _Value_ .


FALL EDGE( _Value_ ) which reports as the result the first run when the waveform crosses below
the threshold _Value_ . The algorithm used requires that one point in the
waveform be above _Value_ and the succeeding point be below _Value_ .


LIST is an optional keyword that results in the model parameter values that are statistically
varied being printed out prior to each run. If it is omitted then the statistically generated
model parameter values are not produced prior to each run.


OUTPUT is an optional keyword indicating the type of output to be produced by runs after the initial
nominal run. The output produced for each run sampled is determined by the .PLOT, .PRINT
and .PROBE statements in the NETLIST. If this keyword is missing output is produced only
for the nominal run.


_OutputSampleType_ indicates the method by which runs are selected for output reporting. The output produced for each run selected is determined by the .PLOT, .PRINT and .PROBE statements in
the NETLIST. _OutputSampleType_ must be one of the following:


ALL indicates that the output is to be produced for all runs.


FIRST _Nruns_ indicates that the output is to be produced only for the first _Nruns_ runs.


EVERY _NthRun_ indicates that the output is to be produced for _NthRun_ th run.


RUNS _Run1_ [ _Run2 ..._ [ _Run25_ ] ] indicates that the output is to be produced for the indicated runs. Up to 25 runs can be indicated.


RANGE is an optional range indicating the range of the sweep variable over which _OutputFunction_
is to be performed. If this keyword is missing, output is produced but the range is not
restricted. The range of the sweep variable to be considered is from _LowValue_ to _HighValue_
inclusive.


_LowValue_ is the low end of the sweep variable to be considered in evaluating _OutputFunction_ .


_HighValue_ is the low end of the sweep variable to be considered in evaluating _OutputFunction_ .


SEED is the keyword for the seed of the random number generator used in Monte Carlo Analysis


_SeedValue_ is the value of the seed used in the random number generator used to select sample runs at
random. (Optional; Default: 17,533; 1 _≤_ _SeedValue≤_ 32 _,_ 767)


_Note_


_Monte Carlo Analysis_ 71


1. A typical use of Monte Carlo analysis is to predict yield of a circuit by examining the effect of process
variations such as length and width of transistors.


2. A .TEMP statement also can result in multiple circuit simulations as the temperature is varied. In
conjunction with a .MC statement a Monte Carlo analysis is performed for each temperature before the
temperature is updated in a temperature sweep.


3. Only model parameters (parameters in a .MODEL statement) are varied.


4. If the _AnalysisType_ is DC only one independent voltage or current source can be specified in the .DC
statement (discussed on page 55).


5. The random number generator is the subtractive method generator described by Knuth [28, p. 171].


6. The initial run uses the nominal parameter values given in the NETLIST. Subsequent runs statistically
vary model parameters indicated as having either lot LOT or device DEV tolerances. These tolerances
are specified in a .MODEL statement (see page 72).


_Method_
The initial Run of a Monte Carlo Analysis uses the nominal values of the model parameters possibly updated
to their new values if the analysis temperature is different from the the nominal temperature in effect when
the .MODEL statement was read. The nominal values of the model parameters as well as their tolerances and
type of statistical distribution are specified in a .MODEL statement (see page 72). If _X_ ( _T_ ) is the value of
the model parameter at temperature _T_, _r_ is a random number between _−_ 1 and +1 inclusive, and _XT_ is the
tolerance of _X_ ( _T_ NOM) is the nominal temperature, the value of X to be used in Monte Carlo analysis is


_X_ _[′]_ ( _T_ ) = _X_ ( _T_ )(1 + _rXT_ ) (6.1)


The random number _r_ has a statistical distribution which has a type indicated in the .MODEL statement. The distribution type must be either one of the built-in distributions or specified by the user in a
.DISTRIBUTION statement (see page 61). The tolerance is specified immediately following the distribution
in a .MODEL statement. Specification of the distribution type and tolerance assignment are described on
page 74.


72 _CHAPTER 6. STATEMENT CATALOG_

### .MODEL Model Statement


Model statements specify the parameters of elements that either are too numerous to put on the element
line or are common to many elements.


_Form_


.MODEL _ModelName ModelType_ ( _Keyword=Value ..._ )


PSpice _Form_


.MODEL _ModelName ModelType_ ( _Keyword=Value_ [ _ToleranceSpecification_ ] _. . ._ )


_ModelName_ is the name of the model specified by the user.


_ModelType_ is the model type which is specific to particular elements. The model types are given in the
table below.


_ToleranceSpecification_ is the specification of the statistical distribution and tolerance of a parameter. This
is used in a Monte Carlo simulation to assign random variations to the model parameter.
_ToleranceSpecification_ is discussed on page 74.


_Keyword_ is the name of the model parameter which is discussed on the pages referred to below.


_Value_ is the numeric value of the model parameter.


_Example_


.MODEL MOSFET1 MOS (LEVEL=2 VTO=-0.76 GAMMA=0.6 CGSO=3.35E-10)


_Model Statement_ 73


MODEL SPICE ELEMENT DESCRIPTION PAGE
TYPE VERSION— NAME

PASSIVE DEVICE MODELS
RES R resistor model 236, 237
CAP C capacitor model 150, 150
IND PSpice L inductor model 187

SEMICONDUCTOR DEVICE MODELS
D D diode model 152
NPN Q NPN bjt model 228
PNP Q PNP bjt model 228
LPNP PSpice Q Lateral PNP bjt model 228
NJF J N-channel junction FET (JFET) 175
PJF J P-channel junction FET (JFET) 176
GASFET PSpice B N-channel GaAs MESFET 264, 118
NMF Spice3 B N-channel GaAs MESFET
PMF Spice3 B P-channel GaAs MESFET
NMOS M N-channel MOSFET 191
PMOS M P-channel MOSFET 191
SWMODEL Spice3 **??**
URC Spice3 T Lossy RC transmission line 243

MISCELLANEOUS DEVICE MODELS
CORE PSpice K nonlinear, transformer (magnetic core) 183
VSWITCH PSpice S voltage switch 240
ISWITCH PSpice W current switch 254
SW Spice3 **??**
CSW Spice3 **??**

DISTRIBUTED DEVICE MODELS
URC Uniform Distributed RC model 243


MODEL SPICE ELEMENT DESCRIPTION PAGE
TYPE VERSION NAME

DIGITAL INTERFACE AND DIGITAL DEVICE MODELS
DINPUT PSpice N digital input model 222
DOUTPUT PSpice O digital output model 224
UIO PSpice U digital I/O model
UGATE PSpice U standard gate
UTGATE PSpice U tri-state gate
UEFF PSpice U edge-triggered flip-flop
UGFF PSpice U gated flip-flop
UWDTH PSpice U pulse width checker
USUHD PSpice U setup and hold checker
UDLY PSpice U digital delay line
UADC PSpice U multi-bit analog-to-digital converter
UDAC PSpice U multi-bit digital-to-analog converter


Virtually all of the device model parameters have default values which generally result in typical operation.


_Tolerance and Distribution Assignment_


74 _CHAPTER 6. STATEMENT CATALOG_


Immediately following the specification of a model parameter a statistical distribution and tolerance can be
assigned. These are used in conjunction with Monte Carlo analysis which is controlled by the .MC statement
described on page 69 The Monte Carlo analysis is a statistical analysis of the circuit causing the circuit to
be analyzed many times with a random change of certain model parameters). The form of the tolerance and
distribution assignment is


DEV [/DeviceTrackingIndex] [/ _DistributionType_ ] Tolerance [%]
+ LOT [/LotTrackingIndex] [/ _DistributionType_ ] Tolerance [%]


DEV is the keyword for the device tolerance specification.


_DeviceTrackingIndex_ specifies which random number to use. It must be one of 1, 2, ... 10. Two parameters
with the same _DeviceTrackingIndex_ are correlated. Conversely if two parameters have different _DeviceTrackingIndex_ then they are uncorrelated.
_LotTrackingIndex_ and _DeviceTrackingIndex_ refer to different random numbers and so choosing the same _LotTrackingIndex_ and _DeviceTrackingIndex_ does not correlate the LOT and DEV
distributions.
(Units: none; Optional; Default: 1)


_DistributionType_ is the type of the statistical distribution used in generating random numbers. There are
two predefined distribution types and a user specified distribution type can be used. The
allowable types are:


UNIFORM specifies a uniform distribution of random numbers between -1 and +1.


GAUSS specifies a Gaussian distribution of random numbers between _±_ 4 _σ_ . In this
case _Tolerance_ specifies _σ_ .


_DistributionName_ is the name of a user specified distribution specified in a .DISTRIBUTION
statement (see page 61).


_LotTolerance_ is the lot tolerance specification. It may be specified as an absolute quantity or as a percentage if followed by %. It is converted to a fraction of the nominal value. The magnitude
of the fractional value must be _≤_ 1.


LOT is the keyword for the lot tolerance specification.


_LotTrackingIndex_ specifies which random number to use. It must be one of 1, 2, ... 10. Two parameters
with the same _LotTrackingIndex_ are correlated. Conversely two parameters have different
_LotTrackingIndex_ ’s then they are uncorrelated.
_LotTrackingIndex_ and _DeviceTrackingIndex_ refer to different random numbers and so choosing the same _LotTrackingIndex_ and _DeviceTrackingIndex_ does not correlate the LOT and DEV
distributions.
(Units: none; Optional; Default: 1)


_DeviceTolerance_ is the device tolerance specification. It may be specified as an absolute quantity or as
a percentage if followed by %. It is converted to a fraction of the nominal value. The
magnitude of the fractional value must be _≤_ 1.


_Example_


.MODEL


_Note_


_Model Statement_ 75


1. Both lot (LOT) and device (DEV) tolerances can be specified separately. Lot and device tolerances
combine for the purposes of determining the total tolerance of a model parameter. The sum of device
and lot tolerances must be less than the nominal model parameter value (i.e. is less than 100%).


2. A total of 20 random number are generated internally. Of these 10 are for lot tolerancing and 10 are
for device tolerancing. Parameters with the same lot tolerance index ( _LotToleranceIndex_ ) use the same
random number to generate statistical variations and so are fully correlated. Similarly parameters
with the same device tolerance index ( _DeviceToleranceIndex_ ) use the same random number. However
the random number for a lot and that for a device are always uncorrelated. If _X_ ( _T_ ) is the value of
a model parameter at temperature _T_, _R_ LOT( _LotToleranceIndex_ ) is random number for lot variations
and _R_ DEV( _DeviceToleranceIndex_ ) is random number for device variations, _X_ LOT is the fractional lot
tolerance _X_ DEV is the fractional device tolerance, the value used in a Monte Carlo simulation is


_X_ _[′]_ ( _T_ ) = _X_ ( _T_ ) (1 + _R_ LOT( _LotTrackingIndex_ ) _X_ LOT + _R_ DEV( _DeviceTrackingIndex_ ) _X_ DEV) (6.2)


76 _CHAPTER 6. STATEMENT CATALOG_

### .NODESET Node Voltage Initialization


_Form_


.NODESET V( _NodeName_ ) _=Voltage_ [V( _NodeName_ ) _=Voltage . . ._ ]


_V_ is the keyword specifying a node voltage


_NodeName_ is the name of a node. Note that in Spice2g6 and Spice3 _NodeName_ must be an integer.


_Example_


.NODESET V(11)=4.9 V(2)=2.5


_Note_


1. This statement can be used if convergence problems are encountered in a DC analysis. For most circuits
Spice will be able to determine the DC voltage or initial transient solution.


2. The statement can be used with astable circuits such as multivibrators and flip flops to ensure that
these circuits are initialized in a particular state.


_Small-Signal Noise Analysis_ 77

### .NOISE Small-Signal Noise Analysis


In noise analysis the noise generated by active devices and resistors is evaluated.
_Form_


.NOISE _OutputVoltageSpecification InputSourceName OutputInterval_


Spice3 _Form_


.NOISE _OutputVoltageSpecification InputSourceName_ DEC
+ _FrequenciesPerDecade FStart FStop_ [ _OutputInterval_ ]


.NOISE _OutputVoltageSpecification InputSourceName_ OCT
+ _FrequenciesPerOctave FStart FStop_ [ _OutputInterval_ ]


.NOISE _OutputVoltageSpecification InputSourceName_ LIN
+ _NumberPoints FStart FStop OutputInterval_


_OutputVoltageSpecification_ is a specification of an output voltage which is to be the output of the noise
analysis. It acts as a summing point for the noise contributions of the individual noise
current generators. The noise voltage appearing at the output for each noise generator is
summed in the RMS sense. Any voltage specification may be used including the voltage
at a node, e.g. using V(5), or the voltage between nodes, e.g. using V(5,3). The noise is _√_
reported in units of V/ Hz.



_InputSourceName_ is the name of the independent voltage (V) or current (I) source that is to be the input
reference source to which equivalent input noise is referred. The input source does not
produce noise itself. If the input source is an independent voltage source then the equivalent _√_
input noise is reported in units of V/ Hz. If the input source is an independent current



input noise is reported in units of V/ Hz. If the input source is an independent current _√_

source then the equivalent input noise is reported in units of A/ Hz.



Hz.



_OutputInterval_ is the optional output reporting interval at which the values of the noise current generators internal to the elements of the circuit are reported. The report is produced every
_OutputInterval_ th frequency. If zero or omitted no detailed output is produced.


DEC is the decade sweep keyword specifying that the noise analysis is to be evaluated at a number
of frequency points. The frequency is swept logarithmically by decades.


_FrequenciesPerDecade_ specifies the number of frequencies per decade.


OCT is the octave sweep keyword specifying that the noise analysis is to be evaluated at a number
of frequency points. The frequency is swept logarithmically by octaves.


_FrequenciesPerOctave_ specifies the number of frequencies per octave.


LIN is the linear frequency sweep keyword. At each frequency a noise analysis is performed.


_NumberPoints_ specifies the total number of frequencies in a linear sweep.


_FStart_ is the starting frequency of the sweep.


_FStop_ is the stopping frequency of the sweep.


_Example_


78 _CHAPTER 6. STATEMENT CATALOG_


.NOISE V(5) VIN DEC 10 1kHZ 100Mhz
.NOISE V(5,3) V1 OCT 8 1.0 1.0e6 1


_Example_


.NOISE V(5) VIN
.NOISE V(5,3) I1


_Note_


1. In noise analysis the noise generated by active devices and resistors is evaluated as a noise spectral
density. The densities are integrated over the the range of frequencies to obtain a gross noise measure
for the circuit (for the specified frequency range). The finer the frequency spacing the more accurate
will be the noise analysis. The noise contributions of individual noise generators are summed at the
node or branch specified by _OutputVoltageSpecification_ . The noise at this output port is reported as
well as the equivalent input noise (the output noise referred to the input) at the input source identified
by _InputSourceName_ .


2. Two types of output are produced by noise analysis:


(a) noise spectral density versus frequency, and


(b) total integrated noise over the specified frequency range.


3. In Spice3 the AC frequency sweep for noise analysis must be specified in the .NOISE statement. In
PSpice the frequency sweep specified in the .AC statement is used.


4. The noise table is produced while analysis is being performed. Noise reporting is produced using the
.PRINT and .PLOT statements.


5. Noise is generated by resistors and by semiconductor devices. Resistors generate thermal noise while
the noise model of semiconductor devices includes thermal noise, shot noise and flicker noise. Noise
models of individual elements are discussed in the element catalog beginning on page 115.


_Two-Port Noise and Gain Calculations_

This is supported in a few versions of Spice.
For all circuits the output ONOISE and effective input noise INOISE are calculated. Also the voltage gain
GAIN is calculated as the output voltage devided by the voltage across the source. Extended gain and noise
parameters are available if the circuit is defined as a two port. The two-port parameters that are calculated
are defined in terms of the signal and noise powers shown in Fig. 6.1 The actual noise and signal powers that
are delivered to the circuit are _Pi_ and _Ni_ . Also the actual noise and signal powers that are delivered to the
load resistance are _Po_ an _No_ . The available noise and signal powers are the powers that would be delivered
to the circuit with ideal lossless matching networks. That is, when the input and output impedances equal
the source ( _RS_ ) and load ( _RL_ ) resistances — so that _Pi_ = _PAi_ and _Po_ = _PAo_ ; and _NI_ = _NA_ and _NO_ = _NA_ .
Two-port noise analysis yields the following quantities which can be specified in the .PRINT and .PLOT
statements: _√_
ONOISE     - _VNO_ RMS output noise voltage in V/ Hz



ONOISE - _VNO_ RMS output noise voltage in V/ Hz _√_

INOISE - _VNO_ RMS equivalent input noise voltage in V/



INOISE - _VNO_ RMS equivalent input noise voltage in V/ Hz

GAIN - _G_ voltage gain
GT - _GT_ transducer gain
NF - _NF_ _[′]_ spot noise factor
SNR - SNR _i_ output voltage signal-to-noise ratio
TNOISE - _T_ NOISE output noise temperature in celsius.


_Small-Signal Noise Analysis_ 79


_SIGNAL_



_Available_ _Actual_ _Available_ _Actual_



_Available_
_Output Signal_



_Actual_
_Output Signal_



_P_
_Ai_



_Actual_
_Input Signal_




























|Col1|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|+−<br><br>_Port 1_||||_CIRCUIT_|||
|+−<br><br>_Port 1_||||_CIRCUIT_|_Port 2_||
|+−<br><br>_Port 1_|||||||



Figure 6.1: Signal and noise definitions for a two-port.


All of the quantities can be output in dB with the exception of _T_ NOISE. When DB(NF) is used the spot
noise figure is obtained.
The transducer gain, _GT_, for the two port is defined as


_GT_ = _Po/PAi_ (6.3)


The most common measure of the noise performance of a two port is the noise factor or noise figure.
The spot noise factor NF’ of a linear two-port network is defined as the ratio of the noise power delivered
by the network to the load impedance to the fraction of the noise power due to the input termination alone.
This noise is calculated with the input termination, _RS_, at the standard temperature _T_ 0 = 290 K. Note
that this differs from the default analysis temperature of spice which is 300 K or 16.85 c. The noise power
delivered to the output is the total noise power indicated by ONOISE less the noise power contributed to the
output by _RL_ since it is not part of the two-port. These subtractions must be done using squared voltage
quantities because the noises are uncorrelated. The noise power at the output due to _RS_ is the voltage
gain squared multiplied by the square of the noise voltage in series with _RS_ . The noise factor calculated by
SomeVersionsOfSpice is the spot noise factor as the noise powers are not averaged over frequency. The
spot noise factor is

0 _[V]_ _NO_ [ 2] _[−]_ _[V]_ _NO,RL_ [ 2]
_NF_ _[′]_ = (6.4)

0 _[V]_ _NO,RS_ [ 2]


Here the leading zero subscript indicates that the noise is calculated with _RS_ at _T_ 0. 0 _[V]_ _NO_ [is the output]
noise voltage with _RS_ at _T_ 0, _VNO,RL_ is the component due to the noise generated by _RL_ and 0 _VNO,RS_ is
the component due to the noise generated by _RS_ at _T_ 0.
The noise temperature in Kelvin is


_TNOISE_ = _TK_ ( _NF_ _[′]_ _−_ 1) (6.5)


where _TK_ is the analysis temperature in Kelvin.


80 _CHAPTER 6. STATEMENT CATALOG_


2 PORT















_V_









1  Vμ





50 Ω



|R 50 Ω|Col2|Col3|Col4|
|---|---|---|---|
|+−<br>_RS_<br>_Port 1_<br>_Port 2_<br>_R_<br>_R_<br>_R_<br>1<br>2<br>3<br>50Ω<br>550Ω<br>50 Ω<br>1<br>3<br>2<br>0<br>0<br>50 Ω|_R_<br>_R_<br>_R_<br>1<br>2<br>3<br>50Ω<br>550Ω<br>50 Ω|3|3|
|+−<br>_RS_<br>_Port 1_<br>_Port 2_<br>_R_<br>_R_<br>_R_<br>1<br>2<br>3<br>50Ω<br>550Ω<br>50 Ω<br>1<br>3<br>2<br>0<br>0<br>50 Ω|_R_<br>_R_<br>_R_<br>1<br>2<br>3<br>50Ω<br>550Ω<br>50 Ω|_Port 2_||
|+−<br>_RS_<br>_Port 1_<br>_Port 2_<br>_R_<br>_R_<br>_R_<br>1<br>2<br>3<br>50Ω<br>550Ω<br>50 Ω<br>1<br>3<br>2<br>0<br>0<br>50 Ω||||


Figure 6.2: Circuit used as an example for specifying noise analysis.


The output voltage signal-to-noise ratio is the ratio of the signal voltage to the noise voltage:

SNR _o_ = _VO_ _[′′]_ _√_ (6.6)
_VNO_ _[′′]_ 2

_√_
where the 2 is required since noise voltages are specified in RMS terms but the signal voltages are specified

as a peak voltage. _VO_ is the signal voltage at the output taking into account the signal-to-noise ratio, SNR _i_,
at the input of the circuit. SNR _i_ can either be specified on the voltage source line or, if not, calculated usnig
the thermal voltage of _RS_ .
Three parameters affect the results of the noise analysis. These are the source resistance _RS_, the load
resistance, _RL_ and the input signal to noise ratio, SNR _i_ . The values used for the parameters are as follows:
_RS_ = The resistance of port 1 (ZL, or if Port 1 is not defined,
= The RS resistance specified on the source line, or if not specified.
= 50 Ω.


_RL_ = The resistance of port 2 (ZL, or if Port 2 is not defined.
= The RL resistance specified on the source line, or if not specified,
= 50 Ω.


SNR _i_ = The SNR specified on the source line, or if not specified.
= it is calculated as the signal voltage specified on the input line devided by the thermal noise voltage of _RS_ with appropriate correction
for the difference between RMS and peak quantities.


_Example of Two-Port Noise and Gain Analysis_
The netlist for performing a two-port noise and gain analysis of the circuit in Fig. 6.2 is as follows.
Gain and noise analysis of resistive attenuator
vin 1 0 AC 1u RS=50 SNR=100
RS 1 2 50
R1 2 0 55
R2 2 3 500
R3 3 0 55
RL 3 0 50
*The following sets the analysis temperature to the standard temperature
.TEMP 16.85
.AC DEC 1 1MEG 2G
.NOISE V(3,0) VIN 1
.PRINT NOISE nf db(nf) gt db(gt) gain snr inoise onoise
.END


The example below performs the same analysis using ports and also prints the scattering parameters of
the circuit.


_Small-Signal Noise Analysis_ 81


Gain and noise analysis of resistive attenuator using ports.
vin 1 0 AC 1u SNR=100
PIN PNR=1 ZL=50
R1 2 0 55
R2 2 3 500
R3 3 0 55
POUT PNR=2 ZL=50
*The following sets the analysis temperature to the standard temperature
.TEMP 16.85
.AC DEC 1 1MEG 2G
.NOISE V(3) VIN 1
.PRINT NOISE nf db(nf) gt db(gt) gain snr inoise onoise
.PRINT AS S(1,1) S(1,2), S(2,1), S(2,2)
.END


82 _CHAPTER 6. STATEMENT CATALOG_

### .OP Operating Point Analysis


In the operating point analysis a DC analysis is performed to determine the DC voltages and currents
without performing any sweeps.
_Form_


.OP


_Note_


1. The operating point analysis is performed by default prior to AC small-signal (.AC) and transient
(.TRAN) analyses to determine the operating point about which the circuit is linearized for AC analysis
and as the initial starting point for transient analysis.


2. The (.OP) analysis is performed if no other analyses are specified.


3. The operating point analysis is performed with inductors shorted and capacitors opened.


4. Following DC analysis the nonlinear devices are linearized to determine their AC small-signal models.


5. A .TRAN analysis performs its own DC analysis to determine the initial conditions (or bias point) for
transient analysis ignoring the bias point determined in a .OP analysis.


_Option Specification_ 83

### .OPTIONS Option Specification


The options specification provides the user control over the program and a way of setting defaults for
certain elements and analyses.
_Form_


.OPTIONS [ _Keyword_ ] _..._ [ _Keyword=Value_ ] _..._


Multiple keywords can be included in a single .OPTIONS statement and in any order.


Keywords:


ACCT Sets reporting of accounting and statistics. This option is a flag and does not have a value.
(Default: not set)


ABSTOL= _Value_ Sets the absolute current error tolerance.
(Default: 1 pA (10 _[−]_ [12] ))


BYPASS The bypass option.
Spice3 only.


CHGTOL= _Value_ Resets the charge tolerance of the program.
(Units: C; Default: 10 fC 10 _[−]_ [14] )


CPTIME= _Value_ Sets the maximum CPU-time.
(Units: s; Default: _∞_ )
Spice2g6 only.


DEFAD= _Value_ Sets the default value of the MOS drain diffusion area (AD) used in the M element (see page
189).
(Units: m [2] Default: 0)


DEFAS= _Value_ Sets the default value of the MOS source diffusion area (AS) used in the M element (see
page 189).
(Units: m [2] Default: 0)


DEFL= _Value_ Sets the value of the MOS channel length (L) used in the M element (see page 189).
(Units: m; Default: 100 _μ_ m (1E-4))


DEFW= _Value_ Resets the value for MOS channel width (W) used in the M element (see page 189).
(Units: m; Default: 100 _μ_ m (1E-4))


EXPAND Reports in output logfile the devices and nodes created in subcircuit expansions. This option
is a flag and does not have a value.
(Default: no expansion)
PSpice only.


GMIN= _Value_ Resets the value of the minimum conductance _G_ MIN. The usage of _G_ MIN is controlled by
the code implementing individual elements. Generally is the minimum conductance between
nodes. It is used to aid convergence.
(Units: S; Default: 10 _[−]_ [12] (1E-12))


84 _CHAPTER 6. STATEMENT CATALOG_


ITL1= _IntegerValue_ Sets the limit on the number of DC iterations.
(Default: 100)


ITL2= _IntegerValue_ Sets the DC transfer curve iteration limit.
(Default: 50)


ITL3= _IntegerValue_ Sets the minimum number of iterations used in transient analysis.
(Default: 4)
Spice2g6 only.


ITL4= _IntegerValue_ Sets the maximum of transient iterations at each time point.
(Default: 10)
Spice2g6 only.


ITL5= _IntegerValue_ Sets the transient analysis total iteration limit. If ITL5=0 this test is omitted. Used in
transient analysis (.TRAN).
PSpice only.
(Default: 5000)


LIBRARY Reports in output logfile the statements and devices extracted from a library file This option
is a flag and does not have a value.
(Default: no report)
PSpice only.


LIMPTS= _Value_ Sets the maximum number of points that can be printed or plotted in a DC, AC or transient
analysis.
(Default: 201)
Spice2g6 only.


LIMTIM= _Value_ Sets the maximum CPU time for generating plots. Used only if the program was terminated
because the time specified by the CPTIME option was exceeded.
(Units: s; Default: 10)
Spice2g6 only.


LIST Sets summary reporting of circuit elements in input NETLIST.
(Default: not set)


LVLCOD= _IntegerValue_ Sets an internal option of the program when running on CDC computers. If LVLCOD=1
machine code for the matrix solution is generated.
(Default: 2)
Spice2g6 only.


LVLTIM= _IntegerValue_ If LVLTIM=1 then iteration time step control is used. If LVLTIM=2 then the time step
indicated by the truncation error is used. If METHOD=GEAR and MAXORD¿2 then LVLTIM
is set to 2 by SPICE.
(Default: 2)
Spice2g6 only.


MAXORD= _IntegerValue_ Sets the maximum order of the integration method if METHOD=GEAR
(Default: 2; 2 _≤_ MAXORD _≤_ 6)
Spice2g6 only.


_Option Specification_ 85


METHOD= _String_ Sets the numerical integration method to be used. If METHOD=GEAR then Gear’s method is
used. If METHOD=TRAPEZOIDAL then the trapezoidal method is used.
(Default: TRAPEZOIDAL)
Spice2g6 only.


NODE Sets reporting of the node table.
(Default: not set)


NOECHO Suppresses listing of input file in output log file.
(Default: input lines listed.)
PSpice only.


[NOFREQ ] Number of frequency points to be used in simulation of distributed circuit. Must be a
power of 2.
(Default: 1024)


NOMOD Un-sets reporting of model parameters.
(Default: set)


NOPAGE Un-sets page breaks in the output log file. Useful if the log file is to printed by a program
which automatically paginates the output. This option is a flag and does not have a value.
(Default: set)


NUMDGT= _IntegerValue_ Sets the number of significant digits used in printing values in the output log file.
(Default: 4; 0 _< IntegerValue ≤_ 8)
Spice2g6 and PSpice only.


OPTS Sets reporting of the option values.
(Default: not set)


PIVREL= _Value_ Sets the minimum acceptable pivot value used in partial pivoting in the solution of the
network equations (such as solving for the nodal voltages **v** _n_ in (4.1) on page 34). PIVREL
is the minimum acceptable ratio of an acceptable pivot value to the largest column entry.
(Default: 0.001)


PIVTOL= _Value_ Sets the minimum value of a matrix element for it to be used as a pivot.
(Default: 10 _[−]_ [13] )


RELTOL= _Value_ Sets the relative error tolerance of voltages and currents.
(Default: 0.001)


TNOM= _Value_ Sets the nominal temperature. This is assumed to be the temperature at which the model
parameters were measured. In some cases it is overwritten by a temperature parameter in
the .MODEL statement.
(Units: _[◦]_ C; Default: 27 _[◦]_ C (300K))


TRTOL= _Value_ Sets the factor by which the approximated truncation error evaluated in transient analysis
is scaled.
(Default: 7)


VNTOL= _Value_ Sets the absolute voltage error tolerance.
(Units: V; Default: 1 _μ_ V (1E-6))


86 _CHAPTER 6. STATEMENT CATALOG_

### .PARAM PSpice Only


Parameter Definition
This statement defines parameters that can be used in subsequent statements and element lines.
PSpice _Form_


.PARAM [ _ParameterName = NumericValue . . ._ ] [ _ParameterName = { Expression_
_} . . ._ ]


_ParameterName_ Name of a parameter with first character being alphabetic (a-z). If this is the name of a
previously defined parameter at the same level of subcircuit expansion then the parameter
value is changed. If the .PARAM statement is is in the top level circuit then the parameter
value is global. If the .PARAM statement is is in a subcircuit then the parameter value is
local and can be used at the current subcircuit expansion level or lower in the subcircuit
expansion hierarchy.


_NumericValue_ is a numeric value which can be an integer or floating point number followed by optional
scale factor and/or unit. (e.g. 1.E-9, 1N, 1NV and 1.E-9V are equivalent.)


_Expression_ is a standard expression as described in the Algebraic Expressions section on page **??** . Note
that the expression must be enclosed in braces ( _{ . . . }_ ).


_Example_


.PARAM VDD = 10V, VSS = 0 VREF = 2.5
.PARAM VREF = VDD/2 .PARAM LENGTH = 1.10*L


_Note_


PSpice _Only_ 87


1. Predefined parameters are supported and the user must avoid using these. Predefined parameters:

**Name** **Value** **Description**

TEMP not supported Analysis temperature.
Reserved for future expansion


VT not supported Thermal voltage.
Reserved for future expansion


2. In PSpice, in most places where a numeric value is required an expression (within braces _{ . . . }_ ) can
be used instead. An expression can contain any support mathematical operation, constant numeric
values or expressions. Exceptions are


_•_ Polynomial coefficients.


_•_ The values of the transmission line device parameters NL and F.


_•_ The values of the piece-wise linear characteristic in the PWL form of the independent voltage (V)
and current (I) sources.


and


_•_ The values of the resistor device parameter TC.


_•_ As node numbers.


_•_ Values of most statements (such as .TEMP, .AC, .TRAN etc.)


Specifically included are


_•_ The values of all other device parameters.


_•_ The values in .IC and .NODESET statements.


_•_ The values in .SUBCKT statements.


and


_•_ The values of all model parameters. F.


3. Hierarchical usage of .PARAM statements in subcircuits is supported. The parameters defined in a
.PARAM statement are available in the subcircuit in which they are defined or in lower nested subcircuits.
Thus parameters defined in a subcircuit are not available higher in the hierarchy. The same concept
applies to values of a parameter changed in a subcircuit. Value changes are local and are available in
the current subcircuit and lower nested subcircuits.


4. Libraries are searched for parameters not defined in the circuit NETLIST or in included files. A .PARAM
statement does not have to be within a subcircuit in a library.


88 _CHAPTER 6. STATEMENT CATALOG_

### .PLOT Plot Specification


The plot specification controls the information that is plotted as the result of various analyses.
_Form_


.PLOT TRAN _OutputSpecification_ [ _PlotLimits_ ]
+ [ _OutputSpecification_ [ _PlotLimits_ ] _. . ._ ]


.PLOT AC _OutputSpecification_ [ _PlotLimits_ ]
+ [ _OutputSpecification_ [ _PlotLimits_ ] _. . ._ ]


.PLOT DC _OutputSpecification_ [ _PlotLimits_ ]
+ [ _OutputSpecification_ [ _PlotLimits_ ] _. . ._ ]


.PLOT NOISE _NoiseOutputSpecification_ [( _DistortionReportType_ )] [ _PlotLimits_ ]
+ [ _NoiseOutputSpecification_ [( _DistortionReportType_ )] [ _PlotLimits_ ]


.PLOT DISTO _DistortionOutputSpecification_ [( _DistortionReportType_ )] [ _PlotLimits_
]
+ [ _DistortionOutputSpecification_ [( _DistortionReportType_ ) ] [ _PlotLimits_ ] _. . ._ ]

[( _DistortionReportType_ )] [ _PlotLimits_ ]


PSpice _Form_


.PLOT TRAN _OutputSpecification_ [ _PlotLimits_ ]
+ [ _OutputSpecification_ [ _PlotLimits_ ] _. . ._ ]


.PLOT AC _OutputSpecification_ [ _PlotLimits_ ]
+ [ _OutputSpecification_ [ _PlotLimits_ ] _. . ._ ]


.PLOT DC _OutputSpecification_ [ _PlotLimits_ ]
+ [ _OutputSpecification_ [ _PlotLimits_ ] _. . ._ ]


.PLOT NOISE _NoiseOutputSpecification_ [( _DistortionReportType_ )] [ _PlotLimits_ ]
+ [ _NoiseOutputSpecification_ [( _DistortionReportType_ )] [ _PlotLimits_ ]


_Plot Specification_ 89


TRAN is the keyword specifying that this .PLOT statement controls the reporting of results of a
transient analysis initiated by the .TRAN statement.


AC is the keyword specifying that this .PLOT statement controls the reporting of results of a
small-signal AC analysis initiated by the .AC statement.


DC is the keyword specifying that this .PLOT statement controls the reporting of results of a DC
analysis initiated by the .DC statement.


NOISE is the keyword specifying that this .PLOT statement controls the reporting of results of a
noise analysis initiated by the .NOISE statement.


DISTO is the keyword specifying that this .PLOT statement controls the reporting of results of a
small-signal AC distortion analysis initiated by the .DISTO statement.


_OutputSpecification_ specifies the voltage or current to be plotted against the sweep variable. The sweep
variable is dependent on the type of analysis.
Many forms of OutputSpecification are supported by PSpice . Below is a description
of the basic forms that are supported both by Spice2g6 and PSpice . A comprehensive
description of OutputSpecification supported by PSpice is given in the section on output
specification on page 94.


Voltages may be specified as an absolute voltage at a node: V( _NodeName_ ) or the voltage
at one node with respect to that at another node, e.g. V(Node1Name,Node2Name).
For the reporting of the results of an AC analysis the following outputs can be specified by
replacing the V as follows:
VR            - real part
VI            - imaginary part
VM            - magnitude
VP            - phase
VDB            - 10 log(10 _magnitude_ )
In AC analysis the default is VM for magnitude.


Currents are specified by referencing the name of the voltage source through which the
current is measured, e.g. I(V _VoltageSourceName_ ).
For the reporting of the results of an AC analysis the following outputs can be specified by
replacing the I as follows:
IR            - real part
II            - imaginary part
IM            - magnitude In AC analIP            - phase
IDB            - 10 log(10 _magnitude_ )

ysis the default is IM for magnitude.


_PlotLimits_ are optional and can be placed after any output specification. _PlotLimits_ has the form
( _LowerLimit_, _UpperLimit_ ) . All quantities will be plotted using the same _PlotLimits_ . The
default is to automatically scale the plot and perhaps use different scales for each of the
quantities to be plotted.


_NoiseOutputSpecification_ specifies the noise measure to be reported. The two options are ONOISE which
reports the output noise and INOISE which reports the equivalent input noise. See the
.NOISE statement on page 77 for a detailed explanation.


90 _CHAPTER 6. STATEMENT CATALOG_


It must be one of the following:
ONOISE            - magnitude of the output noise
DB(ONOISE)            - output noise in dB
INOISE            - magnitude of the equivalent input noise
DB(INOISE)            - equivalent input noise in dB
GAIN            - voltage gain
DB(GAIN)            - voltage gain in dB (= 20 log(GAIN)
GT            - transducer gain
DB(GT)            - transducer gain in dB (= 10 log(GT)
NF            - spot noise factor
DB(NF)            - spot noise figure (= 10 log(NF)
SNR            - output signal-to-noise ratio
DB(SNR)            - output signal-to-noise ratio in dB (= 20 log(SNR)
TNOISE            - output noise temperature.


_SParameterOutputSpecification_ specifies the S-parameter output variables that are to be printed. Each variable must have one of the following forms:
S(i,j)            - Magnitude of _Sij_
SR(i,j)            - Real part of _Sij_
SI(i,j)            - Imaginary part of _Sij_ The port
SP(i,j)            - Phase of _Sij_ in degrees
SDB(i,j)            - Magnitude of _Sij_ in dB (= 20 log(S(i,j)))
SG(i,j)            - Group delay of _Sij_

numbers are _i, j_ which are specified using the PNR keywor when the port (‘P’) element is
specified.


_DistortionOutputSpecification_ specifies the distortion component to be reported in a tabular format of up to
8 columns plus an initial column with the sweep variable. The _DistortionOutputSpecification_
is one of the following:
HD2            - the second harmonic distortion
HD3            - the second harmonic distortion
SIM2            - the sum frequency intermodulation component See the .DISTO
DIM2            - the difference frequency intermodulation component
DIM3            - the third order intermodulation component

statement on page 58 for a description of these distortion components.


_DistortionReportType_ specifies the format for reporting the distortion components. It must be one of the
following:
R         - real part
I                 - imaginary part
M       - magnitude The default
P         - phase
DB         - 10 log(10 _magnitude_ )

is M for magnitude.


_Example_


.PLOT TRAN V(10) V(5,3) I(VIN)
.PLOT AC VM(10) VR(5,3) IP(VLOAD)
.PLOT DC V(10) V(5,3) I(VIN)
.PLOT NOISE ONOISE INOISE DB(ONOISE) DB(INOISE)
.PLOT NOISE GAIN DB(GT) DB(NF) SNR TNOISE
.PLOT AS SDB(1,1) SP(1,1) SDB(1,2) SP(1,2)
.PLOT DISTO HD2 HD3 SIM2(DB)


_Plot Specification_ 91


_Note_


1. There can be any number of .PLOT statements.


2. All of the output quantities specified on a single .PLOT statement will be plotted on the same graph
using ASCII characters. An overlap will be indicated by the letter X. The plot produced by the .PLOT
statement is a line printer plot. While plotting is primitive it can be plotted on any printer and is
incorporated in the output log file.


3. The plot output of the results of an AC analysis always have a logarithmic vertical scale.


4. The current through any element can be found by inserting independent voltage sources in series with
the elements. This is generally what is required in Spice2g6and Spice3. However PSpice supports
direct specification of the voltage and currents of most elements. See the section on page 94.


5. More elaborate plotting is available with Spice3 using the NUTMEG plotting program described on
the NUTMEG chapter beginning on page **??** ; and with PSpice using the .PROBE statement described
on page 98.


92 _CHAPTER 6. STATEMENT CATALOG_

### .PRINT Print Specification


The print specification controls the information that is reported as the result of various analyses.
_Form_


.PRINT TRAN _OutputSpecification_ [ _OutputSpecification . . ._ ]


.PRINT AC _OutputSpecification_ [ _OutputSpecification . . ._ ]


.PRINT DC _OutputSpecification_ [ _OutputSpecification . . ._ ]


.PRINT DISTO _DistortionOutputSpecification_ ( _DistortionReportType_ )
+ [ _DistortionOutputSpecification_ ( _DistortionReportType_ ) _. . ._ ]


TRAN is the keyword specifying that this .PRINT statement controls the reporting of results of a
transient analysis initiated by the .TRAN statement.


AC is the keyword specifying that this .PRINT statement controls the reporting of results of a
small-signal AC analysis initiated by the .AC statement.


DC is the keyword specifying that this .PRINT statement controls the reporting of results of a
DC analysis initiated by the .DC statement.


NOISE is the keyword specifying that this .PRINT statement controls the reporting of results of a
noise analysis initiated by the .NOISE statement.


DISTO is the keyword specifying that this .PRINT statement controls the reporting of results of a
small-signal AC distortion analysis initiated by the .DISTO statement.


_OutputSpecification_ specifies the voltage or current to be reported in a tabular format of up to 8 columns
plus an initial column with the sweep variable.
Many forms of OutputSpecification are supported by PSpice . Below is a description
of the basic forms that are supported both by Spice2g6 and PSpice . A comprehensive
description of OutputSpecification supported by PSpice is given in the section on output
specification on page 94.


Voltages may be specified as an absolute voltage at a node: V( _NodeName_ ) or the voltage
at one node with respect to that at another node, e.g. V(Node1Name,Node2Name).
For the reporting of the results of an AC analysis the following outputs can be specified by
replacing the V as follows:
VR            - real part
VI            - imaginary part
VM            - magnitude
VP            - phase
VDB            - 10 log(10 _magnitude_ )
In AC analysis the default is VM for magnitude.


Currents are specified by referencing the name of the voltage source through which the
current is measured, e.g. I(V _VoltageSourceName_ ).


_Print Specification_ 93


For the reporting of the results of an AC analysis the following outputs can be specified by
replacing the I as follows:
IR            - real part
II            - imaginary part
IM            - magnitude In AC analIP            - phase
IDB            - 10 log(10 _magnitude_ )

ysis the default is IM for magnitude.


_NoiseOutputSpecification_ specifies the noise measure to be reported. The two options are ONOISE which
reports the output noise and INOISE which reports the equivalent input noise. See the
.NOISE statement on page 77 for a detailed explanation.
It must be one of the following:
ONOISE            - RMS output noise voltage
DB(ONOISE)            - output noise voltage in dB (= 20 log(ONOISE)
INOISE            - RMS equivalent input noise voltage
DB(INOISE)            - equivalent input noise voltage in dB (= 20 log(INOISE)
GAIN            - voltage gain
DB(GAIN)            - voltage gain in dB (= 20 log(GAIN)
GT            - transducer gain
DB(GT)            - transducer gain in dB (= 10 log(GT)
NF            - spot noise factor
DB(NF)            - spot noise figure (= 10 log(NF)
SNR            - output signal-to-noise ratio
DB(SNR)            - output signal-to-noise ratio in dB (= 20 log(SNR)
TNOISE            - output noise temperature.


_SParameterOutputSpecification_ specifies the S-parameter output variables that are to be printed. Each
variable must have one of the following forms:
S(i,j)            - Magnitude of _Sij_
SR(i,j)            - Real part of _Sij_
SI(i,j)            - Imaginary part of _Sij_
SP(i,j)            - Phase of _Sij_ in degrees
SDB(i,j)            - Magnitude of _Sij_ in dB (= 20 log(S(i,j)))
SG(i,j)            - Group delay of _Sij_


The port numbers are _i, j_ which are specified using the PNR keyword when the port element
is specified.


_DistortionOutputSpecification_ specifies the distortion component to be reported in a tabular format of up to
8 columns plus an initial column with the sweep variable. The _DistortionOutputSpecification_
is one of the following:
HD2            - the second harmonic distortion
HD3            - the second harmonic distortion
SIM2            - the sum frequency intermodulation component
DIM2            - the difference frequency intermodulation component
DIM3            - the third order intermodulation component


94 _CHAPTER 6. STATEMENT CATALOG_


See the .DISTO statement on page 58 for a description of these distortion components.


_DistortionReportType_ specifies the format for reporting the distortion components. It must be one of the
following:
R         - real part
I                 - imaginary part
M       - magnitude
P         - phase
DB         - 10 log(10 _magnitude_ )


The default is M for magnitude.


_Example_


.PRINT TRAN V(10) V(5,3) I(VIN)
.PRINT AC VM(10) VR(5,3) IP(VLOAD)
.PRINT DC V(10) V(5,3) I(VIN)
.PRINT NOISE ONOISE INOISE DB(ONOISE) DB(INOISE)
.PRINT NOISE GAIN DB(GT) DB(NF) SNR TNOISE
.PRINT AS SDB(1,1) SP(1,1) SDB(1,2) SP(1,2)
.PRINT DISTO HD2 HD3 SIM2(DB)


_Note_


1. There can be any number of .PRINT statements.


2. The number of significant digits of the results reported is NUMDGT which is set in a .OPTIONS statement
(see page 85).


3. The current through any element can be found by inserting independent voltage sources in series with
the elements. This is generally what is required in Spice2g6and Spice3. However PSpice supports
direct specification of the voltage and currents of most elements. See the section on page 94.


_Output Specification for_ PSpice

PSpice supports a relatively large variety of output specifications compared to that available with Spice2g6


and Spice3. The output specifications described in the following can be used .PRINT and .PLOT statements.
The various forms of output specifications enable the current and voltages of virtually all devices to be
examined¿


_Print Specification_ 95


DC and TRAN Reporting
The output specifications available for the DC sweep and transient analyses are


I( _DeviceName_ ) Current through a two terminal device (such as a resistor R element) or the output of a
controlled voltage or current source. e.g. I(R22) is the current flowing through resistor R22
from node _N_ 1 to _N_ 2 of R22.


I TerminalName( _DeviceName_ ) Current flowing into terminal named _TerminalName_ (such as B for gate)
from the device named _DeviceName_ (such as Q12). e.g. IB(Q12)


I PortName( _TransmissionLineName_ ) Current at port named _PortName_ (either A or B) of the transmission
line device named _TransmissionLineName_


V( _NodeName_ ) Voltage at a node of name _NodeName_ .


V( _n_ 1 _, n_ 2) Voltage at node _n_ 1 with respect to the voltage at node _n_ 2.


V( _DeviceName_ ) Voltage across a two terminal device (such as a resistor R element) or at the output of a
controlled voltage or current source.


V TerminalName( _DeviceName_ ) Voltage at terminal named _TerminalName_ (such as G for gate) of the device
named _DeviceName_ (such as M12). e.g. VG(M12)


V TerminalName1 TerminalName2( _DeviceName_ ) Voltage at terminal named _TerminalName1_ (such as G for
gate) th respect to the terminal name _TerminalName2_ (such as S for source) of the device
named _DeviceName_ (such as M12). e.g. VGS(M12)


V PortName( _TransmissionLineName_ ) Voltage at port named _PortName_ (either A or B) of the transmission
line device named _TransmissionLineName_ (such as T5). e.g. VA(M5)


Two Terminal Device Types Supported for DCand Transient Analysis Reporting


The single character identifier for the following elements as well as the rest of the device name can be used
as the _DeviceName_ in the I( _DeviceName_ ) and I( _DeviceName_ ) output specifications.

Element Type Description
C capacitor
D diode
E voltage-controlled voltage source
F current-controlled current source
G voltage-controlled current source
H current-controlled voltage source
I independent current source
L inductor
R resistor
V independent voltage source


Multi-Terminal Device Types Supported for DCand Transient Analysis Reporting


The single character identifier for the following elements as well as the rest of the device name can be used
as the _DeviceName_ in the I TerminalName( _DeviceName_ ), V TerminalName( _DeviceName_ ) and
V TerminalName1 TerminalName2( _DeviceName_ ) output specifications.


96 _CHAPTER 6. STATEMENT CATALOG_


Element Type Description
B GaAs MESFET Terminals:
D — drain
G — gate
S — source
J JFET Terminals:
D — drain
G — gate
S — source
M MOSFET Terminals:
B — bulk or substrate
D — drain
G — gate
S — source
Q BJT Terminals
C — collector
B — base
E — emitter
S — source


AC Reporting
The output specifications available for reporting the results of an AC frequency sweep analysis includes all of
the specification formats discussed above for DC and transient analysis together with a number of possible
suffixes:
DB     - 10 log(10 _magnitude_ )
M     - magnitude
P     - phase
R     - real part
I     - imaginary part
G     - group delay = _∂φ/∂f_
where _φ_ is the phase of the quantity being reported and _f_
is the analysis frequency.
In AC analysis the default suffix is M for magnitude.


Two-Terminal Device Types Supported for AC Reporting


The single character identifier for the following elements as well as the rest of the device name can be
used as the _DeviceName_ in the I( _DeviceName_ ) and I( _DeviceName_ ) output specifications.

Element Type Description
C capacitor
D diode
I independent current source
L inductor
R resistor
V independent voltage source


Multi-Terminal Device Types Supported for DCand Transient Analysis Reporting


_Print Specification_ 97


The single character identifier for the following elements as well as the rest of the device name can be used
as the _DeviceName_ in the I TerminalName( _DeviceName_ ), V TerminalName( _DeviceName_ ) and
V TerminalName1 TerminalName2( _DeviceName_ ) output specifications.


Element Type Description
B GaAs MESFET Terminals:
D — drain
G — gate
S — source
J JFET Terminals:
D — drain
G — gate
S — source
M MOSFET Terminals:
B — bulk or substrate
D — drain
G — gate
S — source
Q BJT Terminals
C — collector
B — base
E — emitter
S — source


98 _CHAPTER 6. STATEMENT CATALOG_

### .PROBE Data Output Specification


**There is a big problem here — Probe is a trademark of Microsim corporation**
The .PROBE statement saves the node voltages and device currents in a file for subsequent probing.
PSpice _Form_


.PROBE [/CSDF] [ _OutputSpecification . . ._ ]


/CSDF is a keyword resulting in the output probing file being written in ASCII format. By default
the probing file is output in the more efficient binary format. However, only the ASCII
formated is fully portable between computers and operating systems.


_OutputSpecification_ specifies a node voltage or device current to be included in the probe data file. The
output specifications supported are those supported for the .PRINT and .PLOT statements.
A comprehensive description of the OutputSpecification supported is given in the section
on output specification on page 94.
If an _OutputSpecification_ is not given then all node voltages and device currents are stored
in the probing file.


_Example_



.PROBE V(10) V(5,3) I(VIN)
.PROBE VM(10) VR(5,3) IP(VLOAD)
.PROBE/CSDF V(10) IG(VIN)
.PROBE



The first exam


ple will output data from .DC, .AC and .TRAN analyses.
The second example will output data only from a .AC analysis.
The third example will output the node voltage at node 10 for .DC, .AC and .TRAN analyses but output the
group delay of the current in the independent voltage source VIN only from an .AC analysis. As well the
data will be output in ASCII format.
The fourth example results in all node voltages and device currents being stored.


_Note_


1. The probing data is stored in the file PROBE.DAT .


2. The results of DC, AC and transient analyses are saved. An _OutputSpecification_ which is unique to a
particular type of analysis is ignored when the the results of analyses are being selected to storage. An
example is VI(10) which selects the imaginary part of the voltage at node 10 and so only applies for
storage of the results for an AC small-signal analysis.


3. The results stored in the probe file can subsequently be viewed using the Probeprogram described in
chapter **??** .


_Pole-Zero Analysis_ 99

### .PZ Pole-Zero Analysis


In pole zero analysis the poles and zeros of the small signal ACtransfer function of a two-port is evaluated.
_Form_


.PZ _Node1 Node2 Node3 Node4_ CUR POL
.PZ _Node1 Node2 Node3 Node4_ CUR ZER
.PZ _Node1 Node2 Node3 Node4_ CUR PZ
.PZ _Node1 Node2 Node3 Node4_ VOL POL
.PZ _Node1 Node2 Node3 Node4_ VOL ZER
.PZ _Node1 Node2 Node3 Node4_ VOL PZ


_Node1_ is the positive input node.


_Node2_ is the negative input node.


_Node3_ is the positive output node.


_Node4_ is the negative output node.


CUR is the keyword to evaluate the transfer function (output voltage)/(input current)


VOL is the keyword to evaluate the transfer function (output voltage)/(input voltage)


POL is the keyword to evaluate the poles of the transfer function only.


ZERO is the keyword to evaluate the zeroes of the transfer function only.


PZ is the keyword to evaluate the poles and zeroes of the transfer function.


_Example_


.PZ 1 0 3 0 CUR POL
.PZ 2 3 5 0 VOL ZER
.PZ 4 1 4 1 CUR PZ


_Note_


1. The pole-zero analysis works with resistors R, capacitors C, inductors L, linear controlled sources E,F,G
and H; independent voltage and current sources V and I, bipolar junction transistors, Q; MOSFETs, M;
JFETs J; and diodes D. In particular distributed devices such as Transmission lines are not supported
as these do not have a pole-zero description.


2. In interactive mode, the command syntax is the same except that the first field is PZ instead of .PZ.
To print the results, one should use the command “PRINT ALL”.


3. The program first computes the DC operating point and then determines the linearized, small-signal
models for all the nonlinear devices in the circuit. This circuit is then used to find the poles and zeros.


100 _CHAPTER 6. STATEMENT CATALOG_

### .SAVEBIAS Save Bias Conditions


_Sensitivity Analysis_ 101

### .SENS Sensitivity Analysis


The sensitivity analysis calculates the DC small-signal sensitivities of each output quantity with respect
to every circuit parameter.
_Form_


.SENS _OutputSpecification_ [ _OutputSpecification . . ._ ]


_OutputSpecification_ is the specification of the small-signal output quantity. It has the same format as the
_OutputSpecification_ in a .PRINT statement (see page 92).


_Example_


.SENS V(10) V(10,2) I(VLOAD)


_Note_


1. The .SENS statement initiates a small-signal AC analysis.


2. The transfer function computed is the sensitivity (or partial derivative) of the DC value of the output
quantity with respect to the each and every circuit parameter. For example, if a resistor is specified
with value _x_ and a capacitor is specified with value _c_ then, for the above examples the following
sensitivities are computed:

102 _CHAPTER 6. STATEMENT CATALOG_

### .STEP Parameteric Analysis

**SUBCIRCUIT**
3


_SubcircuitName_



_Form_



_N_
_N_


Figure 6.3: Subcircuit.


.SUBCKT _SubcircuitName N_ 1 [ _N_ 2 _N_ 3 _... NN_ ]



PSpice _Form_


.SUBCKT _SubcircuitName N_ 1 [ _N_ 2 _N_ 3 _... NN_ ]
+ [PARAMS: [ _Keyword = { Expression } . . ._ ] [ _Keyword = Value . . ._ ] ]


PSpice _Form_


.SUBCKT _SubcircuitName N_ 1 [ _N_ 2 _N_ 3 _... NN_ ]
+ [ _PARAMS:_ [ _keyword = { Expression } . . ._ ] [ _Keyword = Value . . ._ ] ]


_SubcircuitName_ is the name of the subcircuit.


_N_ 1 is the first node of the subcircuit.


_NN_ is the _N_ th node of the subcircuit.


PARAMS: indicates that parameters are to be passed to the subcircuit.


_Keyword:_ is a keyword which may be replaced by a value specified on a subcircuit call (X) element.
(See page 257).


_Value:_ is a numeric value.


_Expression:_ is an algebraic expression which evaluates to a numeric value. (See section **??** on page **??**
for allowable expressions).


_Example_


.SUBCKT MULTI 2 4 17 3 1


_Note_


104 _CHAPTER 6. STATEMENT CATALOG_


1. The global ground node, node 0 (or in PSpice node GND) must not be one of the subcircuit nodes.


2. Subcircuits are incorporated by using the “X” element. The number of nodes of the “X” element must
correspond to the number of nodes in the definition of the subcircuit (i.e. is in the .SUBCKT statement).
See page 257 for a description of the X element.


3. The last line in a subcircuit definition is the .ENDS line (see page 63).


4. The only restriction on the statements within a subcircuit is that control lines such as .AC, .DC or
.OPTIONS are not allowed. However, element lines, model statements and other subcircuit definitions
and subcircuit calls are allowed.


5. Device models or subcircuit definitions included as part of a subcircuit definition are local only. Subcircuits and models that are to be “known” by all elements and subcircuits must be defined at the top
level of the circuit hierarchy.


6. The nodes of elements in the subcircuit definition are local except for those that also appear on the
.SUBCKT statement and for the ground (0) node. The local nodes are given the unique name
_SubcircuitName1_ :[ _SubcircuitName2_ : _. . ._ ] _LocalNodeName_ .
and local devices are given the unique name
_DeviceType_ : _SubcircuitName1_ :[ _SubcircuitName2 . . ._ ] _DeviceName_ .


_Temperature Specification_ 105

### .TEMP Temperature Specification


The .TEMP statement specifies the temperatures at which the circuit is to be simulated.
_Form_


.TEMP _T_ 1 [ _T_ 2 _. . . TN_ ]


_T_ 1 is the first temperature at which the circuit is to be simulated.


_TN_ is the _N_ th temperature at which the circuit is to be simulated.


_Note_


1. The circuit is first simulated at temperature _T_ 1 and then resimulated at temperature _T_ 2 and so on.


2. If the .TEMP statement is missing then _T_ 1 is assumed to be _T_ NOM specified in a .OPTIONS statement.


3. Model parameters are specified at _T_ NOM and prior to the simulation at a new temperature temperature
dependent device parameters are reevaluated.


106 _CHAPTER 6. STATEMENT CATALOG_

### .TEXT Text Parameter Definition


_Transfer Function Specification_ 107

### .TF Transfer Function Specification


The transfer function specifies a small-signal DC analysis from which a small-signal transfer function and
input and output resistances are computed..
_Form_


.TF _OutputSpecification InputSourceName_


_OutputSpecification_ is the specification of the small-signal output quantity. It has the same format as the
_OutputSpecification_ in a .PRINT statement (see page 92).


_InputSourceName_ specifies the the name of the small-signal input independent voltage (V) or current (I)
source.


_Example_


.TF V(10) VINPUT
.TF V(10,2) ISOURCE
.TF I(VLOAD) ISOURCE


_Note_


1. The .TF statement initiates a small-signal DC analysis from which a small-signal transfer function and
input and output resistances are computed.


2. The transfer function computed is the ratio of the DC value of the output quantity to the input quantity.
In the above examples the following transfer functions are computed:


EXAMPLE Transfer Function


V(10)
.TF V(10) VINPUT
VINPUT


V(10 _,_ 2)
.TF V(10,2) ISOURCE
ISOURCE


I(VLOAD)
.TF I(VLOAD) ISOURCE

ISOURCE


108 _CHAPTER 6. STATEMENT CATALOG_

### TITLE Title Line


The TITLE line must be the first line of the input file. The string on this line included as the banner in
the output log file appearing at the top of each page.


_Transient Analysis_ 109

### .TRAN Transient Analysis


In transient analysis the current and voltages in a circuit are computed as a function of time.
General form:
_Form_


.TRAN _TSTEP TSTOP_ [ _TSTART_ [ _TMAX_ ] ] [UIC]


_TSTEP_ is the time increment for reporting transient simulation results.
(Units: s)


_TSTOP_ is the final analysis time.
(Units: s)


_TSTART_ is the start time for reporting the transient results. Transient analysis always begins at time
0. Before the time TSTART no results are recorded.
(Units: s; Optional; Default: 0)


_TMAX_ is the maximum step size used in incrementing the time during transient analysis.
(Units: s; Optional; Default: the smaller of TSTEP and (TSTOP-TSTART)/50)


UIC is the optional keyword to use initial conditions specified on the element line, by a .IC
statement or a .NODESET statement. Normally the operating point is determined (using
a DC analysis) before a transient analysis is initiated. If the UIC keyword is present the
initial DC analysis is omitted and instead the initial conditions specified by the IC parameter
supported by certain elements, by the .IC statement, or by the .NODESET statement are
used. In addition PSpice supports using an operating point solution that was previously
saved using the .SAVEBIAS statement.


_Example_


.TRAN 1NS 100NS
.TRAN 1NS 1000NS 500NS
.TRAN 10NS 1US UIC


_Note_


110 _CHAPTER 6. STATEMENT CATALOG_


1. If the UIC keyword is not present a DC analysis is automatically performed prior to a transient (.TRAN)
analysis to find the operating point of the circuit. All sources which are not time dependent (for
example, power supplies) are set to their DC value. The transient time interval is specified on a .TRAN
control line. The operating point solution is used as the initial conditions for a transient analysis.
Individual operating point solutions are overridden by initial transient conditions specified on the
.TRAN statement or by the initial conditions specified for specific elements by the IC keyword.


2. Normally the operating point is determined (using a DC analysis) before a transient analysis is initiated.
If the UIC keyword is present the initial DC analysis is omitted and instead the initial conditions specified
by the IC parameter supported by certain elements, by the .IC statement (see 66), or by the .NODESET
statement (see 76) are used. In addition PSpice supports using an operating point solution that was
previously saved using the .SAVEBIAS statement described on page 100.


3. If the UIC keyword is present the initial conditions specified in the .IC statement (described on page 66)
are used to establish the initial conditions. Initial conditions specified for individual elements using the
IC parameter on the element line will always have precedence over those specified in a .IC statement.
No DC analysis is performed prior to a transient analysis. Thus it is important to establish the initial
conditions at all nodes using the .IC statement or using the IC element parameter.


_Watch Analysis Statement_ 111

### .WATCH Watch Analysis Statement


112 _CHAPTER 6. STATEMENT CATALOG_

### .WCASE Sensitivity and Worst Case Analysis


The sensitivity and worst case analysis is a statistical analysis of a circuit causing the circuit to analyzed
many times with a random change of model parameters (parameters in a .MODEL statement).
_Form_


.WCASE _NumberOfRuns AnalysisType OutputSpecification OutputFunction_ [LIST]
+ [OUTPUT( _OutputSampleType_ )] [RANGE( _LowValue_, _HighValue_ )]


_NumberOfRuns_ is the total number of runs to do. This number includes the initial nominal run.


_AnalysisType_ is the type of analysis to be performed in Monte Carlo runs after the initial nominal run.
All analyses specified in the NETLIST are performed in the nominal run. The _AnalysisType_
must be one of the following:


to be filled in


DC is a keyword indicating that the DC analysis as specified by the .DC statement is repeated.
The sweep variable used in analyzing the output _OutputSpecification_ is the value of the
independent voltage or current source specified in the .DC statement which is discussed on
page 55.


AC is a keyword indicating that the AC small-signal analysis as specified by the .AC statement is
repeated. The sweep variable used in analyzing the output _OutputSpecification_ is frequency.


TRAN is a keyword indicating that the transient analysis as specified by the .TRAN statement is
repeated. The sweep variable used in analyzing the output _OutputSpecification_ is time.


_OutputSpecification_ specifies the quantity to be reported as the result of the Monte Carlo Analysis. It has
the same format as the _OutputSpecification_ in a .PRINT statement (see page 92). The result
is the value of the _OutputSpecification_ with respect to a sweep for DC and AC analysis, and
as a waveform for TRAN analysis.


_OutputFunction_ indicates the function to be performed on the output indicated by _OutputSpecification_ to
reduce the sweep or waveform at each run to a single numeric value. The _OutputFunction_
must be one of the following keywords:


YMAX which produces the greatest deviation of the sweep or waveform from the nominal run.


MAX which results in the maximum value in each sweep or waveform.


MIN which results in the minimum value in each sweep or waveform.


RISE EDGE( _Value_ ) which reports as the result the first run when the waveform crosses above the threshold
_Value_ . The algorithm used requires that one point in the waveform be below _Value_ and the
succeeding point be above _Value_ .


_Sensitivity and Worst Case Analysis_ 113


FALL EDGE( _Value_ ) which reports as the result the first run when the waveform crosses below the threshold
_Value_ . The algorithm used requires that one point in the waveform be above _Value_ and the
succeeding point be below _Value_ .


RANGE is an optional range indicating the range of the sweep variable over which _OutputFunction_
is to be performed. If this keyword is missing output is produced the range is not restricted.
The range of the sweep variable to be considered is from _LowValue_ to _HighValue_ inclusive.


_LowValue_ is the low end of the sweep variable to be considered in evaluating _OutputFunction_ .


_HighValue_ is the low end of the sweep variable to be considered in evaluating _OutputFunction_ .


LIST is an optional keyword that results in the model parameter values that are statistically varied
being printed out prior to each run. If it is omitted then the the statistically generated model
parameter values are not produced prior to each run.


OUTPUT is an optional keyword indicating the type of output to be produced by runs after the initial
nominal run. The output produced for each run sampled is determined by the .PLOT, .PRINT
and .PROBE statements in the NETLIST. If this keyword is missing output is produced only
for the nominal run.


_SEED_ is the keyword for the seed of the random number generator used in Monte Carlo Analysis


_SeedValue_ is the value of the seed used in the random number generator used to select sample runs at
random. (Optional; Default: 17,533; 1 _≤_ _SeedValue≤_ 32 _,_ 767)


_Note_


1. If the _AnalysisType_ is DC only one independent voltage or current source can be specified in the .DC
statement (discussed on page 55).


2. The random number generator is the subtractive method generator described by Knuth [28, p. 171].


3. The initial run uses the nominal parameter values given in the NETLIST. Subsequent runs statistically
vary model parameters indicated as having either lot LOT or device DEV tolerances. These tolerances
are specified in a .MODEL statement (see page 72).


114 _CHAPTER 6. STATEMENT CATALOG_

### .WIDTH Width Specification


_Form_


.WIDTH OUT= _ColumnWidth_


OUT is the keyword for column width of the output file.


_ColumnWidth_ is the column width of the output file. It must be either 80 or 132. If there is no .WIDTH
statement the ColumnWidth defaults to 80.

Figure 7.3: Schematic of the GASFET model. _VGS_, _VDS_, and _VGD_ are intrinsic gate-source, drain-source
and gate-drain voltages between the internal gate, drain, and source terminals designated _G_, _D_, and _S_
respectively. _RI_ is not used in PSpice.


120 _CHAPTER 7. ELEMENT CATALOG_


LEVEL = 1 _→_ Curtice Quadratic model
This was the first widely accepted model for a GaAs MESFET and
described in [11]. It uses rather simple empirical fits to measured
data. See page 120. (versions: PSpice)


LEVEL = 2 _→_ Raytheon model
This model is also known as the Statz model and model was developed at Raytheon for the modeling of GaAs MESFETs used
in digital circuits. It is also based on empirical fits to measured
data [23]. See page 120. (versions: PSpice)


LEVEL = 3 _→_ TOM or TriQuint model
The name of this model derives from _TriQuint’s Own Model_ [24].
See page 120. (versions: PSpice)


LEVEL = 4 _→_ Curtice-Ettenberg Cubic model
This is a refinement on the LEVEL 1 model [12]. It also uses simple
empirical fits to measured data. See page 120.


LEVEL = 5 _→_ Materka-Kacprzak model [13]
A distinguishing characteristic is that the drain-source current is
analytic and so it has better convergence characteristics than the
other models. See page 138.


LEVEL = 6 _→_ Angelov model
Another empirical GASFET model with analytic characteristics.
See page 143.


LEVEL = -1 _→_ TOM-2 model
An improved model from TriQuint. Another empirical GASFET
model with analytic characteristics. See page 136.


_GaAs MESFET_ 121


LEVEL 1, 2, 3 and 4 GASFET models


Many parameters of the LEVEL 1, 2, 3 and 4 GASFET models are the same and so these models will be
considered together. The parameter keywords are given in table **??** . It is assumed that the model parameters
were determined or measured at the nominal temperature _T_ NOM (default 27 _[◦]_ C) specified in the most recent
.OPTIONS statement preceding the .MODEL statement.


Table 7.2: MESFET model parameters.


ALPHA saturation voltage parameter (LEVEL=1,2,3,-1) ( _α_ ) V _[−]_ [1] 2
ALFA alternative keyword of ALPHA (LEVEL=1,2,3,-1) V _[−]_ [1] 2
(version: SomeVersionsOfSpice) ( _α_ )

Continued on next page


122 _CHAPTER 7. ELEMENT CATALOG_


Table 7.2: MESFET model parameters.


**Name** **Description** **Units** **Default**
AQ linear temperature coefficient of Q (LEVEL=3) _◦_ C _[−]_ [1] 0
(version: SomeVersionsOfSpice) ( _AQ_ )



AR1 linear temperature coefficient of R1 (LEVEL=1,4)
(version: SomeVersionsOfSpice) ( _AR_ 1)

AR2 linear temperature coefficient of R2 (LEVEL=1,4)
(version: SomeVersionsOfSpice) ( _AR_ 2)

ALPHATCE exponential temperature coefficient of ALPHA (LEVEL=-1)
( _TC,α_ )




_◦_ C _[−]_ [1] 0


_◦_ C _[−]_ [1] 0


%/ _[◦]_ C 0



ARD alternative keyword for TRD1 ( _ARD_ ) _◦_ C _[−]_ [1] 0
ARF linear temperature coefficient of RF (LEVEL=1,4) ( _ARF_ ) _◦_ C _[−]_ [1] 0
ARG alternative keyword for TRG1 ( _ARG_ ) _◦_ C _[−]_ [1] 0
ARI linear temperature coefficient of RI ( _ARI_ ) _◦_ C _[−]_ [1] 0
ARS alternative keyword for TRS1 ( _ARS_ ) _◦_ C _[−]_ [1] 0
AT linear temperature coefficient of TAU ( _Aτ_ ) _◦_ C _[−]_ [1] 0
AU linear temperature coefficient of U (LEVEL=1,3) ( _AU_ ) _◦_ C _[−]_ [1] 0
AVDS linear temperature coefficient of VDS0 (LEVEL=4) ( _AV DS_ 0) _◦_ C _[−]_ [1] 0
AVBD linear temperature coefficient of VBD ( _AV BD_ ) _◦_ C _[−]_ [1] 0
AVT0 (AVT-zero) linear temperature coefficient of VTO ( _AV T_ 0) _◦_ C _[−]_ [1] 0
B doping tail extending parameter ( _B_ ) V _[−]_ [1]
(version: PSpice) (LEVEL=2)
(version: SomeVersionsOfSpice) (LEVEL=2,3)



V _[−]_ [1] 0.3



BETA transconductance coefficient (LEVEL=1,2,3) ( _β_ ) A/V [2] 0.1
BETA transconductance coefficient (LEVEL=4) 1/V [2] 0
(version: SomeVersionsOfSpice) ( _β_ )



BETATCE exponential temperature coefficient of
BETA ( _TC,β_ )

BRD quadratic temperature coefficient of RD
(version: SomeVersionsOfSpice) ( _BRD_ )

BRG quadratic temperature coefficient of RG
(version: SomeVersionsOfSpice) ( _BRG_ )

BRI quadratic temperature coefficient of RI
(version: SomeVersionsOfSpice) ( _BRI_ )

BRS quadratic temperature coefficient of RS
(version: SomeVersionsOfSpice) ( _BRD_ )

BVT0 quadratic temperature coefficient of VT0
(version: SomeVersionsOfSpice) ( _BV T_ 0)

CDS drain-source capacitance ( _CDS_ ) F 0
CGD zero-bias gate-drain p-n capacitance ( _CGD_ ) F 0
CGD0 alternative keyword for CGD F 0
(version: SomeVersionsOfSpice) ( _CGD_ )

CGS zero-bias gate-source p-n capacitance ( _CGS_ ) F 0
CGS0 alternative keyword for CGS F 0
(version: SomeVersionsOfSpice) ( _CGS_ )

DELTA output feedback parameter (LEVEL=3) ( _δ_ ) (AV) _[−]_ [1] 0
DELTA output feedback parameter (LEVEL=-1) ( _δ_ ) (AV) _[−]_ [1] 0.2
Continued on next page


_GaAs MESFET_ 123


Table 7.2: MESFET model parameters.


**Name** **Description** **Units** **Default**
DELT alternative keyword for DELTA (LEVEL=3) (AV) _[−]_ [1] 0
(version: SomeVersionsOfSpice) ( _δ_ )



DELT alternative keyword for DELTA (LEVEL=-1)
(version: SomeVersionsOfSpice) ( _δ_ )

DLVL breakdown model flag not used
DLVL = 1 use original model
= 2 use enhanced model

E drain current power law coefficient
(version: SomeVersionsOfSpice) (LEVEL=1) ( _E_ )

EG bandgap voltage (barrier height) at 0 K ( _EG_ (0))
Schottky Barrier Diode: 0.69
Silicon: 1.16
Gallium Arsenide: 1.52
Germanium: 0.67 (LEVEL=1,2,3,4)

EG bandgap voltage (barrier height) at 0 K ( _EG_ (0))
Schottky Barrier Diode: 0.69
Silicon: 1.16
Gallium Arsenide: 1.52
Germanium: 0.67 (LEVEL=-1)


FC forward-bias depletion capacitance factor ( _FC_ ) - 0.5
GAMMA Static feedback parameter also known as - 0
voltage slope parameter of pinch-off voltage
(version: PSpice) (LEVEL=3)
(version: SomeVersionsOfSpice) (LEVEL=1,3) ( _γ_ )



GAMA alternative keyword for GAMMA
(version: SomeVersionsOfSpice) (LEVEL 1,3,-1)
( _γ_ )

GAMA Slope of drain characteristic in the linear region
(LEVEL=4) (version: SomeVersionsOfSpice) ( _γ_ _[′]_ )

GAMMATCE exponential temperature coefficient of
GAMMA ( _TC,γ_ )

GAP1 First bandgap correction factor ( _F_ GAP1)
Silicon: 0.000473
Old Value for Silicon: 0.000702
Gallium Arsenide: 0.000541
Germanium: 0.000456
(version: HSpice; SomeVersionsOfSpice)

GAP2 Second bandgap correction factor ( _F_ GAP2)
Silicon: 0.000636
Old Value for Silicon: 0.001108
Gallium Arsenide: 0.000204
Germanium: 0.000210
(version: HSpice; SomeVersionsOfSpice)




- 0


- 1.5


%/ _[◦]_ C 0


eV/ _[◦]_ C 0.000541


_◦_ C 0.000204



GMAX enhanced breakdown model parameter not used S 0
IS gate p-n saturation current ( _IS_ ) A 1E-14
K1 enhanced breakdown model parameter not used V _[−]_ [1] 0
Continued on next page


124 _CHAPTER 7. ELEMENT CATALOG_


Table 7.2: MESFET model parameters.


**Name** **Description** **Units** **Default**
K2 enhanced breakdown model parameter not used V 0
K3 enhanced breakdown model parameter not used V [2] 0
KF flicker noise coefficient ( _KF_ )   - 0
LAMBDA channel-length modulation (LEVEL=1,2,3,-1) ( _λ_ ) V _[−]_ [1] 0
LAMB alternative keyword for LAMBDA (LEVEL=1,2,3) V _[−]_ [1] 0
(version: SomeVersionsOfSpice) ( _λ_ )



LEVEL model index 1 _→_ Curtice quadratic model
2 _→_ Raytheon model
3 _→_ TOM (Triquint) model
4 _→_ Curtice cubic model
5 _→_ Materka-Kacprzak model
6 _→_ Angelov model
LEVELs 4,5,6 SomeVersionsOfSpice only




- 1



M gate p-n grading coefficient ( _M_ ) - 0.5
MGS gate-source p-n grading coefficient - M
(version: SomeVersionsOfSpice) ( _MGS_ )



MGD gate-drain p-n grading coefficient
(version: SomeVersionsOfSpice) ( _MGS_ )




- M



N gate p-n emission coefficient ( _n_ ) - 1
NG constant part of threshold ideality factor LEVEL -1 SomeV- - 1
ersionsOfSpice only ( _NG_ )



ND part of threshold ideality factor that depends on _VDS_
LEVEL -1 SomeVersionsOfSpice only ( _ND_ )

NPLT (not used) (version: SomeVersionsOfSpice)
( _VGMN_ )



V _[−]_ [1] 0


s 0



Q power-law parameter (LEVEL=3,-1) ( _Q_ ) - 2
R1 breakdown gate-drain resistance (LEVEL=1,4) Ω _∞_
(version: SomeVersionsOfSpice) not used ( _R_ 1)



R2 breakdown dependency on channel current (LEVEL=1,4)
(version: SomeVersionsOfSpice) (LEVEL=1,4) not
used ( _R_ 2)



Ω 0



RD drain resistance ( _RD_ ) Ω 0
RF forward-biased gate-source resistance (LEVEL=1,4) Ω _∞_
(version: SomeVersionsOfSpice) ( _RF_ )

RG gate resistance ( _RG_ ) Ω 0
RI channel resistance (not used) Ω 0
(version: SomeVersionsOfSpice) ( _RI_ )

RS source resistance ( _RS_ ) Ω 0
T alternative keyword for TAU s 0
(version: SomeVersionsOfSpice) ( _τ_ )



TBET alternative keyword for BETATCE
(version: SomeVersionsOfSpice) ( _TC,β_ )

TJ junction temperature (not used)
(version: SomeVersionsOfSpice) ( _TJ_ )



s 0


s 0



TM (not used) (version: SomeVersionsOfSpice) ( _TM_ ) s 0
TME (not used) (version: SomeVersionsOfSpice) ( _TME_ ) s 0
Continued on next page


_GaAs MESFET_ 125


Table 7.2: MESFET model parameters.


**Name** **Description** **Units** **Default**
TNOM nominal temperature (not used) s 0
(version: SomeVersionsOfSpice) ( _T_ NOM)

TAU conduction current delay time ( _τ_ ) s 0
TRG1 linear temperature coefficient of RG ( _ARG_ ) _◦_ C _[−]_ [1] 0
TRD1 linear temperature coefficient of RD ( _ARD_ ) _◦_ C _[−]_ [1] 0
TRS1 linear temperature coefficient of RS ( _ARS_ ) _◦_ C _[−]_ [1] 0
U critical field parameter for mobility degradation V/m 0
(LEVEL=1,2,3)
(version: SomeVersionsOfSpice) ( _U_ )

VBI gate p-n potential ( _V_ BI) V 1
VBR enhanced breakdown model parameter not used V [2] _∞_
VBD breakdown voltage V _∞_
(version: SomeVersionsOfSpice) ( _AV BD_ ))



VDELTA capacitance transistion voltage
(LEVEL=2,3) ( _V_ Δ)

VDS0 _VDS_ at which BETA was measured
(LEVEL=4) ( _V_ Δ)



V 0.2


V 4



VGMN (not used) ( _VGMN_ ) s 0
VGMX (not used) ( _VGMN_ ) s 0
VDMX (not used) ( _VGMN_ ) s 0
VMAX capacitance limiting voltage V 0.5
(LEVEL=2,3) ( _V_ MAX)



VTO (VT-oh) pinch-off voltage ( _VT_ 0) V -2.5
VT0 (VT-0) alternative keyword for VTO V -2.5
(version: SomeVersionsOfSpice) ( _AV DS_ 0))



V -2.5



VTOTC linear temperature coefficient of VTO ( _TC,V T_ 0) V/ _[◦]_ C 0
XTI temperature exponent of IS ( _XT I_ ) - 0
VBITC linear temperature coefficient of VBI ( _TC,BI_ ) - 0



Some versions of Spice use incorrect default values for some of the parameters. One example is the
default value for EG. The accepted value has changed with time. It is always a good idea not to rely on
default values other than 0.
The physical constants used in the model evaluation are


_k_ Boltzmann’s constant 1 _._ 3806226 10 _[−]_ [23] J/K
_q_ electronic charge 1 _._ 6021918 10 _[−]_ [19] C


_Standard Calculations_


Absolute temperatures (in kelvins, K) are used. The thermal voltage _V_ TH = _kT/q_ and the band gap energy
at the nominal temperature is


_EG_ ( _T_ NOM) = _EG_ (0) _−_ _F_ GAP14 _T_ NOM [2] _[/]_ [ (] _[T]_ [NOM][ +] _[ F]_ [GAP2][)] _[.]_ (7.1)


Here _EG_ (0) is the parameter EG — the band gap energy at 0 K. _F_ GAP1 and _F_ GAP2 are not parameters in
PSpice. PSpice documentation indicates that PSpice uses _F_ GAP1 = 0.000702 and _F_ GAP2 = 1108.


126 _CHAPTER 7. ELEMENT CATALOG_


_Temperature Dependence_


Temperature effects are incorporated as follows where _T_ and _T_ NOM are absolute temperatures in Kelvins
(K).
The parasitic resistance parameter dependencies are summarized in figure 7.4.
**Leakage Currents**


Current flows across the normally reverse biased gate-source and gate-drain junctions. The gate-source
leakage current _IGS_ = _Area ISe_ [(] _[V][GS][/V]_ [TH] _[ −]_ [1)] (7.32)
and the gate-drain leakage current _IGD_ = _Area ISe_ [(] _[V][GD][/V]_ [TH] _[ −]_ [1)] (7.33)


The dependencies of the parameters describing the leakage current are summarized in figure 7.5.

**LEVEL 2 (Raytheon Model)**


LEVEL _2 (Raytheon Model) I/V Characteristics_


The LEVEL 2 current/voltage characteristics are evaluated after first determining the mode (normal: _VDS ≥_ 0
or inverted: _VDS <_ 0) and the region (cutoff, linear or saturation) of the current ( _VDS, VGS_ ) operating point.


_Normal Mode: (VDS ≥_ 0 _)_


130 _CHAPTER 7. ELEMENT CATALOG_


The regions of operation are defined as follows with _VGST_ = _VGS −_ _VT_ 0 (7.39)
cutoff region: _VGST_ ( _t −_ _τ_ ) _≤_ 0
linear region: _VGST_ ( _t −_ _τ_ ) _>_ 0 and _VDS ≤_ 3 _/α_
saturation region: _VGS_ ( _t −_ _τ_ ) _> VT_ 0 and _VDS >_ 3 _/α_

The capacitance parameter dependencies are summarized in figure 7.9. The above capacitance model



KEYWORD
PARAMETERS

ALPHA _α_
CGD _CGD_
CGS _CGS_
CDS _CDS_
VBI _VBI_
VT0 _VT_ 0
VDELTA _V_ Δ
VMAX _V_ MAX



+ GEOMETRY
PARAMETER

_Area_



_→_ DEVICE
PARAMETERS
_CDS_ _[′]_ [=] _[ f]_ [(] _[Area, C][DS]_ [)]
_CGD_ _[′]_ [=] _[ f]_ [(] _[Area, C][GD][, α,]_
_B, FC_ _, VBI_ _, VT_ 0)
_CGS_ _[′]_ [=] _[ f]_ [(] _[Area, C][GS][, α,]_
_B, FC_ _, VBI_ _, VT_ 0)



Figure 7.9: LEVEL 2 (Raytheon model) capacitance dependencies.


does not satisfy drain-source charge conservation. Over a cycle, charge can be pumped from the drain to
the source. In practice this is often not a problem when this capacitance model is used buyt the user must
be ware. If it is a problem the user will see a periodic reponse can not be obtained even if the excotation is
periodic. For a further discussion see References [26,27].


132 _CHAPTER 7. ELEMENT CATALOG_


The above capacitance model does not satisfy drani-source charge conservation. Over a cycle charge can
be pumped from the drain to the source. In practice this is often not a problem when this capacitance model
is used but the user must be wary. If it is a problem the user will see that a periodic response can not be
obtained even if the excitation is periodeic. For a further discussion see References [26] and [27].
**LEVEL 3 (TOM Model)**


The LEVEL 3 model is an implementation of the TOM model (“Triquint’s Own Model) [24].


LEVEL _3 (TOM Model) I/V Characteristics_


The LEVEL 3 current/voltage characteristics are evaluated after first determining the mode (normal: _VDS ≥_ 0
or inverted: _VDS <_ 0) and the region (cutoff, linear or saturation) of the current ( _VDS, VGS_ ) operating point.
_Normal Mode: (VDS ≥_ 0 _)_


The regions of operation are defined as follows with _VGST_ = _VGS −_ _VP_ (7.51)
and _VP_ = _VT_ 0 _−_ _γVDS_ (7.52)


cutoff region: _VGST_ ( _t −_ _τ_ ) _≤_ 0
linear region: _VGST_ ( _t −_ _τ_ ) _>_ 0 and _VDS ≤_ 3 _/α_
saturation region: _VGST_ ( _t −_ _τ_ ) _>_ 0 and _VDS >_ 3 _/α_

Ktanh is a taylor series approximation to the tanh function of the LEVEL 1 model.


_Inverted Mode: (VDS <_ 0)


In the inverted mode the MESFET I/V characteristics are evaluated as in the normal mode (7.75) but with
the drain and source subscripts exchanged, and _VGD_ used as the controlling voltage instead of _VGS_ .
The following description does apply to SuperSpice.
The relationships of the parameters describing the I/V characteristics of the LEVEL 3 model are summarized
in figure 7.13.


LEVEL 3 (TOM Model) Capacitances



**LEVEL -1 (TOM-2 Model)**


The LEVEL -1 model is an enhancement of the LEVEL 3 TOM model.


LEVEL _-1 (TOM Model) I/V Characteristics_


134 _CHAPTER 7. ELEMENT CATALOG_



KEYWORD
PARAMETERS

ALPHA _α_
CGD _CGD_
CGS _CGS_
CDS _CDS_
VBI _VBI_
VT0 _VT_ 0
LAMBDA _VT_ 0
VMAX _V_ MAX
VDELTA _V_ Δ



+ GEOMETRY
PARAMETER

_Area_



_→_ DEVICE
PARAMETERS
_CDS_ _[′]_ [=] _[ f]_ [(] _[Area, C][DS]_ [)]
_CGD_ _[′]_ [=] _[ f]_ [(] _[Area, C][GD][,]_
_α, B, FC_ _, VBI_ _, VT_ 0)
_CGS_ _[′]_ [=] _[ f]_ [(] _[Area, C][GS][,]_
_α, B, FC_ _, VBI_ _, VT_ 0)



Figure 7.11: LEVEL 3 (TOM model) capacitance dependencies.


The LEVEL -1 current/voltage characteristics are evaluated after first determining the mode (normal: _VDS ≥_
0 or inverted: _VDS <_ 0) and the region (cutoff, linear or saturation) of the current ( _VDS, VGS_ ) operating
point.
_Normal Mode: (VDS ≥_ 0 _)_


The regions of operation are defined as follows with _VGST_ = _VGS −_ _VP_ (7.65)
and _VP_ = _VT_ 0 _−_ _γVDS_ (7.66)


cutoff region: _VGST_ ( _t −_ _τ_ ) _≤_ 0
linear region: _VGST_ ( _t −_ _τ_ ) _>_ 0 and _VDS ≤_ 3 _/α_
saturation region: _VGST_ ( _t −_ _τ_ ) _>_ 0 and _VDS >_ 3 _/α_


Then



_IDS_ = _Area IDS_ 0 _/_ (1 + _δIDS_ 0 _VDS_ ) (7.67)



_IDS_ 0 =




0 cutoff region
_β_ (7.68)
1 + _UVGST_ _[V]_ _GST_ _[ Q]_ [(] _[t][ −]_ _[τ]_ [)] _[F][d]_ [(] _[αV][DS]_ [)] linear and saturation regions



_x_
_Fd_ ( _αVDS_ ) = _√_



(7.69)
1 + _x_ [2]



_VG_ = _QVST_ ln [ _exp_ ( _VGST /_ ( _QVST_ ) + 1] (7.70)
_VST_ = _NST_ ( _kT/q_ ) (7.71)

_NST_ = _NG_ + _NDVDS_ (7.72)


_Inverted Mode: (VDS <_ 0)


In the inverted mode the MESFET I/V characteristics are evaluated as in the normal mode (7.92) but with
the drain and source subscripts exchanged, and _VGD_ used as the controlling voltage instead of _VGS_ .
The relationships of the parameters describing the I/V characteristics of the LEVEL -1 model are summarized in figure 7.15.


LEVEL -1 (TOM-2 Model) Capacitances


These are evaluated the same way the LEVEL 3 capacitanceaas described on 135 are evaluated.
**LEVEL -1 (TOM2 Model)**


_GaAs MESFET_ 135



KEYWORD
PARAMETERS

ALPHA _α_
BETA _β_
DELTA _δ_
GAMMA _γ_
LAMBDA _λ_
U _μ_
VTO _VT_ 0



+ GEOMETRY
PARAMETER

_Area_



_→_ DEVICE
PARAMETERS
_IDS_ = _f_ ( _Area, α, β, δ, γ,_
_λ, UVT_ 0)



Figure 7.12: LEVEL -1 (TOM-2 model) I/V dependencies.


The LEVEL -1 model is an implementation of the TOM model (“Triquint’s Own Model) [24].
LEVEL _-1 (TOM2 Model) I/V Characteristics_


The LEVEL -1 current/voltage characteristics are evaluated after first determining the mode (normal: _VDS ≥_
0 or inverted: _VDS <_ 0) and the region (cutoff, linear or saturation) of the current ( _VDS, VGS_ ) operating
point.
_Normal Mode: (VDS ≥_ 0 _)_


The regions of operation are defined as follows with _VGST_ = _VGS −_ _VP_ (7.73)
and _VP_ = _VT_ 0 _−_ _γVDS_ (7.74)


cutoff region: _VGST_ ( _t −_ _τ_ ) _≤_ 0
linear region: _VGST_ ( _t −_ _τ_ ) _>_ 0 and _VDS ≤_ 3 _/α_
saturation region: _VGST_ ( _t −_ _τ_ ) _>_ 0 and _VDS >_ 3 _/α_


Then



_IDS_ = _Area IDS_ 0 _/_ (1 + _δIDS_ 0 _VDS_ ) (7.75)




   0 cutoff region
_IDS_ 0 = _VG_ _[Q]_ [(] _[t][ −]_ _[τ]_ [)] _[F][d]_ [(] _[αV][DS]_ [)] linear and saturation regions [(7.76)]



_x_
_Fd_ ( _x_ ) = _√_




      -       _VGST_
_VG_ = _QVST_ ln exp

_QVST_



(7.77)
1 + _x_ [2]




- 
+ 1) (7.78)



_VST_ = _NST_




_kT_


_q_





(7.79)



_NST_ = _NG_ + _NDVDS_ (7.80)


_Inverted Mode: (VDS <_ 0)


In the inverted mode the MESFET I/V characteristics are evaluated as in the normal mode (7.75) but with
the drain and source subscripts exchanged, and _VGD_ used as the controlling voltage instead of _VGS_ .
The relationships of the parameters describing the I/V characteristics of the LEVEL -1 model are summarized
in figure 7.13.


136 _CHAPTER 7. ELEMENT CATALOG_



KEYWORD
PARAMETERS

ALPHA _α_
BETA _β_
DELTA _δ_
GAMMA _γ_
LAMBDA _λ_
U _μ_
VTO _VT_ 0



+ GEOMETRY
PARAMETER

_Area_



_→_ DEVICE
PARAMETERS
_IDS_ = _f_ ( _Area, α, β, δ, γ,_
_λ, UVT_ 0)



Figure 7.13: LEVEL 3 (TOM model) I/V dependencies.


LEVEL -1 (TOM2 Model) Capacitances


The LEVEL -1 (TOM2 Model) capacitances are identical to that of the LEVEL 3 model. This capacitance
model is based on the model proposed by Statz as used in the level 2 model. This is a charge conserving
symmetrical capacitance model.
The drain-source capacitance _CDS_ _[′]_ [=] _[ Area C][DS]_ (7.81)
The gate-source capacitance

**LEVEL -1 (TOM-2 Model)**


The LEVEL -1 model is an enhancement of the LEVEL 3 TOM model.


LEVEL _-1 (TOM Model) I/V Characteristics_


The LEVEL -1 current/voltage characteristics are evaluated after first determining the mode (normal: _VDS ≥_
0 or inverted: _VDS <_ 0) and the region (cutoff, linear or saturation) of the current ( _VDS, VGS_ ) operating
point.
_Normal Mode: (VDS ≥_ 0 _)_


The regions of operation are defined as follows with _VGST_ = _VGS −_ _VP_ (7.90)
and _VP_ = _VT_ 0 _−_ _γVDS_ (7.91)


cutoff region: _VGST_ ( _t −_ _τ_ ) _≤_ 0
linear region: _VGST_ ( _t −_ _τ_ ) _>_ 0 and _VDS ≤_ 3 _/α_
saturation region: _VGST_ ( _t −_ _τ_ ) _>_ 0 and _VDS >_ 3 _/α_


Then



_IDS_ = _Area IDS_ 0 _/_ (1 + _δIDS_ 0 _VDS_ ) (7.92)



_IDS_ 0 =




0 cutoff region
_β_ (7.93)
1 + _UVGST_ _[V]_ _GST_ _[ Q]_ [(] _[t][ −]_ _[τ]_ [)] _[F][d]_ [(] _[αV][DS]_ [)] linear and saturation regions



_x_
_Fd_ ( _αVDS_ ) = _√_



(7.94)
1 + _x_ [2]



_VG_ = _QVST_ ln [ _exp_ ( _VGST /_ ( _QVST_ ) + 1] (7.95)

_VST_ = _NST_ ( _kT/q_ ) (7.96)
_NST_ = _NG_ + _NDVDS_ (7.97)


_Inverted Mode: (VDS <_ 0)


In the inverted mode the MESFET I/V characteristics are evaluated as in the normal mode (7.92) but with
the drain and source subscripts exchanged, and _VGD_ used as the controlling voltage instead of _VGS_ .
The relationships of the parameters describing the I/V characteristics of the LEVEL -1 model are summarized in figure 7.15.


138 _CHAPTER 7. ELEMENT CATALOG_


LEVEL -1 (TOM-2 Model) Capacitances



KEYWORD
PARAMETERS

ALPHA _α_
BETA _β_
DELTA _δ_
GAMMA _γ_
LAMBDA _λ_
U _μ_
VTO _VT_ 0



+ GEOMETRY
PARAMETER

_Area_



_→_ DEVICE
PARAMETERS
_IDS_ = _f_ ( _Area, α, β, δ, γ,_
_λ, UVT_ 0)



Figure 7.15: LEVEL -1 (TOM-2 model) I/V dependencies.


These are evaluated the same way the LEVEL 3 capacitanceaas described on 135 are evaluated.
**LEVEL 4 (Curtice Cubic Model)**


LEVEL _4 (Curtice Cubic Model) I/V Characteristics_


The LEVEL 4 current/voltage characteristics are evaluated after first determining the mode (normal: _VDS ≥_ 0
or inverted: _VDS <_ 0) and the region (cutoff,linear or saturation) of the current ( _VDS, VGS_ ) operating point.
Curtice [11] proposed two DC current models: a quadratic channel current model and a cubic channel current
model. The quadratic channel model is implemented as the LEVEL 4 model.


_Normal Mode: (VDS ≥_ 0 _)_


The regions of operation are defined as follows with with _VGST_ = _VGS −_ _VT_ 0 (7.98)
cutoff region: _VGS_ ( _t −_ _τ_ ) _< VT_ 0
linear and saturation regions: _VGS_ ( _t −_ _τ_ ) _> VT_ 0


Then thedrain source current is given by



0 - - cutoff region
_Area_ _A_ 0 + _A_ 1 _Vx_ + _A_ 2 _Vx_ [2] [+] _[ A]_ [3] _[V]_ _x_ [ 3] tanh ( _γVDS_ ) linear and saturation (7.99)
regions


_Vx_ = _VGS_ ( _t −_ _τ_ ) [1 + _β_ ( _VDS_ 0 _−_ _VDS_ )] (7.100)


_Inverted Mode: (VDS <_ 0)


In the inverted mode the MESFET I/V characteristics are evaluated as in the normal mode (7.99) but with
the drain and source subscripts exchanged, and _VGD_ is the controlling voltage instead of _VGS_ .
The relationships of the parameters describing the I/V characteristics for the LEVEL 4 model are summarized in figure 7.16.


_LEVEL 4 (Curtice Cubic Model) Capacitances_


_GaAs MESFET_ 139



KEYWORD
PARAMETERS

A0 _A_ 0
A1 _A_ 1
A2 _A_ 2
A3 _A_ 3
BETA _β_
GAMMA _γ_
T, TAU _τ_
VTO _VT_ 0



+ GEOMETRY
PARAMETER

_Area_



_→_ DEVICE
PARAMETERS
_IDS_ = _f_ ( _Area,_
_A_ 0 _, A_ 1 _, A_ 2 _, A_ 3 _, β, γ, VT_ 0)



Figure 7.16: LEVEL 4 (Curtice cubic model) I/V dependencies.


The drain-source capacitance _CDS_ _[′]_ [=] _[ Area C][DS]_ (7.101)
the gate-source and gate-drain capacitances are


The LEVEL 4 capacitance parameter dependencies are summarized in figure 7.17.



KEYWORD
PARAMETERS

CGD _CGD_
CGS _CGS_
CDS _CDS_
FC _FC_
VBI _VBI_
MGS _MGS_
MGD _MGD_



+ GEOMETRY
PARAMETER

_Area_



_→_ DEVICE
PARAMETERS
_CDS_ _[′]_ [=] _[ f]_ [(] _[Area, C][DS]_ [)]
_CGD_ _[′]_ [=]
_f_ ( _Area, CGD, FC_ _, VBI_ _, MGD_ )
_CGS_ _[′]_ [=]
_f_ ( _Area, CGS, FC_ _, VBI_ _, MGS_ )



Figure 7.17: LEVEL 4 (Curtice Cubic model) capacitance dependencies.


**LEVEL 5 (Materka-Kacprzak Model)**


The parameter keywords of the Materka-Kacprzak model are given in table 7.3.


140 _CHAPTER 7. ELEMENT CATALOG_


Table 7.3: GASFET level 5 (Materka-Kacprzak) model keywords.
SomeVersionsOfSpice only. Parameters that are NOT USED
are reserved for future expansion.


**Name** **Description** **Units** **Default**
AC10 temperature coefficient of C10 ( _AC_ 10) _◦_ C _[−]_ [1] 0
ACF0 temperature coefficient of CF0 ( _ACF_ 0) _◦_ C _[−]_ [1] 0
AF flicker noise exponent ( _AF_ )   - 1
AE temperature coefficient of E ( _AE_ ) V _[−]_ [1] 0
AFAB slope factor of breakdown current ( _≥_ 0) ( _AF AB_ ) _◦_ C _[−]_ [1] 0
AFAG slope factor of gate conduction current ( _AF AG_ ) V _[−]_ [1] 38.696
AGAM temperature coefficient of GAMA ( _Aγ_ ) _◦_ C _[−]_ [1] 0
AIDS linear temperature coefficient of IDSS ( _Aλ_ ) %/ _[◦]_ C 0
AKE temperature coefficient of KE ( _AKE_ ) _◦_ C _[−]_ [1] 0
AKG temperature coefficient of KG ( _AKG_ ) _◦_ C _[−]_ [1] 0
ARD alternative keyword for TRD1 ( _ARD_ ) _◦_ C _[−]_ [1] 0
ARG alternative keyword for TRG1 ( _ARG_ ) _◦_ C _[−]_ [1] 0
ARS alternative keyword for TRS1 ( _ARS_ ) _◦_ C _[−]_ [1] 0
AR10 temperature coefficient of R10 ( _AR_ 10) _◦_ C _[−]_ [1] 0
ASL temperature coefficient of SL ( _ASL_ ) _◦_ C _[−]_ [1] 0
ASS temperature coefficient of SS ( _ASS_ ) _◦_ C _[−]_ [1] 0
AT temperature coefficient of T ( _AT_ ) _◦_ C _[−]_ [1] 0
AVBC linear temperature coefficient of VDC ( _AV BC_ )) _◦_ C _[−]_ [1] 0
AVP0 linear temperature coefficient of VP0 ( _AV P_ 0)) _◦_ C _[−]_ [1] 0
C10 gate-source Schottky barrier capacitance for F 0
_VGS_ = 0. ( _C_ 10)

CF0 gate-drain feedback capacitacne for _VGD_ = 0. ( _CF_ 0) F 0
C1S constant parasitic component of gate-source capacitance F 0
( _C_ 1 _S_ )

CDE drain-source electrode capacitance not used ( _CDE_ ) F 0
CDGE drain-gate electrode capacitance not used ( _CDGE_ ) F 0
CDS drain-source capacitance ( _CDS_ ) F 0
CDSD low frequency trapping capacitance (not used) F 0
( _CDSD_ )

CGE gate-source electrode capacitance not used ( _CDE_ ) F 0
CGS0 zero-bias gate-source p-n capacitance in Raytheon capaci- F 0
tance model. Used if CLVL = 2 ( _CGS_ )



CGD0 zero-bias gate-drain p-n capacitance in Raytheon capacitance model. Used if CLVL = 2 ( _CGS_ )

CLVL capacitance model flag
CLVLV = 1 use Materka-Kacprzak capacitance model
CLVLV = 2 use Raytheon capacitance model ( _CLV L_ )



F 0


- 1



E constant part of drain current power ( _E_ ) - 2
FCC ( _FCC_ ) - 0.8
GAMA Voltage slope parameter of pinch-off voltage ( _γ_ ) V _[−]_ [1] 0
IB0 current parameter of gate-drain breakdown A 0
source ( _≥_ 0) ( _IB_ 0)

IDSS frain saturation current for _VGS_ = 0 ( _IDSS_ ) A 0.1
Continued on next page


_GaAs MESFET_ 141


Table 7.3: GASFET level 5 (Materka-Kacprzak) model keywords.
SomeVersionsOfSpice only. Parameters that are NOT USED
are reserved for future expansion.


**Name** **Description** **Units** **Default**
IG0 saturation current of gate-source schottky A 0
barrier ( _IG_ 0)

K1 slope parameter of gate-source capacitance ( _K_ 1) V _[−]_ [1] 1.25
KE dependence of drain current power on _VGS_ ( _KE_ ) V _[−]_ [1] 0
KF slope parameter of gate-drain feedback capacitance ( _KF_ )   - 0
KFL flicker noise coefficient ( _KF L_ )   - 0
KG linearregion drain current _VGS_ dependence ( _KG_ ) V _[−]_ [1] 0
KR slope factor of intrinsic channel resistance ( _KR_ ) V _[−]_ [1] 0
LEVEL model index must be 5   - 1
M gate p-n grading coefficient ( _M_ )   - 0.5
MGS gate-source p-n grading coefficient ( _MGS_ )   - M
MGD gate-drain p-n grading coefficient ( _MGS_ )   - M
R10 intrinsic channel resistance for _VGS_ = 0. ( _R_ 10) Ω _∞_
RD drain resistance ( _RD_ ) Ω 0
RDSD channel trapping resistance not used ( _RDSD_ ) Ω _∞_
RG gate resistance ( _RG_ ) Ω 0
RS source resistance ( _RS_ ) Ω 0
SL slope of _VGS_ = 0 drain current, linear region ( _SL_ ) S 0.15
SS slope of _VGS_ = 0 drain current, saturated region ( _SS_ ) S 0
T channel transit time delay ( _τ_ ) s 0
TJ junction temperature (version: SomeVersionsOf- K 298
Spice) ( _TJ_ )



TNOM model reference temperature ( _>_ 0) (version: SomeVersionsOfSpice) ( _TNOM_ )



K 298



TRG1 temperature coefficient of RG ( _ARG_ ) _◦_ C _[−]_ [1] 0
TRD1 temperature coefficient of RG ( _ARD_ ) _◦_ C _[−]_ [1] 0
TRS1 temperature coefficient of RG ( _ARS_ ) _◦_ C _[−]_ [1] 0
VBC breakdown voltage ( _≥_ 0 ( _VBC_ ) V _∞_
VBI gate p-n potential in Raytheon capacitance model. Used V 1
if CLVL = 2. ( _V_ BI)

VP0 (VP-zero) pinch-off voltage for _VDS_ = 0 ( _VP_ 0) V -2.5



_Temperature Dependence_


The Materka-Kacprzak temperature effects are as follows where _T_ and _T_ NOM are absolute temperatures in
Kelvins (K).


142 _CHAPTER 7. ELEMENT CATALOG_


_IDSS_ ( _T_ ) = _IDSS_ ( _T_ NOM (1 + _AIDSS_ ( _T −_ _T_ NOM)) (7.104)
_C_ 10( _T_ ) = _C_ 10( _T_ NOM (1 + _AC_ 10( _T −_ _T_ NOM)) (7.105)

_CF_ 0( _T_ ) = _CF_ 0( _T_ NOM (1 + _ACF_ 0( _T −_ _T_ NOM)) (7.106)
_E_ ( _T_ ) = _E_ ( _T_ NOM (1 + _AE_ ( _T −_ _T_ NOM)) (7.107)

_KE_ ( _T_ ) = _KE_ ( _T_ NOM (1 + _AKE_ ( _T −_ _T_ NOM)) (7.108)
_KG_ ( _T_ ) = _KG_ ( _T_ NOM (1 + _AKG_ ( _T −_ _T_ NOM)) (7.109)

_γ_ ( _T_ ) = _γ_ ( _T_ NOM (1 + _Aγ_ ( _T −_ _T_ NOM)) (7.110)
_R_ 10( _T_ ) = _R_ 10( _T_ NOM (1 + _AR_ 10( _T −_ _T_ NOM)) (7.111)

_RG_ ( _T_ ) = _RG_ ( _T_ NOM (1 + _ARG_ ( _T −_ _T_ NOM)) (7.112)
_RD_ ( _T_ ) = _RD_ ( _T_ NOM (1 + _ARD_ ( _T −_ _T_ NOM)) (7.113)

_RS_ ( _T_ ) = _RS_ ( _T_ NOM (1 + _ARS_ ( _T −_ _T_ NOM)) (7.114)

_SL_ ( _T_ ) = _SL_ ( _T_ NOM (1 + _ASL_ ( _T −_ _T_ NOM)) (7.115)
_SS_ ( _T_ ) = _SS_ ( _T_ NOM (1 + _ASS_ ( _T −_ _T_ NOM)) (7.116)

_τ_ ( _T_ ) = _τ_ ( _T_ NOM (1 + _Aτ_ ( _T −_ _T_ NOM)) (7.117)
_VBC_ ( _T_ ) = _VBC_ ( _T_ NOM (1 + _AV BC_ ( _T −_ _T_ NOM)) (7.118)

_VP_ 0( _T_ ) = _VP_ 0( _T_ NOM (1 + _AV P_ 0( _T −_ _T_ NOM)) (7.119)


_Parasitic Resistances_


The resistive parasitics _RS_ _[′]_ [, and] _[ R]_ _D_ _[′]_ [are calculated from the sheet resistivities][ RS][ (=] _[ R][S]_ [) and][ RD][ (=] _[ R][D]_ [),]
and the _Area_ specified on the element line. RG (= _RG_ ) is used as supplied.


_RD_ _[′]_ = _R_         - _D/Area_ (7.120)

_RG_ _[′]_ = _RRGG/Area_ PSpiceSomeVersionsOfSpice (7.121)

_RG_ _[′]_ = _RG/Area_ (7.122)
_RS_ _[′]_ = _RS/Area_ (7.123)


The parasitic resistance parameter dependencies are summarized in figure 7.18.



KEYWORD
PARAMETERS

RD _RD_
RG _RG_
RS _RS_



+ GEOMETRY
PARAMETER
_Area_



_→_ DEVICE
PARAMETERS

_RD_ _[′]_ [=] _[ f]_ [(] _[Area, R][D]_ [)]
_RG_ _[′]_ [=] _[ f]_ [(] _[Area, R][G]_
_RS_ _[′]_ [=] _[ f]_ [(] _[Area, R][S]_ [)]



Figure 7.18: MESFET parasitic resistance parameter relationships.


LEVEL _5 (Materka-Kacprzak Model) I/V Characteristics_


_GaAs MESFET_ 143


The LEVEL 5 current/voltage characteristics are analytic except for the channel resistance _RI_ determination.



��
1 _−_ _[V][GS]_ [(] _[t][ −]_ _[τ]_ [)]



_VP_ 0 + _γVDS_



�( _E_ + _KEVGS_ ( _t −_ _τ_ ))



_IDS_ = _AreaIDSS_




_VDS_
1 + _SS_
_IDSS_





(7.124)




   _×_ tanh _SLVDS_
_IDSS_ (1 _−_ _KGVGS_ ( _t −_ _τ_ ))




         -          -          -          _IGS_ = _AreaIG_ 0 _e_ _[A][F AG][V][GS]_ _−_ 1 _−_ _IB_ 0 _e_ _[−][A][F AB]_ [(] _[V][GS]_ [ +] _[ V][BC]_ (7.125)




                -                 -                 -                 _IGD_ = _AreaIG_ 0 _e_ _[A][F AG][V][GD]_ _−_ 1 _−_ _IB_ 0 _e_ _[−][A][F AB]_ [(] _[V][GD]_ [ +] _[ V][BC]_ (7.126)

        _R_ 10(1 _−_ _KRVGS_ ) _/Area_ _KRVGS <_ 1 _._ 0
_RI_ = 0 _KRVGS ≥_ 1 _._ 0 (7.127)


The relationships of the parameters describing the I/V characteristics for the LEVEL 5 model are summarized in figure **??** .



KEYWORD
PARAMETERS

AFAG _AF AG_
AFAB _AF AB_
GAMA _γ_
IDSS _IDSS_
IB0 _IB_ 0
IG0 _IG_ 0
KG _KG_
KE _KE_
KR _KR_
R10 _R_ 10
SS _SS_
SL _SL_
T _τ_
VBC _VBC_
VP0 _VP_ 0



+ GEOMETRY
PARAMETER

_Area_



_→_ DEVICE
PARAMETERS
_IDS_ = _f_ ( _Area, E, γ, IDSS,_
_KE, KG, SL, SS, τ, VP_ 0)
_IGS_ = _f_ ( _Area, AF AB, AF AG,_
_IB_ 0 _, IG_ 0 _, VBC_ )
_IGD_ = _f_ ( _Area, AF AB, AF AG,_
_IB_ 0 _, IG_ 0 _, VBC_ )
_RI_ = _f_ ( _Area, KR, R_ 10 _, VGS_ )



Figure 7.19: LEVEL 5 (Materka-Kacprzak model) I/V dependencies.


_LEVEL 5 (Materka-Kacprzak Model) Capacitances_


Two capacitance models are available depending on the value of the _CLV L_ (CLVL) parameter. With _CLV L_ =
1 (default) the standard Materka capacitance model described below is used. With _CLV L_ = 0 the Raytheon
capacitance model described on page 129 is used. The Materka-Kacprzak capacitances are

_CDS_ _[′]_ = _Area C_        - _DS_        -        - (7.128)

_CGS_ _[′]_ = _AreaArea_        - _CC_ 1010(1(1 _− −_ _KFCC_ 1 _VGS_ ) _[M]_ ) _[GS][M][GS]_ + _C_ +1 _CS_ �1 _S_ _KK_ 11 _VVGSGS < F ≥_ _FCCCC_ (7.129)

         -          _CGD_ _[′]_ = _AreaArea_       - _CCFF_ 0 0(1(1 _− −_ _KFCC_ 1 _V_ 1)) _[M][M][GD][GD]_ [�][�] _KK_ 11 _VV_ 11 _< F ≥_ _FCCCC_ (7.130)


The LEVEL 5 capacitance parameter dependencies are summarized in figure 7.20.


144 _CHAPTER 7. ELEMENT CATALOG_



KEYWORD
PARAMETERS

CGD _CGD_
CGS _CGS_
CDS _CDS_
FC _FC_
VBI _VBI_
M _M_



+ GEOMETRY
PARAMETER

_Area_



_→_ DEVICE
PARAMETERS
_CDS_ _[′]_ [=] _[ f]_ [(] _[Area, C][DS]_ [)]
_CGD_ _[′]_ [=] _[ f]_ [(] _[Area, C]_ [10] _[, C]_ [1] _[S][,]_
_FCC_ _, K_ 1 _, VGS, MGS_ )
_CGS_ _[′]_ [=] _[ f]_ [(] _[Area, C][F]_ [ 0] _[, C]_ [1] _[S][,]_
_FCC_ _, K_ 1 _, V_ 1 _, VGS, MGS_ )



Figure 7.20: LEVEL 5 (Materka-Kacprzak model) capacitance dependencies.


**LEVEL 6 (Angelov Model)**


The parameter keywords of the Materka-Kacprzak model are given in table 7.4.


Table 7.4: GASFET model 6 (Angelov) keywords. Parameters that
are NOT USED are reserved for future expansion.


**Name** **Description** **Units** **Default**
AF flicker noise exponent ( _AF_ )   - 1
ACGS linear temperature coefficient of CGS ( _ACGS_ ) _◦_ C _[−]_ [1] 0
ACGD linear temperature coefficient of CGD ( _ACGD_ ) _◦_ C _[−]_ [1] 0
ALFA saturation voltage parameter ( _≥_ 0) ( _α_ ) V _[−]_ [1] 1.5
ARI linear temperature coefficient of RI ( _ARI_ ) _◦_ C _[−]_ [1] 0
ARG linear temperature coefficient of RG ( _ARG_ ) _◦_ C _[−]_ [1] 0
ARD linear temperature coefficient of RD ( _ARD_ ) _◦_ C _[−]_ [1] 0
ARS linear temperature coefficient of RS ( _ARS_ ) _◦_ C _[−]_ [1] 0
B1 unsaturated coefficient of P1 ( _B_ 1)   - 0
B2 drain voltage slope parameter for B1 ( _B_ 2)   - 3.0
BCGD quadratic temperature coefficient of CGD ( _BCGD_ ) _◦_ C _[−]_ [2] 0
BCGS quadratic temperature coefficient of CGS ( _BCGS_ ) _◦_ C _[−]_ [2] 0
BRI quadratic temperature coefficient of RI ( _BRI_ ) _◦_ C _[−]_ [2] 0
BRG quadratic temperature coefficient of RG ( _BRG_ ) _◦_ C _[−]_ [2] 0
BRS quadratic temperature coefficient of RS ( _BRS_ ) _◦_ C _[−]_ [2] 0
BRD quadratic temperature coefficient of RD ( _BRD_ ) _◦_ C _[−]_ [2] 0
CGD0 gate-source capacitance at Ψ3 = Ψ4 = 0 (¿= 0) ( _CGD_ 0) F 0
CGS0 gate-source capacitance at Ψ1 = Ψ2 = 0 (¿= 0) ( _CGS_ 0) F 0
EG barrier height at 0 K ( _EG_ ) V 0.8
GAMA voltage slope parameter for pinch-off V _[−]_ [1] 0
(NO LONGER USED)

IB0 breakdown saturation current ( _≥_ 0) ( _IB_ 0) A 0
IPK drain current at peak _gm_ ( _≥_ 0) ( _IP K_ ) A 0.1
IS diode saturation current ( _≥_ 0) ( _IS_ ) A 0
LAMB slope of the drain characteristic ( _λ_ ) V _[−]_ [1] 0
Continued on next page


_GaAs MESFET_ 145


Table 7.4: GASFET model 6 (Angelov) keywords. Parameters that
are NOT USED are reserved for future expansion.


**Name** **Description** **Units** **Default**
LEVEL model index must be 6   - 1
N diode ideality factor ( _>_ 0 ( _N_ )   - 1
NR breakdown ideality factor ( _>_ 0 ( _NR_ )   - 10
P2 polynomial coefficient of channel current ( _P_ 2) V _[−]_ [2] 0
P3 polynomial coefficient of channel current ( _P_ 3) V _[−]_ [3] 0
P4 polynomial coefficient of channel current ( _P_ 4) V _[−]_ [4] 0
P5 polynomial coefficient of channel current ( _P_ 5) V _[−]_ [5] 0
P6 polynomial coefficient of channel current ( _P_ 6) V _[−]_ [6] 0
P7 polynomial coefficient of channel current ( _P_ 7) V _[−]_ [7] 0
P8 polynomial coefficient of channel current ( _P_ 7) V _[−]_ [8] 0
P10 polynomial coefficient of g-s capacitance ( _P_ 10)   - 0
P11 polynomial coefficient of g-s capacitance ( _P_ 11) V _[−]_ [1] 0
P12 polynomial coefficient of g-s capacitance ( _P_ 12) V _[−]_ [2] 0
P13 polynomial coefficient of g-s capacitance ( _P_ 13) V _[−]_ [3] 0
P14 polynomial coefficient of g-s capacitance ( _P_ 14) V _[−]_ [4] 0
P20 polynomial coefficient of g-s capacitance ( _P_ 20)   - 0
P21 polynomial coefficient of g-s capacitance ( _P_ 21) V _[−]_ [1] 0
P22 polynomial coefficient of g-s capacitance ( _P_ 22) V _[−]_ [2] 0
P23 polynomial coefficient of g-s capacitance ( _P_ 23) V _[−]_ [3] 0
P24 polynomial coefficient of g-s capacitance ( _P_ 24) V _[−]_ [4] 0
P30 polynomial coefficient of g-d capacitance ( _P_ 30)   - 0
P31 polynomial coefficient of g-d capacitance ( _P_ 31) V _[−]_ [1] 0
P32 polynomial coefficient of g-d capacitance ( _P_ 32) V _[−]_ [2] 0
P33 polynomial coefficient of g-d capacitance ( _P_ 33) V _[−]_ [3] 0
P34 polynomial coefficient of g-d capacitance ( _P_ 34) V _[−]_ [4] 0
P40 polynomial coefficient of g-d capacitance ( _P_ 40)   - 0
P41 polynomial coefficient of g-d capacitance ( _P_ 41) V _[−]_ [1] 0
P42 polynomial coefficient of g-d capacitance ( _P_ 42) V _[−]_ [2] 0
P43 polynomial coefficient of g-d capacitance ( _P_ 43) V _[−]_ [3] 0
P44 polynomial coefficient of g-d capacitance ( _P_ 44) V _[−]_ [4] 0
P1CC polynomial coefficient of g-d capacitance ( _P_ 1 _CC_ ) 0
PSAT polynomial coefficient of channel current PSAT ( _P_ 1) V _[−]_ [1] 1.3
RI channel resistacne ( _≥_ 0) NOT USED ( _RI_ ) 0
T channel time delay ( _≥_ 0) ( _τ_ ) s 0
TJ junction temperature ( _TJ_ ) K 298
TM _IDS_ linear temperature coefficient ( _TM_ ) 0
TME _IDS_ power law temperature coefficient ( _TME_ ) 0
TNOM model reference temperature ( _>_ 0) ( _TNOM_ ) K 298
VBD breakdown voltage ( _VBD_ ) 0
VPK0 gate-source voltage for unsaturated peak _gm_ ( _VP K_ 0) V -0.5
VPKS gate-source voltage for peak _gm_ ( _VP KS_ ) V 0
XTI saturation current temperature exponent ( _XT I_ ) 2


_Temperature Dependence_


146 _CHAPTER 7. ELEMENT CATALOG_


The relationships of the parameters describing the I/V characteristics for the LEVEL 6 model are summarized in figure **??** .


### C Capacitor


_Form_

###### _V_ _C_


Figure 7.25: C — capacitor element.


C _name N_ 1 _N_ 2 _CapacitorValue_ [IC= _VC_ ] [L= _Length_ ] [W= _Width_ ]


Spice3 _Form_


C _name N_ 1 _N_ 2 [ _ModelName_ ] _CapacitorValue_ [IC= _VC_ ] [L= _Length_ ] [W= _Width_ ]


PSpice _Form_


C _name N_ 1 _N_ 2 [ _ModelName_ ] _CapacitorValue_ [IC= _VC_ ]


_N_ 1 is the positive element node,


_N_ 2 is the negative element node, and


_ModelName_ is the optional model name.


_CapacitorValue_ is the capacitance. This is modified if _ModelName_ is specified.
(Units: F; Required; Symbol: _CapacitorV alue_ )


_L_ is the length _Length_ of the integrated capacitor.
(Units: m; Required in Spice3 if _ModelName_ specified; Symbol: _L_ ;)


_W_ is the width _Length_ of the integrated capacitor.
(Units: m; Optional; Default: Default width DEFW specified in model _ModelName_ ; Symbol:
_L_ ;)


IC is the optional initial condition specification Using IC= _VC_ is intended for use with the UIC
option on the .TRAN line, when a transient analysis is desired with an initial voltage _VC_ across
the capacitor rather than the quiescent operating point. Specification of the transient initial
conditions using the .IC statement (see page 66) is preferred and is more convenient.


_Example_


CAP1 1 GND 12.3PF
C1 node1 0 ((12.3 + 2.1)/2)


_Model Type_


CAP


_Capacitor_ 151


**CAP Model** Spice3 Only Capacitor Model


_Form_


.MODEL _ModelName_ CAP( [ [ _keyword = value_ ] _..._ ] )


_Example_

.MODEL SMALLCAP CAP( CJ CJSW DEFW10 _[−]_ [6] NARROW)


_Model Keywords_


**Name** **Description** **Units** **Default**
CJ junction bottom capacitance ( _CJ_ ) F/m [2] REQUIRED
CJSW junction sidewall capacitance ( _CJ,_ SW) F/m REQUIRED
DEFW default device width ( _W_ DEF) meters 10 _[−]_ [6]

NARROW narrowing due to side etching ( _X_ NARROW) meters 0


The Spice3 capacitance model is a process model for a monolithicly fabricated capacitor enabling the
capacitance to be determined from geometric information. If the parameter W is not specified on the element
line then _Width_ defaults to DEFW = _W_ DEF. The effective dimensions are reduced by etching so that the
effective length of the capacitor is


_L_ EFF = ( _Length −_ _X_ NARROW) (7.168)


and the effective width is
_W_ EFF = ( _Width −_ _X_ NARROW) (7.169)


The new value of the capacitance


_NewCapacitorValue_ = _CJ_ _L_ EFF _W_ EFF + 2 _CJ,_ SW( _L_ EFF + _W_ EFF) (7.170)


**CAP Model** PSpice Only Capacitor Model


_Form_


.MODEL _ModelName_ CAP( [ [ _keyword = value_ ] _..._ ] )


_Example_


.MODEL SMALLCAP GASFET(C=2.5 VC1=0.01 VC2=0.001 TC1=0.02 TC2=0.005)


152 _CHAPTER 7. ELEMENT CATALOG_


_Model Keywords_


**Name** **Description** **Units** **Default**
C capacitance multiplier ( _C_ MULTIPLIER)   - 1
VC1 linear voltage coefficient ( _VC_ 1) 1/V 0
VC2 quadratic voltage coefficient ( _VC_ 2) 1/V 0
TC1 linear temperature coefficient ( _TC_ 1) 1/ _[◦]_ _C_ 0
TC2 quadratic temperature coefficient ( _TC_ 1) 1/ _[◦]_ _C_ 0


The PSpice capacitance model is a nonlinear temperature dependent capacitor model. It is assumed
that the model parameters were determined or measured at the nominal temperature _T_ NOM (default 27 _[◦]_ C)
specified in the most recent .OPTIONS statement preceeding the .MODEL statement.
If the CAP model is specified then a new capacitance is evaluated as

                                 -                                 _C_ = _CapacitorV alue C_        - MULTIPLIER 1 + _VC_ 1 _VC_ + _VC_ 2 _VC_ [2] (7.171)

_×_ 1 + _TC_ 1( _T −_ _T_ NOM) + _TC_ 2( _T −_ _TNOM_ ) [2][�] (7.172)


where _VC_ is the voltage across the capacitor as in figure 7.25 and _T_ is the current temperature. If PSpice
CAP model is not specified then the capacitance specified on the element line is used.


_Diode_ 153

### D Diode


Figure 7.26: D — diode element.


_Form_


D _name n_ 1 _n_ 2 _ModelName_ [ _Area_ ] [OFF] [IC _=VD_ ]


PSpice _Form_


D _name n_ 1 _n_ 2 _ModelName_ [ _Area_ ] [OFF]


_n_ 1 is the positive (anode) diode node.


_n_ 1 is the negative (cathode) diode node.


_ModelName_ is the model name.


_Area_ is an optional relative area factor.
(Units: none; Optional; Default: 1, Symbol: _Area_ )


OFF indicates an (optional) starting condition on the device for DC operating point analysis. If
specified the DC operating point is calculated with the terminal voltages set to zero. Once
convergence is obtained, the program continues to iterate to obtain the exact value of the
terminal voltages. The OFF option is used to enforce the solution to correspond to a desired
state if the circuit has more than one stable state.


IC is the (optional) initial condition specification. Using IC = _VD_ is intended for use with the
UIC option on the other than the quiescent operating point. Specification of the transient
initial conditions using the .IC statement (see page 66) is preferred and is more convenient.


_Example_


DBRIDGE 2 10 DIODE1
DCLMP 3 7 DMOD 3.0 IC=0.2


_Model Type_


DIODE


**DIODE Model** Diode Model


_Note_


154 _CHAPTER 7. ELEMENT CATALOG_


_NAnode_





_NCathode_


Figure 7.27: Schematic of diode element model.


1. In some Spice implementations XTI is called PT and VJ is called PB.


2. It is assumed that the model parameters were determined or measured at the nominal temperature
_T_ NOM (default 27 _[◦]_ _C_ ) specified in the most recent .OPTIONS statement preceeding the .MODEL statement.


The physical constants used in the model evaluation are


_k_ Boltzman’s constant 1 _._ 3806226 10 _[−]_ [23] J/K
_q_ electronic charge 1 _._ 6021918 10 _[−]_ [19] C


_Temperature Dependence_


Temperature effects are incorporated as follows where _T_ and _T_ NOM are absolute temperatures in Kelvins
(K). The thermal voltage


_Diode_ 155


Table 7.5: DIODE model parameters.


**Name** **Description** **Units** **Default** **Area**
AF flicker noise exponent ( _AF_ ) - 1
BV magnitude of reverse breakdown voltage (positive) ( _VB_ ) V _∞_
CJO zero-bias _p-n_ junction capacitance per unit area (CJ-oh) F 0 ( _CJ_ 0)


### F Current-Controlled Current Source

Figure 7.29: F — current-controlled current source element.


F _name N_ + _N−_ _VoltageSourceName Gain_
F _name N_ + _N−_ POLY( _D_ ) _VoltageSourceName_ 1 _... VoltageSourceNameD Polyno-_
_mialCoefficients_


_N_ + is the positive voltage source node.


_N−_ is the negative voltage source node.



_VoltageSourceName_ is the name of the voltage source the current through which is the controlling current.
The voltage source must be a V element.


_Gain_ is the current gain.


POLY is the identifier for the polynomial form of the element


_D_ is the degree of the poynomial. The number of pairs of controlling nodes must be equal to
_Degree_ .


_VoltageSourceNamei_ is the name of the voltage source the current through which is the _i_ th controlling
current. The voltage source must be a V element.


_PolynomialCoefficients_ is the set of polynomial coefficients which must be specified in the standard polynomial coefficient format discussed on page 47.


_Example_


E1 2 3 14 1 2.0 Linear Gain Instance


F _name N_ + _N−_ _NC_ + _NC−_ _Gain_


The value of the voltage generator is linearly proportional to the controlling current:


_vo_ = _Gain vc_ (7.196)


POLYnomial Instance


162 _CHAPTER 7. ELEMENT CATALOG_


F _name N_ + _N−_ POLY( _D_ ) ( _NC_ 1+ _NC_ 1 _−_ ) _..._ ( _NCD_ + _NCD−_ ) _PolynomialCoefficients_


The value of the voltage generator is a polynomial function of the controlling voltages:


_vo_ = _f_ ( _ic_ 1 _, ..., ici, ...icD_ ) (7.197)


where the number of controlling currents is _D_ - the degree of the polynomial specified on the element line.
_ici_ is the _i_ th controlling current and is the current flowing from the + terminal to the _−_ terminal in the _i_ th
voltage source of name _VoltageSourceName_ .


_Voltage-Controlled Current Source_ 163

### G Voltage-Controlled Current Source


###### _i_ _N_

Figure 7.30: G — voltage-controlled current source element.


G _name N_ + _N−_ _NC_ + _NC−_ _Transconductance_
G _name N_ + _N−_ POLY( _D_ ) _NC_ + _NC−_ _PolynomialCoefficients_



PSpice _Form_


G _name N_ + _N−_ _NC_ + _NC−_ _Transconductance_
G _name N_ + _N−_ POLY( _D_ ) ( _NC_ 1+ _NC_ 1 _−_ ) _..._ ( _NCD_ + _NCD−_ ) _PolynomialCoeffi-_
_cients_ G _name N_ + _N−_ VALUE= _{ Expression }_
G _name N_ + _N−_ TABLE _{ Expression }_ =( _TableInput_, _TableOutput_ ) _..._
G _name N_ + _N−_ LAPLACE _{ Expression }_ = _{ TransformExpression }_
G _name N_ + _N−_ FREQ _{ Expression }_ =( _Frequency_, _Magnitude_, _Phase_ ) _..._
G _name N_ + _N−_ CHEBYSHEV _{ Expression }_ = _Type_, _CutoffFrequency ..._, _Phase ..._


164 _CHAPTER 7. ELEMENT CATALOG_


_N_ + is the positive voltage source node.


_N−_ is the negative voltage source node.


_NC_ + is the positive controlling node.


_NC−_ is the negative controlling node.


_Transconductance_ is the transconductance.


POLY is the identifier for the polynomial form of the element


_D_ is the degree of the poynomial. The number of pairs of controlling nodes must be equal to
_Degree_ .


_NCi_ + the positive node of the _i_ th controlling node pair.


_NCi−_ the negative node of the _i_ th controlling node pair.


_PolynomialCoefficients_ is the set of polynomial coefficients which must be specified in the standard polynomial coefficient format discussed on page 47.


VALUE is the identifier for the value form of the element.


_Expression_ This is an expression of the form discussed on page 47.


TABLE is the identifier for the table form of the element.


_TableInput_ This is the independent input of the table. See the TABLE parameter above.


_TableInput_ This is the dependent output of the table. See the TABLE parameter above.


LAPLACE is the identifier for the laplace form of the element.


_TransformExpression_


FREQ is the identifier for the frequency form of the element.


_Frequency_


_Magnitude_


_Phase_


CHEBYSHEV is the identifier for the chebyshev form of the element.


_Type_


_CutoffFrequency_


_Phase_


_Example_


G1 2 3 14 1 2.0


_Note_


_Voltage-Controlled Current Source_ 165


1. Several form of the voltage-controlled voltage source element are supported in addition to the Linear
Transconductance form which is the default. The other forms are selected based on the the identifier
POLY, VALUE, TABLE, LAPLACE, FREQ or CHEBYSHEV.


Linear Transconductance Instance


G _name N_ + _N−_ _NC_ + _NC−_ _Transconductance_


The value of the voltage generator is linearly proportional to the controlling voltage:


_vo_ = _T ransconductance vc_ (7.198)


POLYnomial Instance


G _name N_ + _N−_ POLY( _D_ ) ( _NC_ 1+ _NC_ 1 _−_ ) _..._ ( _NCD_ + _NCD−_ ) _PolynomialCoefficients_


The value of the voltage generator is a polynomial function of the controlling voltages:


_vo_ = _f_ ( _vc_ 1 _, ..., vci, ...vcD_ ) (7.199)


where the number of controlling voltages is _D_ - the degree of the polynomial specified on the element line.
_vci_ is the _i_ th controlling voltage and is the voltage of the _nci_ + node with respect to the _nci_ + node.


VALUE Instance — PSpice92 only


G _name N_ + _N−_ VALUE= _{ Expression }_


The value of the voltage generator is the resultant of an expression evaluation.


_vo_ = _f_ ( _vc_ ) (7.200)


TABLE Instance — PSpice92 only


G _name N_ + _N−_ TABLE _{ Expression }_ =( _TableInput_, _TableOutput_ ) _..._


_vo_ = _f_ ( _vc_ ) (7.201)


LAPLACE Instance — PSpice92 only


G _name N_ + _N−_ LAPLACE _{ Expression }_ = _{ TransformExpression }_


_vo_ = _f_ ( _vc_ ) (7.202)


FREQ — PSpice92 only


G _name N_ + _N−_ FREQ _{ Expression }_ =( _Frequency_, _Magnitude_, _Phase_ ) _..._


166 _CHAPTER 7. ELEMENT CATALOG_


_vo_ = _f_ ( _vc_ ) (7.203)


CHEBYSHEV — PSpice92 only


G _name N_ + _N−_ CHEBYSHEV _{ Expression }_ = _Type_, _CutoffFrequency ..._, _Phase ..._


_Current-Controlled Voltage Source_ 167

### H Current-Controlled Voltage Source

###### N 


_Form_


###### _VoltageSourceName_

Figure 7.31: H — current-controlled voltage source element.


H _name N_ + _N−_ _VoltageSourceName Transresistance_
H _name N_ + _N−_ POLY( _D_ ) _VoltageSourceName_ 1 _... VoltageSourceNameD Polyno-_
_mialCoefficients_


_N_ + is the positive voltage source node.


_N−_ is the negative voltage source node.



_VoltageSourceName_ is the name of the voltage source the current through which is the controlling current.
The voltage source must be a V element.


_Transresistance_ is the Transresistance of the element.


POLY is the identifier for the polynomial form of the element


_D_ is the degree of the poynomial. The number of pairs of controlling nodes must be equal to
_Degree_ .


_VoltageSourceNamei_ is the name of the voltage source the current through which is the _i_ th controlling
current. The voltage source must be a V element.


_PolynomialCoefficients_ is the set of polynomial coefficients which must be specified in the standard polynomial coefficient format discussed on page 47.


_Example_


E1 2 3 14 1 2.0


Linear Transresistance Instance


H _name N_ + _N−_ _NC_ + _NC−_ _Transresistance_


The value of the voltage generator is linearly proportional to the controlling current:


_vo_ = _T ransresistance vc_ (7.204)


POLYnomial Instance


168 _CHAPTER 7. ELEMENT CATALOG_


H _name N_ + _N−_ POLY( _D_ ) ( _NC_ 1+ _NC_ 1 _−_ ) _..._ ( _NCD_ + _NCD−_ ) _PolynomialCoefficients_


The value of the voltage generator is a polynomial function of the controlling voltages:


_vo_ = _f_ ( _ic_ 1 _, ..., ici, ...icD_ (7.205)


where the number of controlling currents is _D_ - the degree of the polynomial specified on the element line.
_ici_ is the _i_ th controlling current and is the current flowing from the + terminal to the _−_ terminal in the _i_ th
voltage source of name _VoltageSourceName_ .


_Independent Current Source_ 169

### I Independent Current Source

###### _+_ _i_




###### _-_



_Form_



Figure 7.32: I — independent current source.


I _name N_ + _N−_ [ [ _DC_ ] [ _DCvalue_ ]
+ [AC [ _ACmagnitude_ [ _ACphase_ ] ] ]
+ [DISTOF1 [ _F1Magnitude_ [ _F1Phase_ ] ] ] + [DISTOF2 [ _F2Magnitude_ [ _F2Phase_ ] ]
]



Spice3 _Form_


I _name N_ + _N−_ [ [ _DC_ ] [ _DCvalue_ ]
+ [AC [ _ACmagnitude_ [ _ACphase_ ] ] ]
+ [ _TransientSpecification_ ]
+ [DISTOF1 [ _F1Magnitude_ [ _F1Phase_ ] ] ]
+ [DISTOF2 [ _F2Magnitude_ [ _F2Phase_ ] ] ]


PSpice _Form_


I _name N_ + _N−_ [ [ _DC_ ] [ _DCvalue_ ] [AC [ _ACmagnitude_ [ _ACphase_ ] ] ]
+ [ _TransientSpecification_ ]


_Example_


IBIAS 1 0 1.0M
ICLOCK 20 5 PULSE(0M 10M 1N 2N 1.5N 21.9N 5N 20N)
ISSIGNAL AC 1U 90


170 _CHAPTER 7. ELEMENT CATALOG_


_N_ + is the positive current source node. (Current flow is out of the positive to the negative node


_N−_ is the negative current source node.


DC is the optional keyword for the DC value of the source.


_DCvalue_ is the DC current value of the source.
(Units: A; Optional; Default: 0; Symbol: _IDC_ )


AC is the keyword for the AC value of the source.


_ACmagnitude_ is the AC magnitude of the source used during ACanalysis. That is, it is the peak AC current
so that the AC signal is _ACmagnitude_ sin( _ωt_ + ACphase). _ACmagnitude_ is ignored for other
types of analyses.
(Units: A; Optional; Default: 1; Symbol: _IAC_ )


_ACphase_ is the ac phase of the source. It is used only in AC analysis.
(Units: Degrees; Optional; Default: 0; Symbol: _φ_ AC)


DISTOF1 is the distortion keyword for distortion component 1 which hass frequency F1. (see the
description of the .DISTO statement on page 58).


_F1magnitude_ is the magnitude of the distortion component at F1. See .DISTOF1 keyword above.
(Units: A; Optional; Default: 1; Symbol: _IF_ 1)


_F1phase_ is the phase of the distortion component at F1. See .DISTOF1 keyword above.
(Units: Degrees; Optional; Default: 0; Symbol: _φF_ 1)


DISTOF2 is the distortion keyword for distortion component 2 which hass frequency F2. (see the
description of the .DISTO statement on page 58).


_F2magnitude_ is the magnitude of the distortion component at F2. See .DISTOF2 keyword above.
(Units: A; Optional; Default: 1; Symbol: _IF_ 2)


_F2phase_ is the phase of the distortion component at F2. See .DISTOF2 keyword above.
(Units: Degrees; Optional; Default: 0; Symbol: _φF_ 2)


_TransientSpecification_ is the optional transient specification described more fully below.


_Note_


1. The independent current source has three different sets of parameters to describe the source for DC
analysis (see .DC on page 55), AC analysis (see .AC on page 53), and transient analysis (see .TRAN on
page 109). The DC value of the source is used during bias point evaluation and DC analysis is _DCValue_ .
It is also the constant value of the current source if no _TransientSpecification_ is supplied. It may also
be used in conjunction with the PWL transient specification if a time zero value is not provided as part
of the transient specification. The AC specification, indicated by the keyword AC is independent of the
DC parameters and the _Transient Specification_ .


2. The original documentation distributed with Spice2g6 and Spice3 incorrectly stated that if a _Tran-_
_sientSpecification_ was supplied then the time-zero transient current was used in DC analysis and in
determiniong the operating point.


**Transient Specification**


_Independent Current Source_ 171


Five transient specification forms are supported: pulse (PULSE), exponential (EXP), sinusoidal (SIN),
piece-wise linear (PWL), and single-frequency FM (SFFM). The default values of some of the parameters of
these transient specifications include TSTEP which is the printing increment and TSTOP which is the final
time (see the .TRAN statement on page 109 for further explanation of these quantities). In the following _t_ is
the transient analysis time.
**Exponential:**



### J Junction Field-Effect Transistor


###### _NDrain_ _NSource_


###### _NGate_


###### _NDrain_ _NSource_


###### _NGate_



(a) (b)


Figure 7.38: J — Junction field effect transistor element: (a) _n_ channel JFET; (b) _p_ channel JFET.


_Form_


J _name NDrain NGate NSource ModelName_ [ _Area_ ] [OFF] [IC _=VDS, VGS_ ]


PSpice _Form_


J _name NDrain NGate NSource ModelName_ [ _Area_ ]


_Example_


J1 7 2 3 JM1 OFF


_NDrain_ is the drain node


_NGate_ is the gate node


_NSource_ is the source node


ModelName is the model name


_Area_ is the area factor. (Units: none; Optional; Default: 1; Symbol: _Area_ )


OFF indicates an (optional) initial condition on the device for DC operating point analysis. If
specified the DC operating point is calculated with the terminal voltages set to zero. Once
convergence is obtained, the program continues to iterate to obtain the exact value of the
terminal voltages. The OFF option is used to enforce the solution to correspond to a desired
state if the circuit has more than one stable state.


IC is the optional initial condition specification. Using IC= _VDS, VGS_ is intended for use with
the UIC option on the .TRAN line, when a transient analysis is desired starting from other
than the quiescent operating point. Specification of the transient initial conditions using
the .IC statement (see page 66) is preferred and is more convenient.


**NJF Model** N-Channel JFET Model


_Junction Field-Effect Transistor_ 177


**PJF Model** P-Channel JFET Model


_D_ _RD_
_NDrain_


Figure 7.39: Schematic of the JFET model. _VGS_, _VDS_, and _VGD_ are intrinsic gate-source, drain-source
and gate-drain voltages between the internal gate, drain, and source terminals designated _G_, _D_, and _C_
respectively.


The parameters of the _n_ -channel (NJF) and of the _p_ -channel (PJF) models are the same and are given
in table 7.6.
The parameters of the JFET can be completely specified in the model _ModelName_ . This facilitates
the use of standard transistors by using absolute quantities in the model. Alternatively scalable process
parameters can be specified in the model _ModelName_ and these scaled by the _Area_ parameter on the JFET
element line. The parameters that can be scaled by _Area_ are BETA, CGS, CGD, IS, RD and RS.
The physical constants used in the model evaluation are


_k_ Boltzman’s constant 1 _._ 3806226 10 _[−]_ [23] J/K
_q_ electronic charge 1 _._ 6021918 10 _[−]_ [19] C


_Standard Calculations_


Absolute temperatures (in kelvins, K) are used. The thermal voltage



The silicon bandgap energy


_Temperature Dependence_



_V_ TH = _[kT]_ [NOM] _._ (7.212)

_q_


_EG_ = 1 _._ 16 _−_ 0 _._ 000702 4 _T_ NOM [2] (7.213)
_T_ NOM + 1108 _[.]_


178 _CHAPTER 7. ELEMENT CATALOG_


Table 7.6: NJF and PJF model keywords for the junction field effect transistor. The Area column indicates
parameters that are scaled by _Area_ .


**Name** **Description** **Units** **Default** **Area**
AF flicker noise exponent ( _AF_ ) - 1
BETA transconductance parameter ( _β_ ) A/V [2] 1.0E-4 CGS zero-bias G-S junction capacitance per unit area ( _CGS_ _[′]_ [)] F 0 CGD zero-bias G-D junction capacitance per unit area ( _CGD_ _[′]_ [)] F 0 FC coefficient for forward-bias depletion - 0.5
capacitance formula ( _FC_ )

IS gate junction saturation current ( _IS_ ) A 1.0E-14 KF flicker noise coefficient ( _KF_ ) - 0
LAMBDA channel length modulation parameter ( _λ_ ) 1/V 0
PB gate junction potential ( _φJ_ ) V 1
RD drain ohmic sheet resistance ( _RD_ ) Ω 0 RS source ohmic sheet resistance ( _RS_ ) Ω 0 VTO threshold voltage (VT-oh) ( _VT_ 0) V -2.0
VTO _<_ 0 indicates a depletion mode JFET
VTO _≥_ 0 indicates an enhancement mode JFET



BETATC temperature coefficient of the transconductance parameter
BETA ( _TC,β_ )



%/ _[◦]_ C 0



M gate _p-n_ junction grading coefficient ( _M_ ) - 0.5
VTOTC temperature coefficient of threshold voltage VTO ( _TC,V T_ 0) V/ _[◦]_ C 0


Temperature effects are incorporated as follows where _T_ and _T_ NOM are absolute temperatures in Kelvins
(K).



The parasitic resistance parameter dependencies are summarized in figure 7.40.


_Junction Field-Effect Transistor_ 179



PROCESS
PARAMETERS
RSH _R_ SH


_Leakage Currents_



+ GEOMETRY
PARAMETERS
NRS _NRS_
NRD _NRD_
NRG _NRG_
NRB _NRB_



_→_ DEVICE
PARAMETERS
RD _RD_ = _f_ ( _R_ SH _, NRD_ )
RS _RS_ = _f_ ( _R_ SH _, NRS_ )
RG _RB_ = _f_ ( _R_ SH _, NRG_ )
RB _RB_ = _f_ ( _R_ SH _, NRB_ )



Figure 7.40: JFET parasitic resistance parameter relationships.



Current flows across the normally reverse biased source-bulk and drain-bulk junctions. The gate-source
leakage current
_IGS_ = _Area ISe_ [(] _[V][GS][/V]_ [TH] _[ −]_ [1)] (7.224)


and the gate-source leakage current


_IGD_ = _Area ISe_ [(] _[V][GD][/V]_ [TH] _[ −]_ [1)] (7.225)


The dependencies of the parameters describing the leakage current in the JFET model are summarized in
figure 7.41.



PROCESS
PARAMETERS
IS _IS_


_I/V Characteristics_



+ GEOMETRY
PARAMETERS
_Area_



_→_ DEVICE
PARAMETERS

_IGS_ = _f_ ( _IS, Area_ )
_IGD_ = _f_ ( _IS, Area_ )



Figure 7.41: JFET leakage current parameter dependecies.



The current/voltage characteristics are evaluated after first determining the mode (normal: _VDS ≥_ 0 or
inverted: _VDS <_ 0) and the region (cutoff, linear or saturation) of the current ( _VDS, VGS_ ) operating point.


_Normal Mode: (VDS ≥_ 0 _)_


The regions are as follows:

In the inverted mode the JFET I/V characteristics are evaluated as in the normal mode (7.226) but with the
drain and source subscripts exchanged. The relationships of the parameters describing the I/V characteristics
are summarized in figure 7.42.


_Mutual Inductor_ 183


K43 LAA LBB 0.999
KXFRMR L1 L2 0.87


PSpice _Example_


KTFMR LAA LBB LCC LDD TRANSFORMER 2.5


_Model Type_


IND PSpice only


_Note_


1. The mutual coupled inductor model represents coupled inductors by self inductances _Li_ and mutual
inductances _Mij_ . This is the model used in Spice2g6 and spicthree and in PSpice if a CORE model
is not supplied. Here _Li_ is the self inductance of the _i_ th inductor element and _Mij_ is the mutual
inductance of the _i_ th and _j_ th inductor elements. The mathematical model of the coupled element
consists of voltage sources controlled by the time derivatives of current. If two inductors are coupled


_K_ COUPLING may have any value between 0 and 1 including 1. Ferrite core provides almost ideal
coupling with _K_ = 0.999 or higher.


3 In Spice2g6 and Spice3 a transformer with several coils must be represented by several K elements.
For example, a transformer with one primary and two secondaries is specified as

      - PRIMARY
L1 1 2 100U

      - FIRST SECONDARY
L2 3 4 100U

      - SECOND SECONDARY
L3 5 6 100U

      - TRANSFORMER
K1 L1 L2 0.999
K2 L1 L3 0.999
K2 L2 L3 0.999


4 In PSpice the transformer above can be either represented using the Spice2g6 and Spice3 format
above or by the more compact format

      - PRIMARY
L1 1 2 100U

      - FIRST SECONDARY
L2 3 4 100U

      - SECOND SECONDARY
L3 5 6 100U

      - TRANSFORMER
K1 L1 L2 L3 0.999


**CORE Model** PSpice Only Magnetic Core Model


_Form_


.MODEL _ModelName_ CORE( [ [ _keyword = value_ ] _..._ ] )


_Example_


.MODEL TRANSFORMER CORE(AREA=1 PATH=9.8 GAP=0.1 MS=1.250M)


_Mutual Inductor_ 185


Table 7.7: Model parameters.


**Name** **Description** **Units** **Default**
A shape parameter ( _A_ ) A/M 10 [3]

ALPHA ( _α_ ) interdomain coupling parameter   - 0.001
AREA mean magnetic crossection ( _Area_ ) cm [2] 0.1
GAMMA domain damping parameter. ( _γ_ )   - _∞_
C domain flexing parameter ( _C_ )   - 0.2
GAP effective air-gap length ( _L_ GAP) cm 0
K domain anisotopy parameter (pinning constant) ( _K_ ) A/M 500
MS magnetization saturation ( _MS_ ) A/M 10 [6]

PACK pack (stacking) factor ( _F_ PACK) cm 0
PATH mean magnetic path length in the core ( _L_ PATH) cm 1


The CORE model models a transformer core. It is assumed that the model parameters were determined or
measured at the nominal temperature _T_ NOM (default 27 _[◦]_ _C_ ) specified in the most recent .OPTIONS statement
preceeding the .MODEL statement.
The CORE model uses the Jiles-Atherton model described in [25]. This model is based on domain wall
motion and includes flexing of the domain wall, interdomain coupling, coercivity, remanence and magnetic
saturation. Hysteresis due to domain wall pinning at defect sites is modeled. This impedance to domain
wall motion dominates the characteristics of magnetic devices.
As with the default mutually coupled inductor model, the CORE model calculates the voltage across the
_i_ th set of windings from the total ampere turns which is the magnetomotive force _MMF_ .


Here the number of turns of the _j_ th winding, _Nj_, is the “ _InductanceValue_ ” of _Lj_ the name of which is the
_j_ th L _name_ given on the K element line. _Ii_ is the curent flowing through the _i_ th winding. _A_ TURNS produces
the magnetic field _H_ CORE in the core. This in turn produces the _B_ field. The _B_ field is proportional to the
flux, in the core and hence to the voltage _Vi_ . The relationship between _B_ and _H_ in the core is nonlinear
and hysteretic. The airgap also affects the B-H relationship.


Air-Gap Effect


Along the complete magnetic path


_H_ CORE _L_ PATH + _H_ GAP _L_ GAP = _MMF_ (7.244)


where _H_ CORE is the magnetic field in the core and _H_ GAP is the magnetic field in the air gap. _L_ PATH and
_L_ GAP are the model parameters PATH and GAP. If the air gap is small then all of the flux in the core passes
through the air gap so that _B_ GAP = _B_ CORE. In the air-gap the magnetization is negligible so that _B_ GAP =
_H_ GAP


186 _CHAPTER 7. ELEMENT CATALOG_


This leads to a relationship beween the _B_ and _H_ fields in the core:


_H_ CORE _L_ PATH + _B_ CORE _L_ GAP = _MMF_ (7.245)


It is a simple matter to solve for _B_ CORE and _H_ CORE if _L_ GAP =0 as then

_H_ CORE = _[MMF]_ (7.246)

_L_ PATH


If _L_ GAP _>_ 0 then (7.245) must be solved in conjunction with the relationship between _H_ CORE and magnetization _M_ in the core. This relationship is based on the theory of loosely coupled domains developed by
Jiles and Atherton.
Jiles-Atherton Model



The B-H curve of a magnetic material biased by AC and DC magnetic fields is called the anhysteric and is
mathematically described by the Jiles-Atherton model. This model determines an anhysteric magnetization
_M_ AN which is related to the saturation magnetization _MS_ by


where _A_ is the shape parameter and the effective field in the core


_H_ EFF = _H_ CORE + _αM_ AN (7.248)


Here H is the magnetizing influence. Domain wall flux is magnetic current which is proportional to the
change in magnetization. The change in magnetization consists of a reversible component due to flexing of
the domain walls and an irreversible component due to movement of domain walls from one pinning location
to another. Energy is dissipated (hence the motion is irreversible) in moving the domain wall from one
pinning location to another but energy is stored (hence reversible) when the domain wall flexs. This is
mathematicly modeled by



where _K_ is the pinning energy per volume and is akin to mechanical drag. _M_ and _H_ CORE are found by
solving (7.249) and (7.245) simultaneously.
The small signal relative permeability of the core is


(7.252)



and the flux passing through the _i_ th winding is


_φi_ = _μ_ 0( _M_ + _H_ CORE) _NiF_ PACK _Size Area_ (7.253)


The voltage across the _i_ th winding is then found as

_Vi_ = _[dφ][i]_ (7.254)

_dt_

_AC Analysis_


_Mutual Inductor_ 187


For AC analysis the mutual inductor model is used even if a CORE model is specified. This allows a different
coefficient of mutual coupling to be used in AC analysis than would otherwise be determined by nonlinear
model evaluation.


_Noise Analysis_


The K element does not contribute to noise.


ND



188 _CHAPTER 7. ELEMENT CATALOG_

### L Inductor

###### _I_ _L L_


Figure 7.45: L — Inductor element.


_Form_


L _name N_ 1 _N_ 2 _InductorValue_ [IC= _IL_ ]


PSpice _Form_


L _name N_ 1 _N_ 2 [ _ModelName_ ] _InductorValue_ [IC= _IL_ ]


_N_ 1 is the positive element node,


_N_ 2 is the negative element node, and


_ModelName_ is the optional model name.


_InductorValue_ is the inductance. (Units: H; Required; Symbol: _InductorV alue_ )


IC is the optional initial condition specification Using IC= _IL_ is intended for use with the UIC
option on the .TRAN line, when a transient analysis is desired with an initial current _IL_
through the inductor rather than the quiescent operating current. Specification of the
transient initial conditions using the .IC statement (see page 66) is preferred and is more
convenient.


_Example_


IND1 1 2 1.3N
IND1 1 2 1.3NH IC=1M


_Model Type_


IND PSpice only


**IND Model** PSpice Only Inductor Model


_Form_


.MODEL _ModelName_ IND( [ [ _keyword = value_ ] _..._ ] )


_Example_


.MODEL SMALLIND IND(L=4.5 IL1=0.1 IL2 = 0.01 TC1=0.01 TC2=0.001)


_Inductor_ 189


_Model Keywords_


**Name** **Description** **Units** **Default**
L inductance multiplier ( _L_ MULTIPLIER)   - 1
IL1 linear current coefficient ( _IC_ 1) 1/A 0
IL2 quadratic current coefficient ( _IC_ 2) 1/A 0
TC1 linear temperature coefficient ( _TC_ 1) 1/ _[◦]_ _C_ 0
TC2 quadratic temperature coefficient ( _TC_ 1) _◦C−_ 2 0


The PSpice inductance model is a nonlinear temperature dependent inductor model. It is assumed
that the model parameters were determined or measured at the nominal temperature _T_ NOM (default 27 _[◦]_ _C_ )
specified in the most recent .OPTIONS statement preceding the .MODEL statement.
The inductance is


where _IL_ is the current flowing through the inductor as in figure 7.45 and _T_ is the current temperature.


190 _CHAPTER 7. ELEMENT CATALOG_

### M MOSFET

(a) (b) (c) (d)


Figure 7.46: M — MOSFET element: (a) _n_ -channel enhancement-mode MOSFET; (b) _p_ -channel
enhancement-mode MOSFET; (c) _n_ -channel depletion-mode MOSFET; and (d) _p_ -channel depletion-mode
MOSFET.


_Form_


M _name NDrain NGate NSsource NBulk ModelName_ [L _=Length_ ] [W _=Width_ ]
+ [AD _=DrainDiffusionArea_ ] [AS _=SourceDiffusionArea_ ]
+ [PD _=DrainPerimeter_ ] [PS _=SourcePerimeter_ ]
+ [NRD _=RelativeDrainResistivity_ ] [NRS _=RelativeSourceResistivity_ ]
+ [OFF] [IC= _VDS, VGS, VBS_ ]


PSpice _Form_


M _name NDrain NGate NSsource NBulk ModelName_ [L _=Length_ ] [W _=Width_ ]
+ [AD _=DrainDiffusionArea_ ] [AS _=SourceDiffusionArea_ ]
+ [PD _=DrainPerimeter_ ] [PS _=SourcePerimeter_ ]
+ [NRD _=RelativeDrainResistivity_ ] [NRS _=RelativeSourceResistivity_ ]
+ [NRG _=RelativeGateResistivity_ ] [NRB _=RelativeBulkResistivity_ ]


_NDrain_ is the drain node.


_NGate_ is the gate node.


_NSource_ is the source node.


_NBulk_ is the bulk or substrate node.


ModelName is the model name.


_MOSFET_ 191


_L_ is the channel lateral diffusion _Length_ .
(Units: m; Optional; Symbol: _L_ ; The default is version dependent.
Spice2g6 and Spice3 Default: the length DEFL most recently specified in a .OPTION statement which in-turn defaults to 100 _μ_ m (100U); PSpice Default: the length L – length
specified in model _ModelName_ which in turn defaults to the default length DEFL most recently specified in a .OPTION statement which in-turn defaults to 100 _μ_ m (100U).)


_W_ is the channel lateral diffusion _Width_ .
(Units: m; Optional; Symbol: _W_ ; The default is version dependent.
Spice2g6 and Spice3 Default: the width DEFW most recently specified in a .OPTION statement which in-turn defaults to 100 _μ_ m (100U);
PSpice Default: the width W – width specified in model _ModelName_ which in turn defaults
to the default width DEFW most recently specified in a .OPTION statement which in-turn
defaults to 100 _μ_ m (100U).)


AD is the area of the drain diffusion ( _DrainDiffusionArea_ ). The default is DEFAD most recently
specified in a .OPTIONS statement.
(Units: m [2] ; Optional; Default: DEFAD; Symbol: _AD_ )


AS is the area of the source diffusion ( _SourceDiffusionArea_ ). The default is DEFAS most recently
specified in a .OPTIONS statement.
(Units: m [2] ; Optional; Default: DEFAS; Symbol: _AS_ )


PD is the perimeter of the drain junction ( _DrainPerimeter_ ).
(Units: m; Optional; Default: 0; Symbol: _PD_ )


PS is the perimeter of the source junction ( _SourcePerimeter_ ).
(Units: m; Optional; Default: 0; symbol: _PS_ )


NRD is the relative resistivity in squares of the drain region ( _RelativeDrainResistivity_ ). The sheet
resistance RSH specified in the model _ModelName_ is divided by this factor to obtain the
parasitic drain resistance.
(Units: squares; Optional; Default: 0; Symbol: _NRD_ )


NRS is the relative resistivity in squares of the source region ( _RelativeSourceResistivity_ ). The
sheet resistance RSH specified in the model _ModelName_ is divided by this factor to obtain
the parasitic source resistance.
(Units: squares; Optional; Default: 0; Symbol: _NRS_ )


NRG is the relative resistivity in squares of the gate region ( _RelativeGateResistivity_ ). The sheet
resistance RSH specified in the model _ModelName_ is divided by this factor to obtain the
parasitic gate resistance.
(Units: squares; Optional; Default: 0; Symbol: _NRG_ )


NRB is the relative resistivity in squares of the bulk (substrate) region ( _RelativeBulkResistivity_ ).
The sheet resistance RSH specified in the model _ModelName_ is divided by this factor to
obtain the parasitic bulk resistance.
(Units: squares; Optional; Default: 0; Symbol: _NRB_ )


192 _CHAPTER 7. ELEMENT CATALOG_


OFF indicates an (optional) initial condition on the device for DC analysis. If specified the DC
operating point is calculated with the terminal voltages set to zero. Once convergence is
obtained, the program continues to iterate to obtain the exact value of the terminal voltages.
The OFF option is used to enforce the solution to correspond to a desired state if the circuit
has more than one stable state.


IC is the optional initial condition specification. Using IC= _VDS, VGS, VBS_ is intended for use
with the UIC option on the .TRAN line, when a transient analysis is desired starting from
other than the quiescent operating point. Specification of the transient initial conditions
using the .IC statement (see page 66) is preferred and is more convenient.


_Example_


M1 24 2 0 20 TYPE1
M31 2 17 6 10 MODM L=5U W=2U
M1 2 9 3 0 MOD1 L=10U W=5U AD=100P AS=100P PD=40U PS=40U


_Note_


1. The parameters of a MOSFET can be completely specified in the model _ModelName_ . This facilitates
the use of standard transistors by using absolute quantities in the model. Alternatively scalable process
parameters can be specified in the model _ModelName_ and these scaled by geometric parameters on the
MOSFET element line.


2. In Spice2g6 and Spice3 the width W can not be specified in the model statement. For these simulators
absolute device parameters must be specified in the model statement if parameters are not input on
the element line.


_Model Type_


NMOS
PMOS


_Example_


M1 5 5 1 1 PCH L=2.0U W=20U AD=136P AS=136P

_·_

_·_

_·_
.MODEL PCH PMOS LEVEL=2 VTO=-0.76 GAMMA=0.6 CGSO=3.35E-10
+ CGDO=3.35E-10 CJ=4.75E-4 MJ=0.4 TOX=225E-10 NSUB=1.6E16
+ XJ=0.2E-6 LD=0 UO=139 UEXP=0 KF=5E-30 LAMBDA=0.02


**NMOS Model** N-CHANNEL MOSFET MODEL


**PMOS Model** P-CHANNEL MOSFET MODEL


_MOSFET_ 193


Two groups of model parameters define the linear and nonlinear elements of the MOSFET models.
One group defines absolute quantities and another group defines quantities that are multiplied by scaling
parameters related to area and dimension which are specified on the element line. This enables the MOSFET
element to be used in two ways. Using the absolute quantities the characteristics of a device can be defined
independent of the parameters on the element line. Thus the model of a standard transistor, perhaps resident
in a library, can be used without user-knowledge required. Using the scalable quantities the parameters of a
fabrication process can be defined in the model statement and scaling parameters such as the lateral diffusion
length (specified by L) and the lateral diffusion width (specified by W), and the drain and source diffusion
areas (specfified by AD and AS specified on the element line). An example is the specification of the drain-bulk
saturation current _ID,_ SAT. This parameter can be specified by the absolute parameter _IS_ specified by the
IS model keyword. It can also be determined as _IS_ = _JS · AD_ using the scalable parameter _JS_ specified by
the JS model keyword and _AD_ specified by the AD element keyword.
Spice provides four MOSFET device models. The first three models, known as LEVELs 1, 2 and 3 differ
in the formulation of the I-V characteristic. The fourth model, known as the BSIM model, uses a completely
different formulation utilizing extensive semiconductor parameters. The parameter LEVEL specifies the
model to be used:


LEVEL = 1 _→_ “Shichman-Hodges”, MOS1
This model was the first SPICE MOSFET model and was developed in 1968 [3]. It is an elementary model and has a limited scaling
capability. It is applicable to fairly large devices with gate lengths
greater than 4 _μ_ m. Its main attribute is that only a few parameters
need be specified and so it is good for preliminary analyses.


LEVEL = 2 _→_ MOS2
This is an analytical model which uses a combination of processing
parameters and geometry. The major development over the LEVEL
1 model is improved treatment of the capacitances due to the channel charge. [4–6]. The model dates from 1980 and is applicable for
chanel lengths of 2 _μ_ m and higher [7].
The LEVEL 2 model has convergence problems and is slower and
less accurate than the LEVEL 3 model.
LEVEL = 3 _→_ MOS3
This is a semi-empirical model developed in 1980 [7]. It is also used
for gate lengths of 2 _μ_ m and more. The parameters of this model
are determined by experimental characterization and so it is more
accurate than the LEVEL 1 and 2 models that use the more indirect
process parameters.
LEVEL = 4 _→_ BSIM
The BSIM model is an advanced empirical model which uses process information and a larger number of parameters (more than 60)
to describe the operation of devices with gate lengths as short as
1 _μ_ m. It was developed in 1985 [9].


Other MOSFET models or LEVELs are available in various versions of SPICE. These LEVELs are
optimized for MOSFETs fabricated in a particular foundary or provide a proprietary edge for the advanced
commercial SPICE programs. The reader interested in more advanced MOSFET models is refered to [8].


194 _CHAPTER 7. ELEMENT CATALOG_


_NBulk_


Figure 7.47: Schematic of LEVEL 1, 2 and 3 MOSFET models. _VGS_, _VDS_, _VGD_, _VGB_, _VDB_ and _VBS_ are
voltages between the internal gate, drain, bulk and source terminals designated _G_, _D_, _B_ and _C_ respectively.


**LEVEL 1, 2 and 3 MOSFET models.**


The schematic of the LEVEEL 1, 2 and 3 MOSFET models is shown in Figure 7.47.
The LEVEL 1, 2 and 3 models have much in common. These models evaluate the junction depletion
capacitances and parasitic resistances of a transistor in the same way. They differ in the procedure used
to evaluate the overlap capacitances ( _CGD_, _CGS_ and _CGB_ ) and that used to determine the current-voltage
characteristics of the active region of a transistor. The overlap capacitances model charge storage as nonlinear
thin-oxide capacitance distributed among the gate, source drain and bulk regions. These capacitances
are important in describing the operation of MOSFETs. The LEVEL 1, 2 and 3 models are intimately
intertwined as combinations of parameters can result in using equations from more than one model. The
LEVEL parameter resolves conflicts when there is more than one way to calculate the transistor characteristics
with the parameters specified by the user. Antognetti and Massobrio provide a comprehensive discussion of
the development of the LEVEL 1, 2 and 3 models [2].
The paramet
ers of the LEVEL 1, 2 and 3 models are given in table 7.9. Parameter extensions are given in
table **??** . It is assumed that the model parameters were determined or measured at the nominal temperature
_T_ NOM (default 27 _[◦]_ _C_ ) specified in the most recent .OPTIONS statement preceeding the .MODEL statement.
In PSpice this is overwritten by the T MEASURED parameter. Most of the parameters have default values.
Those parameters that have INFERRED defaults are calculated from other parameters.


Table 7.9: MOSFET model keywords for LEVELs 1, 2, 3.


**Name** **Description** **Units** **Default**
AF flicker noise exponent ( _AF_ )   - 1
CBD zero-bias B-D junction capacitance ( _CBD_ _[′]_ [)] F 0
CBS zero-bias B-S junction capacitance ( _CBS_ _[′]_ [)] F 0
CGBO gate-bulk overlap capacitance per meter of channel length F/m 0

(PARASITIC) ( _CGBO_ )



CGDO gate-drain overlap capacitance per meter of channel width

(PARASITIC) ( _CGDO_ )

CGSO gate-source overlap capacitance per meter of channel width

(PARASITIC) ( _CGSO_ )



F/m 0


F/m 0


Continued on next page


_MOSFET_ 195


Table 7.9: MOSFET model keywords for LEVELs 1, 2, 3.


**Name** **Description** **Units** **Default**
CJ zero-bias bulk junction bottom capcitance per square me- F/m [2] 0
ter of junction area

(PARASITIC) ( _CJ_ )



CJSW zero-bias bulk junction sidewall capacitance per meter of
junction perimeter

(PARASITIC) ( _CJ,_ SW)

DELTA width effect on threshold voltage (LEVEL=2 and LEVEL=3)
( _δ_ )



F/m 0


- 0



ETA static feedback (LEVEL=3 only) ( _η_ ) - INFERRED
FC coefficient for forward-bias depletion capacitance - 0.5
formula

(PARASITIC) ( _FC_ )



1
GAMMA bulk threshold parameter ( _γ_ ) V 2 INFERRED
IS bulk junction saturation current A 10 _[−]_ [14]

(PARASITIC) ( _IS_ )



JS bulk junction saturation current per sq-meter of junction
area

(PARASITIC) ( _JS_ )



A/m [2] 0



KAPPA saturation field factor (LEVEL=3 only) ( _κ_ ) - 0.2
KF flicker noise coefficient ( _KF_ ) - 0
KP transconductance parameter ( _KP_ ) A/V [2] 2.10 _[−]_ [5]



LAMBDA channel-length modulation
(LEVEL=1, 2 only) ( _λ_ )



1/V 0



LD lateral diffusion ( _XJL_ ) m 0
LEVEL model index - 1
MJ bulk junction bottom grading coefficient - 0.5



(PARASITIC) ( _MJ_ )

MJSW bulk junction sidewall grading coefficient

(PARASITIC) ( _MJ,_ SW)




- 0.33



NSUB substrate doping ( _NB_ ) cm _[−]_ [3] INFERRED
NSS surface state density ( _N_ SS) cm _[−]_ [2] INFERRED
NFS fast surface state density ( _N_ FS) cm _[−]_ [2] 0
NEFF total channel charge (fixed and mobile) coefficient - 1
(LEVEL=2 only) ( _N_ EFF)



PB bulk junction potential ( _φJ_ )
(This is the interface potential in the channel relative to
the source at threshold.)



V 0.8



PHI surface inversion potential (2 _φB_ ) V 0.6
RD drain ohmic resistance Ω 0

(PARASITIC) ( _RD_ )



RS source ohmic resistance

(PARASITIC) ( _RS_ )

RSH drain and source diffusion sheet resistance

(PARASITIC) ( _R_ SH)



Ω 0


Ω/square 0



THETA mobility modulation (LEVEL=3 only) ( _θ_ ) 1/V 0
Continued on next page


196 _CHAPTER 7. ELEMENT CATALOG_


Table 7.9: MOSFET model keywords for LEVELs 1, 2, 3.


**Name** **Description** **Units** **Default**
TOX oxide thickness ( _TOX_ ) m   Default for LEVEL 2 and 3 is 0.1 _μ_ m.
If LEVEL 1 and TOX is omitted then the process oriented
model is not used.



TPG type of gate material: ( _T_ PG)
1 _→_ polysilicon, opposite type to substrate

_−_ 1 _→_ polysilicon, same type as substrate
0 _→_ aluminum gate




- 1



UCRIT critical field for mobility degradation (LEVEL=2 only) ( _UC_ ) V/cm 10 [4]



UEXP critical field exponent in mobility
degradation (LEVEL=2 only) ( _U_ EXP)




- 0



UO surface mobility (U-oh) ( _μ_ 0) cm [2] _/_ V-s 600
UTRA transverse field coefficient (mobility) (LEVEL = 1 and 3 - 0
only) ( _U_ TRA)

VMAX maximum drift velocity of carriers ( _V_ MAX) m/s 0
VTO zero-bias threshold voltage V 0
N-channel devices: positive for enhancement mode
and negative for depletion mode devices.
P-channel devices: negative for enhancement mode
and positive for depletion mode devices.
(VT-oh) ( _VT_ 0)

XJ metallurgical junction depth ( _XJ_ ) m 0
JSSW bulk _p_ - _n_ junction sidewall current per unit length A/m 0

(PARASITIC) ( _JS,_ SW)

L channel length ( _L_ ) m DEFL
N bulk _p_ - _n_ emission coefficient - 0

(PARASITIC) ( _N_ )



PBSW bulk _p_ - _n_ sidewall potential

(PARASITIC) ( _φJ,_ SW)

RB bulk ohmic resistance

(PARASITIC) ( _RB_ )

RG gate ohmic resistance

(PARASITIC) ( _RB_ )



V PB


Ω 0


Ω 0



RDS drain-source shunt resistance ( _RDS_ ) Ω _∞_
T ABS ( _T_ ABS) _◦_ C current
temp.
T MEASURED _◦_ C TNOM
( _T_ MEASURED)
T REL GLOBAL _◦_ C 0
( _T_ REL GLOBAL)
T REL LOCAL _◦_ C 0
( _T_ REL LOCAL)
TT bulk _p_ - _n_ transit time ( _τT_ ) s 0
W channel width ( _W_ ) m DEFW
WD lateral diffusion width ( _WD_ ) m 0
Continued on next page


_MOSFET_ 197


Table 7.9: MOSFET model keywords for LEVELs 1, 2, 3.


**Name** **Description** **Units** **Default**
XQC fraction of channel charge attributable to drain in satura-   - 1
tion region ( _XQC_ )
If _XQC >_ 0 _._ 5 the Meyer Capacitance Model is used.
If _XQC ≤_ 0 _._ 5 the Ward-Dutton Capacitance Model is used.


The MOSFET LEVEL 1,2 and 3 parameters fall into three categories: absolute device parameters, scalable
and process parameters and geometric parameters. In most cases the absolute device parameters can be
derived from the scalable and process parameters and the geometry parameters. However, if specified, the
values of the device parameters are used.
The physical constants used in the model evaluation are


_k_ Boltzman’s constant 1 _._ 3806226 10 _[−]_ [23] J/K
_q_ electronic charge 1 _._ 6021918 10 _[−]_ [19] C
_ϵ_ 0 free space permittivity 8 _._ 854214871 10 _[−]_ [12] F/m
_ϵ_ Si permittivity of silicon 11 _._ 7 _ϵ_ 0
_ϵ_ OX permittivity of silicon dioxide 3 _._ 9 _ϵ_ 0
_ni_ intrinsic concentration of silicon @ 300 K 1 _._ 45 10 [16] m _[−]_ [3]


_Standard Calculations_


198 _CHAPTER 7. ELEMENT CATALOG_


Absolute temperatures (in kelvins, K) are used. The thermal voltage



The silicon bandgap energy



_V_ TH( _T_ NOM) = _[kT]_ [NOM] _._ (7.256)

_q_


_EG_ ( _T_ NOM) = 1 _._ 16 _−_ 0 _._ 000702 4 _T_ NOM [2] (7.257)
_T_ NOM + 1108 _[.]_



The difference of the gate and bulk contact potentials


_φ_ MS = _φ_ GATE _−_ _φ_ BULK _._ (7.258)


The gate contact potential



3 _._ 2 _T_ PG = 0
3 _._ 25 NMOS & _T_ PG = 1
3 _._ 25 + _EG_ NMOS & _T_ PG = _−_ 1
3 _._ 25 + _EG_ PMOS & _T_ PG = 1
3 _._ 25 PMOS & _T_ PG = _−_ 1



_φ_ GATE =


The potential drop across the oxide



⎧
⎪⎪⎪⎪⎨

⎪⎪⎪⎪⎩



_φ_ OX = _−_ _[Q]_ 0 _[′]_ _._ (7.260)
_C_ OX _[′]_



_._ (7.259)



The contact potential of the bulk material

             _φ_ BULK = 3 _._ 25 + _EG_ if NMOS _._ (7.261)
3 _._ 25 if PMOS


The equivalent gate oxide interface charge per unit area


_Q_ _[′]_ 0 [=] _[ qN]_ [SS] _[.]_ (7.262)


The capacitance per unit area of the oxide is

_COX_ _[′]_ [=] _[ ϵ][OX]_ _._ (7.263)

_TOX_


The effective length _L_ EFF of the channel is reduced by the amount _XJL_ (= LD) of the lateral diffusion at
the source and drain regions:
_L_ EFF = _L −_ 2 _XJL_ (7.264)


Similarly the effective length _W_ EFF of the channel is reduced by the amount _WD_ (= WD) of the lateral
diffusion at the edges of the channel.
_W_ EFF = _W −_ 2 _WD_ (7.265)


_κ_ is limited: if the specified value of _κ_ is less than or equal to zero the following parameters are set:


_κ_ = 0 _._ 2 (7.266)


_λ_ = 0 (7.267)

_UC_ = 0 (7.268)


_U_ EXP = 0 (7.269)

_U_ TRA = 0 (7.270)


_Process Oriented Model_


_MOSFET_ 199


If omitted, device parameters are computed from process parameters using defaults if necessary provided
that both TOX = _TOX_ and NSUB = _NB_ are specified. If either TOX or NSUB is not specified then the critical
device parameters must be specified. Which parameters are critical depends on the model LEVEL.
If VTO is not specified in the model statement then it is evaluated as


If PHI is not specified in the model statement then


and is limited to 0.1 if calculated. _NB_ = NSUB as supplied in the model statement and _ni_ at 300 K are used.
If KP is not specified in the model statement then


If UCRIT is not specified in the model statement then


is proportional to the depletion layer widths at the source and rdain regions.


_Temperature Dependence_


200 _CHAPTER 7. ELEMENT CATALOG_


Temperature effects are incorporated as follows where _T_ and _T_ NOM are absolute temperatures in Kelvins
(K).

_Parasitic Resistances_


The resistive parasitics _RS_, _RG_, _RD_ and _RB_ are treated in the same way for the LEVEL 1, 2 and 3 models.
They may be specified as the absolute device parameters RS, RG, RD, and RB or calculated from the sheet
resistivity _R_ SH (= RSH) and area parameters _NRS_ (= NRS), _NRG_ (= NRG), _NRD_ (= NRD) and _NRB_ (= NRB).
As always the absolute device parameters take precedence if they are specified. Otherwise


_RS_ = _NRSR_ SH (7.294)


_RG_ = _NRGR_ SH (7.295)

_RD_ = _NRDR_ SH (7.296)


_RB_ = _NRBR_ SH (7.297)


Note that neither geometry parameters nor process parameters are required if the absolute device resistances
are specified. The parasitic resistance parameter dependencies are summarized in figure 7.48.
_Leakage Currents_


_MOSFET_ 201



PROCESS
PARAMETERS

RSH _R_ SH



+ GEOMETRY
PARAMETERS
NRS _NRS_
NRD _NRD_
NRG _NRG_
NRB _NRB_



_→_ DEVICE
PARAMETERS
RD _RD_ = _f_ ( _R_ SH _, NRD_ )
RS _RS_ = _f_ ( _R_ SH _, NRS_ )
RG _RB_ = _f_ ( _R_ SH _, NRG_ )
RB _RB_ = _f_ ( _R_ SH _, NRB_ )



Figure 7.48: MOSFET LEVEL 1, 2 and 3 parasitic resistance parameter relationships.



PROCESS
PARAMETERS

JS _JS_



+ GEOMETRY
PARAMETERS
AD _AD_
AS _AS_
PD _PD_
PS _PS_



_→_ DEVICE
PARAMETERS
IS _IS_ =
_f_ ( _JS, JS,_ SW _, AD, AS, PD, PS_ )



Figure 7.49: MOSFET leakage current parameter dependecies.


Current flows across the normally reverse biased source-bulk and drain-bulk junctions. The bulk-source
leakage current - _IBS_ = _IBSS_ _e_ [(] _[V][BS][/V]_ [TH][)] _−_ 1 (7.298)



where




   _IBSS_ = _IS_ if IS specified (7.299)
_ASJS_ + _PSJS,_ SW if IS not specified



The bulk-drain leakage current



where




        -         _IBD_ = _IBDS_ _e_ [(] _[V][BD][/V]_ [TH][)] _−_ 1 (7.300)


   _IBDS_ = _IS_ if IS specified (7.301)
_ADJS_ + _PSJS,_ SW if IS not specified



The parameter dependencies of the parameters describing the leakage current in the LEVEL 1, 2 and 3
MOSFET models are summarized in figure 7.49.


_Depletion Capacitances_


202 _CHAPTER 7. ELEMENT CATALOG_


_CBS_ and _CBD_ are the depletion capacitances at the bulk-source and bulk-drain depletion regions respectively.
These depletion capacitances are calculated and used in the same way in all three (LEVEL = 1, 2 and 3)
models. Although they may be specified as absolute device parameters they are strong functions of the
voltages across the junction and are complex functions of geometry and of semiconductor doping. As such
they are usually calculated from process parameters. They are the sum of component capacitances


Figure 7.50: MOSFET LEVEL 1, 2 and 3 junction depletion capacitance parameter relationships.


_CBS,_ TT = _τT GBS_ (7.315)


where the bulk-source conductance _GBD_ = _∂IBD/∂VBD_ and _IBD_ is defined in (7.300).
In the LEVEL 1 MOSFET model the depletion capacitances are piecewise linear. They are calculated at
the current operating point and then treated as linear. In the LEVEL 2 and 3 models they are treated as
nonlinear. The depletion capacitance parameter dependencies are summarized in figure 7.50.


LEVEL 1 _I/V Characteristics_


For the LEVEL 1 model the device parameters (other than capacitances and resistances) are evaluated
using _TOX_ (TOX), _μ_ 0 (UO), _N_ SS (NSS and _NB_ (NSUB) if they are not specified in the .MODEL statement.
The LEVEL 1 current/voltage characteristics are evaluated after first determining the mode (normal:
_VDS ≥_ 0 or inverted: _VDS <_ 0) and the region (cutoff, linear or saturation) of the current ( _VDS, VGS_ )
operating point.


_Normal Mode: (VDS ≥_ 0 _)_


The regions are as follows:


cutoff region: _VGS < VT_
linear region: _VGS > VT_ and _VDS < VGS −_ _VT_
saturation region: _VGS > VT_ and _VDS > VGS −_ _VT_


where the threshold voltage

          _V_ FB + 2 _φB_ + _γ_ _[√]_ 2 _φB −_ _VBS_ _VBS ≥_ 2 _φB_
_VT_ = (7.316)
_V_ FB + 2 _φB_ _VBS <_ 2 _φB_


Then


0 cutoff region


Figure 7.52: MOSFET LEVEL 1 overlap capacitance parameter relationships.


In the inverted mode the MOSFET I/V characteristics are evaluated as in the normal mode (7.317) but
with the drain and source subscripts interchanged. The relationships of the parameters describing the I/V
characteristics for the LEVEL 1 model are summarized in figure 7.51.


LEVEL _1 Overlap Capacitances_


In the LEVEL 1 model the gate overlap capacitances _CGS_, _CGD_ and _CGB_ are constant and are calculated
using the per unit width overlap capacitances _CGSO_ (CGSO), _CGDO_ (CGDO) and _CGBO_ (CGBO):


_CGS_ = _CGSOW_ (7.318)


_CGD_ = _CGDOW_ (7.319)

_CGB_ = _CGBOW_ (7.320)


The overlap capacitance parameter dependencies are summarized in Figure 7.52.


_MOSFET_ 205


LEVEL 2 _I/V Characteristics_


The LEVEL 2 I/V characteristics are based on empirical fits resulting in a more accurate description of the
I/V response than obtained with the LEVEL 1 model. The LEVEL 2 current/voltage characteristics are
evaluated after first determining the mode (normal: _VDS ≥_ 0 or inverted: _VDS <_ 0) and the region (cutoff,
linear or saturation) of the current ( _VDS, VGS_ ) operating point.
_Normal Mode: (VDS ≥_ 0 _)_


The regions are as follows:


cutoff region: _VGS < VT_
weak inversion region: _VT < VGS ≤_ _V_ ON
linear region (strong inversion): _VGS > V_ ON and _VDS < VDS,_ SAT
saturation region (strong inversion): _VGS > V_ ON and _VDS > VDS,_ SAT
where



where
_qN_ FS
_xn_ = 1 + _FN −_ _γ_ EFF _X_ 1 _−_ _X_ 2 _XS_ + _W_ EFF _L_ EFF (7.324)

_COX_ _[′]_


_η_ = 1 + _FN_ (7.325)


the effect of channel width on threshold voltage is modeled by


_V_ FB _[′]_ [=] _[ V]_ [FB] [+] _[ F][N]_ [(2] _[φ][B]_ _[−]_ _[V][BS]_ [)] (7.326)


and the flat band voltage, _V_ FB, is calculated using (7.272) or (7.273).


_VGST_ = _VGS −_ _VON_ (7.327)


The factor describing the effect of channel width on threshold is


_ϵsδπ_
_FN_ = (7.328)
4 _COX_ _[′]_ _[W]_ [EFF]


The effective bulk threshold parameter is affected by charge in the drain and source depletion regions.
This is important for short channels. The factor describing short channel effects is

           _γ_ _γ ≤_ 0 or _NB ≤_ 0
_γ_ EFF = (7.329)
_γ_ (1 _−_ _FDD −_ _FSD_ ) _γ >_ 0 and _NB >_ 0


206 _CHAPTER 7. ELEMENT CATALOG_


where the effect of depletion charge at the drain is described by

_MOSFET_ 207


The expression for _L_ _[′]_ _EF F_ [when (1] _[ −]_ _[λV][DS]_ [)] _[L]_ [EFF] _[ < X][WB]_ [ limits chanel shortening at punch-through. In]
(7.339)
Δ _L_ = _λVDSL_ EFF (7.340)


and the distance that the depletion region at the drain extends into the channel is

              - _√_
_XD_ _φJ_ _NB ̸_ = 0
_XWB_ = (7.341)
0 _._ 25 10 _[−]_ [6] _NB_ = 0


The pinch-off voltage


_VP_ (Grove Frohman approximation) _V_ MAX _≤_ 0


_VDS,_ SAT from Baum’s theory of _V_ MAX _>_ 0
velocity saturation


LEVEL _2 Overlap Capacitances_


In the LEVEL 2 model the gate overlap capacitances asre strong functions of voltage. Two overlap capacitance
models are available in PSpicethe Meyer model based on the model originally proposed by Meyer [4] and
the Ward-Dutton model [5,6]. Spice2g6and Spice3use just the Meyer model. The Meyer and Ward-Dutton
models differ in the derivation of the channel charge.


LEVEL _2 Meyer Model_


This model is selected when the parameter XQC = _XQC_ is not specified or _XQC <_ 0 _._ 5.
The voltage dependent thin-oxide capacitances are used only if _TOX_ is specified in the model statement.
Four operating regions are defined in the Meyer model:


accumulation region: _VGS < V_ ON _−_ 2 _φB_
depletion region: _V_ ON _−_ 2 _φB < VGS < V_ ON
saturation region: _V_ ON _< VGS < V_ ON + _VDS_
linear region: _VGS > V_ ON + _VDS_




(7.374)


so that _QS_ = (1 _−_ _XQC_ ) _Q_ CHANNEL. This partitioning is somewhat arbitrary but produces transient results
that more closely match measurements than does the Meyer capacitance model. However this is at the price
of poorer convergence properties and sometimes error. This is particularly so when _VDS_ is changing sign.
Two operating regions are defined in the Ward-Dutton model:


off region: _VGS ≤_ _VT_
on region: _VGS > VT_



The LEVEL 2 overlap capacitance parameter dependencies are summarized in figure 7.54.


212 _CHAPTER 7. ELEMENT CATALOG_


LEVEL 3 _I/V Characteristics_

The LEVEL 3 I/V characteristics are based on empirical fits resulting in a more accurate description of
the I/V response than obtained with the LEVEL 2 model. The LEVEL 3 current/voltage characteristics are
evaluated after first determining the mode (normal: _VDS ≥_ 0 or inverted: _VDS <_ 0) and the region (cutoff,
linear or saturation) of the current ( _VDS, VGS_ ) operating point.
_Normal Mode: (VDS ≥_ 0 _)_


The regions are as follows:


cutoff region: _VGS < VT_
weak inversion region: _VT < VGS ≤_ _V_ ON
linear region (strong inversion): _VGS > V_ ON and _VDS < VDS,_ SAT
saturation region (strong inversion): _VGS > V_ ON and _VDS > VDS,_ SAT
where
_VT_ = _VT_ 0 _−_ _σVDS_ + _FC_ (7.397)


the effect of short and narrow channel on threshold voltage



and



weak inversion region



When _VGS_ is slightly above _VT_, _ID_ increases slowly over a few thermal voltages _V_ TH in exponential manner
becoming _ID_ calculated for strong inversion. This effect is handled empirically by defining two exponential
which, as well as ensuring an exponential increase in _ID_, also ensure that the transconductance _GM_ (=
_∂ID/∂VGS_ ) is continuous at _VGS_ = _V_ ON.


The LEVEL 3 current-voltage parameter dependencies are summarized in Figure 7.55.


LEVEL _3 Overlap Capacitances_


In the LEVEL 3 model the gate overlap capacitances asre strong functions of voltage. Two overlap
capacitance models are available the Meyer model based on the model originally proposed by Meyer [4] and
the Ward-Dutton model [5,6]. These models differ in the derivation of the channel charge.


LEVEL _3 Meyer Model_


_MOSFET_ 215


This model is selected when the parameter XQC = _XQC_ is not specified or _XQC <_ 0 _._ 5.
The voltage dependent thin-oxide capacitances are used only if _TOX_ is specified in the model statement.
Four operating regions are defined in the Meyer model:


accumulation region: _VGS < V_ ON _−_ 2 _φB_
depletion region: _V_ ON _−_ 2 _φB < VGS < V_ ON
saturation region: _V_ ON _< VGS < V_ ON + _VDS_
linear region: _VGS > V_ ON + _VDS_


LEVEL _3 Ward-Dutton Model_


216 _CHAPTER 7. ELEMENT CATALOG_


This model is selected when the parameter XQC is specified and less than 0.5. The charge in the gate _QG_
and the substrate _QB_ is calculated and the difference of these is taken as the channel charge _Q_ CHANNEL.
This charge is then partitioned and allocated between the source as _QS_ and the drain _QD_ as follows:


_Q_ CHANNEL = _QD_ + _QS_ (7.437)
_QD_ = _XQC_ _Q_ CHANNEL (7.438)


(7.439)


so that _QS_ = (1 _−_ _XQC_ ) _Q_ CHANNEL. This partitioning is somewhat arbitrary but produces transient results
that more closely match measurements than does the Meyer capacitance model. However this is at the price
of poorer convergence properties and sometimes error. This is particularly so when _VDS_ is changing sign.
Two operating regions are defined in the Ward-Dutton model:


off region: _VGS ≤_ _VT_ _[′]_
on region: _VGS > VT_ _[′]_



**BSIM (** LEVEL **4) MOSFET models.**


The parameters of the BSIM (LEVEL 4 model are all values obtained from process characterization, and
can be generated automatically. J. Pierret [10] describes a means of generating a ‘process’ file, and the
program Proc2Mod provided in the UC Berkeley standard SPICE3 distribution converts this file into a
sequence of .MODEL lines suitable for inclusion in a SPICE circuit file. Parameters marked below with an

- in the L/W column also have corresponding parameters with a length and width dependency.
Unlike most other models the BSIM model is designed for use with a process characterization system that
provides all the parameters, thus there are no defaults for the parameters, and leaving one out is considered
an error.


Table 7.10: SPICE BSIM (level 4) parameters.


**Name** **Description** **Units** **Default** **L/W**
A0 drain saturation current for _VGS_ = 0 (LEVEL=4) A 0.1
(version: SomeVersionsOfSpice) ( _A_ 0)



A1 coefficient of _V_ 1 (primary transconductance parameter)
CGBO gate-bulk overlap capacitance per meter channel length

(PARASITIC) ( _CGBO_ )

CGDO gate-drain overlap capacitance per meter channel width

(PARASITIC) ( _CGDO_ )

CGSO gate-source overlap capacitance per meter channel width

(PARASITIC) ( _CGSO_ )

CJ source-drain junction capacitance per unit area

(PARASITIC) ( _CJ_ )

CJSW source-drain junction sidewall capacitance per unit length

(PARASITIC) ( _CJ,_ SW)



F/m REQUIRED


F/m REQUIRED


F/m REQUIRED


F/m [2] REQUIRED


F/m REQUIRED



DL shortening of channel (Δ _L_ ) _μ_ m REQUIRED
DW narrowing of channel (Δ _W_ ) _μ_ m REQUIRED
DELL source-drain junction length m REQUIRED
reduction ( _DELL_ )

ETA zero-bias drain-induced barrier lowering coefficient ( _η_ ) - REQUIRED JS source-drain junction current A/m [2] REQUIRED
density ( _JS_ )

1
K1 body effect coefficient ( _K_ 1) V 2 REQUIRED K2 drain/source depletion charge sharing - REQUIRED coefficient ( _K_ 2)

MJ grading coefficient of source-drain junction ( _MJ_ ) - REQUIRED
MJSW grading coefficient of source-drain junction sidewall - REQUIRED
( _MJ,_ SW)

MUS mobility at zero substrate bias and at _VDS_ = _VDD_ ( _μS_ ) cm [2] _/_ V [2] s REQUIRED MUZ zero-bias mobility ( _μZ_ ) cm [2] _/_ Vs REQUIRED
N0 zero-bias subthreshold slope coefficient (N-zero) ( _N_ 0) - REQUIRED NB sensitivity of subthreshold slope to substrate bias - REQUIRED 
(PARASITIC) ( _NB_ )

ND sensitivity of subthreshold slope to drain bias ( _ND_ ) - REQUIRED Continued on next page


_MOSFET_ 219


Table 7.10: SPICE BSIM (level 4) parameters.


**Name** **Description** **Units** **Default** **L/W**
PB built in potential of source/ V REQUIRED
drain junction ( _φJ_ )



PBSW built in potential of source/
drain juntion sidewall

(PARASITIC) ( _φJ,_ SW)



V REQUIRED



PHI surface inversion potential (2 _φB_ ) V REQUIRED RSH drain and source diffusion sheet resistance Ω-square REQUIRED

(PARASITIC) ( _R_ SH)



TEMP temperature at which parameters were measured ( _T_ ) C REQUIRED
TOX gate oxide thickness ( _TOX_ ) _μ_ m REQUIRED
U0 zero-bias transverse-field mobility degradation coefficient V _[−]_ [1] REQUIRED (U-zero ( _U_ 0)

U1 zero-bias velocity saturation coefficient ( _U_ 1) _μ_ m/V REQUIRED VDD measurement bias range ( _VDD_ ) V REQUIRED
WDF source-drain junction default width m REQUIRED
( _W_ DF)

VFB flat-band voltage ( _V_ FB) V REQUIRED X2E sensitivity of drain-induced barrier lowering V _[−]_ [1] REQUIRED effect to substrate bias ( _X_ 2 _E_ )



X2MS sensitivity of mobility to substrate bias at _VDS_ = _VDD_
( _X_ 2MS)



cm [2] _/_ V [2] s REQUIRED 


X2MZ sensitivity of mobility to substrate bias at _VDS_ = 0 ( _X_ 2MZ) cm [2] _/_ V [2] s REQUIRED X2U0 sensitivity of transverse field mobility V _[−]_ [2] REQUIRED degradation effect to substrate bias
(X2U-zero) ( _X_ 2U0)



X2U1 sensitivity of velocity saturation effect to substrate bias
( _X_ 2U1)

X3E sensitivity of drain-induced barrier lowering effect to drain
bias at _VDS_ = _VDD_ ( _X_ 3 _E_ )



_μ_ mV _[−]_ [2] REQUIRED 

V _[−]_ [1] REQUIRED 


X3MS sensitivity of mobility to drain bias at _VDS_ = _VDD_ ( _X_ 3MS) cm [2] _/_ V [2] s REQUIRED X3U1 sensitivity of velocity saturation effect on drain bias at _VDS_ _μ_ V _[−]_ [2] REQUIRED = _VDD_ ( _X_ 3U1)



XPART gate oxide capacitance charge partition model flag
( _X_ PART)
XPART = 0: selects a 40:60 drain:source
charge partition
XPART = 1: selects a 0:100 drain:source
charge partition


_Table 7.11 continued: BSIM (_ LEVEL _) 4 model keywords, extensions._




 - REQUIRED


220 _CHAPTER 7. ELEMENT CATALOG_


Table 7.11: SPICE BSIM (level 4) parameters, extensions.


**Name** **Description** **Units** **Default**
AF flicker noise exponent ( _AF_ )   - 1
CBD zero-bias B-D junction capacitance ( _CBD_ _[′]_ [)] F 0
CBS zero-bias B-S junction capacitance ( _CBS_ _[′]_ [)] F 0
FC coefficient for forward-bias depletion capacitance   - 0.5
formula ( _FC_ )

IS bulk junction saturation current ( _IS_ ) A 1E-14
KF flicker noise coefficient ( _KF_ )   - 0
L channel length ( _L_ ) m DEFL
N bulk _p_   - _n_ emission coefficient   - 0

(PARASITIC) ( _N_ )



PBSW bulk _p_ - _n_ sidewall potential

(PARASITIC) ( _φJ,_ SW)



V PB



**Name** **Description** **Units** **Default**
JSSW bulk junction sidewall current per unit length A/m 0

(PARASITIC) ( _JS,_ SW)



RB bulk ohmic resistance

(PARASITIC) ( _RB_ )

RD drain ohmic resistance

(PARASITIC) ( _RD_ )



Ω 0


Ω 0



RDS drain-source shunt resistance ( _RDS_ ) Ω 0
RG gate ohmic resistance Ω 0

(PARASITIC) ( _RB_ )



RS source ohmic resistance

(PARASITIC) ( _RS_ )



Ω 0



TT bulk _p_   - _n_ transit time ( _τT_ ) s 0
W channel width ( _W_ ) m DEFL


_AC Analysis_


The AC analysis uses the model of figure 7.46 with the capacitor values evaluated at the DC operating point.ö

The MOSFET noise model accounts for thermal noise generated in the parasitic resistances and shot and
flicker noise generated in the drain source current generator. The rms (root-mean-square) values of thermal
noise current generators shunting the four parasitic resistance _RB_, _RD_, _RG_ and _RS_ are


The rms value of noise current generators in series with the drain-source current generator

### N Digital Input Interface


_HighLevelNode_

**STATE** **ANALOG**


###### _SignalName_


###### _InterfaceNode_



Figure 7.57: N — Digital input interface element. Converts from a digital (state) signal to an analog signal.


_Form_


N _name InterfaceNode LowLevelNode HighLevelNode ModelName_ [SIGNAME = _Dig-_
_italSignalName_ ] [IS = _InitialState_ ]


_InterfaceNode_ Identifier of node interfacing between digital signal and continuous time circuit.


_LowLevelNode_ Identifier of low level reference node. Normally this is the logic “zero” voltage.


_HighLevelNode_ Identifier of high level reference node. Normally this is the logic “one” voltage.


_ModelName_ Name of the model specifying transitions times and resistances and capacitances of each
logic state


SIGNAME Keyword for digital signal name. (optional)


_DigitalSignalName_ Digital signal name. _DigitalSignalName_ is the name of the signal specified in the input
file specified in the element model. If it is omitted then _DigitalSignalName_ defaults element
name N _name_ stripped of the prefix N (i.e. _name_ ).


IS Keyword for initial state. (optional)


_InitialState_ Integer speciftying the initial state. If specified, it must be 0, 1, ..., or 19. This over rides
the state specified at TIME=0 in the digital input file (see the model specification). The
state of the digital interface input (N) element remains as the _InitialState_ state until a state
(other than the state at TIME=0 is input from the specified file.


_Example_


N100 1 0 2 INTERFACE FROM REGISTER SIGNAME=REG1 IS=0
NCONTROL 1 0 2 CONTROL


_Model Type_


DINPUT


_Digital Input Interface_ 223


The digital input interface is modeled by time variable resistances between the _Interface Node_ and the
_Low Level Node_ and between the the _Interface Node_ and the _High Level Node_ . The variable resistances
are shunted by fixed capacitances. The resistance are controlled by parameters specified in the model
_ModelName_ . The resistance varies exponentially from the old state to the new state over the time period
indicated for the new state. This approximates the output of a digital gate.


**DINPUT Model** Digital Input Interface Model


_HighLevelNode_


_SignalName_
_InterfaceNode_


Figure 7.58: Digital input interface model.


The digital input interface is modeled by time variable resistances between the _Interface Node_ and the
_Low Level Node_ and between the the _Interface Node_ and the _High Level Node_ . The variable resistances are
shunted by fixed capacitances. The parameters are controlled by parameters specified in the model. Upon
a state transition the two resistances vary exponentially from the old state to the new state over the time
period indicated for the new state. This approximates the output of a digital gate. The sequence of states
and the state change times are specified in the file specified by the FILE = ( _InputFileName_ ) keyword in the
model. The initial state at TIME 0 is taken from this file unless the IS keyword is specified on the element
line. In the _IS_ (= _InitialState_ ) keyword is specified then the state of the digital input interface is _InitialState_
until a state transition at TIME _>_ 0 is specified in the file _InputFileName_ .


224 _CHAPTER 7. ELEMENT CATALOG_


_Keywords:_


**Name** **Description** **Units** **Default**
FILE digital input filename. If more than one model refers to the   - REQUIRED
same file then the filenames specified must be identical and
not logicly equivalent. This ensures that the file is opened
only once.

FORMAT digital input file format   - 1
TIMESTEP digital input file time step s 1NS
CLO capacitance to low level node F 0
CHI capacitance to high level node F 0
S _n_ NAME state “n” character abreviation   - REQUIRED
_n_ = 0, 2, ..., or 19



S _n_ TSW state “n” switching time
_n_ = 0, 2, ..., or 19

S _n_ RLO state “n” resistance to low level node
_n_ = 0, 2, ..., or 19

S _n_ RHI state “n” resistance to high level node
_n_ = 0, 2, ..., or 19



s REQUIRED


Ω REQUIRED


Ω REQUIRED


_Digital Output Interface_ 225

### O Digital Output Interface

###### _Interface Node_ _SignalName_ _ReferenceNode_


Figure 7.59: O — Digital output interface element.


_Form_


O _name InterfaceNode ReferenceNode ModelName_ [SIGNAME = _DigitalSignalName_
]


_InterfaceNode_ Identifier of node interfacing between digital signal and continuous time circuit.


_ReferenceNode_ Identifier of reference node. Normally this is ground


_ModelName_ Name of the model specifying transistions times and resistances and capacitances of each
logic state.


SIGNAME Keyword for digital signal name. (optional)


_DigitalSignalName_ Digital signal name.


_Example_


O100 1 0 INTERFACE TO MEMORY SIGNAME=MEM1
OADD1 1 0 2 ADD1


_Model Type_


DOUTPUT


The digital output interface is modeled by time variable resistances between the _Interface Node_ and the
_Low Level Node_ and between the the _Interface Node_ and the _High Level Node_ . The variable resistances are
shunted by fixed capacitances. The parameters are controlled by parameters specified in the model. The
resistance varies exponentially from the old state to the new state over the time period indicated for the new
state. This approximates the output of a digital gate.


**DOUTPUT Model** Digital Output Interface Model


226 _CHAPTER 7. ELEMENT CATALOG_


_Keywords:_


**Name** **Description** **Units** **Default**
FILE digital output filename. If more than one model refers to the   - REQUIRED
same file then the filenames specified must be identical and
not logicly equivalent. This ensures that the file is opened
only once.

FORMAT digital output file format   - 1
TIMESTEP digital output file time step s 1NS
TIMESCALE digital output file time scale s 1
CHGONLY Output type flag:   - 0
= 0 _→_ output at each TIMESTEP
= 1 _→_ output only on state change

CLOAD capacitance F 0
RLOAD resistance Ω 1000
S _n_ NAME state “n” character abreviation   - REQUIRED
_n_ = 0, 2, ..., or 19



S _n_ VLO state “n” low level voltage
_n_ = 0, 2, ..., or 19

S _n_ VHI state “n” high level voltage
_n_ = 0, 2, ..., or 19



s REQUIRED


s REQUIRED



The digital output interface is modeled by a resistance _RLoad_ and capacitance _CLoad_ between the _Inter-_
_faceNode_ and the _Reference Node_ . The values of _Rload_ and _CLoad_ are specified in the model _ModelName_ .
A state transistion from state _n_ ( _n_ = one of 0, 1, 2, ... 19) is indicated if the interface voltage
_VInterfaceNode −_ _VReferenceNode_ between the _InterfaceNode_ and the _ReferenceNode_ node is outside the
range S _n_ VHI _−_ S _n_ VLO. If there is a state transistion then the valid voltage range of each state _k_ is considered
in order from state k = 0 to state 19 to determine which voltage range S _k_ VHI _−_ S _k_ VLO brackets the current
interface voltage _VInterfaceNode −_ _VReferenceNode_ . The first valid state becomes the new state. If there
is no valid state then the new state is indeterminate and designated by “?”. At each TIME being a multiple
integer of TIMESTEP a line is written to the digital output file _OutputFileName_ . If the new state at the time
_ti_ = _i ·_ TIMESTEP is _n_ then the _i_ th line is:


i _nt_ ( _i ·_ TIMESCALE) _n_


where int() is the integer operation. An example of the first few lines of _OutputFileName_ with a TIMESTEP
of 1 ns and TIMESCALE of 2 is: 0 _._ 012042638?101120141


_Port Element_ 227

### P Port Element


Some versions of spice only.




###### N + N 

|+<br>Z<br>V L<br>AS<br>-|Col2|
|---|---|
|+<br>-<br>_VAS ZL_||
|+<br>-<br>_VAS ZL_||



_Form_



Figure 7.60: P — port element.


P _name N_ + _N−_ PNR= _PortNumber_ [ZL= _ReferenceImpedance_ ]


_N_ + is the positive element node,


_N−_ is the negative element node, and


_PNR_ is the integer index of the port. The port index must be numbered sequentially beginning
at 1. That is, the first occurrence of a P element in the in input netlist must have PNR=1,
the second occurrence PNR=2, etc. (Units: none; Required; Symbol: _PortNumber_ ;)


_ZL_ is the reference impedance of port (Units: Ω; Optional; Default: 50 Ω; Symbol: _ZL_ ;)



_Example_


PORT1 1 0 PNR=1 ZL=75


_Note_


1. _VAS_ in Fig. 7.60 is not visible to the user and is used by the program to test for the S parameters. As
an example of using the port specification with a source consider the partial circuit in Fig. 7.61


. The spice code defining this is _Example_


P _name N_ + _N−_ PNR= _PortNumber_ [ZL= _ReferenceImpedance_ ]

[VIN _N−_ 0 PULSE (Pulse Specification) ]










|Col1|Col2|Col3|
|---|---|---|
|+<br>-|+<br>-<br>_VAS_<br>_ZL_||
|_N_-|_N_-||
|_N_-|||



Figure 7.61: Example of the usage of a P element with a pulse voltage source.


228 _CHAPTER 7. ELEMENT CATALOG_

### Q Bipolar Junction Transistor


###### _NCollector_


###### _NCollector_


###### _NSubstrate_ _NSubstrate_


###### _NSubstrate_


###### _NBase_


###### _NEmitter_


###### _NEmitter_



_Form_



(a) (b)


Figure 7.62: Q — bipolar junction transistor element: (a) NPN transistor; (b) PNP transistor.


Q _name NCollector NBase NEmitter_ [ _NSubstrate_ ] _ModelName_ [ _Area_ ] [OFF]
+ [IC= _Vbe,Vce_ ]



_NCollector_ is the collector node.


_NBase_ is the base node.


_NEmitter_ is the emitter node.


_NSubstrate_ is the optional substrate node. If not specified, ground is used as the substrate node. If
_NSubstrate_ is a name as allowed in PSpice) it must be enclosed in square brackets, e.g.

[ _NSubstrate_ ], to distinguish it from _ModelName_ .


_ModelName_ is the model name.


_Area_ is the area factor
If the area factor is omitted, a value of 1.0 is assumed. (Units: none; Optional; Default: 1;
Symbol: _Area_ )


OFF indicates an (optional) initial condition on the device for the DC analysis. If specified the
DC operating point is calculated with the terminal voltages set to zero. Once convergence is
obtained, the program continues to iterate to obtain the exact value of the terminal voltages.
The OFF option is used to enforce the solution to correspond to a desired state if the circuit
has more than one stable state.


IC is the optional initial condition specification using IC= _VBE, VCE_ is intended for use with the
UIC option on the .TRAN line, when a transient analysis is desired starting from other than
the quiescent operating point. See the _.IC_ line description for a better way to set transient
initial conditions.


_Example_


Q20 10 50 0 QFAST IC=0.65,15.0
Q5PUSH 10 29 14 200 MODEL1


_Bipolar Junction Transistor_ 229


**NPN Model** NPN Si Bipolar Transistor Model


**PNP Model** PNP Si Bipolar Transistor Model


**LPNP Model** PSpice Only Lateral PNP Si Bipolar Transistor Model








###### _NCollector_




Figure 7.63: Schematic of the NPN bipolar junction transistor model. In the NPN and PNP models node
_NX_ is connected to node C In the LPNP model node _NX_ is connected to node B.


The NPN and PNP BJT models are identical but with the positive sense of currents and voltages opposite
so that the model parameters are always positive. The LPNP model is used for a lateral PNP IC transistor
structure. In the NPN and PNP models the node _NX_ in figure 7.63 is connected to node C — the internal
collector node. In the LPNP model node _NX_ is connected to node B — the internal base node. Only the
model type designated on the element line distinguishes which schematic is used.
The bipolar junction transistor model in Spice is based on the charge control model of Gummel and
Poon. Extensions in the Spice implementation deal with effects at high bias levels. The model reduces to
the simpler Ebers-Moll model with the ommission of appropriate model parameters.


Table 7.12: BJT model parameters.


**Name** **Description** **Units** **Default** **Are**
AF flicker noise exponent ( _AF_ ) - 1
BF ideal maximum forward beta ( _βF_ ) - 100
Continued on next page


230 _CHAPTER 7. ELEMENT CATALOG_


Table 7.12: BJT model parameters.


**Name** **Description** **Units** **Default** **Are**
BR ideal maximum reverse beta ( _βR_ ) - 1
C2 alternative keyword for ISE
PSpice only.
C4 alternative keyword for ISC
PSpice only.
CCS alternative keyword for CJS
PSpice only.
CJC base-collector zero-bias depletion F 0 capacitance ( _CJC_ )



CJE base-emitter zero-bias depletion
capacitance ( _CJE_ )

CJS zero-bias collector-substrate
capacitance ( _CJS_ )



F 0 

F 0 


EG energy gap voltage (barrier height) ( _EG_ ) eV 1.11
FC coefficient for forward-bias depletion - 0.5
capacitance formula ( _FC_ )



IK alternative keyword for IKF
PSpice only.
IKF corner of forward beta high current
roll-off ( _IKF_ )

IKR corner of reverse beta high current
roll-off ( _IK_ _F_ )

IRB current where base resistance falls halfway to its minimum
value ( _IRB_ )



A _∞_ 

A _∞_ 

- _∞_ 


IS transport saturation current ( _IS_ ) A 1.0E-16 ISC base-collector leakage saturation A 0 current ( _ISC_ ) If ISC is greater than 1 it is treated as a
multiplier. In this case _ISC_ = ISC _IS_



ISE base-emitter leakage saturation
current ( _ISE_ ) If ISE is greater than 1 it is treated as a
multiplier. In this case _ISE_ = ISE _IS_

ISS substrate p-n junction saturation current ( _ISS_ )
PSpice only.



A 0 

A 0 


ITF high-current parameter for effect on TF ( _IτF_ ) A 0 KF flicker-noise coefficient ( _KF_ ) - 0
MC alternative keyword for MJC
PSpice only.
ME alternative keyword for MJE
PSpice only.
MJC base-collector junction exponential - 0.33
factor ( _MJC_ )



MJE base-emitter junction exponential
factor ( _MJE_ )

MJS substrate junction exponential
factor ( _MJS_ )




- 0.33


- 0


Continued on next page


_Bipolar Junction Transistor_ 231


Table 7.12: BJT model parameters.


**Name** **Description** **Units** **Default** **Are**
MS alternative keyword for MJS
PSpice only.
NC base-collector leakage emission - 2
coefficient ( _NC_ )

NE base-emitter leakage emission coefficient ( _NE_ ) - 1.5
NF forward current emission coefficient ( _NF_ ) - 1.0
NR reverse current emission coefficient ( _NR_ ) - 1
NS substrate p-n emission coefficient ( _NS_ ) - 1 PSpice only.

PC alternative keyword for VJC
PSpice only.
PE alternative keyword for VJE
PSpice only.
PS alternative keyword for VJS
PSpice only.
PT alternative keyword for XTI
PSpice only.
PTF excess phase at frequency=1.0/(TF 2 _π_ ) Hz ( _PτF_ ) degree 0
RB zero bias base resistance ( _RB_ ) Ω 0 RBM minimum base resistance at high currents ( _RBM_ ) Ω RB RC collector resistance ( _RC_ ) Ω 0 RE emitter resistance ( _RE_ ) Ω 0 TF ideal forward transit time ( _τF_ ) s 0
TR ideal reverse trarsit time ( _τR_ ) s 0
TRB1 RB linear temperature coefficient ( _TRB_ 1) _◦_ C _−_ 1 1 PSpice only.



TRB2 RB quadratic temperature coefficient ( _TRB_ 2)
PSpice only.

TRC1 RC linear temperature coefficient ( _TRC_ 1)
PSpice only.

TRC2 RC quadratic temperature coefficient ( _TRC_ 2)
PSpice only.

TRE1 RE linear temperature coefficient ( _TRE_ 1)
PSpice only.

TRE2 RE quadratic temperature coefficient ( _TRE_ 2)
PSpice only.

TRM1 RBM linear temperature coefficient ( _TRM_ 1)
PSpice only.

TRM2 RBM quadratic temperature coefficient ( _TRM_ 2)
PSpice only.


VA alternative keyword for VAF
PSpice only.
VB alternative keyword for VAR
PSpice only.
VAF forward Early voltage ( _VAF_ ) V _∞_
VAR reverse Early voltage ( _VAR_ ) V _∞_
Continued on next page


232 _CHAPTER 7. ELEMENT CATALOG_


Table 7.12: BJT model parameters.


**Name** **Description** **Units** **Default** **Are**
VJC base-collector built-in potential ( _VJC_ ) V 0.75
VJE base-emitter built-in potential ( _VJE_ ) V 0.75
VJS substrate junction built-in potential ( _VJS_ ) V
VTF voltage describing _VBC_ dependence of TF ( _VτF_ ) V _∞_
XCJC fraction of B-C depletion capacitance connected to internal - 1
base node ( _XCJC_ )



XTB forward and reverse beta temperature
exponent ( _XT B_ )

XTI temperature exponent for effect on
IS ( _XT I_ )

XTF coefficient for bias dependence of
TF ( _XτF_ )


_Standard Calculations_


The physical constants used in the model evaluation are






- 3





_k_ Boltzman’s constant 1 _._ 3806226 10 _[−]_ [23] J/K
_q_ electronic charge 1 _._ 6021918 10 _[−]_ [19] C


Absolute temperatures (in kelvins, K) are used. The thermal voltage


_V_ TH( _T_ NOM) = _[kT]_ [NOM] _._ (7.466)

_q_


_Bipolar Junction Transistor_ 233


_Temperature Dependence_


Temperature effects are incorporated as follows where _T_ and _T_ NOM are absolute temperatures in Kelvins
(K).




236 _CHAPTER 7. ELEMENT CATALOG_


_Noise Analysis_


The BJT noise model accounts for thermal noise generated in the parasitic resistances and shot and flicker
noise generated in the base-emitter and base-collector junction regions. The rms (root-mean-square) values
of thermal noise current generators shunting the three parasitic resistance _RB_, _RC_, and _RE_ are




   _In,B_ =

   _In,C_ =

   _In,E_ =



_√_
4 _kT/RB_ A/

_√_
4 _kT/RC_ A/

_√_
4 _kT/RE_ A/



Hz (7.512)


Hz (7.513)


Hz (7.514)



The rms value of the base noise current generator is




IC is the optional initial condition specification Using IC= _VC_ is intended for use with the UIC
option on the .TRAN line, when a transient analysis is desired with an initial voltage _VC_ across
the capacitor rather than the quiescent operating point. Specification of the transient initial
conditions using the .IC statement (see page 66) is preferred and is more convenient.


_Example_


R1 1 2 12.3MEG


_Model Type_


RES


**RES Model** Spice3 Only Resistor Model


_Form_


.MODEL _ModelName_ RES( [ [ _keyword = value_ ] _..._ ] )


238 _CHAPTER 7. ELEMENT CATALOG_


_Example_


.MODEL SMALLRES RES( )


_Model Keywords_


**Name** **Description** **Units** **Default**
DEFW default device width ( _W_ DEF) meters 1e-6
NARROW narrowing due to side etching ( _X_ NARROW) meters 0.0


The Spice3 resistor model is a process model for a monolithicly fabricated resistor enabling the capacitance to be determined from geometric information. If the parameter W is not specified on the element line
then _Width_ defaults to DEFW = _W_ DEF. The effective dimensions are reduced by etching so that the effective
length of the capacitor is
_L_ EFF = _Length −_ _X_ NARROW (7.521)


and the effective width is
_W_ EFF = _Width −_ _X_ NARROW (7.522)


The value of the capacitance


_CapacitorValue_ = _CJ_ _L_ EFF _W_ EFF + _CJ,_ SW _L_ EFF + _W_ EFF + _L_ EFF + _W_ EFF) (7.523)


**RES Model** PSpice Only Resistor Model


The resistor model consists of process-related device data that allow the resistance to be calculated from
geometric information and to be corrected for temperature. The parameters available are:
_Keywords:_


**Name** **Description** **Units** **Default**
R resistance multiplier ( _R_ MULTIPLIER)   - 1
TC1 first order temperature coefficient ( _TC_ 1) _◦_ C _[−]_ [1] 0
TC2 second order temperature coefficient ( _TC_ 2) _◦_ C _[−]_ [2] 0
TCE exponential temperature coefficient ( _TCE_ ) % _/_ _[◦]_ C _[−]_ [2] 0


The sheet resistance is used with the narrowing parameter and L and W from the resistor line to determine
the nominal resistance by the formula



_ResistorV alue_ no model specified


_ResistorV alue R_ - MULTIPLIER
_×_ 1 + _TC_ 1( _T −_ _T_ NOM) + _TC_ 2( _T −_ _T_ NOM) [2][�] model specified and
TCE not specified


_ResistorV alue R_ MULTIPLIER1 _._ 01 [[] _[T][CE]_ [(] _[T][ −]_ _[T]_ [NOM][)]] model and TCE specified

Figure 7.65: S — voltage controlled switch element.


S _name N_ + _N−_ _NC_ + _NC−_ _ModelName_ [ON] [OFF]



PSpice _Form_


S _name N_ + _N−_ _NC_ + _NC−_ _ModelName_


_Example_


S1 1 2 3 4 SWITCH1
S2 5 6 3 0 SM2
SWITCH1 1 2 10 0 SMODEL1


_N_ + is the positive node of the switch.


_N−_ is the negative node of the switch.


_NC_ + is the positive controlling node of the switch.


_NC−_ is the negative controlling node of the switch.


_ModelName_ is the model name and is required.


ON is the optional initial condition. It is intended for use with the UIC option on the .TRAN
line, when a transient analysis is desired starting from other than the quiescent operating
point. It is also the initial condition on the device for DC analysis.


OFF is the optional initial condition. If specified the DC operating point is calculated with the
terminal voltages set to zero. Once convergence is obtained, the program continues to iterate
to obtain the exact value of the terminal voltages. The OFF option is used to enforce the
solution to correspond to a desired state if the circuit has more than one stable state.


The initial conditions are optional. For the voltage controlled switch, nodes _NC_ + and NC- are the positive
and negative controlling nodes respectively. For the current controlled switch, the controlling current is that
through the specified voltage source. The direction of positive controlling current flow is from the positive
node, through the source, to the negative node.


Figure 7.66: VSWITCH — voltage controlled switch model.


The voltage-controlled switch model is supported by both Spice3 and PSpice. However the model
keywords differ slightly.


Spice3 _keywords:_


**Name** **Description** **Units** **Default**
VT threshold voltage ( _V_ ON) V 0.0
VH hysteresis voltage ( _V_ OFF) V 0.0
RON on resistance ( _R_ ON) Ω 1.0
ROFF off resistance ( _R_ OFF) Ω 1/GMIN


PSpice _keywords:_


**Name** **Description** **Units** **Default**
VON threshold voltage ( _V_ ON) V 0.0
VOFF hysteresis voltage ( _V_ OFF) V 0.0
RON on resistance ( _R_ ON) Ω 1.0
ROFF off resistance ( _R_ OFF) Ω 1/GMIN


Care must be exercised in using the switch. An instantaneous switch is highly nonlinear and will very likely
lead to convergence problems. This problem is alleviated in the VSWITCH model by ramping the resistance
of the switch from its off value to its on value. For this ramping action to be effective the difference between
_V_ ON and _V_ OFF must not be too small. Also the values of _R_ ON and _R_ OFF should not be extreme. The ration
_R_ ON _/R_ OFF should be be as small as possible.
If _R_ ON _/R_ OFF is large, e.g. _R_ ON _/R_ OFF _>_ 10 [12], then the default error tolerances TRTOL and CHGTOL,
specified in a .OPTIONS statement (see page 83) may need to be changed.


TRTOL Change to 1.0 from 7.0 idf there are convergence problems during transient analysis.


CHGTOL If a switch is across a capacitor then CHGTOL should be reduced to 10 _[−]_ [16] if there are convergence problems during transient analysis.


**Switch Model**


242 _CHAPTER 7. ELEMENT CATALOG_


The switch is modeled by a voltage variable resistor _R_ and an input input resistance _R_ IN, see figure
7.66. _R_ IN = 1 _/G_ MIN to ensure that the controlling nodes are not floating and that the voltage _v_ between
the controlling nodes can not change instantaneously. _G_ MIN = GMIN is described on page **??** .


_Standard Calculations_




_Noise Analysis_


The voltage controlled switch noise model accounts for thermal noise generated in the switch resistance.
The rms (root-mean-square) values of thermal noise current generators shunting the switch resistance is



Hz (7.532)



where _T_ is the analysis temperature in kelvin (K), and _k_ (= 1 _._ 3806226 10 _[−]_ [23] J/K) is Boltzmans constant.


_Transmission Line_ 243

### T Transmission Line


###### n n


###### n n Z0, TD



_Form_



Figure 7.67: T — transmission line element.


T _name n_ 1 _n_ 2 _n_ 3 _n_ 4 Z0 _=CharacteristicImpedance_ TD _=TimeDelay_ [IC _=V_ 1 _, I_ 1 _, V_ 2 _, I_ 2
]


T _name n_ 1 _n_ 2 _n_ 3 _n_ 4 Z0 _=CharacteristicImpedance_ F _=ReferenceFrequency_
+ [NL _=NormalizedElectricalLength_ ] [IC _=V_ 1 _, I_ 1 _, V_ 2 _, I_ 2 ]



Spice3 _Form_


T _name n_ 1 _n_ 2 _n_ 3 _n_ 4 [ _ModelName_ ] Z0 _=CharacteristicImpedance_ TD _=TimeDelay_

[IC _=V_ 1 _, I_ 1 _, V_ 2 _, I_ 2 ]


T _name n_ 1 _n_ 2 _n_ 3 _n_ 4 [ _ModelName_ ] Z0 _=CharacteristicImpedance_
+ F _=ReferenceFrequency_ + [NL _=NormalizedElectricalLength_ ] [IC _=V_ 1 _, I_ 1 _, V_ 2 _, I_ 2 ]


PSpice _Form_


T _name n_ 1 _n_ 2 _n_ 3 _n_ 4 Z0 _=CharacteristicImpedance_ TD _=TimeDelay_


T _name n_ 1 _n_ 2 _n_ 3 _n_ 4 Z0 _=CharacteristicImpedance_
+F _=Frequency_ [NL _=NormalizedElectricalLength_ ]


_n_ 1 positive node at port 1.


_n_ 2 negative node at port 1.


_n_ 3 positive node at port 2.


_n_ 4 negative node at port 2.


ModelName is the model name.


Z0 is the characteristic impedance. (Z-zero)
(Units: Ω; Required; Symbol: _Z_ 0; Default: none)


TD transmission line delay. (Units: s; Either TD or F Required; Symbol: _TD_ ; Default: none)


F reference frequency. (Units: Hz; Either TD or F Required; Symbol: _F_ ; Default: none)


244 _CHAPTER 7. ELEMENT CATALOG_


NL normalized electrical length. Normalization is with respect to the wavelength in free space
at the reference frequency F.
(Units: none; Optional; Symbol: _L_ NORMALIZED; Default: 0.25)


IC is the optional initial condition specification using IC= _V_ 1 _, I_ 1 _, V_ 2 _, I_ 2 is intended for use with
the UIC option on the .TRAN line, when a transient analysis is desired starting from other
than the quiescent operating point. Specification of the transient initial conditions using
the .IC statement (see page 66) is preferred and is more convenient.


_Example_


T1 1 0 2 0 Z0=50 TD=10NS


TLONG 1 0 2 0 Z0=50 F=1G NL=10


TLONG 1 0 2 0 Z0=50 F=1G


_Note_


1. The length of the line may be expressed in either of two forms. The transmission delay, _TD_, may be
specified directly (as TD=10ns, for example). Alternatively, a frequency F may be given, together
with NL, the normalized electrical length of the transmission line with respect to the wavelength in
the line at the frequency F. If a frequency is specified but NL is omitted, 0.25 is assumed (that is, the
frequency is assumed to be the quarter-wave frequency). Note that although both forms for expressing
the line length are indicated as optional, one of the two must be specified.


2. Note that only 3 distinct nodes should be specified as this element describes a single propagating mode.
With four distinct nodes specified, two propagating modes may exist on the actual line. If there are
four distinct nodes then two lines are required.


3. The transmission line T element is modeled as a bidirectional ideal delay element. The maximum time
step in Spice is limited to half of the time delay along the line. Thus short transmission lines can result
in many time steps in a transient analysis. Unnecessary short transmission lines should be avoided.


_Model Type_


URC


**URC Model** Lossy RC Transmission Line Model

its reverse saturation current is



_CJ,i_ = _C_ PERL _li_ (7.541)


_IS,i_ = _IS,_ PERL (7.542)


246 _CHAPTER 7. ELEMENT CATALOG_

### U Universal Element


The U element is a universal element for extending the number of elements that Spice can handle. The
element is determined by the model type. In some cases model parameters indicate further refinement.
Since the Spice U element is used to specify many different kinds of physical elements there is no common
form for it. Each physical element is distinguished by the type of the model it refers to. The format and
description of each element is given in the model description as indicated in the following table. The index
is used in this manual to uniquely identify the various elements.
_Model Type_


Model Index Description Page

STRUC STRUC Geometric coupled, lossy planar transmission line **??**
U U311 Geometric coupled planar transmission line (up to 5 lines) **??**
Identifying Model Parameters: LEVEL=3 EVEL=1 PVEL=1



U U312 Geometric coaxial cable
Identifying Model Parameters: LEVEL=3 EVEL=1 PVEL=2

U 32 General transmission line (up to 5 lines) defined by precomputed
parameters.
Identifying Model Parameters: LEVEL=3 EVEL=2

U U34 General transmission line (up to 5 lines) defined by measurements.
Identifying Model Parameters: LEVEL=3 EVEL=3

U U4 Digital output element
Identifying Model Parameter: LEVEL=4

U U5 Digital input element
Identifying Model Parameter: LEVEL=5



Model INdex Description Page

UDLY UDLY Delay Line **??**
UEFF UEFF Edge-Triggered Flip-Flop **??**
UGATE UGATE Standard Gate Model Form **??**
UGFF UGFF Gated Flip-Flop **??**
UIO UIO IO Model **??**
URC URC Lossy RC transmission line 243
USUHD USUHD Setup and Hold Checker **??**
UTGATE UTGATE Tri-State Gate **??**
UWDTH UWDTH Pulse-Width Checker **??**


_Note_


1. One of the problems with Spice is that the first letter of an element’s name is used to determine the
type of an element. One consequence of this is that there can only be 26 elements — one for each letter
of the alphabet. Spice2g6The original version of Spice from which all subsequent versions of Spice
have been developed had less than 26 elements and so this was not a problem. With the addition
of new element types several of the originally unised letters were used and a universal element, the U
element, introduced to handle even more. The U element is used to represent many different type of
elements such as lossy transmission lines and digital devices. All of the U elements refer to models and
the model name, and sometimes model parameters, used to indicate the actual element referred to.


_Independent Voltage Source_ 247

### V Independent Voltage Source

###### _N+_ _E_



_Form_


###### _N-_

Figure 7.69: V — Independent voltage source.


V _name N_ + _N−_ [ [ _DC_ ] [ _DCvalue_ ]
+ [AC [ _ACmagnitude_ [ _ACphase_ ] ] ]
+ [DISTOF1 [ _F1Magnitude_ [ _F1Phase_ ] ] ] + [DISTOF2 [ _F2Magnitude_ [ _F2Phase_ ] ]
]



Spice3 _Form_


V _name N_ + _N−_ [ [ _DC_ ] [ _DCvalue_ ]
+ [AC [ _ACmagnitude_ [ _ACphase_ ] ] ]
+ [ _TransientSpecification_ ]
+ [DISTOF1 [ _F1Magnitude_ [ _F1Phase_ ] ] ]
+ [DISTOF2 [ _F2Magnitude_ [ _F2Phase_ ] ] ]


PSpice _Form_


V _name N_ + _N−_ [ [ _DC_ ] [ _DCvalue_ ] [AC [ _ACmagnitude_ [ _ACphase_ ] ] ]
+ [ _TransientSpecification_ ] [SNR _InputVoltageSNR_ ] [RS _SourceResistanceValue_ ]

[RL _LoadResistanceValue_ ]


_Example_


VBIAS 1 0 5.0
VCLOCK 20 5 PULSE(0 5 1N 2N 1.5N 21.9N 5N 20N)
VSSIGNAL AC 1U 90


248 _CHAPTER 7. ELEMENT CATALOG_


_N_ + is the positive voltage source node.


_N−_ is the negative voltage source node.


DC is the optional keyword for the DC value of the source.


_DCvalue_ is the DC voltage value of the source.
(Units: V; Optional; Default: 0; Symbol: _VDC_ )


AC is the keyword for the AC value of the source.


_ACmagnitude_ is the AC magnitude of the source used during AC analysis. That is, it is the peak AC voltage
so that the AC signal is _ACmagnitude_ sin( _ωt_ + ACphase). _ACmagnitude_ is ignored for other
types of analyses.
(Units: V; Optional; Default: 1; Symbol: _VAC_ )


_ACphase_ is the ac phase of the source. It is used only in AC analysis.
(Units: Degrees; Optional; Default: 0; Symbol: _φ_ AC)


DISTOF1 is the distortion keyword for distortion component 1 which hass frequency F1. (see the
description of the .DISTO statement on page 58).


_F1magnitude_ is the magnitude of the distortion component at F1. See .DISTOF1 keyword above.
(Units: V; Optional; Default: 1; Symbol: _VF_ 1)


_F1phase_ is the phase of the distortion component at F1. See .DISTOF1 keyword above.
(Units: Degrees; Optional; Default: 0; Symbol: _φF_ 1)


DISTOF2 is the distortion keyword for distortion component 2 which hass frequency F2. (see the
description of the .DISTO statement on page 58).


_F2magnitude_ is the magnitude of the distortion component at F2. See .DISTOF2 keyword above.
(Units: V; Optional; Default: 1; Symbol: _VF_ 2)


_F2phase_ is the phase of the distortion component at F2. See .DISTOF2 keyword above.
(Units: Degrees; Optional; Default: 0; Symbol: _φF_ 2)


SNR is the input signal-to-noise ratio keyword. SomeVersionsOfSpice


_InputVoltageSNR_ is the value of the signal-to-noise ratio at the input.
(Units: None; Optional; Default: use thermal noise of _RS_ ; Symbol: SNR _I_ ) SomeVersion
sOfSpice


RS is the source resistance keyword. SomeVersionsOfSpice


_SourceResistanceValue_ is the value of the source resistance.
(Units: Ohms; Optional; Default: 50Ω; Symbol: _RS_ )
Note: if port 1 is specified then the resistance specified for the port takes precedence.

SomeVersionsOfSpice


RL is the source resistance keyword. SomeVersionsOfSpice


_LoadResistanceValue_ is the value of the load resistance.
(Units: Ohms; Optional; Default: 50Ω; Symbol: _RL_ )
Note: if port 2 is specified then the resistance specified for the port takes precedence.

SomeVersionsOfSpice


_TransientSpecification_ is the optional transient specification described more fully below.


_Note_


_Independent Voltage Source_ 249


1. The independent voltage source has three different sets of parameters to describe the source for DC
analysis (see .DC on page 55), AC analysis (see .AC on page 53), and transient analysis (see .TRAN on
page 109). The DC value of the source is used during bias point evaluation and DC analysis is _DCValue_ .
It is also the constant value of the voltage source if no _TransientSpecification_ is supplied. It may also
be used in conjunction with the PWL transient specification if a time zero value is not provided as part
of the transient specification. The AC specification, indicated by the keyword AC is independent of the
DC parameters and the _Transient Specification_ .


2. See the .NOISE statement description for a discussion of how SNR _I RS_, _RL_ are used in noise calculations.


3. The original documentation distributed with Spice2g6 and Spice3 incorrectly stated that if a _Tran-_
_sientSpecification_ was supplied then the time-zero transient voltage was used in DC analysis and in
determiniong the operating point.


**Transient Specification**
Five transient specification forms are supported: pulse (PULSE), exponential (EXP), sinusoidal (SIN),
piece-wise linear (PWL), and single-frequency FM (SFFM). The default values of some of the parameters of
these transient specifications include TSTEP which is the printing increment and TSTOP which is the final
time (see the .TRAN statement on page 109 for further explanation of these quantities). In the following _t_ is
the transient analysis time.
**Exponential:**


_Form_


EXP( _V_ 1 _V_ 2 [ _TD_ 1 ] [ _τ_ 1 ] [ _TD_ 2 ] [ _τ_ 2 ] )
**Name** **Description** **Units** **Default**
_V_ 1 initial voltage A REQUIRED
_V_ 2 pulsed voltage A REQUIRED
_TD_ 1 rise delay time s 0.0
_τ_ 1 rise time constant s TSTEP
_TD_ 2 fall delay time s _TD_ 1 +
TSTEP
_τ_ 2 fall time constant s TSTEP


The exponential transient is a single-shot event specifying two exponentials. The voltage is _V_ 1 for the first
_TD_ 1 seconds at which it begins increasing exponentially towards _V_ 2 with a time constant of _τ_ 1 seconds. At
time _TD_ 2 the voltage exponentially decays towards _V_ 1 with a time constant of _τ_ 2. That is,



**Single-Frequency FM:**


SFFM( _VO VA FC μ FS_ )


250 _CHAPTER 7. ELEMENT CATALOG_


**Name** **Description** **Units** **Default**
_VO_ offset voltage A
_VA_ peak amplitude of AC voltage A
_FC_ carrier frequency Hz 1/TSTOP
_μ_ modulation index   - 0
_FS_ signal frequency Hz 1/TSTOP


The single frequency frequency modulated transient response is described by


_v_ = _VO_ + _VA_ sin (2 _π FC_ _t_ + _μ_ sin (2 _πFSt_ )) (7.544)


**Pulse:**


_Form_


PULSE( _V_ 1 _V_ 2 [ _TD_ ] [ _TR_ ] [ _TF_ ] [ _W_ ] [ _T_ ] )


**Name** **Description** **Units** **Default**
_V_ 1 initial voltage A REQUIRED
_V_ 2 pulsed voltage A REQUIRED
_TD_ delay time s 0.0
_TR_ rise time s TSTEP
_TF_ fall time s TSTEP
_W_ pulse width s TSTOP
_T_ period s TSTOP


The pulse transient waveform is defined by

(7.545)



where
_t_ _[′]_ = _t −_ _TD −_ ( _n −_ 1) _T_ (7.546)


and _t_ is the voltage analysis time and _n_ is the cycle index. The effect of this is that after an initial time
delay _TD_ the transient waveform repeats itself every cycle.
**Piece-Wise Linear:**


_Form_


PWL( _T_ 1 _V_ 1 [ _T_ 2 _V_ 2 _... Ti Vi ... TN VN_ ] _)_


_Independent Voltage Source_ 251

Figure 7.70: Voltage source exponential (EXP) waveform for EXP(0.1 0.8 1 0.35 2 1)



Figure 7.71: Voltage source single frequency frequency modulation (SFFM) waveform for
SFFM(0.2 0.7 4 0.9 1) .


252 _CHAPTER 7. ELEMENT CATALOG_


Each pair of values ( _Ti_, _Vi_ ) specifies that the value of the source is _Vi_ at time = _Ti_ . At times between _Ti_
and _Ti_ +1 the values are linearly interpolated. If _T_ 1 _>_ 0 then the voltage is constant at _DCValue_ (specified
on the element line) until time _T_ 1.



_DCvalue_ _t < T_ 1
_Vi_ _t_ = _Ti_
_Vi_ +1 - - _t_ = _Ti_ +1
_Vi_ + _Tit_ +1 _−T−iTi_ ( _Vi_ +1 _−_ _Vi_ ) _Ti < t ≤_ _Ti_ +1

_VN_ _t > TN_



### W Current Controlled Switch


###### _N_

+


###### _N_

 


_Form_



Figure 7.75: W — current controlled switch.


W _name N_ 1 _N_ 2 _VoltageSourceName ModelName_ [ _ON_ ] [ _OFF_ ]



PSpice _Form_


W _name N_ 1 _N_ 2 _VoltageSourceName ModelName_


_N_ + is the positive node of the switch.


_N−_ is the negative node of the switch.


_VoltageSourceName_ is the name of the voltage source the current through which is the controlling current.
The voltage source must be a V element.


ON is the optional initial condition. It is intended for use with the UIC option on the .TRAN
line, when a transient analysis is desired starting from other than the quiescent operating
point. It is also the initial condition on the device for DC analysis.


OFF is the optional initial condition. If specified the DC operating point is calculated with the
terminal voltages set to zero. Once convergence is obtained, the program continues to iterate
to obtain the exact value of the terminal voltages. The OFF option is used to enforce the
solution to correspond to a desired state if the circuit has more than one stable state.


_Model Type_


ISWITCH


**ISWITCH Model** Current-Controlled Switch Model


The current-controlled switch model is supported by both Spice3 and PSpice. However the model
keywords differ slightly.


256 _CHAPTER 7. ELEMENT CATALOG_

###### _VoltageSourceName_

Figure 7.76: ISWITCH — current controlled switch model.


Spice3 _keywords:_


**Name** **Description** **Units** **Default**
IT threshold current ( _I_ ON) A 0.0
IH hysteresis current ( _I_ OFF) A 0.0
RON on resistance ( _R_ ON) Ω 1.0
ROFF off resistance ( _R_ OFF) Ω 1/GMIN


PSpice _keywords:_


**Name** **Description** **Units** **Default**
ION threshold current ( _I_ ON) A 0.0
IOFF hysteresis current ( _I_ OFF) A 0.0
RON on resistance ( _R_ ON) Ω 1.0
ROFF off resistance ( _R_ OFF) Ω 1/GMIN


Care must be exercised in using the switch. An instantaneous switch is highly nonlinear and will very likely
lead to convergence problems. This problem is alleviated in the ISWITCH model by ramping the resistance
of the switch from its off value to its on value. For this ramping action to be effective the difference between
_I_ ON and _I_ OFF must not be too small. Also the values of _R_ ON and _R_ OFF should not be extreme. The ration
_R_ ON _/R_ OFF should be be as small as possible.
If _R_ ON _/R_ OFF is large, e.g. _R_ ON _/R_ OFF _>_ 10 [12], then the default error tolerances TRTOL and CHGTOL,
specified in a .OPTIONS statement (see page 83) may need to be changed.


TRTOL Change to 1.0 from 7.0 idf there are convergence problems during transient analysis.


CHGTOL If a switch is across a capacitor then CHGTOL should be reduced to 10 _[−]_ [16] if there are convergence problems during transient analysis.


**Switch Model**

_Noise Analysis_


The current controlled switch noise model accounts for thermal noise generated in the switch resistance. The
rms (root-mean-square) values of thermal noise current generators shunting the switch resistance is




 - _√_
_In_ = 4 _kT/R_ A/



Hz (7.555)



where _T_ is the analysis temperature in kelvin (K), and _k_ (= 1 _._ 3806226 10 _[−]_ [23] J/K) is Boltzmanns constant.


258 _CHAPTER 7. ELEMENT CATALOG_

### X Subcircuit Call


###### _N_ _N_ _N_



1


2
###### **SUBCIRCUIT**

3

###### _SubcircuitName_



_Form_


###### _N_

_N_


Figure 7.77: X — subcircuit call element.


X _name N_ 1 [ _N_ 2 _N_ 3 _... NN_ ] _SubcircuitName_



PSpice _Form_


X _name N_ 1 [ _N_ 2 _N_ 3 _... NN_ ] _SubcircuitName_ [ _PARAMS:_ [ _keyword = { Expression_
_} . . ._ ] [ _Keyword = Value . . ._ ] ]


_N_ 1 is the first node of the subcircuit.


_NN_ is the _N_ th node of the subcircuit.


_SubcircuitName_ is the name of the subcircuit.


PARAMS: indicates that parameters are to be passed to the subcircuit.


keyword: is keyword corresponding to the keywords defined in the .SUBCKT statement. (See page
103).


value: is numeric value.


Expression: is an algebraic expression which evaluates to a numeric value. .SUBCKT statement. (See
section **??** on page **??** ).


_Example_


X1 2 4 17 3 1 MULTI


Subcircuits are incorporated by using the “X” element. The number of nodes of the “X” element must
correspond to the number of nodes in the definition of the subcircuit (i.e. is on the .SUBCKT statement (see
page 103).


_Distributed Discontinuity_ 259

### Z Distributed Discontinuity


Only a few versions of Spice support this. _Form_



_n_ 1
_n_ 2
_n_ 3


_n_
_N_



**DISTRIBUTED**
**DISCONTINUITY**


_ModelName_



Figure 7.78: Z — distributed discontinuity.


Z _name N1 ... Nn Mname_


The Z element defines a subcircuit of L‘s and C’s describing a distributed element. The L and C subcircuit
is calculated using field theoretic based models and are optimized for maximum accuracy at 3GHz. In a
contrast a quasistatic model is evaluated at DC and its accuracy will degrade as frequencies increase. The
upper frequency of validity is selectable by the model parameter N. N is the harmonic of 3 GHz at which the
model is valid. The default for N is 5 so that by default the models are valid to a frequency of 15 GHz.
_Mname_ is the name of a model which can be one of several types:
ZSTEP Microstrip impedance step
LBEND Microstrip right-angle bend
MBEND Microstrip right-angle bend
TJUNC Microstrip T-junction (three way junction)
XJUNC Microstrip X-junction (four way bend)


_Example_


Z1 1 5 7 Tjunc1


260 _CHAPTER 7. ELEMENT CATALOG_


**LBEND Model** Microstrip Right-Angle Bend Model





**ER**


Figure 7.79: LBEND — microstrip right-angle bend model.


.MODEL _Mname_ LBEND [ER _=value_ ] H _=xvalue_ W1 _=xvalue_ W2 _=xvalue_ [N _=ivalue_ ]



_Keywords:_


**Name** **Description** **Units** **Default**
ER Permittivity of dielectric layer   - 1.0
H Height of dielectric layer mm REQUIRED
W1 First line width mm REQUIRED
W2 Second line width mm required
N Number of calculated harmonics (0-15)   - 5


_Example_


.MODEL MB1 LBEND ER=9.8 H=0.635 W1=1.2 W2=3.2


_Distributed Discontinuity_ 261


**MBEND Model** Microstrip Mitered Right-Angle Bend Model




**ER**


Figure 7.80: MBEND — microstrip mitered right-angle bend model.


.MODEL _Mname_ MBEND [ER _=value_ ] H _=xvalue_ W1 _=xvalue_ W2 _=xvalue_ [N _=ivalue_ ]



_Keywords:_


**Name** **Description** **Units** **Default**
ER Permittivity of dielectric layer   - 1.0
H Height of dielectric layer mm REQUIRED
W1 First line width mm REQUIRED
W2 Second line width mm REQUIRED
N Number of calculated harmonics (0-15)   - 5


_Example_


.MODEL MB1 MBEND ER=9.8 H=0.635 W1=1.2 W2=3.2


262 _CHAPTER 7. ELEMENT CATALOG_


**TJUNC Model** Microstrip T-Junction Model



Figure 7.81: TJUNC — microstrip T-junction model.


.MODEL _Mname_ TJUNC [ER _=value_ ] H _=xvalue_ W1 _=xvalue_ W2 _=xvalue_ W3 _=xvalue_

[S _=xvalue_ ] [N _=ivalue_ ]



_Keywords:_


**Name** **Description** **Units** **Default**
ER Permittivity of dielectric layer   - 1.0
H Height of dielectric layer mm REQUIRED
W1 First line width mm REQUIRED
W2 Second line width mm REQUIRED
W3 Third line width mm REQUIRED
S Edge offset of line 3 mm 0
N Number of calculated harmonics (0-15)   - 5


_Example_


.MODEL TJ1 TJUNC ER=9.8 H=0.635 W1=1.2 W2=3.2 W3=1.1 W4=1


_Distributed Discontinuity_ 263


**XJUNC Model** Microstrip X-junction


Figure 7.82: XJUNC — microstrip X-junction.


.MODEL _Mname_ XJUNC [ER _=value_ ] H _=xvalue_ W1 _=xvalue_ W2 _=xvalue_ W3 _=xvalue_
W4 _=xvalue_ [S _=xvalue_ ] [N _=ivalue_ ]



_Keywords:_


**Name** **Description** **Units** **Default**
ER Permittivity of dielectric layer   - 1.0
H Height of dielectric layer mm REQUIRED
W1 First line width mm REQUIRED
W2 Second line width mm REQUIRED
W3 Third line width mm REQUIRED
S Edge offset of line 3 mm 0
N Number of calculated harmonics (0-15)   - 5


_Example_


.MODEL TJ1 TJUNC ER=9.8 H=0.635 W1=1.2 W2=3.2 W3=1.1 W4=1


264 _CHAPTER 7. ELEMENT CATALOG_


**ZSTEP Model** Microstrip Impedance Step Model

_Form_



**ER**


Figure 7.83: ZSTEP — microstrip impedance step model.


.MODEL _Mname_ ZSTEP [ER _=value_ ] H _=xvalue_ W1 _=xvalue_ W2 _=xvalue_ [S _=xvalue_ ]

[N _=ivalue_ ]



_Keywords:_


**Name** **Description** **Units** **Default**
ER Permittivity of dielectric layer   - 1.0
H Height of dielectric layer mm required
W1 First line width mm required
W2 Second line width mm required
S Displacement (see figure) mm 0
N Number of calculated harmonics (0-15)   - 5


_Example_


.MODEL STEP1 ZSTEP ER=9.8 H=0.635 W1=1.2 W2=3.2


_MESFET_ 265

### Z MESFET

###### _NDrain_ _NGate_ _NSource_


Figure 7.84: Z — GASFET element.


_Form_


Z _name NDrain NGate NSource ModelName_ [ _AREA_ ] [ _OFF_ ] [ _IC=VDS,VGS_ ]


_Example_


Z1 7 2 3 ZM1 OFF


_NDrain_ is the drain node.


_NGate_ is the gate node.


_NSource_ is the source node.


ModelName is the model name.


OFF indicates an (optional) initial condition on the device for DC analysis. If specified the DC
operating point is calculated with the terminal voltages set to zero. Once convergence is
obtained, the program continues to iterate to obtain the exact value of the terminal voltages.
The OFF option is used to enforce the solution to correspond to a desired state if the circuit
has more than one stable state.


IC is the optional initial condition specification. Using IC= _VDS, VGS, VBS_ is intended for use
with the UIC option on the .TRAN line, when a transient analysis is desired starting from
other than the quiescent operating point. Specification of the transient initial conditions
using the .IC statement (see page 66) is preferred and is more convenient.


_Model Type_


GASFET


**GASFET Model** GaAs MESFET Model


_Form_


.MODEL _ModelName_ GASFET( [ [ _keyword_ = _value_ ] _..._ ] )


266 _CHAPTER 7. ELEMENT CATALOG_


_D_ _RD_
_NDrain_


Figure 7.85: Schematic of the Spice3GASFET model. _VGS_, _VDS_, and _VGD_ are intrinsic gate-source, drainsource and gate-drain voltages between the internal gate, drain, and source terminals designated _G_, _D_, and
_S_ respectively.


_Example_


.MODEL GAAS12 GASFET()


Raytheon model
This model is also known as the Statz model and model was developed at Raytheon for the modeling of
GaAs MESFETs used in digital circuits. It is based on empirical fits to measured data [23].
The parameters of the GASFET model for PSpiceare given in table 7.14.


_MESFET_ 267


It is assumed that the model parameters were determined or measured at the nominal temperature
_T_ NOM (default 27 _[◦]_ C) specified in the most recent .OPTIONS statement preceeding the .MODEL statement.
The physical constants used in the model evaluation are


Table 7.14: Spice3GASFET model keywords.
_Keywords:_


**Name** **Description** **Units** **Default** **Area**
VTO pinch-off voltage _VT_ 0 ( _TC,V T_ 0) V -2.0
BETA transconductance parameter ( _β_ ) A/V [2] 1.0E-4 B doping tail extending parameter ( _B_ ) 1/V 0.3 ALPHA saturation voltage parameter ( _alpha_ ) 1/V 2 LAMBDA channel length modulation parameter ( _λ_ ) 1/V 0
RD drain ohmic resistance ( _RD_ ) Ω 0 RS source ohmic resistance ( _RS_ ) Ω 0 CGS zero-bias G-S junction capacitance ( _CGS_ _[′]_ [)] F 0 CGD zero-bias G-D junction capacitance ( _CGD_ _[′]_ [)] F 0 PB gate junction potential ( _V_ BI) V 1
KF flicker noise coefficient ( _KF_ ) - 0
AF flicker noise exponent ( _AF_ ) - 1
FC coefficient for forward-bias depletion capacitance formula - 0.5


_k_ Boltzman’s constant 1 _._ 3806226 10 _[−]_ [23] J/K
_q_ electronic charge 1 _._ 6021918 10 _[−]_ [19] C


_Standard Calculations_


Absolute temperatures (in kelvins, K) are used. The thermal voltage


_V_ TH = _[kT]_ [NOM] _._ (7.556)

_q_


and the band gap energy at the nominal temperature is


_EG_ ( _T_ NOM) = _EG_ (0) _−_ 0 _._ 000702 4 _T_ NOM [2] (7.557)
_T_ NOM + 1108 _[.]_


Here _EG_ (0) is the parameter EG — the band gap energy at 0 K.


_Temperature Dependence_


268 _CHAPTER 7. ELEMENT CATALOG_


Temperature effects are incorporated as follows where _T_ and _T_ NOM are absolute temperatures in Kelvins
(K).

_Parasitic Resistances_


The resistive parasitics _RS_, _RG_ and _RD_ are are calculated from the sheet resistivities RS (= _RS_ _[′]_ [),][ RG][ (=]
_RG_ _[′]_ [) and][ RD][ (=] _[ R]_ _D_ _[′]_ [), and the] _[ Area]_ [ specified on the element line.]

_RD_ = _RD_ _[′]_ _[Area]_ (7.566)
_RG_ = _RG_ _[′]_ _[Area]_ (7.567)

_RS_ = _RS_ _[′]_ _[Area]_ (7.568)


The parasitic resistance parameter dependencies are summarized in figure 7.86.



PROCESS
PARAMETERS
RD _RD_ _[′]_
RG _RG_ _[′]_
RS _RS_ _[′]_



+ GEOMETRY
PARAMETERS
_Area_



_→_ DEVICE
PARAMETERS



_RD_ = _f_ ( _Area, R_ _[′]_ _D_ )

_RG_ = _f_ ( _Area, R_ _[′]_ _G_ )

_RS_ = _f_ ( _Area, R_ _[′]_ _S_ )



Figure 7.86: MOSFET parasitic resistance parameter relationships.


**Leakage Currents**


Current flows across the normally reverse biased gate-source and gate-drain junctions. The gate-source
leakage current
_IGS_ = _Area ISe_ [(] _[V][GS][/V]_ [TH] _[ −]_ [1)] (7.569)


and the gate-drain leakage current


_IGD_ = _Area ISe_ [(] _[V][GD][/V]_ [TH] _[ −]_ [1)] (7.570)


The dependencies of the parameters describing the leakage current are summarized in figure 7.87.


_MESFET_ 269


_I/V Characteristics_


The current/voltage characteristics are evaluated after first determining the mode (normal: _VDS ≥_ 0 or
inverted: _VDS <_ 0) and the region (cutoff, linear or saturation) of the current ( _VDS, VGS_ ) operating point.


_Normal Mode: (VDS ≥_ 0 _)_


The regions are as follows:


cutoff region: _VGS_ ( _t −_ _τ_ ) _< VT_ 0
linear region: _VGS_ ( _t −_ _τ_ ) _> VT_ 0 and _VDS ≤_ 3 _/α_
saturation region: _VGS_ ( _t −_ _τ_ ) _> VT_ 0 and _VDS >_ 3 _/α_


Then



0 cutoff region


_Area β_ (1 + _λVDS_ ) 1 +[ _V BGS_ [ _V_ ( _GSt −_ ( _tτ −_ ) _−τ_ ) _V −T_ 0 _V_ ] [2] _T_ 0] [Ktanh] linear and saturation

regions



_IDS_ =



⎧
⎪⎪⎪⎪⎨

⎪⎪⎪⎪⎩



(7.571)



where




  1 _−_ 1 _−_ _VDS_ _[α]_



(7.572)
1 saturation regions



Ktanh =



⎧
⎨


⎩



�3

_[α]_ 3 linear region



is a taylor series approximation to the tanh function. _Inverted Mode: (VDS <_ 0)


In the inverted mode the MOSFET I/V characteristics are evaluated as in the normal mode (7.571) but with
the drain and source subscripts exchanged.
The relationships of the parameters describing the I/V characteristics of the model are summarized in
figure 7.88.


_Capacitances_



PROCESS
PARAMETERS

IS _IS_



+ GEOMETRY
PARAMETERS
_Area_



_→_ DEVICE
PARAMETERS

_IGS_ = _f_ ( _IS, Area_ )
_IGD_ = _f_ ( _IS, Area_ )



Figure 7.87: GASFET leakage current parameter dependencies.


270 _CHAPTER 7. ELEMENT CATALOG_


The drain-source capacitance
_CDS_ = _Area CDS_ _[′]_ (7.573)


The gate-source capacitance



Figure 7.88: LEVEL 2 (Raytheon model) I/V dependencies.


_MESFET_ 271


The capacitance parameter dependencies are summarized in figure 7.89.


_AC Analysis_


The AC analysis uses the model of figure **??** with the capacitor values evaluated at the DC operating
point with

_gm_ = _[∂I][DS]_ (7.583)

_∂VGS_


and
_RDS_ = _[∂I][DS]_ (7.584)

_∂VDS_


_Noise Analysis_


The MOSFET noise model accounts for thermal noise generated in the parasitic resistamces and shot and
flicker noise generated in the drain source current generator. The rms (root-mean-square) values of thermal
noise current generators shunting the four parasitic resistance _RD_, _RG_ and _RS_ are



PROCESS
PARAMETERS

ALPHA _α_
CGD _CGD_ _[′]_
CGS _CGS_ _[′]_
CDS _CDS_ _[′]_
VBI _VBI_
VT0 _VT_ 0
M _B_



+ GEOMETRY
PARAMETERS

_Area_



_→_ DEVICE
PARAMETERS
_{CDS_ = _f_ ( _Area, CDS_ _[′]_ [)] _[}]_
_{CGD_ = _f_ ( _Area, CGD_ _[′]_ _[, α,]_
_B, FC_ _, VBI_ _, VT_ 0) _}_
_{CGS_ = _f_ ( _Area, CGS_ _[′]_ _[, α,]_
_B, FC_ _, VBI_ _, VT_ 0) _}_



Figure 7.89: Capacitance dependencies.


272 _CHAPTER 7. ELEMENT CATALOG_




   _In,D_ =

   _In,G_ =

   _In,S_ =



_√_
4 _kT/RD_ A/



Hz (7.585)


Hz (7.586)


Hz (7.587)



_√_
4 _kT/RG_ A/

_√_
4 _kT/RS_ A/



Shot and flicker noise are modeled by a noise current generator in series with the drain-source current
generator. The rms value of this noise generator is

          _In,DS_ = _I_ SHOT [2] _,DS_ [+] _[ I]_ FLICKER [2] _,DS_ (7.588)







_√_
Hz A/ Hz (7.589)



_I_ SHOT _,DS_ =


_I_ FLICKER _,DS_ =



2 _√_
4 _kT gm_ A/
3



_KF IDS_ _[A][F]_ A/ _√_ Hz (7.590)
_f_







where the transconductance
_gm_ = _[∂I][DS]_ (7.591)

_∂VGS_


is evaluated at the DC operating point and _f_ is the analysis frequency.


### **Chapter 8**

# **Examples**

##### **8.1 Simple Differential Pair**

The following circuit determines the dc operating point of a simple differential pair. In addition, the ac
small-signal response is computed over the frequency range 1Hz to 100MEGHz.


SIMPLE DIFFERENTIAL PAIR
VCC 7 0 12
VEE 8 0 -12
VIN 1 0 AC 1
RS1 1 2 1K
RS2 6 0 1K
Q1 3 2 4 MOD1
Q2 5 6 4 MOD1
RC1 7 3 10K
RC2 7 5 10K
RE 4 8 10K
.MODEL MOD1 NPN BF=50 VAF=50 IS=1.E-12 RB=100 CJC=.5PF TF=.6NS
.AC DEC 10 1 100MEG
.END

##### **8.2 MOS Output Characteristics**


The following file computes the output characteristics of a MOSFET device over the range 0-10V for VDS
and 0-5V for VGS.


MOS OUTPUT CHARACTERISTICS
VDS 3 0
VGS 2 0
M1 1 2 0 0 MOD1 L=4U W=6U AD=10P AS=10P
.MODEL MOD1 NMOS VTO=-2 NSUB=1.0E15 UO=550

- VIDS MEASURES ID, WE COULD HAVE USED VDS, BUT ID WOULD BE NEGATIVE
VIDS 3 1
.DC VDS 0 10 .5 VGS 0 5 1
.END


273


274 _CHAPTER 8. EXAMPLES_

##### **8.3 Simple RTL Inverter**


The following file determines the dc transfer curve and the transient pulse response of a simple RTL inverter.
The input is a pulse from 0 to 5 Volts with delay, rise, and fall times of 2ns and a pulse width of 30ns. The
transient interval is 0 to 100ns, with printing to be done every nanosecond.


SIMPLE RTL INVERTER
VCC 4 0 5
VIN 1 0 PULSE 0 5 2NS 2NS 2NS 30NS
RB 1 2 10K
Q1 3 2 0 Q1
RC 3 4 1K
.MODEL Q1 NPN BF 20 RB 100 TF .1NS CJC 2PF
.DC VIN 0 5 0.1
.TRAN 1NS 100NS
.END


_8.3. SIMPLE RTL INVERTER_ 275


276 _CHAPTER 8. EXAMPLES_

##### **8.4 Adder**


The following file simulates a four-bit binary adder, using several subcircuits to describe various pieces of
the overall circuit.


ADDER - 4 BIT ALL-NAND-GATE BINARY ADDER
*** SUBCIRCUIT DEFINITIONS
.SUBCKT NAND 1 2 3 4

- NODES: INPUT(2), OUTPUT, VCC
Q1 9 5 1 QMOD
D1CLAMP 0 1 DMOD
Q2 9 5 2 QMOD
D2CLAMP 0 2 DMOD
RB 4 5 4K
R1 4 6 1.6K
Q3 6 9 8 QMOD
R2 8 0 1K
RC 4 7 130
Q4 7 6 10 QMOD
DVBEDROP 10 3 DMOD
Q5 3 8 0 QMOD
.ENDS NAND
.SUBCKT ONEBIT 1 2 3 4 5 6

- NODES: INPUT(2), CARRY-IN, OUTPUT, CARRY-OUT, VCC
X1 1 2 7 6 NAND
X2 1 7 8 6 NAND
X3 2 7 9 6 NAND
X4 8 9 10 6 NAND
X5 3 10 11 6 NAND
X6 3 11 12 6 NAND
X7 10 11 13 6 NAND
X8 12 13 4 6 NAND
X9 11 7 5 6 NAND
.ENDS ONEBIT
.SUBCKT TWOBIT 1 2 3 4 5 6 7 8 9

- NODES: INPUT - BIT0(2) / BIT1(2), OUTPUT - BIT0 / BIT1,

- CARRY-IN, CARRY-OUT, VCC
X1 1 2 7 5 10 9 ONEBIT
X2 3 4 10 6 8 9 ONEBIT
.ENDS TWOBIT
.SUBCKT FOURBIT 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15

- NODES: INPUT - BIT0(2) / BIT1(2) / BIT2(2) / BIT3(2),

- OUTPUT - BIT0 / BIT1 / BIT2 / BIT3, CARRY-IN, CARRY-OUT,
VCC
X1 1 2 3 4 9 10 13 16 15 TWOBIT
X2 5 6 7 8 11 12 16 14 15 TWOBIT
.ENDS FOURBIT
*** DEFINE NOMINAL CIRCUIT
.MODEL DMOD D
.MODEL QMOD NPN(BF=75 RB=100 CJE=1PF CJC=3PF)
VCC 99 0 DC 5V
VIN1A 1 0 PULSE(0 3 0 10NS 10NS 10NS 50NS)
VIN1B 2 0 PULSE(0 3 0 10NS 10NS 20NS 100NS)
VIN2A 3 0 PULSE(0 3 0 10NS 10NS 40NS 200NS)


VIN2B 4 0 PULSE(0 3 0 10NS 10NS 80NS 400NS)
VIN3A 5 0 PULSE(0 3 0 10NS 10NS 160NS 800NS)
VIN3B 6 0 PULSE(0 3 0 10NS 10NS 320NS 1600NS)


_8.5. OPERATIONAL AMPLIFIER_ 277


Descriptions of the basic algorithms of Spice.


278 _CHAPTER 8. EXAMPLES_