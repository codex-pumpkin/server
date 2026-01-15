**26** INTRODUCTION TO ELECTRICAL COMPUTER SIMULATION


biased in the forward active region, as predicted by hand calculations. A value of _{3F,_
BETADC, is computed that takes into account the _Ie_ and _18_ for each transistor. The rest
of the data represent the values of the elements in the linear equivalent model of the
transistor and are described in more detail in Chap. 3.


The above examples are intended to show a new user of computer simulation how
natural the SPICE input language is and how straightforward is the output information
provided by the program for a simple DC analysis. **In** this and the following chapters
all supported elements and analysis modes are described, as well as the best approaches
for using SPICE to solve electrical circuits.
SPICE2 is a batch program. If a circuit element must be changed or an output
request has been omitted, the previous steps must be repeated, namely, editing the input
file, running the simulation, and viewing the output file.
SPICE3, however, is interactive, and the user is transferred inside a _spice shell_
upon invocation of the program:

```
      Spice 1 ->

```

SPICE3 commands must be entered at the prompt. At this point the user needs a few additional commands not available in SPICE2 in order to communicate with the program.
Figure 1.5 is the transcript of an interactive SPICE3 session of the same simulation
as performed above for bj t. ckt. As can be seen, each command is followed by the
results displayed on the screen by the program. The first command, **source,** defines
the input file; the second, **listing,** lists the input file for verification; the third, **op,**
runs the DC operating point; and the fourth, **print** **all,** lists all node voltages and
currents through voltage sources, that is, the same information found under the SMALL

SIGNAL BIAS SOLUTION header in SPICE2.
Note that the print command does not provide the OPERATING POINT INFORMATION of SPICE2, and in release 3d2 this information can be accessed only on a
device-by-device basis by using the **show ql** command. The resulting information
listed on the screen is much more verbose.
For larger circuits it is useful to **display** all available output variables, but **print**
or **plot** only selected ones.
While one circuit is active, the results of various analyses can be either viewed
graphically on the screen or printed out. SPICE3 saves all node voltages of all simulations performed during the same SPICE3 session and provides for the interactive
display of selected waveforms while the simulation is running. Input files can be edited
and repeated simulations can be performed from within the SPICE3 shell. When you
have finished, type **quit** to exit SPICE3. The results of the different runs have been
saved in temporary files, which are displayed before the program exits, and the user has
a last chance to save any desired results.
SPICE3 can also be run in batch mode through the command


`% spice3` `-b bjt.ckt`       - `bjt.out`


USER INTERACTION WITH SPICE ANDTHE COMPUTER **27**


_**__**_ _**"**_ _**ro ••_**_ ._w_,__ _ _~ __ .", ..- .. **n. .•.•••••.** **_ .•_** **.••.••_ •.•••** **~_** **•..••.,'••** **,~"'._**
```
This is a sarrplenew.s.!il~_~stYJ;iJJ.b~_P.;r::!pt~~
whenever spice or nutmeg is started.

Spice 1 -> source bjt.ckt

Circuit: ONE-TRANSISTOR CIRCUIT (FIG. 1.2)

Spice 2 -> listing
    ONE-TRANSISTOR CIRCUIT (FIG. 1.2)

   1 : one-transistor circuit (fig. 1.2)
   3 ql'2 1 0 qrnod'" -, ~~ .
   4 rc 2 3 lk
   5 rb 1 3 200k
   6 vcc 3 0 5
   9 .model qrnodnpn is=le-16 bf=100
   15 .end
```

`Spice 3` -> `op`
```
Spice 4 -> print all
v(l) = 7.934384e-Ol
v(2) = 2.896719e+OO
v(3) = 5.000000e+OO
vcc#branch = -2.12431e-03
Spice 7 -> quit
Warning: the following plot hasn't been saved:
op2 ONE-TRANSISTOR CIRCUIT (FIG. 1.2), operating point

Are you sure you want to quit (yes)? yes
Spice- 3d2 done

```

**Figure 1.5** Transcriptof interactiveSPICE3analysi'sof bj t .ckt.


At completion bj t .out contains information similar to but in a different format from
what is produced by SPICE2. SPICE3 also produces a _raw/tie_ containing data to be
displayed graphically when the - r flag is used. If no filename is specified, the display
data are stored in a file called rawspice. raw. The companion postprocessor for the
SPICE3 rawfiles is called _Nutmeg._ _•_
The most common platform for running SPICE has becom y the IBM PC and PC
clones. Although SPICE2 is not available from DC Berkeley for the PC, a number
of commercial offerings, such as PSpice from MicroSim, IsSpice from Intusoft, and
HSPICE from Meta Software, run under DOS or Windows. SPICE3 is distributed by
DC Berkeley for the PC; the models supported range from the AT to the 486.
Although the sequence of operations remains the same, the command to simulate
may differ from package to package. Some packages offer DOS shells, which facilitate
the simulation sequence of creating or modifying the input circuit, running SPICE, and


**28** **,** INTRODUCTION TO ELECTRICAL COMPUTER SIMULATION


viewing the results. The schematic capture available in the Design Center from Mi..£oSim and SpiceNet frQillTutusoftallow the circuit specificati~entered grap!!''*' [
ically rather than through the...sm.~e.
Although in Windows-based packages most operations can be performed from
menus, it is still useful to follow file-naming conventions similar to those introduced
above for circuit identification. When one runs PSpice from DOS, the input and output
file names follow the program name as command arguments:


`C`      - `PSPICE BJT.CKT BJT.OUT`


The output file from PSpice is of the same format and contains the same information
as that from SPICE2. The name of the output file must not be specified unless a different suffix than . OUT is desired. Note that BJT . OUT as saved by PSPICE is similar
in format to that saved by SPICE2. SPICE3 and Nutmeg can be run similarly on a Pc.
First, SPICE3 is run in batch mode, then Nutmeg is run to view the results. (The two
commands can be saved in a . BAT file, SPICE3 . BAT, which runs BSPICE, the name
of batch SPICE3 on a PC, and then runs Nutmeg on the result file RAWSPICE. RAW
created by BSPICE.) More on displaying results is presented in the following two
sections.
Although not as common as on the PC, SPICE is also available on the Apple Macintosh. PSpice and IsSpice are offered on the Macintosh, as is MacSpice, from Deutsch
Engineering, which is specifically tailored for the Macintosh interface.
Both SPICE2 and SPICE3 are distributed by the University of California, Berkeley,
for several computers and operating systems. For the VMS operating system on DEC
computers, the same steps as in UNIX must be followed for simulating circuits. When
the input file is ready, type

```
      $ run spice

```

SPICE2 will prompt for an _input_ _file_ and then for an _output_ _file._ SPICE3 transfers to its
shell, where the same commands as in UNIX are valid.
SPICE2 and SPICE3 run in batch mode on a variety of mainframe computers, such
as **IBM,** CDC, and Cray. Typically, the jobs submitted to such computers contain job
control statements in addition to the SPICE circuit description. Job control statements
define the user identification, time limit, computer resources, input and output units,
and the program to be run. The Electronics Research Laboratory at UC Berkeley tells
where users can get a copy of SPICE for a specific mainframe computer.


**1.3.3** **SPICE Results for AC and TRAN Analyses**


So far we have learned how to write a SPICE circuit file, what types of statements are
available, how to run the analysis on the most common computers, and how to interpret
the results of a DC analysis in the output file. Only one control statement, • **OP,** has


l,



USER INTERACTION WITH sPICE,ANDTHE COMPUTER **29**


been introduced so far; this was sufficient for obtaining all computed node voltages in
the output files, bridget. out and bj t .out.
In addition to a DC analysis, SPICE also performs a steady-state sinusoidal analysis, invoked by the **.AC** control line, and a time-domain analysis, invoked by **the. TRAN**
line. These analyses result in large amounts of data, due to the fact that each node voltage is computed for all frequencies or times. Forsmall circuits such as the ones in Examples 1.1 and 1.2,this may not bea problem. But as the circuits grow, so will the size
of the output files, making the results of interest more difficult to find. Thus the • **PRINT**
and • **PLOT** control statements define the node voltages of interest or, more generally,
the desired output variables .• **PRINT** and • **PLOT** define only the results saved in the
output file; various versions of SPICE have additional control lines or interactive commands that let the user access results that have been saved in binary files and display
them in graphical mode with the help. Ofpostprocessing programs.
The interpretation of the results of SPICE simulations is best understood if exern [c]
plified for typical applications. The following example introduces the SPICE frequency,
or AC, analysis and how to display the results as a Bode plot.


_**EXAMPLE 1.5**_


Compute the node voltages and the current for the series RLC circuit shown in Figure
1.6 assuming the following periodic input signal:


.)

_Vin_ = 5 cos _27T1Ot_


Write the SPICE deck and run the program to .verify the results derived from hand
calculation. Then, vary the frequency of the input signal _Vi~_ from 1 Hz to 10 kHz and
obtain the Bode plot of the magnitud~ and the phase of the voltage across the capacitor
_C_ _1, V3._


_**Solution**_
First, the solution for the network is obtained using phasor calculations. In calculating
the current, the resistanceR1 and the inductorreactancewL1 can be neglected compared
to the reactance of the capacitor, 1/ _w_ C1. The crihent is ".



I = _Vin_ = _V_ _[in]_
Z _R1_ + _l/iwC_ _1_
III = 0.31 rnA, LI = 90°



5'.10- [3]
0.2;-j16 '= _jO.31 ._ 10-3 (1. 7)



The voltages at nodes 2 and 3, _V2_ and _V3,_ closely follow the input signal:


**30** 1 INTRODUCTION TO ELECTRICAL COMPUTER SIMULATION

.125mH

        

**Figure 1.6** Series RLC circuit.


The SPICE deck for this circuit, rIc. ckt, is based on the previous examples.

```
      SERIES RLC CIRCUIT
```

       ```
      VIN 1 0 AC 5 0
      L1 2 3 0.125
```

Cl 3 0 10
```
      R1 1 2 200
      .AC LIN 1 10 10
      .PRINT AC 1M (VIN) IP(VIN) VM(2) VP(2) VM(3) VP(3)
```

        - END


Two new control statements are used, • **AC** and • **PRINT.** The first statement represents
a request for a steady-state frequency-domain analysis and defines the type of frequency
variation, **LIN,** the number of frequencies, 1, and the starting and ending frequencies,
which in this case are the same, 10Hz.
The second statement,        - **PRINT,** is necessary if the user wants the results of the
analysis to be written into the output file. Unlike the case of the DC operating point
analysis,        - **OP,** where SPICE automatically prints the results in the output file, for the
other analyses the user must specify which data are to be saved in the output file. The
**. PRINT** keyword must be followed by the type of analysis, AC in this case, and circuit
variables to be saved in the output file. For AC variables the character V (for voltage)
or I (for current) must be followed by one or more additional characters specifying
whether polar or rectangular values are desired. AC voltages and currents are phasor
quantities and can be expressed in terms of either real and imaginary parts, as in VR (2 )
and VI (2 ), or a magnitude and a phase, as in VM( 2) and VP (2 ) . These two statements are described in detail in Chaps. 5 and 4, respectively. **In** most SPICE versions,
including SPICE2 and SPICE3, only the currents flowing through voltage sources can
be measured; therefore, a current requested on a • **PRINT** line must always have as
argument a voltage source name.
The following results are computed by SPICE for the desired phasors at 10Hz:

```
        FREQ 1M (VIN) IP(VIN) VM(2) VP(2) VM(3) VP(3)
      1.000E+01 3.143E-04 -9.072E+01 5.000E+00 -7.203E-01 5.002E+00 -7.203E-01

```

USER INTERACTION WITH SPICEAND THE COMPUTER 31


If the amplitude of the input signal were 1 V, the voltage at each node computed by
SPICE would represent the transfer function at that node referred to the input. The
phase of the current, I P (VIN), is negative because the direction of flow is assumed in
SPICE to be from the positive to the negative terminal through the voltage source.
The next part of this example is to obtain the Bode plot of the magnitude and phase
of the voltage across the capacitor for the frequency range from 1 Hz to 10 kHz. The
only two statements that need to be changed are the. ACstatement, to reflect the desired
frequency range, and the output request line. We also change the amplitude of _Vin_ to 1
V in order to obtain the transfer function _V3/ Vin'_
For the frequency variation a logarithmic scale is desirable, because it provides an
even number of analysis points in all ranges. SPICE offers two choices of logarithmic
intervals, the decade, DEC,and the octave, OCT.The most commonly used frequency
interval is the decade, and we will use it for obtaining the Bode plot. The new .AC
line is

```
.AC DEC 10 1 10K

```

This statement requests an AC solution of the RLC circuit at 10 frequencies per decade
in the interval from 1 Hz to 10kHz.
In addition to the. PRINT capability, SPICE supports a • PLOT command, which
produces an ASCII character, or line-printer, plot. The information entered on the
•PLOT line is identical to that entered on a •PRINT line. For the desired Bode plot the
requesting statement is

```
.PLOT AC VDB(3) VP(3)

```

Note that the magnitude ofthe voltage is requested in decibels as specified by the suffix
DB. The new •ACline and the above •PLOT line should replace the existing •AC and

 - PRINT lines in the SPICE input file rlc.ckt. The resulting Bode plot, shown in
Figure 1.7, is taken from the SPICE output file, rIc. au t. The amplitude peaks at 450
Hz, the resonant frequency of the circuit, and the phase changes by 180 [0] because of the
two complex poles (see also Chap. 6).

```
******* 09/08/92 ******** SPICE 2G.6 3/15/83 ******** 19:45:56 ********

SERIES RLC CIRCUIT

**** AC ANALYSIS TEMPERATURE = 27.000 DEG C

***********************************************************************
LEGEND:

```

*: VDB(3)
```
+: VP(3)

```

Figure 1.7 SPICE2 ASCII plot of VDB (3) and VP (3) .


USER INTERACTION WITH SPICEAND THE COMPUTER 33


There are ways to obtain SPICE plots with high-quality graphics on a computer
screen or printer. For the UC Berkeley releases, SPICE 2G6 and SPICE3, the graphic
postprocessor is Nutmeg. SPICE2 plots can be viewed or printed in Nutmeg on a UNIX
system by setting the rawfile option, - r f i 1ename, on the command line:


`spice2` `-r rlc_sp2.raw` < `rlc.ckt` - `rlc.out`


Before a rawfile created by SPICE2 can be opened in Nutmeg, the _sconvert_ utility must
be run, which translates the file to the SPICE3/Nutmeg rawfile format:

```
sconvert 0 rlccsp2.raw a rlc_sp3.raw

```

The Bode plot of the capacitor voltage magnitude and phase produced by Nutmeg
from a SPICE2 rawfile is shown in Figure 1.8. I( SPICE3 is used for simulation, the plot
of any desired circuit variable can be obtained while running the program interactively
from the spice3 shell, as shown in Section 1.3.2. If SPICE3 is run in batch mode, it
creates by default a binary result file called rawfile. raw, which can then be directly
loaded and viewed in Nutmeg. The rawfile created by SPICE3 can be assigned any
name with the -r filename option on the command line, as in the following:


`spice3` `-b -r rlc.raw rlc.ckt` - `rlc.out`


Note that SPICE3 does not support the • **PRINT** and. **PLOT** commands of SPICE2 and
most other commercial SPICE programs.

```
            20

```

-- VDB(3)

                - - ro [VP] (3)


            

-20
`eO` e1 e2 e3 e4
Figure 1.8 Bode plot ofVDB (3) and VP (3) from
Nutmeg.


**34** 1 INTRODUCTION TO ELECTRICAL COMPUTER SIMULATION


Another graphics package available on UNIX machines that run X-Windows is
_xgraph._ The tabular output created by the SPICE2 • **PRINT** command can be used as
input to _xgraph._ The data produced by the • **PRINT** command are extracted from the
SPICE output file, a few headers are added, and the results can then be viewed or printed
in the xgraph tool; consult the manual page of xgraph for the details.
Commercial PC SPICE packages offer postprocessing for all popular PC graphics,
including SVGA, VGA, EGA, CGA, and Hercules. Besides using the regular output
file, the user can view the results of the simulation in graphic mode. MicroSim offers
_Probe,_ which can display and perform arithmetic operations on waveforms. **In** order to
generate the graphics file PROBE. DAT, a control statement, • **PROBE,** must be added to
the PSpice input file. IntuScope, the postprocessor for IsSpice, best takes advantage of
PC graphics.
On Macintosh computers tabular output created by the • **PRINT** command on a
Macintosh or another computer can be viewed and printed using plotting programs
such as Cricket Graph or Kaleidograph.
The rest of this section is dedicated to introducing the third major analysis mode
of SPICE, time-domain, or transient, analysis. The following example describes how
to obtain the SPICE time-domain solution for the above RLC circuit.


_**EXAMPLE 1.6**_


Use SPICE to compute the time-domain response of the series RLC circuit of Figure
1.6 to a pulse with an amplitude of 5 V applied at the input at time 0 for 25 ms. Find
the waveform of _V3(t)_ between 0 and 50 ms. Use _R]_ = 500,.


_**Solution**_
Two new items must be introduced in the SPICE deck of the RLC circuit in order to
perform a transient analysis. First, a pulse with the defined characteristics must be assigned to the voltage source VIN. Second, the control line • **THAN** must be included,
which defines the time interval for the analysis. The complete SPICE deck for the transient analysis is listed below.

```
      SERIES RLC CIRCUIT
```

      ```
      VIN 1 0 PWL 0 0 10N 5 25M 5 25.01M 0
      L1 2 3 0.125
      C1 3 0 lU
      R1 1 2 50
       .TRAN .2M 50M
       .PRINT TRAN V(3) V(l)
```

        - END


The first difference from the input file used in the AC analysis is found on the VIN
line: the two nodes are followed by the keyword **PWL,** which identifies a piecewise linear


USER INTERACTION WITH SPICEAND THE COMPUTER **35**


function generated by the input source. The values following the keyword represent
pairs of time-voltage values. Other waveform functions can be generated by a source;
complete information on independent sources is in Section 2.2.6.
The • **TRAN** control line contains three values: the time step, which is the interval
at which values are printed or plotted by a • **PRINT or . PLOT** command; the final time,
and the starting time. SPICE uses an internally adjusted, variable time step for solving
the circuit equations (see also Chaps. 6 and 9); the value on **the.** **TRAN** line is used only
for result output purposes. All the details on specifying a time-domain analysis can be
found in Chap. 6.
A • **PRINT** statement followed by an analysis type, **TRAN,** is also present in the
deck. Two waveforms are requested, V (1 ), the input, and V (3 ), the voltage across
the capacitor. The tabular output saved in r 1 C • au t is used in this case as input for
_xgraph,_ which produces the plot of Figure 1.9. The voltage across capacitor C1 displays an overshoot, which takes almost the entire pulse width to settle. This behavior
corresponds to the peaked frequency characteristic displayed by the circuit; see Figures
1.7 and 1.8.
If PSpice is used for this analysis and the line • **PROBE** is included in the deck,
upon completion of the SPICE run the user is transferred into the Probe program, which
enables the results to be viewed on the screen or a hardcopy to be produced as shown
in Figure 1.10.
Note that both the AC and transient analyses can be made part of a single SPICE
run by the addition of the **PWL** specification to the AC characteristics on the VIN line
and the inclusion of the • **AC** and • **TRAN** lines together with the relevant output request
lines in the same input file.

```
                       Rle

```

8.00



6.00


- 4.00

"0 <Ii
~ 2.00
a.
«E 0.00


-2.00


-4.00


0.0000 10.0000 20.0000 30.0000


Time, ms


**Figure 1.9** _xgraph_ plot of transient waveform V ( 3 ) .



V(1)


V(3)


40.0000 50.0000


**36** 1 INTRODUCTION TO ELECTRICAL COMPUTER SIMULATION


RLC


Daterrime run: 09/16/92 16:43:41 Temperature: 27.0
10


5

         "C ai
:E
c.
« E
0


```
-5
```

  
 - v(3)



10 `20`



`30` `40` 50



Time, ms



**Figure 1.10** Probe plot of transient waveform V ( 3 ) .


The main analysis modes of SPICE as well as how to display the results of the
analyses have been covered in this section. Alternatives for obtaining graphs of the results have been presented; the list of graphics packages available on computers, engineering workstations, and personal computers is intended not to be complete but only to
exemplify an approach for obtaining high-quality plots from SPICE • **PRINT** data. For
uniformity, the plots in the rest of the book are produced using the Oscilloscope and
Network Analyzer tools of the Analog Workbench because of their superior graphic
quality.


**1.4** **SUMMARY**


This chapter introduced the basic capabilities of the electrical simulation program
SPICE. The solution process of SPICE was linked to the knowledge of electric circuits
necessary for using the simulation. You should be able to write a SPICE input deck for
a simple linear circuit, run the basic analyses, and save the results in a output file or
create a plot.
All the elements used so far can be specified in SPICE according to the following
format:


_Aname nodel node2 <node3> ... <MODELname> <value>_


Associated with complex elements, such as transistors, is the global statement • **MODEL,**
which defines the parameters for a number of elements:


•MODEL _MODELname MODELtype <PARAM1=valuel PARAM2=value2 ... >_


REFERENCES **37**


The following analysis control statements are defined:

**.op**

**•AC** _INTERVAL numpts fstart fstop_
**. TRAN** _TSTEP TSTOP <TSTART>_


for performing a DC, frequency-domain, or time-domain analysis, respectively. SPICE
results are requested with the following control statements:


•PRINT _ANALYSIS OULvarI_ _OUT_var2_ _._
•PLOT _ANALYSIS OULvarI_ _OUT_var2_ _._


The general structure of SPICE deck is shown on page 22; all SPICE circuit descriptions must start with a _title_ line and end with an • **END** line.
Examples of several plotting tools were presented, such as _Nutmeg, xgraph,_ and
_Probe._ The plots in the following chapters of this book are all created using the display
tools of the Analog Workbench. . - .


**REFERENCES**


Branin, F. H., G. R. Hogsett, R. L. Lunde, and L. E. Kugel. 1971. ECAP II-A new electronic
circuit analysis program. _IEEE Journal of Solid-State Circuits SC-6_ (August): 146-165.
Dorf, R. C. 1989. _Introduction to Electric Circuits._ New York: John Wiley & Sons.
Nagel, L. 1975. SPICE2: A computer program to simulate semiconductor circuits. Univ. of California, Berkeley, ERL Memo UCBIERL M75/520 (May).
Nagel, L., and R. A. Rohrer. 1971. Computer analysis of nonlinear circuits, excluding radiation
(CANCER), _IEEE Journal of Solid-State Circuits SC-6_ (August): 166-182.
Nilsson, J. W. 1990. _Electric Circuits._ 3d ed. Reading, MA: Addison-Wesley.
Paul, C. R. 1989. _Analysis of Linear Circuits._ New York: McGraw-Hill.
IBM. 1965. 1620 electronic circuit analysis program [ECAP], [l620-EE-02X] User's Manual,
IBM Application Program File H20-0170-1. -,,
Pederson, D. O. 1984. A historical review of circuit simulation. _IEEE Transactions on Circuits_
_and Systems_ CAS-31 (January): 103-111. '
Quarles, T. L. 1989. SPICE3 version 3Cl user's guide. Univ. of California, Berkeley, UCBIERL
Memo M89/46 (April).
MicroSim. 1991. _PSpice: Circuit Analysis Users Guide Version 5.0._ Irvine, CA: Author.
Vladimirescu, A., K. Zhang, A. R. Newton, D. O. Pederson, and A. L. Sangiovanni-Vincentelli.
1981 (August). SPICE version 2G user's guide, Dept. of Electrical Engineering and Computer Science, Univ. of California, Berkeley.
Weeks, W. T., A. J. Jimeniz, G. W. Mahoney, D. Mehta, H. Quassenizadeh, and T. R. Scott.
1973. Algorithms for ASTAP-A network analysis program. _IEEE Transactions on Circuit_
_Theory_ CT-20 (November): 620-634.


_**Two**_


_**CIRCUIT**_ _**ELEMENT AND**_
_**NETWORK**_ _**DESCRIPTION**_


2.1~ **ELEMENTS, MODELS, NODES, AND CONVENTIONS**



**38**



Element statements and model statements represent the core of the circuit description,
as shown in Sec. 1.3.1. Every element type accepted by SPICE2 and SPICE3 is presented in this and the following chapter. All commercial SPICE versions support the elements available in SPICE2, but not all implement the newer element types of SPICE3.
SPICE elements are-classified in threecategories:.two::tertniiial elements, described in
Sec. 2.2; multiterminanlemenfs, presented in Sec: 2.3;'-and semiconductor devices,
presented in Chap. 3.
An element statement contains connectivity information and, either explicitly or
by reference to a model name, the values of the defined element. Model statements are
necessary for defining the parameters of complex elements. SPICE2 supports models
only for semiconductor devices; these model types, common to all SPICE versions, are
described in Chap. 3. SPICE3 and PSpice, however, have extended model support to
most elements.
The following conventions must be observed in the SPICE2 (Vladimirescu, Zhang,
Newton, Pederson, and Sangiovanni- Vincentelli 1981), SPICE3 (Johnson, Quarles,
Newton, Pederson, and Sangiovanni-Vincentelli 1991), and PSpice (MicroSim 1991)
circuit definitions.

The circuit nodes must always be positive integers in SPICE2 or positive integers
and names in SPICE3. The circuit nodes need not be numbered sequentially. A circuit
must always contain a ground node, which must always be number O.
Every node in the circuit must have at least two elements connected to it; the only

G

exceptions are the substrate node in MOSFETs, which has internal connections to the
drain and to the source, and the nodes of unterminated transmission lines.


TWO-TERMINAL ELEMENTS 39


Every node in the circuit must have a DC path to ground. In DC, capacitors represent open circuits and inductors represent shorts. This requirement prevents the occurrence of floating nodes, for which the program cannot find a bias point.
Because SPICE2 uses modified nodal analysis (Ho, Ruehli, and Brennan 1975; McCalla 1988; see Chap. 9) to solve for both node voltages and currents of voltage-defined
elements, such as voltage sources and inductors, two restrictions must be observed: the
circuit cannot contain a loop of voltage sources or inductors, and it cannot contain a cutset of current sources or capacitors. The former is disallowed due to Kirchhoff's voltage
law, KVL, and the latter due to Kirchhoff's current law, KCL.
Any violation of the above restrictions results in an error message and termination
of the SPICE program. The possible error messages and corrective actions are described
in Appendix B.
Several conventions are observed in the following sections in the presentation of
element statements. In the statement format definition the characters or keywords that
must be present in an actual statement are boldface, and optional keywords or values
appear between angle brackets, < >.
The following description summarizes the conventions for different typesets.
1. Monotype is used for:

            - Computer (program) input and output

            - References made in the text to names, titles, or variables appearing in a
computer input or output
2. Boldface monotype is used for:

            - Command names, parameter names, model and analysis types, and characters that are keywords for the program; the same type is used whether these
keywords appear in a statement definition or are referred to in the text
3. Italic type is used for:

            - Variable names (subscripted characters as well)

            - Names of fields in SPICE statement definitions

            - Reference to the value of a program parameter with the same name; for
example the parameter name is L and the variable is _L_

            - Highlighting new concepts
4. Uppercase versus lowercase in SPICE statement definitions:

            - Variables in uppercase or starting with uppercase in statement definitions
denote a character field, such as _MODELname_

            - Variables in lowercase denote a numeric field in a statement as in TC=
_tel, tc2_

            - Exception: when a parameter name is followed by its value, the value may
be denoted by the same characters as the name, in uppercase, but italic type


2.2 **TWO-TERMINAL** **ELEMENTS**


This section describes both the syntax and the branch-constitutive equations (BCEs) of
all two-terminal elements except the semiconductor diode. The semiconductor diode
is presented together with multiterminal semiconductor devices in Chap 3. The I-V


**40** 2 CIRCUIT ELEMENT AND NETWORK DESCRIPTION


relations of semiconductor elements an~ expressed by complex analytic equations,
which require many parameters.
SPICE supports the following two-terminal elements:


Resistors (linear)

Capacitors (linear and nonlinear)

Inductors (linear and nonlinear)

Independent voltage sources (linear)

Independent current sources (linear)

Diodes (nonlinear)


The type of I-V branch-constitutive equation implemented in the program for each element listed above is specified in parentheses. All two-terminal elements supported by
SPICE2, except the diode, are described by simple BCEs, require only one or a few
parameters, and have no associated model statements.
SPICE3 supports semiconductor resistors and capacitors, which can be specified by
geometric and process parameters. These special elements have an **associated.** **MODEL**
statement for the process parameters. SPICE3 supports the following model types introduced in this chapter:


R Diffused resistor model

C Diffused capacitor model

**URC** Uniformly distributed RC model

**SW** Voltage-controlled switch model

**CSW** Current-controlled switch model


JCSpice also supports modeLstatem.ents for resistors, capacitors. inductors, nonlinear
magnetic cores, and switches for all elements except for sources.

        - On any two-terminal element statement the first node, _node},_ is positive, and the
second node, _node2,_ is negative. The branch voltage across any element is computed as


_Ve1em_ = _Vnodel_ _-_ _Vnode2_


and the current is assumed to flow from node _node}_ to node _node2._


**2.2.1** **Resistors**


The general form of the resistor statement is


_Rname node} node2 rvalue_ <TC = _tc1<,tc2»_


R in the first column identifies a resistor labeled _Rname,_ as shown in Figure 2.1, connected between nodes _node}_ and _node2_ of the circuit. Only the first 7 characters in
_name_ are used by SPICE2 to identify this resistor. SPICE3 does not restrict the length
of _name._


The BCE of a resistor is



TWO-TERMINAL ELEMENTS **41**


_niJde1_ _rvalue'_ _node2_
_I_ ____ ~ _Rname._
_R_

_V_ _R_


**Figure 2.1** Resistor model.'


(2.1)



where the proportionality constant _rvalue_ is the resistance measured in ohms, _VR_ the
,voltage across the resistor in volts, and _I_ _R_ t1).ecurrent in amperes. The resistance may
be positive or negative but cannot be zero.
SPICE models the temperature variation of the resistance by a second-order polynomial:


_rvalue(TEMP)_ = _rvalue(TNOM)[l_ + _tel(TEMP_ _- TNOM)_
_+_ _te2(TEMP - TNOM)2]_ _(2.2)_


The keyword **TC** must be present if one or both temperature coefficients are specified;
_tel_ and _te2_ are the first- and second-order temperature coefficients of the resistor specified in parts per °C or eq2, respectively. _TNOM_ is the nominal temperature, 27°C,
assumed in SPICE2, and _TEMP_ is a different simulation temperature specified in a

**• TEMP** statement. Note that SPICE3 and PSpice require the temperature coefficients
to be specified on-the **resistor.** **MODEL** line. PSpice also supports a second temperature
dependence, described by an exponential function.


_Examples_
R1 2 45 100
Rci 12 17 1K TC=O.001,0.015 (SPICE2)
RC1 12 17 `RMOD` 1K (SPICE3,PSpice)
`.MODEL` `RMOD` R TC1=0.001 TC2=0.015


**2.2:2** **Semiconductor** **Resistors (SPICE3)**


SPICE3 supports an extension of the general resistor element that allows a convenient
description of a diffused resistor from geometric and process information.
The general form of a semiconductor resistor statement is


_Rname nodel node2 <rvalue><Mname><L'=L><W=_ _W>_


If _rvalue_ is specified, this statement is equivalent to 'the ge~eral resisto~ statement and
any information following the value is discarded. Note that SPICE3 does not support
temperature coefficients on the resistor statement. A model statement with the general
format described in Sec. 1.3.1 must be used in order to define the parameters listed in
Table 2.1 for a model of type R.


**42** 2 CIRCUIT ELEMENT AND NETWORK DESCRIPTION


**Table 2.1** Semiconductor Resistor Model Parameters


**Name** **Parameter** **Units** **Default** **Example**

TCl First-order temperature coefficient lIoC 0.0 5E-3
TC2 Second-order temperature coefficient lI("C [2] ) 0.0 20E-6
RSH Sheet resistance flIsq. 0.0 50
DEFW Default width m 10- `[6]` 2E-6
NARROW Narrowing due to side etching m 0.0 lE-7


The resistance is computed from the length _L_ and width _W_ of the diffusion specified
in the resistor statement and the values _RSH_ and _NARROW_ of the model statement:


_L-NARROW_
(2.3)
_rvalue_ = _RSH._ _W - NARROW_


The temperature behavior is modeled the same way as for regular resistors (see Eq.
2.2). Note that the program provides default values only for Wand _DEFW,_ and not
for _L,_ because the width of most diffused resistors on a chip is equal to the minimum
feature size; a default value for _DEFW_ also prevents division by zero in Eq. 2.3 when

_W_ is omitted.


_EXAMPLE_ 2.1

```
      RDIFFl 1 2 RMODl L=50U W=5U
       .MODEL RMODl R RSH=lOO NARROW=.25U

```

The above statements define a resistor of resistance


_rvalue_ = 100. 50 - 0.25 n = 1047 n
5 - 0.25


**2.2.3** **Capacitors**


The general form of a capacitor statement is

_Cname node] node2 cvalue_ <IC = _Veo_ _>_


The C in the first column identifies a capacitor labeled _Cname_ and connected between
nodes _node]_ and _node2_ of the circuit, as shown in Figure 2.2.
The BeE of a capacitor is


_._ _I_ _dve_
_Ie_ = _eva ue ._ _---;It_ (2.4)


TWO-TERMINAL ELEMENTS **43**


_nog_e1_---<I_ _cvalue•...I ___ _n-(oge2_


_IC~_ _Cname_
_Vc_


**Figure** 2.2 Capacitor model.


where _cvalue_ is'the capacitance in farads and represents the proportionality constant
between the current through the capacitor, _ic,_ and the rate of change of the voltage
across the capaCitor, _Ve._ The integral variant of Eg. 2.4 is used in SPICE to model the
capacitor:

Ve = _-.-l-_ 1 _It_ _iedt_ + _Veo_ (2.5)
, . _cva ue_ 0


**IC** is optional and is used to input _Veo,_ the initial value (time _t_ = 0) of the capacitor
voltage. This value is used at _t_ = 0 only when **UlC** _(use initial conditions)_ is specified
in the. **TRAN** statement (see Chap. 6).


_Examples_
```
C2 2 0 lOP
CGS1 12 14 50F
```

CLOAD 310 20P IC=5


The above statement describes a linear capacitor with constant capacitance.
SPI and PS ice a 0 su ort nonlinear capacitors whose capacitance is a non"linear polynomial function of the termina vo age _Ve._
The general form of a nonlinear cap~citor statement is


_Cname node] node2_ **POLY** cO _c1 <c2 ..._ ><IC = _Veo_ _>_


The keyword **POLY** identifies the capacitor _Cname_ as nonlinear, and the values _cO,_
_c1,."_ are the coefficients of the corresponding powers _ofve._ The value of this capaCitor
is computed at each time point as



_cvalue_ = cO + _c1 ._ Ve + c2 . v~ + .,:


The BCE for the nonlinear capaCitor becomes.


_,_ _dq_ _d._ _d ('_ 2 3 )
Ie = _'dt_ = _d/cvalue'_ vc) = _dt cO._ Ve _+,.c1._ Ve + _c2._ Ve + ...



(2.6)


(2.7)



Thus the coefficients _cO,c1, c2, ..._ should not be mistaken for a polynomial representation of the charge _q._ _._


**44** 2 CIRCUIT ELEMENT AND NETWORK DESCRIPTION


_EXAMPLE_ 2.2

```
      CI 3 5 POLY IN 75P 200F

```

The value of C 1 is evaluated for every new value of _Vc_ across the capacitor according to Eq. 2.6:


_cvalue_ = 10- [9] + 75 . _1O-12vC_ + 200. _1O-15v~_ + ... farad


**2.2.4** **Semiconductor Capacitor (SPICE3)**


SPICE3 supports an extension of the general capacitor element to allow for a convenient
description of the capacitance of a planar diffused region from geometric and process
information.
The general form of a semiconductor capacitor statement is


_Cname node} node2 <cvalue><Mname><L=L><W=_ _W><IC_ = _Vco_ _>_


If _cvalue_ is specified, this statement is equivalent to the general capacitor statement and
any information following the value is discarded except the initial value. If _Mname_ is
specified, the capacitance is calculated from the process information in model _Mname_
and the given length, _L,_ and width, _W._ Note that if _cvalue_ is not specified, _Mname_ and
_L_ must be provided; _W_ assumes the default value in the model if not specified. Also
note that either _cvalue_ or _Mname, L,_ and _W_ may be specified, but not both.
A model type C statement must be used in order to define the parameters listed in
Table 2.2. The capacitance is'computed as follows:



_cvalue_ = _CJ(L - NARROW)(W_ _- NARROW)_
+ 2 . _CJSW(L_ + _W -_ 2 . _NARROW)_



(2.8)



_EXAMPLE_ 2.3

```
CDIFF PDIFF, 0 PCAP L=5U W=5U
.MODEL PCAP C CJ=IOOU CJSW=IN

```

**Table 2.2** Semiconductor Capacitor Model Parameters


**Name** **Parameter** **Units** **Default** **Example**

CJ Junction bottom capacitance Fm- [2] 5E-5
CJSW Junction sidewall capacitance Fm- [1] 2E-ll
DEFW Default device width m 10- `[6]` 2E-6
NARROW Narrowing due to side etching m 0.0 lE-7


TWO-TERMINAL ELEMENTS **45**


The above statements define a diffused capacitor between node PDIFF and node
0, with a value computed according to Eq. 2.8:


_cvalue_ = 10- [4] . 5 . 10- [6 ] . 5 . 10- [6] F + 2 . 10- [9 ] . (5 + 5) . 10- [6] F = 22.5 iF


Note that node names are accepted in SPICE3.


**2.2.5** **Inductors**


The general form of an inductor statement is

_Lname node] node2 lvalue_ <IC = _iLO_ _>_


The L in the first column identifies an inductor labeled _Lname_ and connected between
nodes _node]_ and _node2_ of the circuit, as shown in Figure 2.3.
The BCE of an inductor is


_diL_
_VL_ = _lvalue'_ _dt_ (2.9)


_lvalue_ is the inductance in henries and represents the proportionality constant between
the voltage across the inductor and the rate of change of the current through the inductor.
The integral variant of Eq. 2.9 is used in SPICE to model the inductor:

_lL_ . = _-I-I -_ 1 _It_ _VL_ _d_ _t_ + _lLO._ (2.10)
_va ue_ 0


**IC** is optional and is used to input the initial (time _t_ = 0) inductor current, _iLO'_
This value is used at _t_ = 0 only when **UIC** is specified in the • **TRAN** statement, as
described in Chap. 6.


_Examples_
```
      LXTAL 5 6 0.8
      LSHUNT 23 51 lOU IC=15.7M

```

The statements presented so far describe linear inductors characterized by the constant inductance _lvalue._ SPICE2 also supports nonlinear inductors the inductance of


_no~e2_


_lL~_ _Lname_
_V_ _L_


**Figure** 2.3 Inductor model.


**46** 2 CIRCUIT ELEMENT AND NETWORK DESCRIPTION


which is a nonlinear polynomial function of the current _iL._ The general form of a nonlinear inductor statement is

_Lname node] node2_ **POLY** _ZO_ _II_ < _12 ..._        - <IC = _iLO>_


The keyword **POLY** identifies the inductor _Lname_ as nonlinear and the values _ZO,_
_ll, ..._ as the coefficients of the corresponding powers of _iL._ At least one other coefficient must be specified besides _ZO._ The value of this inductor is computed at each time
point as



_lvalue_ = _to_ + _II ._ _iL_ + _12 . if_ + ...


The BCE for the nonlinear inductor becomes


_VL_ = ~~ = _:t(lvalue'iL)_ = _:t(ZO'iL+ll'if+12'it+_ _... )_



(2.11)


(2.12)



The coefficients _to, ll, 12, ..._ are the coefficients for a polynomial representation
not of the magnetic flux _<p_ but of the inductance.


_EXAMPLE_ 2.4

```
      LPAR 21 0 POLY 0 5M 1

```

The BCE for inductor LPAR is obtained from Eq. 2.12:


_VL_ = _:t_ (0.005 . _if_ + _it)_


which is solved at each time point.


**2.2.6** **Independent** **Bias and Signal Sources**


Voltage and current sources that are independent of any circuit variables are defined by
the following general statements:


_Vname node] node2_ < <DC> _devalue>_ <AC _<ac...mag <aephase>_        - >
_+_ _<TRAN_junction_ _<value]_ _<value2_ _..._ »>

_Iname_ _node] node2_ «DC> _devalue>_ <AC _<ac...mag <aephase»>_
_+_ _<TRAN_junction_ _<value]_ _<value2_ _..._ »>


The V and the I in the first column identify a voltage source and a current source,
respectively, connected between nodes _node]_ and _node2._ The polarity conventions are
shown in Figure 2.4. The _devalue_ is the voltage difference between nodes _node1_ and


TWO-TERMINAL ELEMENTS **47**


_**Vname**_ _Iname_


**Figure 2.4** Independent voltage and current sources.


_node2_ for a voltage source and the current flowing from node _nodel_ to node _node2_
through the source for a current source.
The voltage across the terminals of a voltage source is independent of the current
flowing through it. Likewise, the current Bowing through a current source is independent of the voltage across its terminals.
Independent sources are used to describe biases and signals for the three analytic
modes of SPICE: DC, transient (time-domain), and small-signal AC.1f a source definition contains no other information except the name and the nodes, the program assumes
a DC source of value O. . .


_EXAMPLE_ 2.5


vee `10` `0 DC` `5`
IE 0 1 lOU
IBl 1 0 -'lOU
```
VMEAS 4 5

```

All four statements define DC sources. The keyword DC is not necessary for defining the DC value of vee and is used mostly for clarity when a lot of information is
present on the source line. The current _IB_ flows from ground into node 1 of source lB.
I B 1 is identical to I B since both the order of the nodes and the sign of the current have
been changed. VMEAS is a zero-value.voltage source used in SPICE to measure currents
(see also Chapter 4). The DC value of a source remains constant during a transient analysis if no other information is provided.


_acmag_ and _acphase_ are the magnitude and phase in degrees of an AC smallsignal voltage or current. These values must be preceded by the keyword **AC** and are
used only in conjunction with an AC analysis request, described in Chapter 5. If the
keyword **AC** is alone, a magnitude of 1 and a phase of 0 are assumed by the program.
The value of the _transfer function_ at any point in the circuit referred to the input
can be obtained by monitoring an AC voltage or current. The input _Vin(jw)_ is defined
by the AC source. The output variables computed by the program, such as _Vout(j_ _w),_ are


48 2 CIRCUIT ELEMENT AND NETWORK DESCRIPTION


identical to the transfer function, _T(jw),_ if the input signal has a magnitude of 1 and
phase of 0:



since



_Vout(jw)_ = _T(jw)Vin(jw)_ = _T(jw)_


_Vin(jw)_ = _ac-mag'_ exp(j . _ac-phase)_ = 1



(2.13)


(2.14)



For the large-signal time-domain analysis, SPICE supports five types of timedependent signals: pulse, exponential, sinusoidal, piecewise linear, and single-frequency
frequency modulated. The _TRAN -function_ specification in a source statement contains
a keyword that identifies one of the five functions and a set of parameters. In the following description of the five functions, the parameters and their defaults are specified.


2.2.6.1 Pulse Function
The general format of the _TRAN -function_ specification of the source statement is


PULSE _(Vi V2 <TD <TR <TF <PW <PER»»»_


where the seven parameters have the meanings shown in Figure 2.5 and described in
Table 2.3. The order of the values following the _TRAN_function_ is essential for the correct specification of the signal characteristics. The parameters must be input in the given
order. The initial and pulsed values, _Vi_ and _V2,_ must be specified. If no values follow
the function name, SPICE2 and SPICE3 perform the simulation and do not flag an error; PSpice, however, announces an error and aborts the analysis. The rest of the values,
_TD_ through _PER,_ need not be input, but all values preceding the last nonzero parameter must be specified. The default values listed in Table 2.3 are used for unspecified
parameters and are related to _TSTEP_ and _TSTOP_ of the transient analysis introduced
in Chap. 1 and described in detail in Chap. 6; _TSTEP_ is the output resolution of the
waveforms, or time step, and _TSTOP_ is the end of the time interval.


Amplitude, V or A


Time, S

```
                      PER

```

Figure 2.5 SPICE PULSE source function.


TWO-TERMINAL ELEMENTS **49**



**Table** 2.3 Pulse Source Parameters



**Default**


0.0
0.0
0.0
_TSTEP_
_TSTEP_
_TSTOP_
_TSTOP_



**Units**


VorA
VorA
s
s
s
s
s



**Name**


VI
V2
TD
TR
TF
PW
PER


_EXAMPLE_ 2.6



**Parameter**


Initial value
Pulsed value
Delay time
Rise time
Fall time
Pulse width
Period


```
VD 3 0 PULSE (1 -1 1U)
IKICK 0 2 PULSE (0 1M 1U 0 0 2U)
VIN 1 0 PULSE (0 5 0 IN IN 99N 200N)
VSAW 3 4 PULSE (0 1 0 IOU IOU O.lU 20.1U)
```

The waveforms generated by the four statements are shown in Figure 2.6. The
**PULSE** source can describe a step function, such as VD, a single pulse, such as IKICK,
or a periodic signal, such as VIN and VSAW. VIN is a rectangular signal, and VSAW a
sawtooth. For a step function neither _PW_ nor _PER_ need to be specified, and for a single
pulse _PER_ must not be specified.
The DC value of each of the above sources is equal to the initial value of the pulse.
Neither SPICE2 nor PSpice accepts a DC value different from the first value of the
PULSE function. SPICE3, however, allows the user to define a DC value different from


1.0V

0

-1.0V

~ 1.0mA

<.:>
52
OmA


5.0V
z
:>
ov


~ 1.0V
«
_en_

- ov

5 10


Time, IlS


**Figure 2.6** Sample **PULSE** source functions.


50 2 CIRCUIT ELEMENT AND NETWORK DESCRIPTION


the starting value _VI_ of the PULSE function. In the absence of _devalue,_ a warning
message is output stating that the time zero value is used for DC.
The step function described by VD does not need any additional information besides
the initial and pulsed values and the delay time of the step. SPICE uses the defaults of
_TSTEP_ for the fall time and _TSTOP,_ the end of the transient analysis, for the pulse
width.
The single pulse IKICK defines a pulse of 2 fJ-s width and zero _TR_ and _TF._ Due
to the numerical integration algorithm used by SPICE, explained in more detail in
Chap. 9, a voltage or current change in zero time can cause the solution not to converge. Therefore, the program substitutes the default value, _TSTEP_ for _TR_ and _TF._
Values smaller than _TSTEP_ can be specified for _TR_ and _TF,_ but the faster rise and fall
times cannot be seen on the line-printer plot.
For the sawtooth voltage source, VSAW, the pulse width, _PW,_ should be zero.
SPICE, however, does not accept a zero value for _PW_ and replaces it by the default
value, _TSTOP._ Thus a value one or two orders of magnitude smaller than _TR_ and _TF_
needs to be specified.


2.2.6.2 Sinusoidal Function
The general format of the sinusoidal function in the source statement is


_SIN(VO_ _VA <FREQ_ _<TD <THETA»»_


where the five parameters are illustrated in Figure 2.7 and described in Table 2.4. The
offset and the amplitude must always be specified; the other values are optional.
The source assumes the offset value _VO_ for times from _t_ = 0 to _t_ = _TD_ and behaves according to the following function for _t_      - _T D:_



_f(t)_ = _VO_ + _VA sin(27TFREQ(t_ _- TD))e-THETA(t-TD)_


Amplitude. V or A



(2.15)



T _VA_

_VA_
###### t
1



_1/FREQ_


_1/THETA_


Figure 2.7 SPICE SIN source "function.



Time. s


**Table 2.4** Sinusoidal Source Parameters



**Name**


VO
```
     VA
```

FREQ
TD
```
     THETA

```

_EXAMPLE_ 2.7



**Parameter**

Offset
Amplitude
Frequency
Delay
Dampingfactor



**Units**

VorA
VorA
Hz
s
```
S-I

```


TWO-TERMINAL ELEMENTS **51**


**Default**


0.0
0.0
_VTSTOP_
0.0
```
   0.0

```

```
VSIN 33 34 SIN(O 1 1MEG)
I2 2 0 SIN (1M .2M 10MEG 1U 1MEG)
veas 5 6 SIN (0 5 lOOK -2.5U)

```

The first example describes a sinusoidal signal of 1 V amplitude, zero DC offset,
and 1MHz frequency. The number of signal periods depends on _TSTOP,_ the length of
the time interval for the transient analysis. A single-period sinusoid independent of the
transient analysis interval can be specified by omitting the frequency. The default for
_FREQ_ according to the parameter table is _lITSTOP;_ in other words, the period is equal
to the time interval of the analysis.
The second example is a current source that supplies a sinusoidal signal of 1 rnA
DC current, 0.2 rnA amplitude, and 10 MHz frequency that is delayed by 1 _f-Ls_ and
decays by a factor of _e,_ equal to 2.73, over 10 periods.
The last source, veas, implements a cosine signal by specifying a negative delay
equal to 2.5 _f-Ls,_ or a quarter of a period. SPICE3 and PSpice allow a negative delay,
but not SPICE2. Therefore, in SPICE2 the signal veas would be a sine wave.
The waveforms produced by the three sources are plotted in Figure 2.8 over a time
interval of 10 _f-L_ s. The number of periods that can be viewed for this interval are 10 for
VSIN, 90 for 12, and 1 for veas.


**2.2.6.3** **Frequency-Modulated Sinusoidal Function**
The general format for a single-frequency frequency-modulated (SFFM) transient
function on a source statement is


**SFFM** _(VO VA <Fe <MDI <FS»»_


The five parameters are defined in Table 2.5. The SFFM source is a special case of a
sinusoidal source; indeed, if only the first three parameters are defined and if they are
identical, the **SIN** and **SFFM** functions produce identical waveforms. The last two parameters differ between the two functions, in one case defining damping characteristics
and in the other, modulation. Note that an SFFM function does not contain any delay.


52 2 CIRCUIT ELEMENT AND NETWORK DESCRIPTION



z
ii5




1 V


-1 V



(J) 5.0V
0
C>

-5.0V


1.2 mA


C\l

O.8mA



2 4



6 8



Time,~s


Figure 2.8 Example SIN source functions.


A signal described by an SFFM function has the following time behavior:


_f(t)_ = _va_ + _VAsin(27TFC'_ _t_ + _MDlsin(27TFS'_ _t))_


_EXAMPLE_ 2.8

```
VIN 3 0 SFFM (0 1 lMEG 2 250K)

```


(2.16)



The above source produces a 1 MHz sinusoid of 1 V amplitude modulated at 250 kHz.
It is shown in Figure 2.9. 

Table 2.5 Frequency-Modulated Sinusoidal Source Parameters



Name


VO
```
VA
FC
```

MDI
```
FS

```


Parameter


Offset
Amplitude
Carrier frequency
Modulation index
Signal frequency



Units


VorA
VorA
Hz


Hz



Default


0.0
0.0
_l/TSTOP_
0.0
_l/TSTOP_


1 V


z
:>


2 4


Figure 2.9 SPICE SFFM source function.



TWO-TERMINAL ELEMENTS 53


6 8



Time, Jls



2.2.6.4 Exponential Function
The general format of the EXP _TRAN_function_ in the source statement is


EXP _(Vi V2 <TDi_ _TAW TD2 <TAU2»)_


where the six parameters are as illustrated in Figure 2.10 and are described in Table 2.6.
The initial and pulsed values, _Vi_ and _V2,_ must be specified, and the other parameters need not be specified; the defaults listed in the table are used for any missing
parameter values.
The time behavior of an exponential source is described by the following functions
of time _t:_


Amplitude, V or A


Time. S
_TD1_


_TD2_


Figure 2.10 SPICE EXP source function.


54 2 CIRCUIT ELEMENT AND NETWORK DESCRIPTION


Table 2.6 Exponential Source Parameters


Name Parameter Units Default

VI Initial value VorA 0.0
V2 Pulsed value VorA 0.0
TDl Rise delay time s 0.0
TAUl Rise time constant s _TSTEP_
TD2 Fall delay time s _TDI_ + _TSTEP_
TAU2 Fall time constant s _TSTEP_



_Vi_
_v(t)_ = VI(t) = _Vi_ + _(V2 - Vl)(1_ _-_ _e-(t-TDl)/TAUI)_



for 0 ::5 _t::5_ _TDi_
for _TDi_ < _t_ ::5 _TD2_
for _TD2_ < _t_ ::5 _TSTOP_
(2.17)



_{_



_V2(t)_ = VI _(t)_ + _(Vi_ _- V2)_ (1 - _e-_ _[U]_ _-_ _[TD2]_ _)/TAU2)_



_EXAMPLE_ 2.9

```
VEXP 1 0 EXP (0 5 0 1U 1)
IDEC1 3 1 EXP (1M 0 0 0 0 1U)

```

The first source, VEXP, represents an exponential signal that rises from 0 to 5 V
with a time constant of 1 J-Ls.The last value, 1, on the VEXP line is necessary for defining
the delay _TD2_ before the source starts decaying; by default the value of _VEXP_ would
start to fall after _TSTEP_ seconds.
The second source, IDEC1, is intended to be a current that exponentially decays
from 1 rnA to 0 with a time constant of 1 J-Ls.Note that since the initial value, _Vi,_ of
IDECl is larger than the pulsed value, _V2,_ the meanings of rise and fall are reversed;
that is, _TDi_ and _TAUl_ become the fall delay and time constant, respectively, and _TD2_
and _TAU2_ become the rise delay and time constant, respectively. This is why after a
short decay with a time constant equal to _TSTEP,_ until _TD2_ = _TSTEP,_ the current
resumes increasing back towards 1 rnA with a time constant equal to 1 J-Ls.Thus, the
correct definition of a decaying current is the following:

```
IDEC2 3 1 EXP 1M 0 0 1U 1

```

Note that a large value, 1 second, must be specified for _TD2;_ otherwise the current may
start increasing before the end of the analysis interval _TSTOP._ The three waveforms
are plotted in Figure 2.11, where _TSTEP_ = 0.1 J-LS.


2.2.6.5 Piecewise Linear Function
The general format of a piecewise linear function on a source statement is

PWL (tl _VI_ < _t2 V2_ < _t3 V3 ..._ »)


TWO-TERMINAL ELEMENTS **55**



a-x
U.J



()
U.J
9



4V


OV


1 mA


OmA



Time, J.Is


**Figure 2.11** Example **EXP** source functions.


The parameters for this function are time-value coordinates. The signal described by a

**PWL** statement is formed of straight lines that connect the pairs of coordinates _(ti, Vi)._
There is no limit to the number of coordinate pairs specified. This type of function is
useful for describing sequences of pulses.
Neither _tl_ nor the last defined time needs to coincide with the transient analysis
limits, 0 and _TSTOP._ If _tl_ - 0, the first coordinate pair assumed by SPICE is (0, _VI);_
if the time of the last coordinate pair, _tn,_ is greater than _TSTOP,_ the source assumes the
last value, _Vn,_ at _TSTOP_ in SPICE2. SPICE3 and PSpice interpolate the source value
at _TSTOP:_


_TSTOP - tn-I_
_V(TSTOP)_ = _Vn-I_ + _-----(Vn_ _- Vn-d_
_tn - tn-I_


_**EXAMPLE 2.10**_

```
IBITl 1 0 PWL (0 0 lU 0 1.lU 1M 2U 1M 2.1U 0 4U 0 4.1U 1M 5U 1M
```

+ `5.1U 0 7U 0 7.1U 1M 8U 1M 8.1U 0)`
```
VDATA 21 0 PWL (0 0 0.2U 5 3U 5 3.2U 0 6U 0 6.2U 5)

```

The two waveforms are shown in Figure 2.12; IBITl preserves its last specified value,
0, from 8.1 JLS through _TSTOP,_ equal to 10 JLS. Both IBITl and VDATA are specified
with finite rise and fall times; note that SPICE does not accept more than one **PWL** source
value for a given time point.


56 2 CIRCUIT ELEMENT AND NETWORK DESCRIPTION


« 5.0V
f-«
0

    - OV


1.0mA


f~


OmA


Time, !is


Figure 2.12 PWLfunctions.


2.3 **MULTITERMINAL** **ELEMENTS**


SPICE2 supports the following types of multiterminal elements:


Mutual inductors (linear and nonlinear)

Controlled sources (linear and nonlinear)

Transmission lines (linear)

Bipolar and field effect transistors (nonlinear)


In addition to the above element types, SPICE3 contains models for:


Switches

Uniformly distributed RC lines

Lossy transmission lines


In PSpice the switch and the lossy transmission line are also supported.
This section covers multi terminal elements with the exception of semiconductor elements, which are treated separately in Chap. 3. The elements presented in this section,
generally, require only simple specifications.


2.3.1 **Coupled** **(Mutual)** **Inductors**


The general format of a coupled inductors statement is

_Kname Lnamel Lname2 k_


K in the first column identifies a mutual inductance specification between the two inductors _Lnamel_ and _Lname2,_ defined somewhere else in the input file. _k_ is the coefficient
of coupling, which must be greater than 0 and less than or equal to 1. See Figure 2.13.


MULTITERMINAL ELEMENTS **57**


_**EXAMPLE 2.11**_


The SPICE specification of two coupled inductors L1 and L2 is

```
L1 121M
L2 4 3 1M
KL1L2 L1 L2 .99

```

The polarity of coupling between the two inductors is defined by the position of the dots
as shown in the schematic representation in Figure 2.13. Note that the positive inductor
node, containing the dot, must be defined first on the inductor statement. The value of
the mutual inductance _M_ is computed as


_M_ = _kJL]L2_ (2.18)


where _k_ is the coupling coefficient and _L]_ and ~ are the inductances., The mutual inductance of the coupled inductors is _M_ = .99 mHo


The BCEs of coupled inductors in SPICE are


(2.19)


Systems of coupled inductors are not limitt;d to two and can be extended to a multitude
of inductor pairs. The above equations must be modified accordingly to include all
mutual inductances and terminal pairs. . .


_**Kname**_


**Figure 2.13**
Coupled inductors.


**58** 2 CIRCUIT ELEMENT AND NETWORK DESCRIPTION


Coupled inductors can be used to model an _ideal transformer_ in SPICE. An ideal
transformer has two pairs of terminals, the primary, with _N_ _1_ turns, and the secondary,
with _N2_ turns, and the voltages and currents obey the following relations:


(2.20)


(2.21)


_**EXAMPLE 2.12**_


Write the SPICE2 input for a transformer that has _turns ratio_ _NdN1_ = 5 and whose
primary has self-inductance _L1_ = 1 mHo


_**Solution**_
First calculate the inductance of the secondary knowing that the inductance is proportional to the square of the turns:


_L2_ = _N2)2N_ _Ll_ = 25 mH (2.22)
_(_ _1_


The coupling coefficient for an ideal transformer is 1, and therefore the SPICE2 input
specification for the transformer is the following:

```
      LPRIM 121M
      LSEC 3 4 25M
      KXFRMR LPRIM LSEC 1

```

ote that PSpice restricts the value of _k_ to less than 1. Additionally, PSpice and other
'-¥ commercial SPICE versions, such as SpicePLUS, implement a nonlinear magnetic core
~ model.

G


**2.3.2** **Dependent (Controlled) Sources**


Dependent sources, also known as controlled sources, supply voltages or currents that
are functions of voltages or currents in other parts of the circuit. SPICE supports four
types of dependent sources, a _voltage-controlled current source, VCCS; a voltage-_
_controlled voltage source, VCVS; a current-controlled current source, CCCS;_ and a
_current-controlled voltage source, CCVS._ Dependent sources are useful for implementing a variety of large-signal input/output transfer functions (Epler 1987).


MULTITERMINAL ELEMENTS **59**


SPICE supports both linear and nonlinear dependent sources. A linear controlled
source has two ports, and the output is equal to the input, or controlling variable, times a
proportionality constant. A nonlinear controlled source is limited to a polynomial function of an arbitrary number of circuit variables in SPICE2. SPICE3 and PSpice accept
an arbitrary nonlinear function of both voltages and currents in the circuit; see Sec.
7.4.1 and Sec. 7.4.4.
The general format of dependent sources is


_CSname node+ node-_ _<POLY(ndim»_ _CTRLname/nodes_ _Po_ < PI < _pz ... »_


For a linear source only the information outside the brackets is specified. _CTRLname/_
_nodes_ is a pair of nodes for voltage-controlled sources or a voltage source name that
measures the controlling current for current-controlled sources. _Po, PI, pz, ..._ are coefficients for the polynomial description. Only SPICE2 and PSpice recognize the **POLY**
specification. The four types of dependent sources are as follows:


VCCS G _Ie_ = _GVe_ linear
_Ie_ = _g(Vc)_ nonlinear

VCVS E _VE_ = _EVe_ linear
_VE_ = _e(Vc)_ nonlinear

CCCS F _IF_ = _FIe_ linear
_IF_ = _f(lc)_ nonlinear

CCVS H _VH_ = _HIe_ linear
_VH_ = _h(lc)_ nonlinear


The different types listed next to the four kinds of controlled sources represent the identification character on an element statement; the symbols and controlling elements are
shown in Figure 2.14. A nonlinear source can depend on more than one current or voltage. In SPICE3 only linear controlled sources are identified by **G, E, F,** or H; all types
of nonlinear controlled sources have B as the first character of the element name.
The sequence of values in the dependent source statement is a function of the number of dimensions of the polynomial. Let _Po, PI, Pz, ..._ on the dependent source statement denote polynomial coefficients, _Xl, Xz, x3_ be three controlling variables, and _f (x)_
be the dependent polynomial function.
The one-dimensional polynomial _(ndim_ = 1) is the default in SPICE2, and neither the keyword **POLY** nor _ndim_ needs to be specified. The input values represent the
following coefficients:


(2.23)


An exception to the above assignment of coefficients is made when only one value
appears on the source statement. In this case that value becomes the coefficient of the
linear term, Xl . Thus, a linear controlled source statement is a special case of the general
**POLY** statement, with all optional fields deleted and only one coefficient given.


`60` 2 CIRCUIT ELEMENT AND NETWORK DESCRIPTION


_nc+~+_ `11-` _nc+o---_ _+_ `11+`


_Vnc_ _+,_ _nc-_ _Vnc+,nr_


_llC-O---_ _-_ `11+` _nc-e>--- -_ `11-`
G E

```
                               + 11- + 11+

```

F H


Figure 2.14 Dependent sources.


_EXAMPLE_ 2.13

```
        G1 3 2 1 2 1E-3
        G1 3 2 POLY(l) 1 2 1E-3
```

G2 5 6 3 4 10M 1M (SPICE2)
`G2 5 6 VALUE` = `(O.Ol+lE-3*V(3,4)}` (PSpice)


The first two statements represent the same VCCS, or transconductance, of a current of 1 rnA flowing from mode 3 through the source to node 2 and controlled by the
voltage, _VI.2,_ between nodes 1 and 2:


The above discrepancy in the meaning of _Po_ has been deliberately chosen for onedimensional polynomial sources, because in this way the general nonlinear dependent
source statement takes the particular form of a linear controlled source for _ndim_ = 1.
The second statement is rejected by SPICE3.
The third example, 82, is interpreted like a regular polynomial source in SPICE2
but causes an error in PSpice. The fourth statement represents the preferred syntax for
PSpice; the third statement is accepted by PSpice ifthe keyword POLY (1) is included.
82 must be described by a B statement in SPICE3 (see Sec. 7.4.1). The value of 82 is
evaluated according to the following equation:


MULTITERMINAL ELEMENTS **61**


A two-dimensional polynomial function is expressed as


_f_ _(x],_ _X2)_ = _Po_ + _PIX]_ + _P2X2_ + _P3XI_ + _P4X]X2_
```
                   23223
```

_+_ _P5_ _[X]_ _2_ + _P6_ _[X]_ _]_ + _P7_ _[X]_ _]X2_ + _P8_ _[X]_ _]X2_ + _P9_ _[X]_ _2_ (2.24)


A three-dimensional polynomial function assigns the values on the source statement to coefficients in the following order:


_f(x],_ _X2, X3)_ = _Po_ + _PIX]_ + _P2X2_ + _P3X3_ + _P4XI_ + _P5X]X2_ + _P6X]X3_
```
                  2 2 3 2
```

_+_ _P7_ _[X]_ _2_ + _P8_ _[X]_ _2_ _[X]_ _3_ + _P9_ _[X]_ _3_ + _PIOX]_ + _PllX]X2_
_+_ _P12_ _[X]_ _I_ _[X]_ _3_ + _P13X]X~_ + _P]4X]X2X3_ + _P]5X]X~_

_+_ _p]6_ _[X]_ _i_ + _P17X~X3_ + _P]8X2X~_ + _P]9X~_ + ... (2.25)


Controlled sources are useful for emulating analog and digital circuit blocks, such
as gain stages, operational amplifiers, converters, and many others.


**2.3.2.1** **Voltage-Controlled Current Source** (VCCS)
The general format of a linear VCCS is


_Gnamen+ n- nc+ nc- gvalue_


A G in the first column followed by up to seven characters and digits define the unique
name of a VCCS. _n+_ and _n-_ are the nodes between which the current source is connected, with current flowing from the positive node, _n+,_ through the source to the negative node, _n-_ (see Figure 2.14). The positive and negative controlling nodes are _nc+_
and _nc-,_ respectively; the voltage difference _Vnc+,nc-_ is the controlling variable. The
BCE of a VCCS is


_Ie_ = _gvalue . Vnc+,nc-_ (2.26)


where _gvalue_ is the transconductance in mhos. The linear VCCS is only a special case
of the more general nonlinear VCCS.
The general format of a nonlinear VCCS is


_Gnamen+ n-_ <POLY( _ndim)_  - nc1 + _nc1-_ < _nc2+ nc2- ..._  _+_ _Po_ < _p]_ < _P2 ..._  - > <Ie = _Vnc1 +,nc1-,_ _Vnc2+,nc2-,_ _..._  

The first difference between this statement and that of a linear VCCS is the keyword
**POLY,** which can be present only when a nonlinear VCCS is specified; _ndim_ is the number of controlling voltages, and _nc_ 1 + and _nc_ 1- are the terminals of the first controlling
voltage. The second difference is that for each additional controlling voltage a pair of
controlling nodes, _nc2+, nc2-,_ must be specified. The coefficients _Po, PI,_ _P2,_ _..._ take
the meaning described above depending on the number of controlling variables. The


**62** 2 CIRCUIT ELEMENT AND NETWORK DESCRIPTION


third difference from the statement for a linear VCCS is that initial conditions can be defined for the controlling voltages. These values are used only in conjunction with the **ure**
option in the • **TRAN** statement to initialize the controlled source at the first time point.
If no initial values are present, the controlling voltages are assumed to be zero, if the
**ure** option is chosen, or equal to the resulting value from the DC bias point otherwise.


_**EXAMPLE 2.14**_

```
      GRPOLY 17 3 POLY (1) 17 301M 1. 5M IC=2
      G2DIM 23 17 POLY (2) 3 5 1 201M 17M 3.5U IC=2.5,1.3

```

The first example represents a nonlinear conductance, because the terminal nodes
of the controlled current source are identical with the nodes of the controlling voltage.
The BCE of the nonlinear conductance GRPOLY is


_Ie_ = 0.001, _Ve_ + 0.0015 . _V~_

**In** a transient analysis, at _t_ =0 the terminal voltage, _Ve_ is 2 V, because the **re** keyword
and initial value are present on the GRPOLY line. Note that the keyword **POLY** is needed
in PSpice for a one-dimensional source, but not in SPICE2.
The second example is a two-dimensional nonlinear VCCS of value


_Ie_ = 0.001, _V3,S_ + 0.017, _V_ _I,2_ + 3.5 . _1O-_ _[6V]_ _ts_


**In** a transient analysis that starts from initial conditions (that is, when the **ure** flag is
on), the two controlling voltages are initialized to 2.5 V and 1.3 V; see Chap. 6 for
details.


**2.3.2.2** **Voltage-Controlled Voltage Source** (VCVS)
The general format of a linear VCVS is


_Ename n+ n- nc+ nc- evalue_


An E in the first column followed by up to seven characters and digits defines the unique
name of a VCVS. _n+_ and _n-_ are the positive and negative nodes of the voltage source,
respectively, as shown in Figure 2.14. _nc+_ and _nc-_ are the positive and negative controlling nodes, respectively; the voltage difference _Vnc+,nc-_ is the controlling variable.
The BeE of a VCVS is


_V_ _E_ = _evalue'_ _Vnc+,nc-_ (2.27)


where _evalue_ is the voltage gain. The linear VCVS is only a special case of the more
general nonlinear VCVS.


MULTITERMINAL ELEMENTS **63**


The general format of a nonlinear VCVS is


_Ename n+ n-_ <POLY _(ndim)_   - _nel_ + _ne1-_ _<ne2+_ _ne2-_ _..._   
_+_ _Po_ < _PI_ < _P2 ..._   - > <IC= _vllcl_ +.Ilcl-, _Vllc2+.llc2-,..._   

The keyword **POLY** must be present when a nonlinear VCVS is specified; _ndim_ is the
number of controlling voltages. ncl + and _ncl-_ are the terminals of the first controlling
voltage; for each additional controlling voltage, a pair of controlling nodes, _ne2_ +, _ne2 -,_
must be specified. The coefficients _Po, PI, P2, ..._ take the meaning described above
depending on the number of controlling variables. **IC** is optional and defines the initial
values of the controlling voltages; these values are used only in conjunction with the
**UIC** option in the • **TRAN** statement to initialize the controlled source at the first time
point. If no initial values are present, the controlling voltages are assumed to be zero,
if the **UIC** option is chosen, or equal to the resulting value from the DC bias point
otherwise.


_**EXAMPLE**_ **2. 15**

```
E1 3 4 POLY (1) 21 17 10.5 2.1 1.75
ESUM 17 0 POLY(3) 1 0 2 0 3 0 0 1 1 1 1C=1,2,3

```

The first example, E 1, defines a nonlinear voltage gain function


_VE_ = 10.5 + 2.1, _V21.17_ + 1.75. _Vh17_


The second example represents a voltage summer, since the value of the controlled
source ESUM is the sum of _Vl,O,V2.0,_ and _V3.0._


_Exercise_
Run an AC analysis of the voltage summer ESUM using SPICE and verify if this VCCS
still performs the add function. Use different values for _VI.o, V2.0,_ and _V3.0._ For an explanation of the result, see Chaps. 5 and 7.


**2.3.2.3** **Current-Controlled Current Source** (CCCS)
The general format of a linear CCCS is


_Fname n_ + _n - Vname fvalue_


An F in the first column followed by up to seven characters and digits defines the unique
name of a CCCS. _n+_ and _n-_ are the positive and negative nodes of the current source,
and current flows from the positive node through the source to the negative node (see
Figure 2.14). _Vname_ is the voltage source through which the controlling current flows.


**64** 2 CIRCUIT ELEMENT AND NETWORK DESCRIPTION


_I(Vname)_ is the controlling variable. The BCE of a CCCS is


h = _fvalue_ _'I(Vname)_ (2.28)


where _fvalue_ is the current gain. The linear CCCS is only a special case of the more
general nonlinear CCCS.
The general format of a nonlinear CCCS is

_Fname n+n-_ <POLY _(ndim»_ _Vname1_ _<Vname2_ _..._       - _Po <PI <P2 ... »_
+ <IC = _i(Vnamel),_ _i(Vname2)_ _..._     

The keyword **POLY** must be present when a nonlinear CCCS is specified; _ndim_ is the
number of controlling currents. _Vnamel_ is the voltage source measuring the first controlling current; for each additional controlling current a voltage source must be specified. The coefficients _Po, PI, P2, ..._ take the meaning described above depending on
the number of controlling variables. **IC** is optional and defines the initial values of the
controlling currents; these values are used only in conjunction with the **UIC** option in
the • **TRAN** statement to initialize the controlled source at the first time point. If no initial
values are present, the controlling currents are assumed to be zero if the **UIC** option is
chosen, or equal to the resulting value from the DC bias point otherwise.


_**EXAMPLE 2.16**_

```
      FCON 13 4 POLY (1) VC1 0.001 1E-4 1E-5
      F2 2 3 POLY (2) VCON1 VCON2 0 0 0 0 1

```

FeON defines a current that is a quadratic function of the current flowing through
the voltage source ve 1:


. The current of F2 is equal to the product of the currents flowing through voltage sources
. veONl and veON2.


_Exercise_
Replace transistor QI in Example 1.2 with a CCCS connected from collector to emitter
having value _fvalue_ = _Ih_ = 100 and controlled by the current _iRB,_ and show that
the bias point obtained by SPICE is close to the one obtained in Chap. 1. Explain the
difference and modify the circuit to obtain the same answer.


**2.3.2.4** **Current-Controlled Voltage Source** (CCVS)
Th~ general format of a linear CCVS is


'~
_•Hname n_ + _n -_ _Vname hvalue_


MULTITERMINAL ELEMENTS **65**


An Hin the first column followed by up to seven characters and digits defines the unique
name of a CCVS. _n_ + and _n-_ are the positive and negative nodes of the voltage source,
as shown in Figure 2.14. _Vname_ is the voltage source through which the controlling
current flows. _I(Vname)_ is the controlling variable. The BCE of a CCVS is


_V_ _H_ = _hvalue' I(Vname)_ (2.29)


where _hvalue_ is the transresistance in ohms. The linear CCVS is only a special case of
the more general nonlinear CCVS.
The general format of a nonlinear CCVS is

_Hname n+ n-_ <POLY _(ndim)_       - _Vnamel <Vname2 ..._       - _Po <PI <pz ... »_
+ <IC = _i(Vnamel), i(Vname2) ..._ _>_


The keyword **POLY** can be present only when a nonlinear CCVS is specified; _ndim_ is
the number of controlling currents. _Vnamel_ is the voltage source measuring the first
controlling current; for each additional controlling current a voltage source must be
specified. The coefficients _Po,PI, pz, ..._ take the meaning described above depending on the number of controlling variables. **IC** is optional and defines the initial values of the controlling currents; these values are used only in conjunction with the
**OIC** option in the • **TRAN** statement to initialize the controlled source at the first time
point. If no initial values are present, the controlling currents are assumed to be zero
if the **OIC** option is chosen, or equal to the resulting value from the DC bias point
otherwise.


_**EXAMPLE 2.17**_

```
       HRNL 1 2 POLY (1) V12 0 0 1
       HXY 13 20 POLY(2) V1N1 V1N2 0 0 0 1 -2 1 10=0.5,1.3

```

The voltage between nodes 1 and 2 of HRNL is equal to the square of the current
flowing through V12, and the value of HXYis equal to the square of the difference of
the currents through voltage sources VINl and VIN2.


**2.3.3** **Switches**


SPICE3 and PSpice support a nearly ideal switch model. An ideal switch has zero ON
resistance and infinite OFF resistance. This behavior can be approximated satisfactorily with ON and OFF resistances that are significantly smaller or larger, respectively,
than the other resistances in the circuit. The switch is therefore a resistor that toggles between a very small value, the ON resistance, and a very large value, the OFF resistance,
-depending on a controlling voltage or current.


`66` 2 CIRCUIT ELEMENT AND NETWORK DESCRIPTION


Voltage- and current-controlled switches have the following general formats:


_Sname n+ n- nc+ nc- Model_ <ON/OFF>
_Wnamen+ n- Vname Model_ <ON/OFF>


where an S in the first column identifies a voltage-controlled switch, a Widentifies a
current-controlled switch, and the flag ON/OFF specifies the initial state of the switch.
The switch is connected between nodes _n_ + and _n-_ and is controlled either by the
voltage between nodes _nc+_ and _nc-_ or by the current flowing from the positive node
to the negative node of the voltage source _Vname. Model_ is the name of the model
statement that contains the parameters of the switch.
There are two types of switch models, SW, the voltage-controlled switch, and CSW,
the current-controlled switch. Each model type defines four parameters, shown in
Table 2.7.
The resistance of the switch as a function of the controlling variable is shown in Figure 2.15. The switch in SPICE3 displays hysteresis, switching at _Vcontrol_ = _VT_ when
_Vcontrol_ is rising and at _VT - VH_ when _Vcontrol_ is falling. _GMIN_ in the table is a minimum
conductance, used in SPICE to protect against an ill-conditioned set of nodal equations;
for other uses of GMIN see Chap. 3, and for modifying it see Chap. 9.
Because switches are highly nonlinear, their use in a circuit can lead to convergence
problems. In order to prevent the failure of the time-domain analysis, that is, in order
to avoid the situation in which the time step is too small (see Chap. 9), _RON_ should be
negligible compared to the smallest resistance and _ROFF_ should be large enough not
to affect the total value when connected in parallel to the largest resistor. It is strongly
recommended that


_ROFF_ < 1012
(2.30)
_RON_ _-_


Another remedy for convergence failure of circuits with switches is the addition of
capacitors across the controlling voltage and inductors in series with the controlling
current, which prevent sudden changes in the controlling variables.



~



Note that the PSpice switch does not have hysteresis. The parameters VT and VH
are replaced by VON and VOFF for an S switch, and IT and IH are replaced by ION
and IOFF for a Wswitch. The interval between the two variables is used to provide for
a smooth transition between _RON_ and _ROFF._


Table 2.7 Switch Model Parameters


Name Parameter Units Default Model

VT Threshold voltage V 0.0 `SW`
IT Threshold current A 0.0 `CSW`
VH Hysteresis voltage V 0.0 `SW`
IH Hysteresis current A 0.0 `CSW`
RON ON resistance n 1.0 `SW,CSW`
ROFF OFF resistance n. _lIGMIN_ `SW,CSW`


Rswitch


_ROFF_


_RON_



MULTITERMINAL ELEMENTS **67**


_`VT`_ **Vcontrol**



**Figure 2.15** Switch resistance as a function of controlling voltage.


_**EXAMPLE 2.18**_


Use switches to model a NOR gate in SPICE3.


_**Solution**_
A straightforward implementation is shown in Figure 2.16; the circuit is equivalent to
the MOS implementation of a NOR gate with the transistors replaced by switches and a
load resistor connected to 5 V. The value of the load resistor is 1 ko'. For best results in
SPICE, _RON_ and _ROFF_ are selected such that they are much smaller and much larger,
respectively, than 1 ko'. The values are _RON_ = 1 0" _ROFF_ = 1 Mo'.


_Vee._

      


_Rs_
_V'l"_ ~1'



_R4_ _V_ _4_




     -      -      **Figure 2.16** NOR gate implemented with switches.


**68** 2 CIRCUIT ELEMENT AND NETWORK DESCRIPTION


The SPICE3 input description is listed below. The controlling terminals, nodes 3
and 4, represent the two inputs of the NOR gate. The two input signals are a sequence
of logic 0 and 1 described as **PWL** voltage sources, introduced in Sec. 2.2.6.5.


NOR GATE WITH SWITCHES
** NOR-GATE

       RL 2 1 1K

Sl 1 0 3 0 SW
```
      S2 1 0 4 0 SW
```

`vee` 2 0 5

** INPUT SIGNALS

       V3 3 0 PWL 0 0 1U 0 1.01U 5 2U 5 2.01U 0 3U 0 3.01U 5

R3 3 0 1

V4 4 0 PWL 0 0 2U 0 2.01U 5

R4 4 0 1

       .MODEL SW SW RON=l ROFF=lMEG VT=1 VH=O

       .TRAN .02U 4U

.PLOT TRAN V(l) V(3) V(4)

. END


_Exercise_
Run this circuit in SPICE3 and study the impact of various values for the hysteresis
width, _VH,_ as well as for different values of _RON_ and _ROFF._ PSpice users must replace
VT and VHwith **VON** and **VOFF** and the model type byVSWITCH;for current-controlled
switches, model type **ISWITCH,** and **ION** and **IOFF** must be specified. See also Chap.
7 for more details on this subject.


**2.3:4** **Transmission Lines**


The general form of a transmission line statement is


_Tname nl n2 n3 n4 ZO=ZO <TD=TD><F=freq_ _<NL=NL»_
_+_ _<IC=Vnl,n2,_ _ii, Vn3,n4, i2_ _>_


A T in the first column identifies a transmission line element, _nl_ and _n2_ are the
nodes at port 1, and _n3_ and _n4_ are the nodes at port 2. A transmission line together with the SPICE equivalent model is shown in Figure 2.17. Only lossless
lines are supported in SPICE2; SPICE3 and PSPICE support also lossy transmission lines. _ZO_ is the characteristic impedance of the line; one additional characteristic


MULTITERMINAL ELEMENTS **69**


_**Tname**_
_n1_ 0---------_0 _n3_


_n2_ 0>----------0 _n4_


_n1_


_n2_


**Figure 2.17** Transmission line and
equivalent model.


must be specified about the line, which can be either the line delay, _TD,_ or the normalized electrical line length, _NL,_ expressed in wavelength units, at a given frequency _jreq._
If only a frequency is specified andNLis omitted, NLdefaults to 0.25; that _is,Jreq_ is the
quarter-wave frequency. The three parameters are described by the following equation:


_TD_ = _NL_
(2.31)
_jreq_


where


_I_
_NL_ =- (2.32)
A


with _I_ the physical length of the line and A the wavelength.
Initial Conditions, **IC,** are optional and consist of the currents and voltages at the
terminals of the two ports. These values are used only in conjunction with the **UIC**
option on the • **TRAN** statement.
The BCEs of the transmission line are expressed as the following functional forms
of the voltage sources _VI (t)_ and _vz(t)_ in the equivalent model (Branin 1967) of Figure
2.17:



_VI (t)_ = _Vn3,n4(t -_ _TD)_ + _20 ._ _iz(t_ _-_ _TD)_

_VZ(t)_ = _Vnl,n2(t_ _-_ _TD)_ + _20._ _iI(t_ _-_ _TD)_



(2.33)


(2.34)



The two equations represent the incident and reflected waves along a lossless transmission line.


**70** 2 CIRCUIT ELEMENT AND NETWORK DESCRIPTION


_**EXAMPLE 2.19**_


The following three definitions ofline Tl are equivalent; see Eq. 2.31 and 2.32.

```
      Tl 1 0 2 0 ZO=50 TD=10N
      T1 1 0 2 0 ZO=50 F=100MEG NL=1
      T1 1 0 2 0 ZO=50 F=25MEG

```

A coaxial cable is described by two transmission lines, the first representing the
inner conductor with respect to the shield, and the second the shield with respect to the
outside world:

```
      TINT 1 2 3 4 ZO=50 TD=1.5N
      TEXT 2 0 4 0 ZO=100 TD=1N

```

Study the difference in the response ofline TLINE to a pulse when terminated with
a load resistor _R_ _L_ of 50 nand 100 n. The SPICE input is listed below:

```
      TRANSMISSION LINE EXAMPLE
```

       ```
      VIN 1 0 PULSE 0 5 0 0.1N 0.1N 5N SON
      RIN 1 2 50
      TLINE 2 0 3 0 ZO=50 TD=10N
      RL 3 0 50
      .TRAN .25N SON
      .PLOT TRAN V(2) V(3)

```

2.5



N:;0
2.5

_cry_
:;0
2.5

N:;0
3.33


_cry_
:;- 0


|Col1|Col2|
|---|---|
|||
|||
|||
|_RL=_ 50n||



|Col1|Col2|Col3|
|---|---|---|
||||
||||
||||
||||
|_RL=100n_|_RL=100n_||


,-, I [,-], I,,,,, .,,-,





10 `20`



30 `40`



Time, ns


**Figure 2.18** Transmission line response for _R_ _L_ = 50 nand _R_ _L_ = 100 n.


SUMMARY **71**


.PRINT TRAN V(2) V(3)

. END


The waveforms at the input and output of TLINE for the two values of the load resistor
_RL_ are shown in Figure 2.18. The difference is that a matched line with _Rin_ = _RL_ = _ZO_
delays the input pulse by _TD_ while the unmatched line reflects the pulse between input
and output with an attenuation corresponding to the values of _Rin, RL,_ and _ZOo_


**2.4** **SUMMARY**


This chapter describes all the elements supported in SPICE with the exception of the
semiconductor devices. Both the syntax and the relation between the branch-constitutive
equations and SPICE statement parameters were explained and exemplified.
First, the two-terminal passive elements, resistor, **R,** capacitor, **C,** and inductor, **L,**
were defined. T~ese elements use the following SPICE syntax:


_Rname nodeI_ _node2 rvalue_ <TC= _tcl,_ _<tc2»_

_Cname nodeI_ _node2 cvalue_ <IC = _Vco_ _>_

_Lname nodeI_ _node2 lvalue_ <IC = ho        

Capacitors and inductors can be also defined as nonlinear, polynomial expressions of
voltage and current, respectively.
Independent voltage and current bias and signal sources can be specified using the
following generic SPICE statement:


_V/Iname_ _nodeI_ _node2_ «DC> _dc_value><AC_ _<acJ11ag <ac-phase»>_
_+_ _<TRAN_function_ _<valueI_ _<value2_ _..._ »>

where _TRANfunction_ can be one of the following:

**PULSE** _(VI V2 <TD <TR <TF <PW_ <PER»»»

**SIN** _(Va VA <FREQ_ _<TD <THETA»»_

**SFFM** _(va_ _VA <Fe_ _<MDI_ _<FS>_       - »

**EXP** _(VI V2 <TDI_ _<TAW_ _<TD2_ _<TAU2»»)_

**PWL** (tl VI _<t2 V2 <t3_ _V3 ..._ »)

For each of the optional parameters SPICE provides default values.
Multiterminal elements supported in SPICE include coupled inductors, controlled
(dependent) sources, switches, and transmission lines. Coupled inductors have the following syntax:


_Kname Lname I Lname2_ _k_


Four types of controlled sources are supported in SPICE, a voltage-controlled
current source, type **G,** a voltage-controlled voltage source, type **E,** a current-controlled


72 2 CIRCUIT ELEMENT AND NETWORK DESCRIPTION


current source, type **F,** and a current-controlled voltage source, type H. A linear dependent source has the following syntax:


_G/Ename node+ node-_ _nc+ nc- value_

_F/Hname node+ node-_ _Vname value_


_Vname_ is the name of the voltage source used to measure the controlling current. Nonlinear polynomial controlled sources use the following general syntax:


_G/E/FlHnamenode+ node-_ _POLY(ndim) Vname/ncnodes_ _Po PI_
_+_ _<P2_ _<P3 ... »_


More complex nonlinear dependent sources supported in SPICE3 and PSpice are defined in Chap. 7.
A nearly ideal switch is implemented in SPICE3 and PSpice; the operation of the
switch can be controlled by a voltage (type S) or a current (type W).The syntax for the
two types of switches is


_Sname n+ n- nc+ nc- Model_ <ON/OFF>

_Wname n+ n-_ _Vname Model_ <ON/OFF>


One or more switch elements reference a **.MODEL** statement that defines the necessary
parameters.
The last element introduced in this chapter is the ideal transmission line defined by
the following statement:

_Tname nl n2 n3 n4_ **Zo** = _ZO_ <TD = _TD>_ <F = _freq_ <NL = _NL> >_
+ < **Ie** = _VnI,n2,_ iI, _Vn3.n4, i2_ _>_


This chapter has detailed all SPICE circuit elements except semiconductor devices,
which are the subject of the following chapter.


**REFERENCES**


Branin, F. H. 1967. Transient analysis oflossless transmission lines. _Proc. IEEE_ 55: 2012-2013.
Epler, B. 1987. SPICE2 application notes for dependent sources. _IEEE Circuits and Devices_
_Magazine_ 3 (September): 36-44.
Ho, C. w., A. E. Ruehli, and P. A. Brennan. 1975. The modified nodal approach to network
analysis. _IEEE Transactions on Circuits and Systems._ CAS-22 (June): 504-509.
Johnson, B., T. Quarles, A. R. Newton, D. O. Pederson, and A. L. Sangiovanni- Vincentelli. 1991.
(April). _SPICE3 Version 3E User's Manual._ Berkeley: Univ. of California.
McCalla, W. J. 1988. _Fundamentals of Computer-Aided Circuit Simulation._ Boston: Kluwer
Academic.
MicroSim. 1991. _PSpice, Circuit Analysis User's Guide, Version 5.0._ Irvine, CA: Author.
Vladimirescu, A., K. Zhang, A. R. Newton, D. O. Pederson, and A. L. Sangiovanni-Vincentelli.
1981 (August). _SPICE Version_ 2G _User's Guide._ Department of Electrical Engineering and
Computer Science, Univ. of California, Berkely.


_**Three**_


_**SEMICONDUCTOR-DEVICE**_
_**ELEMENTS**_


**3.1** **INTRODUCTION**


Semiconductor elements are presented together as a group because they have a common
specification methodology. Unlike the elements described in Chap. 2, semiconductor
elements are defined by complex nonlinear BCEs characterized by a large number,of
.earameters. These parameters are specified in a • **MODEL** statement. As mentioned in the
beginning of Chap. 2, SPICE2 supports four different semiconductor-device models,
and SPICE3 and PSpice accept five different semiconductor devices.
The element statement for any semiconductor device has the following general
format:


The device name _DEVname_ starts with one of four characters **D,** **Q,** **J,** and M corresponding to the four kinds of semiconductor elements accepted by SPICE2, diode, bipolar
transistor (BJT),junction field effect transistor (JFET), and metal-oxide-semiconductor
field effect transistor (MOSFET), respectively. The additional semiconductor device
supported in SPICE3 and PSpice, the metal-semiconductor field effect transistor (MESFET), is identified by a Z in SPICE3 and a B in PSpice. Up to seven characters can
follow to identify the element. Two to four node numbers specify the connection of
the semiconductor element terminals. _MODname_ is the name of a model statement
that contains the parameter values; one or more semiconductor devices can reference
the same model. SPICE2 was initially developed for integrated circuits (ICs), and the
```
                                       73

```

74 3 SEMICONDUCTOR-DEVICE ELEMENTS


commonality of model parameters can be traced back to the common process parameters. Besides the process parameters, which are general model parameters, each semiconductor device has certain geometric characteristics, _valuel,_ _value2,_ and so on, that
are unique and differentiate it from other devices having the same model parameters.
Diodes, BJTs, JFETs, and MESFETs use only one parameter, _area,_ to scale their geometry with respect to a _unit device._ MOSFETs require more detailed geometric information,
such as channel dimensions and areas. More complete geometric information is available
for MOSFETs because of the importance of this device type in LSI and VLSI circuits.
The rest of the information in a semiconductor element statement specifies the initial state of the device. These initial conditions are optional and are seldom used. The
OFF flag is a toggle that initializes the device in the nonconducting state for the DC
solution. The iterative DC solution process assumes that at the start all semiconductor
elements are either conducting or on the verge of conduction. OFF devices are held in
the cutoff state until convergence is reached, at which point the constraint is removed
and iterations continue until the first converged solution is confirmed or a new solution is found. In other words, a device initially assumed to be OFF may tum out to be
conducting at the completion of the SPICE DC solution.
The optional IC specification defines the values of the terminal voltages of a semiconductor device at time zero. This specification is used only in conjunction with a
transient analysis, which precludes the computation of a DC bias solution. The values
defined as part of the IC option are used only when the UIC option is specified in the
•TRAN statement; see Chap. 6. In all other circumstances these values are ignored.
The companion model statement for semiconductor-element statements has the following general format:

•MODEL _MODname_ _MOD type <PARAMl=valuel_ _<PARAM2=value2_ _..._ »


_MODname_ is a unique eight-character name in SPICE2 and a name of arbitrary length
in SPICE3 associated with the parameter values defined in this statement. This name
is referenced by the device statements. _MODtype_ is one of seven recognized device
types in SPICE2 and one of twelve in SPICE3. SPICE2, SPICE3, and PSpice support
the following model types:



D
```
NPN
PNP
NJF
PJF
NMOS
PMOS

```


Diode model

npn BJT model

pnp BJT model

n-channel JFET model

p-channel JFET model

n-channel MOSFET model

p-channel MOSFET model



SPICE3 supports the following additional semiconductor model types:


R Diffused resistor model
c Diffused capacitor model


DIODES 75


URe Uniformly distributed RC model

NMF n-channel MESFET model


PMF p-channel MESFET model


PSpice also has a built-in model for an n-channel gallium-arsenide FET, called a GASFET, and an additional BJT model type for a lateral pnp, called an LPNP.
Four sets of semiconductor parameter names occur in SPICE2, eight in SPICE3, and
five in PSpice. More than one model type can share the same parameters, for example,
npn and pnp bipolar transistors. Only those parameter names must appear on the model
statement that are assigned different values from the defaults built into the program. A
model statement with no values assigns the defaults of the specific type to that model
name. In this chapter each element is described together with its model parameters.
The following sections describe the supported semiconductor elements. The descriptions of both the element and the companion model are presented. The parameters
and supporting equations for the first-order models are introduced. For details on the
semiconductor-device physics underlying the models described in this chapter, several reference texts (Grove 1967; Muller and Kamins 1977; Sze 1981) are suggested.
The complete equations and list of parameters for semiconductor devices are contained
in Appendix A and in more detail in _Semiconductor_ _Device_ _Modeling_ _with SPICE_
(Antognetti and Massobrio 1988).


3.2 **DIODES**


The general format of a diode element statement is

_Dname n_ + _n-_ _MODname_ _<area>_ <OFF> < IC=VDO       

The letter D must be the first character in _Dname;_ D identifies a diode and can be followed by up to seven characters in SPICE2. _n+_ is the positive node, or anode, and _n-_
is the negative node, or cathode. The schematic symbol of a diode is presented together
with its pn-junction SPICE implementation in Figure 3.1.
_M_ 0 _Dname_ is the name of the model defining the parameters for this diode element.
The variable _area_ is a scale factor equal to the number of identical diodes connected in
parallel; _area_ defaults to 1. For the initial iterations of the DC bias solution, the keyword
OFF initializes the diode in the cutoff region; otherwise diodes are initialized at the limit
of tum-on, with _V_ _D_ = 0.6 V, for the DC solution. The keyword IC defines the voltage

VDO at time _t_ = 0 for a time domain analysis. VDO is used as initial value only when the
UIC option is present in the • TRAN statement.
The BCE of the diode in DC is described by an exponential function:


_I_ _D_ = _IS(eqVD/NkT -_ 1) (3.1)


where _IS_ is the saturation current, _N_ is the emission, or nonideality coefficient, and _T_
is the temperature in degrees Kelvin, K. _q_ and _k_ are the electron charge and Boltzmann's


76 3 SEMICONDUCTOR-DEVICE ELEMENTS


n+

```
                         n```

Figure 3.1 Diode element.


constant, equal to 1.6x 10- [19] C and 1.38x 10- [22] JK- [1], respectively; these two constants
and the diode temperature define the _thermal voltage,_ _Vth_ = _kT / q._
The I-V characteristic of the diode described by Eq. 3.1 is shown in Figure 3.2.
The two model parameters, IS and N, can be easily derived as the slope and the intercept at the origin of the log _ID_ versus _VD_ plot, that is, of a semilogarithmic plot of
Eq. 3.1. The breakdown current occurring when the diode is reverse-biased is also modeled if the value of the breakdown voltage parameter, BV, is defined. The current at
the breakdown voltage is set to the value of parameter IBV; see Appendix A for complete equations .
. The variation in time of the diode current of a short-base diode (Muller and Kamins
1977) is controlled by the two types of charge storage in a semiconductor pn junction,
the diffusion charge and the depletion charge.


10- [6]


10- [8]


10- [10]


10- [12]

,,/
_IS_


_(h)_


Figure 3.2 1-V characteristics of a diode: _(a)_ _I_ _D_ versus _V_ _D;_ _(b)_ log _I_ _D_ versus _YD._


DIODES 77


The diffusion charge _QD_ is defined by


_QD_ = _TT._ _ID_ (3.2)
,
where _TT_ is the average transit time of minority carriers through the narrow region of
a short-base diode.
The depletion charge Q] atthe pn junction is stored in a voltage-dependent junction
capacitanc~, _C]:_


_CJO_
(3.3)
C] = (l - _VD/VJ)M_


(3.4)


_CJO, VJ,_ and _M_ are the zero-bias junction capacitance, built-in voltage, and grading
coefficient, respectively.
In the small-signal AC analysis, the diode is modeled as the conductance in the
operating point _gd_ and two capacitances _CD_ and C] corresponding to the two charges,
respectively,


1 _`dID`_
(3.5)
_dV_ _D_


_CD_ = _TT._ _gd_ (3.6)


. two additional parameters needea for a' first-order definition onhe diode model
afe-tl'ie""parasiticseries resistance, **RS,** and the energy gap, EG. The latter is used to
differentiate between different types of diodes, such as silicon pn-junction diodes, other
semiconductor junctions, and Schottky diodes.
The general format 'of the diode model statement is


_.MODELMODnameD_ _<IS=IS_ _<N=N_ _... »_


Table 3.1 summarizes the diode model parameters introduced so far along with the
default values assigned by SPICE2. The scale'factor column indicates whether and
how the parameter is scaled by the factor _area_ appearing in the device statement.


_EXAMPLE_ 3.1


Following are the SPICE descriptions for two diodes.


DIN' 0 1 DMOD OFF

.MODEL DMOD D


`78` 3 SEMICONDUCTOR-DEVICE ELEMENTS


Table 3.1 Diode Model Parameters


Name Parameter Units Default Example Scale Factor

IS Saturation current A 10- [14] IE-16 _area_
N Emission coefficient I 1.5
RS Ohmic resistance n 0 100 _l/area_
TT Transit time s 0 O.IN
CJO Zero-bias junction capacitance F 0 2P _area_
VJ Junction potential V I 0.6
M Grading coefficient 0.5 0.33
EG Activation energy eV 1.11 1.11 Si
0.69 Sbd
0.67 Ge
BV Breakdown voltage V 00 40
lEV Current at breakdown voltage A 10- [3] IOU _area_


DIN describes a protective diode at the input of another device that is normally off.
Only default parameters are used to model DIN.

```
      DSBD 11 17 DS1 IC=O.4
       .MODEL DS1 D IS=lP CJO=O.2P VJ=O.7 M=O.5 EG=O.69

```

The above two statements define a Schottky-barrier diode. The junction is initialized at
0.4 V, the value ofthe voltage drop when conducting; also note that _TT_ = 0, because of
the absence of minority carriers. The value of _EG_ corresponds to an aluminum-silicon
contact.


3.3 BIPOLAR JUNCTION TRANSISTORS


The general form of a bipolar junction transistor (BIT) statement is


_Qname nc nb ne <ns> MODname <area>_ <OFF><IC= _VBEO, VCEO >_


The letter Q must be the first character in _Qname;_ Q identifies a BJT and can be followed by up to seven characters in SPICE2. _nc, nb,_ and _ne_ specify the collector, base,
and emitter nodes, respectively. The fourth number, _ns,_ is the substrate node, and its
specification is optional. If _ns_ is not present, the substrate is assumed to be connected
to ground.
_MODname_ is the name of the model defining the parameter values for this transistor. Two BIT device types are supported, NPN and PNP. The schematic symbols for the
two types of BITs are shown in Figure 3.3.
The scale factor _area_ is equal to the number of identical transistors connected
in parallel; _area_ defaults to 1. The keyword OFF initializes the transistor in the cutoff


BIPOLAR JUNCTION TRANSISTORS **79**


region for the initial iterations of the DC bias solution. By default, BJTs are initialized
in the forward active region, with _VSE_ = 0.6 V and _Vsc_ = -1.0 V for the DC solution.
The keyword **IC** defines the values of the junction voltages, _VSEO_ and _VCEO_ at time _t_ = 0
for the transient analysis. _VSEO_ and _VCEO_ are used as initial values only when the **UIC**
option is present in the • **TRAN** statement.


**3.3.1** **DC Model**


The basic DC model used in SPICE to describe the BCEs of a bipolar transistor is
the Ebers-Moll model (Muller and Kamins 1977). The model shown in Figure 3.4 is
the _injection_ _version_ of the Ebers-Moll model, which uses diode currents _IF_ and _IR_ as
reference:


(3.7)


where the emission coefficients (see Eq. 3.1) have been assumed to equall. The three
terminal currents of the transistor, _Ic, IE,_ and _Is_ can be expressed as functions of the
two reference currents and the forward and reverse current gains, _CXF_ and _CXR,_ of the
common-base (CB) connected BJT:


_Ic_ = _cxFIF - IR_



_IE_ = _-IF_ + _cxRIR_

_Is_ = (1 - _cxF)IF_ + (1 - _cxR)IR_



(3.8)



_IEs_ and _Ics_ are the saturation currents of the BE and BC junctions, respectively. These
two currents satisfy the reciprocity equation


(3.9)


where _IS,_ a SPICE **BJT** model parameter, is the saturation current of the transistor.
The SPICE implementation of the Ebers-Moll model is a variant known as the
_transport_ _version_ and is shown in Figure 3.5. The injection version is commonly documented in textbooks and has been repeated above for comparison with the transport
version. The currents flowing through the two sources, which represent the transistor
effect of the two back-to-back pn junctions, are chosen as reference:


_Icc_ = _IS(eQV8e1NF'kT -_ 1)

(3.10)
_ICE_ = _IS(eQV8c1NR.kT -_ 1)


**80** 3 SEMICONDUCTOR-DEVICE ELEMENTS


**Figure 3.5** Ebers-Moll transport
model of an npn transistor.


BIPOLAR JUNCTION TRANSISTORS 81


The three terminal currents assume the following expressions:


_f3R_ + 1 1
_Ic_ = _Icc_ _-_ _--ICE_ = _ICT -_ _-ICE_
_f3R_ _f3R_



(3.11)



where



_f3F_ + 1 1
_Ie_ = _ICE -_ _---Icc_ = _-ICT_ _-_ _-Icc_
_f3F_ _f3F_


1 1
_IB_ = _f3F Icc_ + _f3R ICE_ = _IBC_ + _IBE_


_ICT_ = _Icc_ _- ICE_



_f3F_ and _f3R_ in the above equations are the forward and reverse current gains, SPICE
parameters BF and BR, of a bipolar transistor in the common-emitter (CE) configuration.
Depending on the values ofthe two controlling voltages, _VBE_ and _VBC,_ the transistor
can operate in the following four modes:



Forward active


Reverse active


Saturation


Cutoff



_VBE_ - 0 and _VBC_ < 0

_VBE_ < 0 and _VBC_ - 0

_VBE_ - 0 and _VBc_ - 0

_VBE_ < 0 and _VBC_ < 0



In most applications the transistor is operated in the forward active, or linear, region,
and in some situations in the saturation region. The suffixes _F_ and _R_ in many SPICE
parameter names indicate the region of operation.
The I-V characteristics described by Eqs. 3.11 are shown in Figure 3.6 for positive
values of _VBE_ and _VCE._ These characteristics are ideal, ignoring the effects of finite output conductance in the forward and reverse regions and the parasitic series resistances
associated with the collector, base, and emitter regions; these resistances are modeled
by parameters RC, RB, and RE, respectively.
The finite output conductance of a BJT is modeled in SPICE by the Early effect
(Muller and Kamins 1977) implemented by two parameters, VAF and VAR. The _Early_
_voltage_ is the point on the _VBC_ axis in the _(Ic, VBc)_ plane where the extrapolations of
the linear portions of all _I_ _c_ characteristics meet. This geometric interpretation of the
Early effect and its SPICE implementation is shown in Figure 3.7 for the _Ic_ = _!(VCE)_
characteristics: _VCE_ = _VBE -_ _VBC'_ The reverse Early voltage, _VAR,_ has a similar interpretation for the reverse region. For most practical applications _VAF_ is important and
_VAR_ can be neglected.


**82** 3 SEMICONDUCTOR-DEVICE ELEMENTS


**Figure 3.7** Early voltage parameter, VAF.



••I


BIPOLAR JUNCTION TRANSISTORS **83**


With the addition of the Early voltage, _Ic_ and _ICT_ in Eqs. 3.11 are modified as
follows:



_VBC_ _VBE)_ I
_Ic_ = (Icc - _ICE)_ 1 - _(_ _VAF_ _-_ _VAR_ _-_ _{3/CE_ = _ICT - IBc_


**3.3.2** **Dynamic** **and Small-Signal Models**



(3.12)



The dynamic behavior of a BIT is modeled by five different charges. Two charges,
_QDE_ and _QDC,_ are associated with the mobile carriers. These are the diffusion charges
represented by the current sources _Icc_ and _ICE_ in the Ebers-Moll model. The other
three charges model the fixed charges in the depletion regions of the three junctions:
base-emitter, _QJE;_ base-collector, _QJC;_ and collector-substrate, _QJs._
The diffusion charges are modeled by the following equations in the large-signal
transient analysis:


_QDE_ = _TF._ _Icc_

(3.13)
_QDC_ = _TR._ _ICE_


_TF_ and _TR_ are the forward and reverse transit times, respectively, of the injected minority carriers through the neutral base.
The depletion charges can be derived using the nonlinear equation that defines the
depletion capacitance, _CJ,_ of a pnjunction, Eq. 3.3. The SPICE large-signal implementation of the three depletion charges is according to Eq. 3.4, which defines the charge
_QJ._ The three voltage-dependent junction capacitances are described by the following
functions:


_CJE_
(l - _VBdVJE)MJE_



_CJC_
(l - _VBclVJC)MJC_


_CJS_
(l - _VcS/VJS)MJS_



(3.14)



Each junction can be characterized in SPICE by up to three parameters: _CJX,_ the
zero-bias junction capacitance; _VJX,_ the built-in potential; and _MJX,_ the grading coefficient. X stands for _E,_ C, or S, denoting the emitter, collector, or substrate junction,
respectively.
The nonlinear BIT model in SPICE including charge storage and parasitic terminal
resistances is depicted in Figure 3.8. The five charges are consolidated into three: _QBE,_
which includes _QDE_ and _QJE; QBC,_ which includes _QDC_ and _QJC;_ and _Qcs,_ modeled by


**84** 3 SEMICONDUCTOR-DEVICE ELEMENTS


_Ccs,_ the collector-substrate capacitance. Figure 3.8 is a first-order representation of the
complete Gummel-Poon BJT model available in SPICE and is sufficiently accurate for
many applications. The complete model includes second-order effects, such as _f3F_ and

_'TF_ dependency on _Ie,_ base push-out, and temperature effects. The complete equations
and model parameters are summarized in Appendix A.
The linearized small-signal model of a BJT, also known as the hybrid-1T model, is
shown in Figure 3.9. The nonlinear diodes and the current generator _lCT_ in Figure 3.5
are replaced by the following linear resistances (conductances) and transconductances:


Figure 3.8 Large-signal SPICE BJT model.


BIPOLAR JUNCTION TRANSISTORS **85**

**Figure 3.9** Small-signal SPICE BJT model.


The above small-signal parameters have been derived assuming no parasitic terminal
resistances _Re, RE, andRE;_ if these resistances are present, terminal voltages _VB'E'_ and

VB'creplace _VBEand VBC'_ _'_
The small-signal AC collector current _ie,_ can be expressed from Eqs. 3.12 and 3.15

and the hybrid-7T model (see Figure 3.9) as

```
                                      (3.16)

```

where _Vbe_ has been replaced by _Vbe - Vee_ in the second term. **In** the forward active region

_f_ the small-signal equations assume the more commonly known expressions (Gray and

Meyer 1993):


_ie_ = _gm Vbe :, gmFvbe_
```
                          qIc
```

_gm_ = _gmF_ = _~Fg~_ _=_

_NF.kT_

1 _~F_ (3.17)
_r~_ =g~ _gm_

_rlJ- ~_ 00, glJ- = 0

1 _VAF_ _VAF_
_r_ _o_ _.=_
_go_ _`Ie`_ _gmVth_


86 3 SEMICONDUCTOR-DEVICE ELEMENTS


In small-signal AC analysis charge-storage effects are modeled by nonlinear capacitances. The diffusion charges are modeled by two diffusion capacitors, _CDE_ and _CDC:_


(3.18)
_dQDC_ _alcT_
_CDC_ = -- = _TR--_ = _TR'gmR_
_dVBC_ _aVBC_


where _gmF_ and _gmR_ are the forward and reverse transconductances of the BJT (Eqs.
3.15). The junction capacitances are defined by Eqs. 3.14. In the small-signal BJT
model (Figure 3.9) the two types of capacitances for the BE and BC regions are consolidated in C 7r and C M, corresponding to _QBE_ and _QBC,_ respectively.


(3.19)

C M = _CDC_ + _CJc_


An important characteristic of a BJT is the cutoff frequency, _fr,_ where the current gain
drops to unity; _fr_ can be expressed as a function of the small-signal parameters:


(3.20)


3.3.3 Model Parameters


The general form of the BJT model statement is


.MODEL _MODname_ NPNIPNP _<IS=IS <BF=BF ..._ »


In every model one of the keywords NPN or PNP, indicating the transistor type, must
be specified.
Table 3.2 summarizes the model parameters introduced in this section together with
the default values assigned by SPICE2.


_EXAMPLE_ 3.2


The following are two BJT specifications.

```
      QX12 14 15 21 QMOD IC = 0.6,5.0
      .MODEL QMOD NPN BF=200 RB=100 CJC=5P TF=10N

```

BIPOLAR JUNCTION TRANSISTORS 87


**Table** 3.2 BJT Model Parameters


Name Parameter Units Default Example Scale Factor

IS Saturation current A 10- [16] lE-I6 _area_
BF Forward current gain 100 80
BR Reverse current gain I 3
NF Forward emission coefficient I 2
NR Reverse emission coefficient I 1.5
VAF Forward Early voltage V 00 100
VAR Reverse Early voltage V 00 250
RC Collector resistance 11 0 200 _I/area_
RE Emitter resistance 11 0 2 _I/area_
RB Base resistance 11 0 100 _I/area_
TF Forward transit time s 0 IN
TR Reverse transit time s 0 lOON
CJE BE zero-bias junction capacitance F 0 2P _area_
VJE BE built-in potential V 0.75 0.6
MJE BE grading coefficient 0.33 0.33
CJC BC zero-bias junction capacitance F 0 2P _area_
VJC BC built-in potential V 0.75 0.6
MJC BC grading coefficient 0.33 0.5
CJS CS zero-bias junction capacitance F 0 2P _area_
VJS CS built-in potential V 0.75 0.6
MJS CS grading coefficient 0 0.5


QX12is initialized at _VBEO_ = 0.6 V and _VCEO_ = 5.0 V in a transient analysis (see Chap.
6); its switching time is governed by the BCjunction capacitance and the forward transit
time. Defaults are used for the remaining parameters.

```
QFFl 1 3 0 QQ
QFF2 2 4 0 QQ OFF
```

.MODEL QQ PNP IS=lP BF=50 CJE=lP CJC=2P


QFFl and QFF2 are the two transistors of a flip-flop. QFF2 is specified OFF in order
to speed up the solution of the DC bias point. For more detail on flip-flop initialization,
see Example 4.8.


For some standard parts SPICE parameters are available from semiconductor
manufacturers because of the widespread use of SPICE simulation in circuit design.
Generally, however, model parameters must be derived, and how the SPICE parameters
can be derived for physical transistors becomes an important question. This topic is
addressed in the following pages. The characteristics of IC transistors are derived from
a test structure built on the same wafer. The measurement techniques leading to the
SPICE parameters of bipolar transistors are presented in detail by Getreu (1976). The
same measurements can be used to characterize discrete transistors if lab equipment
and the transistor of interest are available. A different approach is necessary for discrete


**88** 3 SEMICONDUCTOR-DEVICE ELEMENTS


transistors when the only information available is a data sheet. The extraction of the
main parameters from a data sheet is outlined in the following example.


_EXAMPLE_ 3.3


Derive the SPICE DC model parameters for the MPS2222 npn transistor, similar to a
2N2222. Use the _Motorola_ _Semiconductors_ _Data Book_ (Motorola Inc. 1988) for electrical characteristics. Simulate the _Ie_ = _f(VeE,_ _Is)_ characteristics with SPICE.


_**Solution**_
The information needed for extracting the model parameters is found in the MPS2222
data sheet, Figure 3.10, under _electrical_ _characteristics._ Several categories of characteristics are included, namely the _OFF, ON, small-signal,_ and _switching_ characteristics.
In addition to these data, provided as _minimum_ or _maximum_ values, many transistor data
sheets contain graphs of several electrical quantities. When graphs are available, they

     - should be used as primary sources of characteristic data, because the graphs represent
a typical device.
The first parameter to be extracted is the saturation current, _IS._ From the graph
entitled _ON Voltages,_ we obtain the BE voltage in saturation, _VSEsat,_ as a function of
_Ie_ for a set ratio _lei Is,_ equal to 10 for this transistor. Choose _Ie_ = 150 rnA and the
resulting _VSEsat_ = 0.85 V. Obtain from Eqs. 3.11 a relation between _Ie, Is,_ and _VSEsat_
by substituting the current _ICE_ from the _Is_ equation into the _Ie_ equation; Eqs. 3.10 are
then used with _N F_ = 1 to obtain the following expression for _IS:_


_IS_ = _Is (Ie_ + __l_)e-VBEsat/Vth_ = 0.015, _12e-O.85/0.0258_ = 1.14. 10- [15] A
_Is_ 1 - _CXR_
(3.21)


In the above calculation it has been assumed that _CXR_ = 0.5, or _BR_ = 1, which is the
default value in SPICE (see Table 3.2). This approximation is of no consequence unless
the transistor is operated in the reverse region most of the time.
Next, we derive a value for _BF,_ the current gain factor. This can be obtained from
the plot of the _DC current gain, hFE,_ as a function of _Ie._ Because _BF_ is a constant
and because _hFE_ dependence on _Ie_ is not supported in the first-order model, an average value should be chosen for _hFE_ over the _Ie_ range that the transistor is expected to
operate. Choose


_h_ _FE1_ = 150 at _Ie_ = 1 rnA

_hFE2_ = 200 at _Ie_ = 10 rnA

_hFE3_ = 240 at _Ie_ = 100 rnA


The average of these three values results in _BF_ = 190.


|MAXIMUM RATINGS|Col2|Col3|Col4|
|---|---|---|---|
|Rating|Symbol|MPS2222 MPS2222A|Unit|
|Collector-Emitter<br>Voltage|VCEO|30<br>40|Vde|
|Collector-Base Voltage|VCBO|60<br>75|Vde|
|Emitter-Base Voltage|VEBO|5.0<br>6.0|Vde|
|Collector Current -<br>Continuous<br>Total Device Dissipation @TA<br>= 25'C|IC<br>Po|600<br>625|mAde<br>mW|
|Derate above 25'C<br>Tota' Device Dissipation @ TC = 25'C|Po|5.0<br>1.5|mWrC<br>Watts|


Derate above 25'C 12 _mWrC_

Operating and Storage Junction TJ, Tstg -55 to + 150 'c
Temperature Range



**MPS2222, A***


CASE 29-04, STYLE 1
TO-92 (TO-226AA)

.:~"='
##### _,1_

2 1 Emitter
3


GENERAL PURPOSE
TRANSISTORS


NPN SIUCON


|THERMAL CHARACTERISTICS|Col2|Col3|Col4|
|---|---|---|---|
|Characteristic|Symbol|Max|Unit<br>|
|Thermal Resistance, Junction to Case|ReJC|83.3|'c/w<br>|



|ELECTRICAL CHARACTERISTICS (TA = 25'C unless otherwise noted.) Characteristic OFF CHARACTERISTICS|Symbol|Min|Max|Unit|
|---|---|---|---|---|
|OFF CHARACTERISTICS<br>Collector-Emitter<br>Breakdown Voltage<br>(lC = 10 mAde, 'B = 0)<br>MPS2222|V(BR)CEO|30|-<br>|Vde|
|<br>MPS2222A<br>Collector-Base Breakdown Voltage<br>(lC = 10 ~de,<br>IE = 0)<br>MPS2222<br>|V(BR)CBO|40<br>60|-<br>-<br>|Vde|
|<br> <br>MPS2222A<br>Emitter-Base Breakdown Voltage<br>(IE = 10 ~de,<br>IC = 0)<br>MPS2222|V(BR)EBO|75<br>5.0|-<br>-<br>|Vde|
|<br> <br>MPS2222A<br>Collector Cutoff Current<br>|ICEX|6.0<br>-|-<br>10|nAde|
|(VCE = 60 Vde, VEB(offl = 3.0 Vde)<br>MPS2222A<br>Collector Cutoff Current<br>ICBO<br>~de<br>(VCB = 50 Vde, IE = 0)<br>MPS2222<br>-<br>0.01<br>(VCB = 60 Vde, 'E = 0)<br>MPS2222A<br>-<br>0.01<br>(VCB = 50 Vde, IE = 0, TA = 125'C)<br>MPS2222<br>-<br>10<br>  <br>|(VCE = 60 Vde, VEB(offl = 3.0 Vde)<br>MPS2222A<br>Collector Cutoff Current<br>ICBO<br>~de<br>(VCB = 50 Vde, IE = 0)<br>MPS2222<br>-<br>0.01<br>(VCB = 60 Vde, 'E = 0)<br>MPS2222A<br>-<br>0.01<br>(VCB = 50 Vde, IE = 0, TA = 125'C)<br>MPS2222<br>-<br>10<br>  <br>|(VCE = 60 Vde, VEB(offl = 3.0 Vde)<br>MPS2222A<br>Collector Cutoff Current<br>ICBO<br>~de<br>(VCB = 50 Vde, IE = 0)<br>MPS2222<br>-<br>0.01<br>(VCB = 60 Vde, 'E = 0)<br>MPS2222A<br>-<br>0.01<br>(VCB = 50 Vde, IE = 0, TA = 125'C)<br>MPS2222<br>-<br>10<br>  <br>|(VCE = 60 Vde, VEB(offl = 3.0 Vde)<br>MPS2222A<br>Collector Cutoff Current<br>ICBO<br>~de<br>(VCB = 50 Vde, IE = 0)<br>MPS2222<br>-<br>0.01<br>(VCB = 60 Vde, 'E = 0)<br>MPS2222A<br>-<br>0.01<br>(VCB = 50 Vde, IE = 0, TA = 125'C)<br>MPS2222<br>-<br>10<br>  <br>|(VCE = 60 Vde, VEB(offl = 3.0 Vde)<br>MPS2222A<br>Collector Cutoff Current<br>ICBO<br>~de<br>(VCB = 50 Vde, IE = 0)<br>MPS2222<br>-<br>0.01<br>(VCB = 60 Vde, 'E = 0)<br>MPS2222A<br>-<br>0.01<br>(VCB = 50 Vde, IE = 0, TA = 125'C)<br>MPS2222<br>-<br>10<br>  <br>|
|<br>(VCB = 50 Vde, IE = 0, TA = 125'C)<br>MPS2222A<br>Emitter Cutoff Current<br>|lEBO|-<br>-|10<br>10|nAde|
|(VEB = 3.0 Vde, IC = 0)<br>MPS2222A<br>Base Cutoff Current<br> <br>|IBL|-|20|nAde|
|(VCE = 60 Vde, VEBloffl = 3.0 Vde)<br>MPS2222A<br>|(VCE = 60 Vde, VEBloffl = 3.0 Vde)<br>MPS2222A<br>|(VCE = 60 Vde, VEBloffl = 3.0 Vde)<br>MPS2222A<br>|(VCE = 60 Vde, VEBloffl = 3.0 Vde)<br>MPS2222A<br>|(VCE = 60 Vde, VEBloffl = 3.0 Vde)<br>MPS2222A<br>|
|ON CHARACTERISTICS<br>DC Current Gain<br>(lC = 0.1 mAde, VCE = 10 Vde)<br>(lC = 1.0 mAde, VCE = 10 Vde)<br>(lC = 10 mAde, VCE = 10 Vdel<br>(lC = 10 mAde, VCE = 10 Vde, TA = -55'C)<br>MPS2222A only<br>(lC = 150 mAde, VCE = 10 Vde)(1)<br>(lC = 150 mAde, VCE = 1.0 Vde)(1)<br>(lC = 500 mAde, VCE = 10 Vde)(1)<br>MPS2222|hFE|35<br>50<br>75<br>35<br>100<br>50<br>30|-<br>-<br>-<br>-<br>300<br>-<br>-<br>|-|
|MPS2222A<br>40<br>-<br>Collector-Emitter<br>Saturation Voltage(1)<br>VCE(sat)<br>Vde<br>(lC = 150 mAde, IB = 15 mAde)<br>MPS2222<br>-<br>0.4<br>MPS2222A<br>-<br>0.3<br>(lC = 500 mAde, 'B = 50 mAde)<br>MPS2222<br>-<br>1.6<br><br><br>|MPS2222A<br>40<br>-<br>Collector-Emitter<br>Saturation Voltage(1)<br>VCE(sat)<br>Vde<br>(lC = 150 mAde, IB = 15 mAde)<br>MPS2222<br>-<br>0.4<br>MPS2222A<br>-<br>0.3<br>(lC = 500 mAde, 'B = 50 mAde)<br>MPS2222<br>-<br>1.6<br><br><br>|MPS2222A<br>40<br>-<br>Collector-Emitter<br>Saturation Voltage(1)<br>VCE(sat)<br>Vde<br>(lC = 150 mAde, IB = 15 mAde)<br>MPS2222<br>-<br>0.4<br>MPS2222A<br>-<br>0.3<br>(lC = 500 mAde, 'B = 50 mAde)<br>MPS2222<br>-<br>1.6<br><br><br>|MPS2222A<br>40<br>-<br>Collector-Emitter<br>Saturation Voltage(1)<br>VCE(sat)<br>Vde<br>(lC = 150 mAde, IB = 15 mAde)<br>MPS2222<br>-<br>0.4<br>MPS2222A<br>-<br>0.3<br>(lC = 500 mAde, 'B = 50 mAde)<br>MPS2222<br>-<br>1.6<br><br><br>|MPS2222A<br>40<br>-<br>Collector-Emitter<br>Saturation Voltage(1)<br>VCE(sat)<br>Vde<br>(lC = 150 mAde, IB = 15 mAde)<br>MPS2222<br>-<br>0.4<br>MPS2222A<br>-<br>0.3<br>(lC = 500 mAde, 'B = 50 mAde)<br>MPS2222<br>-<br>1.6<br><br><br>|


•Also available as a PN2222,A.


Figure 3.10 MPS2222 data sheet.


```
89

```

|ELECTRICAL CHARACTERISTICS (continued) (TA = 25°C unless otherwise noted|Col2|.)|Col4|Col5|Col6|
|---|---|---|---|---|---|
|<br>   <br>Characteristic<br>Symbol<br>Min<br>Max<br>Unit<br>Base-Emitter Saturation Voltage(1)<br>VBE(sat)<br>Vde<br>(lC = 150 mAde, IB = 15 mAde)<br>MPS2222<br>-<br>1.3<br>MPS2222A<br>0.6<br>1.2<br>(lC = 500 mAde, IB = 50 mAde)<br>MPS2222<br>-<br>2.6<br><br><br>|<br>   <br>Characteristic<br>Symbol<br>Min<br>Max<br>Unit<br>Base-Emitter Saturation Voltage(1)<br>VBE(sat)<br>Vde<br>(lC = 150 mAde, IB = 15 mAde)<br>MPS2222<br>-<br>1.3<br>MPS2222A<br>0.6<br>1.2<br>(lC = 500 mAde, IB = 50 mAde)<br>MPS2222<br>-<br>2.6<br><br><br>|<br>   <br>Characteristic<br>Symbol<br>Min<br>Max<br>Unit<br>Base-Emitter Saturation Voltage(1)<br>VBE(sat)<br>Vde<br>(lC = 150 mAde, IB = 15 mAde)<br>MPS2222<br>-<br>1.3<br>MPS2222A<br>0.6<br>1.2<br>(lC = 500 mAde, IB = 50 mAde)<br>MPS2222<br>-<br>2.6<br><br><br>|<br>   <br>Characteristic<br>Symbol<br>Min<br>Max<br>Unit<br>Base-Emitter Saturation Voltage(1)<br>VBE(sat)<br>Vde<br>(lC = 150 mAde, IB = 15 mAde)<br>MPS2222<br>-<br>1.3<br>MPS2222A<br>0.6<br>1.2<br>(lC = 500 mAde, IB = 50 mAde)<br>MPS2222<br>-<br>2.6<br><br><br>|<br>   <br>Characteristic<br>Symbol<br>Min<br>Max<br>Unit<br>Base-Emitter Saturation Voltage(1)<br>VBE(sat)<br>Vde<br>(lC = 150 mAde, IB = 15 mAde)<br>MPS2222<br>-<br>1.3<br>MPS2222A<br>0.6<br>1.2<br>(lC = 500 mAde, IB = 50 mAde)<br>MPS2222<br>-<br>2.6<br><br><br>|<br>   <br>Characteristic<br>Symbol<br>Min<br>Max<br>Unit<br>Base-Emitter Saturation Voltage(1)<br>VBE(sat)<br>Vde<br>(lC = 150 mAde, IB = 15 mAde)<br>MPS2222<br>-<br>1.3<br>MPS2222A<br>0.6<br>1.2<br>(lC = 500 mAde, IB = 50 mAde)<br>MPS2222<br>-<br>2.6<br><br><br>|
|MPS2222A<br><br>2.0|MPS2222A<br><br>2.0|MPS2222A<br><br>2.0|MPS2222A<br><br>2.0|MPS2222A<br><br>2.0|MPS2222A<br><br>2.0|
|SMAll-SIGNAL<br>CHARACTERISTICS<br>Current-Gain -<br>Bandwidth Produet(2)<br>(lC = 20 mAde, VCE = 20 Vde, f = 100 MHz)<br>MPS2222|SMAll-SIGNAL<br>CHARACTERISTICS<br>Current-Gain -<br>Bandwidth Produet(2)<br>(lC = 20 mAde, VCE = 20 Vde, f = 100 MHz)<br>MPS2222|IT|250|-<br>|MHz|
|<br><br>MPS2222A<br>Output Capacitance|<br><br>MPS2222A<br>Output Capacitance|Cobo|300<br>-|-<br>8.0|pF|
|<br>(VCB = 10 Vde, IE = 0, f = 1.0 MHz)<br>Input Capacitance<br>(VEB = 0.5 Vde, IC = 0, f = 1.0 MHz)<br>MPS2222|<br>(VCB = 10 Vde, IE = 0, f = 1.0 MHz)<br>Input Capacitance<br>(VEB = 0.5 Vde, IC = 0, f = 1.0 MHz)<br>MPS2222|Cibo|-<br>|30|pF|
|<br><br>MPS2222A<br>Input Impedance<br>(lC = 1.0 mAde, VCE = 10 Vde, f=<br>1.0 kHz)<br>MPS2222A|<br><br>MPS2222A<br>Input Impedance<br>(lC = 1.0 mAde, VCE = 10 Vde, f=<br>1.0 kHz)<br>MPS2222A|hie|-<br>2.0|25<br>8.0|k{}|
|<br> <br><br>(lC = 10 mAde, VCE = 10 Vde, f = 1.0 kHz)<br>MPS2222A<br>Voltage Feedback Ratio<br>(lC = 1.0 mAde, VCE = 10 Vde, f = 1.0 kHz)<br>MPS2222A|<br> <br><br>(lC = 10 mAde, VCE = 10 Vde, f = 1.0 kHz)<br>MPS2222A<br>Voltage Feedback Ratio<br>(lC = 1.0 mAde, VCE = 10 Vde, f = 1.0 kHz)<br>MPS2222A|hre|0.25<br>-<br>|1.25<br>8.0<br>|X 10-4|
|<br>(lC = 10 mAde, VCE = 10 Vde, f = 1.0 kHz)<br>MPS2222A<br>Small-Signal Current Gain<br>(IC = 1.0 mAde, VCE = 10 Vde, f = 1.0 kHz)<br>MPS2222A|<br>(lC = 10 mAde, VCE = 10 Vde, f = 1.0 kHz)<br>MPS2222A<br>Small-Signal Current Gain<br>(IC = 1.0 mAde, VCE = 10 Vde, f = 1.0 kHz)<br>MPS2222A|hfe|-<br>50<br>|4.0<br>300<br>|-|
|<br>(lC = 10 mAde, VCE = 10 Vde, f = 1.0 kHz)<br>MPS2222A<br>Output Admittance<br>(lC = 1.0 mAde, VCE = 10 Vde, f = 1.0 kHz)<br>MPS2222A|<br>(lC = 10 mAde, VCE = 10 Vde, f = 1.0 kHz)<br>MPS2222A<br>Output Admittance<br>(lC = 1.0 mAde, VCE = 10 Vde, f = 1.0 kHz)<br>MPS2222A|hoe|75<br>5.0<br>|375<br>35<br>|ILmhos|
|<br>(lC = 10 mAde, VCE = 10 Vde, f = 1.0 kHz)<br>MPS2222A<br>Collector Base TIme Constant<br>|<br>(lC = 10 mAde, VCE = 10 Vde, f = 1.0 kHz)<br>MPS2222A<br>Collector Base TIme Constant<br>|rb'Ce|25<br>-|200<br>150|ps|
|(IE = 20 mAde, VCB = 20 Vdc, f = 31.8 MHz)<br>MPS2222A<br>Noise Figure<br>NF<br>-<br>4.0<br>dB<br>(lC = 100 !LAde, VCE = 10 Vde, RS = 1.0 kO, f = 1.0 kHz)<br>MPS2222A|(IE = 20 mAde, VCB = 20 Vdc, f = 31.8 MHz)<br>MPS2222A<br>Noise Figure<br>NF<br>-<br>4.0<br>dB<br>(lC = 100 !LAde, VCE = 10 Vde, RS = 1.0 kO, f = 1.0 kHz)<br>MPS2222A|(IE = 20 mAde, VCB = 20 Vdc, f = 31.8 MHz)<br>MPS2222A<br>Noise Figure<br>NF<br>-<br>4.0<br>dB<br>(lC = 100 !LAde, VCE = 10 Vde, RS = 1.0 kO, f = 1.0 kHz)<br>MPS2222A|(IE = 20 mAde, VCB = 20 Vdc, f = 31.8 MHz)<br>MPS2222A<br>Noise Figure<br>NF<br>-<br>4.0<br>dB<br>(lC = 100 !LAde, VCE = 10 Vde, RS = 1.0 kO, f = 1.0 kHz)<br>MPS2222A|(IE = 20 mAde, VCB = 20 Vdc, f = 31.8 MHz)<br>MPS2222A<br>Noise Figure<br>NF<br>-<br>4.0<br>dB<br>(lC = 100 !LAde, VCE = 10 Vde, RS = 1.0 kO, f = 1.0 kHz)<br>MPS2222A|(IE = 20 mAde, VCB = 20 Vdc, f = 31.8 MHz)<br>MPS2222A<br>Noise Figure<br>NF<br>-<br>4.0<br>dB<br>(lC = 100 !LAde, VCE = 10 Vde, RS = 1.0 kO, f = 1.0 kHz)<br>MPS2222A|
|SWITCHING CHARACTE|RISTICS<br>MPS2222A only<br>(VCC = 30 Vde, VBE(off) = 0.5 Vde,<br>|||||
|Delay TIme|Delay TIme|td|-<br>|10|ns|
|Rise Time|IC = 150 mAde, IB1 = 15 mMe)<br>(Figure I)<br>(VCC = 30 Vde, IC = 150 mAde,<br> <br>|tr|-<br>|25|ns|
|Storage Time|Storage Time|ts|-<br>|225|ns|



(1) Pulse Test: Pulse Width'" 300 /LS,Duty Cycle'" 2.0%.
(2) IT is defined as the frequency at which Ihfel extrapolates to unity.


SWITCHING TIME EQUIVALENT TEST CIRCUITS


FIGURE 1 - TURN-ON TIME FIGURE 2 - TURN-QFF TIME



+30 v



_I 1-1.0 to 100,",S. DUTY



200, +16V~ CYCLE"'2%


_l_ 0
```
                       -T- lk
```
___ J :Cs. < 10pF -14 V                   - I -<20n5 lN914

Scope Rise Time < 4 ns
-Total,hunt capacitance of test jig,
connectors, and oscilloscope.


Figure 3.10 _(continued)_



+30 v


200

,,
__L__ -, .
:Cs. < 10 pF
___J



.4 V



.90


**MPS2222, A**


FIGURE 3 - DC CURRENT GAIN


TJ=1250C


I
.I..-l
**--** ......
25°C
I-- I I **--** - '- [-] I- ~-i".. - -

.~50C


.1
I



1000

700


500
'"•... z •• 300200
~
'"B 100
u 70
c
50
;

30


20



VCE=1.0V
•..••• "'7'" - VCE=10V
I I I I III



10
0.1 0.2 0.3 0.5 0.7 1.0 2.0 3.0 5.0 7.0 10 20 30 50 70 100 200 300 500 700 1.0 k



IC. COLLECTOR CURRENT (mAl



1.0


O.S


0.6


0.4


0.2


|Col1|Col2|Col3|Col4|Col5|FIG|URE 4 -|CO|LLE|CT|OR|SA|TU|RATI|ON R|EGIO|N|Col18|Col19|Col20|Col21|Col22|Col23|Col24|Col25|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||||||||||||||||||||||||TJ = 25°C|
||||||||||||||||||||||||||
|||||||||||||||150mA<br>|150mA<br>|||||||500 rnA<br>|500 rnA<br>||
||||||lOrnA|lOrnA|lOrnA|lOrnA|lOrnA|lOrnA|lOrnA|lOrnA|lOrnA|lOrnA|lOrnA|lOrnA|lOrnA|lOrnA|lOrnA|lOrnA|lOrnA|lOrnA|lOrnA|lOrnA|
|||||||||||||||1\<br>||||||||<br>\<br>|||
|||||||||||||||\<br>||||||||\<br>|||
|||||||||||||||\||||||||\|||



\ 1\

I' .•....
-- 0.02 0.03 0.05 0.1 0.2 0.3 0.5 1.0 2.0





\ 1\




0.005 0.01 0.02 0.03 0.05 0.1 0.2 0.3 0.5 1.0 2.0 3.0 5.0 10 20 30 50



FIGURE 5 - TURN'()N TIME



200


100


70


50
g 30

w 20
'" [;::]

10


7.0


5.0


3.0


2.0

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
||..........||||I ••••••|'d@lVESl<br>|offl<br>|= 2.0 V_<br>|
|||||||'d@lVES|off)|= 0|
|||......|||||||

5.0 7.0 10


|Col1|Col2|Col3|Col4|VCC = 30 V|
|---|---|---|---|---|
|t',!" .11/S If||||IC/IS = 10<br>If): ~~~|



20 30 50 70 100 200 300 500


IC. COLLECTOR CURRENT (rnA)



ICIIS = 10
TJ = 25°C


..•...
...•... ..••....



IS. SASE CURRENT (mAl


500


300


200


100


c 70

w 50

;:: '" 30


20


10



FIGURE 6 - TURN'()FF TIME


II ......
...•..





**1"'-_**



20 30 50 70 100 200 300 500


IC. COLLECTOR CURRENT (rnA)


**91**



7.0
5.0
5.0 7.0 10



**Figure 3.10** _(continued)_


10


8.0
~
w
**~** **6.0**
<.0
;;:
~

- ~. z 4.0
z


2.0


   








30


20


~~
... w'-' Z.. 7.010
;::;
~ 5.0
..
'-'


3.0


|GURE|E 1Q - CUR|Col3|RRENT|
|---|---|---|---|
|UR|E 1Q -<br>CU<br>|E 1Q -<br>CU<br>|REN|
||VCE<br>|I I<br> = 20 V<br>||
||<br>TJ|<br>.250C||


|Col1|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
||||<br>||
|-||~|I<br>-rr<br>.-<br>|I<br>-+<br><br>|
|||||I|


|Col1|Col2|Col3|"|
|---|---|---|---|
||||"|
|||'/<br>||










|Col1|Col2|Col3|r---|Ccb t'-1--J.|
|---|---|---|---|---|
|||||t'-1--J.|
|||||I<br>|





2.0










|Col1|Col2|
|---|---|
|||
|||







1.0


0.8


'" ':;

**~** **0.6**
w
<.0
.....
**c5** **0.4**

>'


0.2

















|FIGURE 7 - FREQUENCY EFFECTS FIGURE 8 - SOURCE RESISTANCE EFFECTS<br>10 II 1111111 I<br>t. ;.0 ~H~ III II V I j<br>. ~, 8.0 IC=50I .A 1111 / I<br>w 'IOO.A<br>' <:" > .0 6.0 1\ 500 .A 1/ J I<br>; w;: l/ 1.0mA J<br>'"<br>0 z 4.0 )' 1/ /<br>~.<br>z "-<br>2.0 ~ ...•. ./<br>a<br>0.02 0.05 0.1 0.2 0.5 1.0 2.0 5.0 10 20 50 100 50 100 200 500 1.0k 2.0k 5.0k 10k 20k 50k 100<br>I. FREQUENCY 1kHz) RS. SOURCE RESISTANCE 10HMS)<br>FIGURE 9 - CAPACITANCES FIGURE 1Q - CURRENT.GAIN BANDWIDTH PRODUCT<br>I I I I<br>- -rr -+ VCE = 20 V<br>.- t; TJ.250C<br>~ I :g> 300<br>C.b g:<br>"<br>or<br>:; 200<br>'/<br>3 cz..:,. ./<br>/<br>z<br>/<br>~ 1001/<br>r--- t'-1C --c Jb ' ~"<br>.<br>I ' '" " 70<br>B<br>I<br>~ 50<br>.1 0.2 0.3 0.5 1.0 2.0 3.0 5.0 10 20 30 50 1.0 2.0 3.0 5.0 7.0 10 20 30 50 70 100<br>REVERSE VOLTAGE (VOLTS) IC. COLLECTOR CURRENT ImA)<br>FIGURE 11 - "ON" VOLTAGES FIGURE 12 - TEMPERATURE COEFFICIE ~NTS<br>+0.5 III<br>~ ~<br>I<br>I--<br>RINCforVCElsatll-<br>l-<br>~<br>1.0 V :; -0.5 I--<br>E... I--<br>V8Elon)@VCE = 10 V ~ ;::; -1.0<br>f:: I..••<br>w c'-' .1.5<br>-2.0 RIN8forV8E<br>,|Col2|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|FIGURE 7 - FREQUENCY EFFECTS<br>FIGURE 8 - SOURCE RESISTANCE EFFECTS<br>a<br>50<br>100<br>200<br>500<br>1.0k<br>2.0k<br>5.0k<br>10k<br>20k<br>50k 100<br>RS. SOURCE RESISTANCE 10HMS)<br> 0.02<br>0.05 0.1<br>0.2<br>0.5<br>1.0<br>2.0<br>5.0<br>10<br>20<br>50<br>100<br>I. FREQUENCY 1kHz)<br>10<br>8.0<br>.,~<br>w<br>'"<br>6.0<br>:><br><.0<br>;;:<br>w<br>'"0<br>4.0<br>z~.<br>z<br>2.0<br>II<br>1111111<br>I<br>j<br>t. ;.0 ~H~ III II<br>_V_<br>I<br>I<br>1111<br>/<br>IC=50.A<br>I<br>'IOO.A<br>1\<br>500 .A<br>1/<br>_J_<br>I<br>l/<br>1.0mA<br>_J_<br>)'<br>1/<br>/<br>"-<br>~<br>...•.<br>./<br>FIGURE 9 - CAPACITANCES<br>FIGURE 1Q -<br>CURRENT.GAIN<br>BANDWIDTH PRODUCT<br>50<br>70<br>100<br>2.0<br>3.0<br>5.0<br>7.0<br>10<br>20<br>30<br>IC. COLLECTOR CURRENT ImA)<br>I I<br>VCE = 20 V<br>TJ.250C<br>"<br>'/<br>./<br>/<br>/<br>1/<br>70<br>~<br>50<br>1.0<br>t;<br>:>g<br>300<br>g:<br>or<br>:;<br>200<br>3:cz...,<br>z<br>~<br>100<br>'"~<br>'"'"_B_<br>I<br>I<br>-<br>-rr<br>-+<br>.-<br>~<br>I<br>C.b<br>r---<br>Ccb<br>t'-1--J.<br>I<br>I<br>.1<br>0.2 0.3<br>0.5<br>1.0<br>2.0 3.0<br>5.0<br>10<br>20<br>30<br>50<br>REVERSE VOLTAGE (VOLTS)<br>FIGURE 11 - "ON" VOLTAGES<br>FIGURE 12 - TEMPERATURE COEFFICIENTS<br>III<br>~<br>I<br>~<br>~<br>RINCforVCElsatll-<br>I--<br>l-<br>I--<br>I--<br>I..••<br>RIN8forV8E<br>,<br> <br>+0.5<br>~<br>-0.5<br>:;<br>E...<br>~<br>-1.0<br>;::;<br>f::<br>w<br>.1.5<br>c'-'<br>-2.0<br>1.0 V<br> <br><br>V8Elon)@VCE<br>= 10 V|FIGURE 8 - SOURCE<br>II<br>1111111<br>|FIGURE 8 - SOURCE<br>II<br>1111111<br>|FIGURE 8 - SOURCE<br>II<br>1111111<br>|RESIST|ANCE EFFE|CTS<br>|CTS<br>|
|FIGURE 7 - FREQUENCY EFFECTS<br>FIGURE 8 - SOURCE RESISTANCE EFFECTS<br>a<br>50<br>100<br>200<br>500<br>1.0k<br>2.0k<br>5.0k<br>10k<br>20k<br>50k 100<br>RS. SOURCE RESISTANCE 10HMS)<br> 0.02<br>0.05 0.1<br>0.2<br>0.5<br>1.0<br>2.0<br>5.0<br>10<br>20<br>50<br>100<br>I. FREQUENCY 1kHz)<br>10<br>8.0<br>.,~<br>w<br>'"<br>6.0<br>:><br><.0<br>;;:<br>w<br>'"0<br>4.0<br>z~.<br>z<br>2.0<br>II<br>1111111<br>I<br>j<br>t. ;.0 ~H~ III II<br>_V_<br>I<br>I<br>1111<br>/<br>IC=50.A<br>I<br>'IOO.A<br>1\<br>500 .A<br>1/<br>_J_<br>I<br>l/<br>1.0mA<br>_J_<br>)'<br>1/<br>/<br>"-<br>~<br>...•.<br>./<br>FIGURE 9 - CAPACITANCES<br>FIGURE 1Q -<br>CURRENT.GAIN<br>BANDWIDTH PRODUCT<br>50<br>70<br>100<br>2.0<br>3.0<br>5.0<br>7.0<br>10<br>20<br>30<br>IC. COLLECTOR CURRENT ImA)<br>I I<br>VCE = 20 V<br>TJ.250C<br>"<br>'/<br>./<br>/<br>/<br>1/<br>70<br>~<br>50<br>1.0<br>t;<br>:>g<br>300<br>g:<br>or<br>:;<br>200<br>3:cz...,<br>z<br>~<br>100<br>'"~<br>'"'"_B_<br>I<br>I<br>-<br>-rr<br>-+<br>.-<br>~<br>I<br>C.b<br>r---<br>Ccb<br>t'-1--J.<br>I<br>I<br>.1<br>0.2 0.3<br>0.5<br>1.0<br>2.0 3.0<br>5.0<br>10<br>20<br>30<br>50<br>REVERSE VOLTAGE (VOLTS)<br>FIGURE 11 - "ON" VOLTAGES<br>FIGURE 12 - TEMPERATURE COEFFICIENTS<br>III<br>~<br>I<br>~<br>~<br>RINCforVCElsatll-<br>I--<br>l-<br>I--<br>I--<br>I..••<br>RIN8forV8E<br>,<br> <br>+0.5<br>~<br>-0.5<br>:;<br>E...<br>~<br>-1.0<br>;::;<br>f::<br>w<br>.1.5<br>c'-'<br>-2.0<br>1.0 V<br> <br><br>V8Elon)@VCE<br>= 10 V|FIGURE 8 - SOURCE<br>II<br>1111111<br>|FIGURE 8 - SOURCE<br>II<br>1111111<br>|FIGURE 8 - SOURCE<br>II<br>1111111<br>|||I<br>|I<br>|
|FIGURE 7 - FREQUENCY EFFECTS<br>FIGURE 8 - SOURCE RESISTANCE EFFECTS<br>a<br>50<br>100<br>200<br>500<br>1.0k<br>2.0k<br>5.0k<br>10k<br>20k<br>50k 100<br>RS. SOURCE RESISTANCE 10HMS)<br> 0.02<br>0.05 0.1<br>0.2<br>0.5<br>1.0<br>2.0<br>5.0<br>10<br>20<br>50<br>100<br>I. FREQUENCY 1kHz)<br>10<br>8.0<br>.,~<br>w<br>'"<br>6.0<br>:><br><.0<br>;;:<br>w<br>'"0<br>4.0<br>z~.<br>z<br>2.0<br>II<br>1111111<br>I<br>j<br>t. ;.0 ~H~ III II<br>_V_<br>I<br>I<br>1111<br>/<br>IC=50.A<br>I<br>'IOO.A<br>1\<br>500 .A<br>1/<br>_J_<br>I<br>l/<br>1.0mA<br>_J_<br>)'<br>1/<br>/<br>"-<br>~<br>...•.<br>./<br>FIGURE 9 - CAPACITANCES<br>FIGURE 1Q -<br>CURRENT.GAIN<br>BANDWIDTH PRODUCT<br>50<br>70<br>100<br>2.0<br>3.0<br>5.0<br>7.0<br>10<br>20<br>30<br>IC. COLLECTOR CURRENT ImA)<br>I I<br>VCE = 20 V<br>TJ.250C<br>"<br>'/<br>./<br>/<br>/<br>1/<br>70<br>~<br>50<br>1.0<br>t;<br>:>g<br>300<br>g:<br>or<br>:;<br>200<br>3:cz...,<br>z<br>~<br>100<br>'"~<br>'"'"_B_<br>I<br>I<br>-<br>-rr<br>-+<br>.-<br>~<br>I<br>C.b<br>r---<br>Ccb<br>t'-1--J.<br>I<br>I<br>.1<br>0.2 0.3<br>0.5<br>1.0<br>2.0 3.0<br>5.0<br>10<br>20<br>30<br>50<br>REVERSE VOLTAGE (VOLTS)<br>FIGURE 11 - "ON" VOLTAGES<br>FIGURE 12 - TEMPERATURE COEFFICIENTS<br>III<br>~<br>I<br>~<br>~<br>RINCforVCElsatll-<br>I--<br>l-<br>I--<br>I--<br>I..••<br>RIN8forV8E<br>,<br> <br>+0.5<br>~<br>-0.5<br>:;<br>E...<br>~<br>-1.0<br>;::;<br>f::<br>w<br>.1.5<br>c'-'<br>-2.0<br>1.0 V<br> <br><br>V8Elon)@VCE<br>= 10 V|FIGURE 8 - SOURCE<br>II<br>1111111<br>|FIGURE 8 - SOURCE<br>II<br>1111111<br>|FIGURE 8 - SOURCE<br>II<br>1111111<br>||_V_<br>/|_V_<br>/|_V_<br>/|
|FIGURE 7 - FREQUENCY EFFECTS<br>FIGURE 8 - SOURCE RESISTANCE EFFECTS<br>a<br>50<br>100<br>200<br>500<br>1.0k<br>2.0k<br>5.0k<br>10k<br>20k<br>50k 100<br>RS. SOURCE RESISTANCE 10HMS)<br> 0.02<br>0.05 0.1<br>0.2<br>0.5<br>1.0<br>2.0<br>5.0<br>10<br>20<br>50<br>100<br>I. FREQUENCY 1kHz)<br>10<br>8.0<br>.,~<br>w<br>'"<br>6.0<br>:><br><.0<br>;;:<br>w<br>'"0<br>4.0<br>z~.<br>z<br>2.0<br>II<br>1111111<br>I<br>j<br>t. ;.0 ~H~ III II<br>_V_<br>I<br>I<br>1111<br>/<br>IC=50.A<br>I<br>'IOO.A<br>1\<br>500 .A<br>1/<br>_J_<br>I<br>l/<br>1.0mA<br>_J_<br>)'<br>1/<br>/<br>"-<br>~<br>...•.<br>./<br>FIGURE 9 - CAPACITANCES<br>FIGURE 1Q -<br>CURRENT.GAIN<br>BANDWIDTH PRODUCT<br>50<br>70<br>100<br>2.0<br>3.0<br>5.0<br>7.0<br>10<br>20<br>30<br>IC. COLLECTOR CURRENT ImA)<br>I I<br>VCE = 20 V<br>TJ.250C<br>"<br>'/<br>./<br>/<br>/<br>1/<br>70<br>~<br>50<br>1.0<br>t;<br>:>g<br>300<br>g:<br>or<br>:;<br>200<br>3:cz...,<br>z<br>~<br>100<br>'"~<br>'"'"_B_<br>I<br>I<br>-<br>-rr<br>-+<br>.-<br>~<br>I<br>C.b<br>r---<br>Ccb<br>t'-1--J.<br>I<br>I<br>.1<br>0.2 0.3<br>0.5<br>1.0<br>2.0 3.0<br>5.0<br>10<br>20<br>30<br>50<br>REVERSE VOLTAGE (VOLTS)<br>FIGURE 11 - "ON" VOLTAGES<br>FIGURE 12 - TEMPERATURE COEFFICIENTS<br>III<br>~<br>I<br>~<br>~<br>RINCforVCElsatll-<br>I--<br>l-<br>I--<br>I--<br>I..••<br>RIN8forV8E<br>,<br> <br>+0.5<br>~<br>-0.5<br>:;<br>E...<br>~<br>-1.0<br>;::;<br>f::<br>w<br>.1.5<br>c'-'<br>-2.0<br>1.0 V<br> <br><br>V8Elon)@VCE<br>= 10 V||<br>I<br>1111<br>IC=50.A<br>'IOO.A<br>500 .A<br>|<br>I<br>1111<br>IC=50.A<br>'IOO.A<br>500 .A<br>|||I||
|FIGURE 7 - FREQUENCY EFFECTS<br>FIGURE 8 - SOURCE RESISTANCE EFFECTS<br>a<br>50<br>100<br>200<br>500<br>1.0k<br>2.0k<br>5.0k<br>10k<br>20k<br>50k 100<br>RS. SOURCE RESISTANCE 10HMS)<br> 0.02<br>0.05 0.1<br>0.2<br>0.5<br>1.0<br>2.0<br>5.0<br>10<br>20<br>50<br>100<br>I. FREQUENCY 1kHz)<br>10<br>8.0<br>.,~<br>w<br>'"<br>6.0<br>:><br><.0<br>;;:<br>w<br>'"0<br>4.0<br>z~.<br>z<br>2.0<br>II<br>1111111<br>I<br>j<br>t. ;.0 ~H~ III II<br>_V_<br>I<br>I<br>1111<br>/<br>IC=50.A<br>I<br>'IOO.A<br>1\<br>500 .A<br>1/<br>_J_<br>I<br>l/<br>1.0mA<br>_J_<br>)'<br>1/<br>/<br>"-<br>~<br>...•.<br>./<br>FIGURE 9 - CAPACITANCES<br>FIGURE 1Q -<br>CURRENT.GAIN<br>BANDWIDTH PRODUCT<br>50<br>70<br>100<br>2.0<br>3.0<br>5.0<br>7.0<br>10<br>20<br>30<br>IC. COLLECTOR CURRENT ImA)<br>I I<br>VCE = 20 V<br>TJ.250C<br>"<br>'/<br>./<br>/<br>/<br>1/<br>70<br>~<br>50<br>1.0<br>t;<br>:>g<br>300<br>g:<br>or<br>:;<br>200<br>3:cz...,<br>z<br>~<br>100<br>'"~<br>'"'"_B_<br>I<br>I<br>-<br>-rr<br>-+<br>.-<br>~<br>I<br>C.b<br>r---<br>Ccb<br>t'-1--J.<br>I<br>I<br>.1<br>0.2 0.3<br>0.5<br>1.0<br>2.0 3.0<br>5.0<br>10<br>20<br>30<br>50<br>REVERSE VOLTAGE (VOLTS)<br>FIGURE 11 - "ON" VOLTAGES<br>FIGURE 12 - TEMPERATURE COEFFICIENTS<br>III<br>~<br>I<br>~<br>~<br>RINCforVCElsatll-<br>I--<br>l-<br>I--<br>I--<br>I..••<br>RIN8forV8E<br>,<br> <br>+0.5<br>~<br>-0.5<br>:;<br>E...<br>~<br>-1.0<br>;::;<br>f::<br>w<br>.1.5<br>c'-'<br>-2.0<br>1.0 V<br> <br><br>V8Elon)@VCE<br>= 10 V|1\<br>|1\<br>|1\<br>|1/||_J_|_J_|
|FIGURE 7 - FREQUENCY EFFECTS<br>FIGURE 8 - SOURCE RESISTANCE EFFECTS<br>a<br>50<br>100<br>200<br>500<br>1.0k<br>2.0k<br>5.0k<br>10k<br>20k<br>50k 100<br>RS. SOURCE RESISTANCE 10HMS)<br> 0.02<br>0.05 0.1<br>0.2<br>0.5<br>1.0<br>2.0<br>5.0<br>10<br>20<br>50<br>100<br>I. FREQUENCY 1kHz)<br>10<br>8.0<br>.,~<br>w<br>'"<br>6.0<br>:><br><.0<br>;;:<br>w<br>'"0<br>4.0<br>z~.<br>z<br>2.0<br>II<br>1111111<br>I<br>j<br>t. ;.0 ~H~ III II<br>_V_<br>I<br>I<br>1111<br>/<br>IC=50.A<br>I<br>'IOO.A<br>1\<br>500 .A<br>1/<br>_J_<br>I<br>l/<br>1.0mA<br>_J_<br>)'<br>1/<br>/<br>"-<br>~<br>...•.<br>./<br>FIGURE 9 - CAPACITANCES<br>FIGURE 1Q -<br>CURRENT.GAIN<br>BANDWIDTH PRODUCT<br>50<br>70<br>100<br>2.0<br>3.0<br>5.0<br>7.0<br>10<br>20<br>30<br>IC. COLLECTOR CURRENT ImA)<br>I I<br>VCE = 20 V<br>TJ.250C<br>"<br>'/<br>./<br>/<br>/<br>1/<br>70<br>~<br>50<br>1.0<br>t;<br>:>g<br>300<br>g:<br>or<br>:;<br>200<br>3:cz...,<br>z<br>~<br>100<br>'"~<br>'"'"_B_<br>I<br>I<br>-<br>-rr<br>-+<br>.-<br>~<br>I<br>C.b<br>r---<br>Ccb<br>t'-1--J.<br>I<br>I<br>.1<br>0.2 0.3<br>0.5<br>1.0<br>2.0 3.0<br>5.0<br>10<br>20<br>30<br>50<br>REVERSE VOLTAGE (VOLTS)<br>FIGURE 11 - "ON" VOLTAGES<br>FIGURE 12 - TEMPERATURE COEFFICIENTS<br>III<br>~<br>I<br>~<br>~<br>RINCforVCElsatll-<br>I--<br>l-<br>I--<br>I--<br>I..••<br>RIN8forV8E<br>,<br> <br>+0.5<br>~<br>-0.5<br>:;<br>E...<br>~<br>-1.0<br>;::;<br>f::<br>w<br>.1.5<br>c'-'<br>-2.0<br>1.0 V<br> <br><br>V8Elon)@VCE<br>= 10 V|l/|1.0mA|||_J_|||
|FIGURE 7 - FREQUENCY EFFECTS<br>FIGURE 8 - SOURCE RESISTANCE EFFECTS<br>a<br>50<br>100<br>200<br>500<br>1.0k<br>2.0k<br>5.0k<br>10k<br>20k<br>50k 100<br>RS. SOURCE RESISTANCE 10HMS)<br> 0.02<br>0.05 0.1<br>0.2<br>0.5<br>1.0<br>2.0<br>5.0<br>10<br>20<br>50<br>100<br>I. FREQUENCY 1kHz)<br>10<br>8.0<br>.,~<br>w<br>'"<br>6.0<br>:><br><.0<br>;;:<br>w<br>'"0<br>4.0<br>z~.<br>z<br>2.0<br>II<br>1111111<br>I<br>j<br>t. ;.0 ~H~ III II<br>_V_<br>I<br>I<br>1111<br>/<br>IC=50.A<br>I<br>'IOO.A<br>1\<br>500 .A<br>1/<br>_J_<br>I<br>l/<br>1.0mA<br>_J_<br>)'<br>1/<br>/<br>"-<br>~<br>...•.<br>./<br>FIGURE 9 - CAPACITANCES<br>FIGURE 1Q -<br>CURRENT.GAIN<br>BANDWIDTH PRODUCT<br>50<br>70<br>100<br>2.0<br>3.0<br>5.0<br>7.0<br>10<br>20<br>30<br>IC. COLLECTOR CURRENT ImA)<br>I I<br>VCE = 20 V<br>TJ.250C<br>"<br>'/<br>./<br>/<br>/<br>1/<br>70<br>~<br>50<br>1.0<br>t;<br>:>g<br>300<br>g:<br>or<br>:;<br>200<br>3:cz...,<br>z<br>~<br>100<br>'"~<br>'"'"_B_<br>I<br>I<br>-<br>-rr<br>-+<br>.-<br>~<br>I<br>C.b<br>r---<br>Ccb<br>t'-1--J.<br>I<br>I<br>.1<br>0.2 0.3<br>0.5<br>1.0<br>2.0 3.0<br>5.0<br>10<br>20<br>30<br>50<br>REVERSE VOLTAGE (VOLTS)<br>FIGURE 11 - "ON" VOLTAGES<br>FIGURE 12 - TEMPERATURE COEFFICIENTS<br>III<br>~<br>I<br>~<br>~<br>RINCforVCElsatll-<br>I--<br>l-<br>I--<br>I--<br>I..••<br>RIN8forV8E<br>,<br> <br>+0.5<br>~<br>-0.5<br>:;<br>E...<br>~<br>-1.0<br>;::;<br>f::<br>w<br>.1.5<br>c'-'<br>-2.0<br>1.0 V<br> <br><br>V8Elon)@VCE<br>= 10 V|)'||1/|||/|/|
|FIGURE 7 - FREQUENCY EFFECTS<br>FIGURE 8 - SOURCE RESISTANCE EFFECTS<br>a<br>50<br>100<br>200<br>500<br>1.0k<br>2.0k<br>5.0k<br>10k<br>20k<br>50k 100<br>RS. SOURCE RESISTANCE 10HMS)<br> 0.02<br>0.05 0.1<br>0.2<br>0.5<br>1.0<br>2.0<br>5.0<br>10<br>20<br>50<br>100<br>I. FREQUENCY 1kHz)<br>10<br>8.0<br>.,~<br>w<br>'"<br>6.0<br>:><br><.0<br>;;:<br>w<br>'"0<br>4.0<br>z~.<br>z<br>2.0<br>II<br>1111111<br>I<br>j<br>t. ;.0 ~H~ III II<br>_V_<br>I<br>I<br>1111<br>/<br>IC=50.A<br>I<br>'IOO.A<br>1\<br>500 .A<br>1/<br>_J_<br>I<br>l/<br>1.0mA<br>_J_<br>)'<br>1/<br>/<br>"-<br>~<br>...•.<br>./<br>FIGURE 9 - CAPACITANCES<br>FIGURE 1Q -<br>CURRENT.GAIN<br>BANDWIDTH PRODUCT<br>50<br>70<br>100<br>2.0<br>3.0<br>5.0<br>7.0<br>10<br>20<br>30<br>IC. COLLECTOR CURRENT ImA)<br>I I<br>VCE = 20 V<br>TJ.250C<br>"<br>'/<br>./<br>/<br>/<br>1/<br>70<br>~<br>50<br>1.0<br>t;<br>:>g<br>300<br>g:<br>or<br>:;<br>200<br>3:cz...,<br>z<br>~<br>100<br>'"~<br>'"'"_B_<br>I<br>I<br>-<br>-rr<br>-+<br>.-<br>~<br>I<br>C.b<br>r---<br>Ccb<br>t'-1--J.<br>I<br>I<br>.1<br>0.2 0.3<br>0.5<br>1.0<br>2.0 3.0<br>5.0<br>10<br>20<br>30<br>50<br>REVERSE VOLTAGE (VOLTS)<br>FIGURE 11 - "ON" VOLTAGES<br>FIGURE 12 - TEMPERATURE COEFFICIENTS<br>III<br>~<br>I<br>~<br>~<br>RINCforVCElsatll-<br>I--<br>l-<br>I--<br>I--<br>I..••<br>RIN8forV8E<br>,<br> <br>+0.5<br>~<br>-0.5<br>:;<br>E...<br>~<br>-1.0<br>;::;<br>f::<br>w<br>.1.5<br>c'-'<br>-2.0<br>1.0 V<br> <br><br>V8Elon)@VCE<br>= 10 V||"-<br>||||||

0.1 0.2 0.5 1.0 2.0 5.0 10 20 50 100 200 500 1.0 k

IC. COLLECTOR CURRENT (mA)

**Figure 3.10** _(continued)_



0.1 0.2 0.5 1.0 2.0 5.0 10 20 50 100 200 500



IC. COLLECTOR CURRENT (mAl



**92**


BIPOLAR JUNCTION TRANSISTORS **93**


The next parameter to be evaluated is the Early voltage for forward operation, _VAF._
This parameter can be calculated from the _small-signal_ _characteristics,_ which are given
as _h_ parameters, or hybrid parameters. The hybrid model is based on a two-port representation of the transistor with _iin_ and _Vo_ as the independent variables. For a transistor
in a CE configuration, _Vin_ and _io_ relate to _iin_ and _Vo_ through the hybrid parameters
_hie, hre, hfe,_ and _hoe._ A transistor can therefore be described by the following hybrid
equations:


_Vin_ = _hieiin_ + _hrevo_

(3.22)
_io_ = _hfeiin_ + _hoevo_


_hoe_ is the data sheet parameter used for evaluating _VAF._ Both a minimum and a maximum value are listed for two values of _I_ _c,_ 1 rnA and 10 rnA. The small-signal value of
_hoe_ is the slope of the _Ic- VCE_ curve at the measured _Ic_ and _VCEo_ Ideally the extrapolations of the two tangents to the _I_ c- _VCE_ curves intersect at _VCE_ = - _VAF,_ as shown in
Figure 3.7. A reasonable estimate for _VAF_ is obtained by first choosing a value between
_Min_ and _Max_ for _hoe_ at the higher current, if this current is not outside the range of the
application. Then _VAF_ is computed from geometric considerations, as in Figure 3.7.


_I_ _c_ 10- [2] A
_VAF_ = _hoe - V_ _CE_ = 102• 10-6 mho - 10 V = 100 V


The data for _hoe_ are measured at _VCE_ = 10 V.
We have now obtained the main BJT SPICE parameters for simulating the DC
behavior of transistor MPS2222. With the information presented so far about SPICE,
we can describe a measurement setup for displaying the _I_ c- _V_ _CE_ characteristics of the
BIT. The setup is shown in Figure 3.11. The corresponding SPICE input follows:

```
I-V CHARACTERISTICS OF 2N2222
```

```
Q1 2 1 0 Q2N2222
IE 0 1 .075M
VC 2 0 10
```

```
* PARAMETERS DERIVED BY HAND
```


_*_ _WI_ `TYPICAL VALUES FROM GRAPHS`
```
*.MODEL Q2N2222 NPN IS=1.14F BF=190 VAF=100
```


`*` _WI_ `MAX VALUES, NO GRAPHS`
```
.MODEL Q2N2222 NPN IS=5.25E-14 BF=190 VAF=100 RC=3.4 RB=37
.OP
.DC VC 0 10 0.5 IB 0.4M 4M 0.9M
.PRINT DC I (VCl
.END

```

**94** 3 SEMICONDUCTOR-DEVICE ELEMENTS


**Figure 3.11** Measurement setup for _!c- VCE_ characteristics.


The only statement that has not been defined so far is

```
      .DC VC 0 10 0.5 IB 0.4M 4M 0.9M

```

which defines the range over which the _V_ C supply and the base current source _IB_
are swept; this statement is described in detail in the following chapter. The plot of
the _Ic_ = _f(VCE,_ _IB)_ characteristics simulated by SPICE with the above parameters is
shown in Figure 3.12. Note that the different curves are equally spaced in the first-order
model based on a constant value of _h_ _FE,_ equal to _BF._ No _I_ C = _f_ (V _CE, I_ _B)_ characteristic is available from the data sheet for comparison with the above simulated curves; the
validity of the model can be verified for a few operating points given in the data sheet.
A slightly different approach must be followed if no graphs are available and all
parameters must be derived from the _electrical_ _characteristics_ data. The two maximum
values, _VCEsatM_ and _VBEsatM,_ are obtained from the saturation characteristics. These
values are too high for following the extraction procedure outlined above.
The difference in _VCEsatM_ for the two values of _I_ _c_ can be attributed to the ohmic
collector resistance, **RC,** the value of which is



_RC_ = _V CEsatMl_ _-_ _V CEsatM2_

ICl - _IC2_



1.2 V
(3.23)
0.35 A = 3.40



Similarly, the difference in _VBEsat_ can be attributed in large part to the voltage drop
across the parasitic base resistance, **RB,** resulting in a resistor value



_RB_ = _VBEsatMl_ _-_ _VBEsatM2_
_I_ _BI -_ _I_ _B2_



1.3 V _r\_
(3.24)
0.035 A = 37 H



The approximation of attributing the _VBEsatM_ difference to an ohmic voltage drop is
supported by the fact that it takes approximately only _VBE_ = _Vth_ = 26 mV to increase
_IB_ from 15 rnA to 50 rnA.


BIPOLAR JUNCTION TRANSISTORS 95


_IB=4.0mA_


_IB=3.1mA_
600.0


_I_ _B_ = 2.2mA
4:

E 400.0
•..•v


_I_ _B_ _=1.3mA_


200.0


_IB=400~A_


-200.0
    - 10


Figure 3.12 _Ic_ = _I (VCE,_ _In)_ characteristics of the MPS2222 npn transistor simulated
by SPICE.


Now IS can be derived from Eqs. 3.10 and 3.11 and the corrected values of _VBEsatM_
and _V CEsatM:_


_VBEsatM_ = _VBEsatMI_ _-_ _RB._ _IBI_ = 0.74 V

_VCEsatM_ = _VCEsatMI_ _-_ _RC'_ _ICI_ = 0.69 V

_IS_ = _ICle-VBEsatM/Vth_ = 0.15.3.5.10- [13] A = 5.25.10- [14] A


In the absence of the _DC current gain_ plots, _BF_ can be estimated from the _ON_
_characteristics_ table, which lists the minimum values of _h_ _FE_ for several values of _Ic._
Usually both a minimum and a maximum _hFE_ value are given for a single _I_ _c_ value,
the highest. Choose _hFEI_ in the range between _Min_ and _Max,_ closer to the minimum.
Calculate _hFE2_ and _hFE3_ at two other values of _Ic_ such that they represent the same
multiple of the corresponding minimum values as _h_ _FEI•_ _BF_ results as the average of
the three midrange values of _hFE: BF_ = 110.The extraction ofVAF is the same as the
above.
The charge-storage characteristics can be derived from the plots of _capacitances_
versus reverse voltage and _switching characteristics._ The junction capacitances, CJC
and CJE, are derived from the former characteristics, and the transit time, **TF,** is estimated from the latter. The three characteristic parameters of a junction capacitance,


**96** 3 SEMICONDUCTOR-DEVICE ELEMENTS


_ClX, MlX,_ and _VlX,_ should be evaluated from a plot of log _Cj_ versus _I_ _(Vj),_ which is
a straight line; see Eqs. 3.14. '
The above parameter extraction approach can be automated by writing a small program for repeated use. Second-order effects can be added, such as low- and high-current
behavior. The package _Parts,_ from MicroSim Corp., computes SPICE parameters for
all the supported semiconductor devices from data book characteristics. For transistor
MPS2222, _Parts_ finds the following DC parameters using typical data:


       - Q2N2222 MODEL CREATED USING PARTS VERSION 4.03 ON 08/02/91 AT 13:59

      - W/ VALUES FROM GRAPHS OR AVERAGED

       .MODEL Q2N2222 NPN(IS=15.01F XTI=3 EG=1.11 VAF=90.7 BF=223.7 NE=2.348
+ ISE=70. 78P IKF=3. 837 XTB=l. 5 BR=1 NC=2 ISC=O IKR=O RC=O CJC=2P
+ MJC=.3333 VJC=.75 FC=.5 CJE=5P MJE=.3333 VJE=.75 TR=10N TF=1N
+ ITF=O VTF=O XTF=O)


A number of parameters that are not in Table 3.2 are present in the **above. MODEL** state- ~"
ment because _Parts_ uses the complete Gummel-Poon model in the extraction. Another ~
parameter extraction package, _MODPEX,_ from Symmetry Design Systems (1992), can
scan a data sheet and generate SPICE parameters.


_Exercise_
Verify that the parameters from _Parts_ result in _Ic_ = _I_ _(VCE,_ _I_ _B)_ characteristics similar
to those in Figure 3.12.


**3.4** **JUNCTION** **FIELD EFFECT TRANSISTORS** **(JFETS)**


The general form of a junction field effect transistor (JFET) statement is


_Jname nd ng ns MODname_ _<area>_ <OFF> <IC= _vDSO,vGso>_


The letter J must be the first character in _lname;_ J identifies a JFET and can be followed
by up to seven characters in SPICE2. _nd, ng,_ and _ns_ are the drain, gate, and source nodes,
respectively.
_MODname_ is the name of the model that defines the parameter values for this transistor. Two JFET models are supported, n-channel (NJF) and p-channel (PJF). The
schematic representations of the two types of JFETs are shown in Figure 3.13. _area_ is
a scale factor equal to the number of identical transistors connected in parallel; _area_
defaults to 1. The keyword **OFF** initializes the transistor in the cut-off region for the initial iterations of the DC bias solution. By default, JFETs are initialized at the threshold
voltage, with _VGS_ = _VTO_ and _VDS_ = 0.0 for the DC solution. The keyword **IC** defines the values of the terminal voltages, _VDSO_ and _VGSO,_ at time _t_ = 0 in a time-domain
analysis. _VDSO_ and _VGSO_ are used as initial values only when the **UIC** option is present
in the • **TRAN** statement.


JUNCTION FIELD EFFECT TRANSISTORS (JFETS) **97**


_nd(D)_

_IDS_
-t


_ng_ (G)


+



_ns_ _(8)_


n-channel

**Figure 3.13** n- and p-channel JFETs.



_ns_ _(8)_


p-channel



The quadratic Shichman-Hodges model (Shichman and Hodges 1968) is used in
SPICE to solve the BCEs. The drain-source current, _IDs,_ is defined by the following
three equations for the three regions of operations, cut-off, saturation, and linear, respectively:


a for _V_ GS ::::; _VT_ 0

_(VGS - VTO)2(l_ + _LAMBDA._ _VDS)_ fora < _VGS - VTO::::; VDS_
_I_ _[_BETA]_ _DS_ _-_

{ _BETA._ _VDs(2(VGS - VTO) - VDs)(l_ + _LAMBDA._ _VDS)_

fora < _VDS_ < _VGS - VTO_


(3.25)


_VTO, BETA,_ and _LAMBDA_ are the threshold, or pinch-off, voltage, the transconductance factor, and output conductance factor in saturation, respectively. Note that
_LAMBDA_ is measured in V-I and is equivalent to the inverse of the Early voltage for
the **BJT,** introduced in Sec. 3.3.1. There is an additional current component due to the
pn junction current, characterized by the saturation current _IS._ The gate pn junctions
are reverse biased, and therefore the pn junction current is negligible.
The above equations are valid for _VDS_   - O. If _VDS_ changes sign, the behavior of
the JFET is symmetrical, the drain and the source swapping roles; _V_ GS is replaced by
_VGD,_ and _VDS_ is replaced by its absolute value in the above equations. The current _IDs_
flows in the opposite direction.
The dynamic behavior of a JFET is modeled by two charges associated with the
gate-drain, OD, and gate-source, OS, junctions, respectively. These charges are accumulated on the depletion capacitances of the two reverse-biased junctions and are
described by Eq. 3.3.



_CGS_
(l - _VGs/PB)O.5_


_CGD_
(l - _VGD/PB)O.5_



(3.26)


**98** 3 SEMICONDUCTOR-DEVICE ELEMENTS


_CGS, CGD,_ and _PB_ are the zero-bias gate-source capacitance, zero-bias gate-drain capacitance, and built-in gate junction potential, respectively. These capacitances are used
in the small-signal analysis. In the large-signal time-domain analysis the gate charges
are computed from Eq. 3.4 using Eqs. 3.26. The large-signal JFET model is shown in
Figure 3.14 and the small-signal model in Figure 3.15. The transconductance _gm_ and
the drain-source resistance _r_ _ds_ of the small-signal model are defined as follows:


_dIDs_
_gm =_ _dV_ _GS_
(3.27)
1 _dIDs_
_gds =_
_rds_ _dVDs_


_V_ _GS_ and _VD,s'_ must be used in Eqs. 3.25, 3.26, and 3.27 when _RD_ and _RS_ are nonzero.
The expression of _IDS_ appropriate t.othe region of operation (Eqs. 3.25) must be used
when deriving _gm_ and _rds'_ Note that in nOmlal operation the GD and GS diodes are
reverse biased and the corresponding small-signal conductances can be neglected.


_nd(D)_


_ns_ _(8)_

Figure 3.14 Large-signal
n-channel JFET model.


JUNCTION FIELD EFFECT TRANSISTORS (JFETS) 99


D'
_nd(D)_


_ns_ (S)
Figure 3.15 Small-signal JFET model.


The general form of the JFET model statement is


•MODEL _MODname_ NJF/PJF <VTO=VTO _<BETA=BETA ..._ »


In every model statement one of the keywords NJF or PJF, indicting the transistor type,
must be specified.
Table 3.3 summarizes the model parameters introduced so far, with the corresponding default values assigned by SPICE2.
The threshold, or pinch-off, voltage, _VTO,_ is sign-sensitive. JFETs operate in depletion mode; that is, they are _normally on._ Therefore _VTO_ is negative for n-channel
devices (NJF) and should be positive for p-channel devices (PJF). Because of a bug in
all recent versions of SPICE2, however, the sign of _VTO_ for a depletion p-channel JFET
should be entered as negative; in other words, _VTO_ for a p-channel JFET is defined with
the same sign as for an n-channel JFET. This discrepancy is present in SPICE3 as well
as PSpice.


Table 3.3 JFET Model Parameters


Name Parameter Units Default Example Scale Factor

YTO Threshold (pinch-off) voltage Y -2.0 -2.5
BETA Transconductance parameter AY-Z 10- [4] 1.0E-3 _area_
LAMBDA Channel length modulation y-I 0 1.0E-4
parameter
RD Drain ohmic resistance n 0 100 _l/area_
RS Source ohmic resistance n 0 100 _l/area_
CGS Zero-bias GS junction capacitance F 0 5P _area_
CGD Zero-bias GD junction capacitance F 0 IP _area_
PB Gate junction potential Y 1 0.6
IS Gate junction saturation current A 10- [14] 1.0E- 16 _area_


**100** 3 SEMICONDUCTOR-DEVICE ELEMENTS


_EXAMPLE_ 3.4

```
      J1 20 1 21 Mom
      .MODEL Mom NJF VTO=,-3 RD=20 RS=20

```

Jl is a normally-on n-channel JFET with parasitic series drain and source resistances. A normally-on p-channel JFET that conducts the same current as Jl in similar
bias conditions is described by the following **MODEL** statement:

```
      .MODEL Mom PJF VTO=-3 RD=20 RS=20

```

_EXAMPLE_ 3.5


Derive from the Motorola semiconductor data book the SPICE DC model parameters
for the 2N4221 n-channel JFET.


_**Solution**_
As in Example 3.3, we choose to derive the SPICE parameters from graphical data if
such graphs are available. The threshold, or pinch-off, voltage, **VTO,** is referred to as
the _gate source cutoff voltage,_ _VGS(off),_ in the data book. For the 2N4221 this value.
is readily available from the _common-source_ _transfer characteristics_ plot; the value is
_VTO_ = _VGS(off)_ = -3.5 V.
The transconductance parameter BETA can be obtained from the zero-gate-voltage
drain current, _!DSS'_ The measurement in the data book is taken at _VDS_ = 15 V, and
therefore the transistor is saturated, according to Eqs. 3.25:


_VGS - VTO_ = 3.5 V < _VDS_


From Eqs. 3.25, _BETA_ is computed as a function of _!DSS'_


4mA -2
_BETA_ = . _!DSS_
(3.5 V)2 = 0.327 rnA V
_(VGS - VTO)2_


_!DSS_ has been set at 4 rnA, which is the average between the minimum and maximum
values provided by the data sheet.

         - The last parameter of importance for DC is **LAMBDA,** the channel modulation parameter, which measures the output conductance in saturation. This value is obtained
from equating the expression of _gds,_ the small-signal DS conductance, defined by Eqs.
3.27, to _Yos,_ the common-source output admittance in the data sheet:


_gds_ = _BETA_ _.LAMBDA(VGS_ _- VTO)2_ = _Yos_ (3.28)


and



METAL-OXiDE-SEMiCONDUCTOR FiELD EFFECT TRANSISTORS (MOSFETs) **101**


_LAMBDA_ = _Y_ _[as]_ 10- [5] mho = 25. 10-3 V-I
_IDss_ 4. 10-3 A .



These values are used in Example 4.4, in the following chapter, for computing the
_ID_ = _f(VDS,_ _Vcs)_ characteristics, which can be checked against the characteristics in
the data book.


SPICE3 and PSpice additionally support a metal-semiconductor FET, or MESFET.
MESFETs can be represented by the same models as those shown in Figures 3.14 and
3.15 for JFETs. The details of the MESFET models can be found in Sec. 3.6.


3.5 **METAL-OXIDE-SEMICONDUCTOR** **FIELD EFFECT TRANSISTORS** (MOSFETs)


The general form of a metal-oxide-semiconductor field effect transistor (MOSFET)
statement is
,
_Mname nd ng ns nb MODname «L=>L>_ «W=>W> _<AD=AD> <AS=AS>_
_+_ _<PD=PD> <PS=PS> <NRD=NRD> <NRS=NRS>_ <OFF>
_+_ _<IC=VDSO, vcso, VBSO>_


The letter M must be the first character in _Mname;_ M identifies a MOSFET and can be
followed by up to seven characters in SPICE2. _nd, ng, ns,_ and _nb_ are four numbers that
specify the drain, gate, source, and bulk nodes, respectively. _MODname_ is the name
of the model that defines the parameters for this transistor. Two MOSFET models are
supported, n-channel (NMOS) and p-channel (PMOS). The schematic representations for
the two types of MOSFETs are shown in Figure 3.16. Note that a MOSFET can be
represented either as a four-terminal or three-terminal device; the bulk terminal is often


_nd(D)_ _nd(D)_ _nd(D)_ _nd(D)_

_IDS_ _IDS_ _iDS_ _iDS_
t t

+ + _t_ _t_



_V_ _DS_



_V_ _DS_



_V_ _DS_ _V_ _DS_

_nb (8)_ _ng(G)~_ _ng(G)~_ _nb (8)_



_V_ _DS_



_ng(G)~_



_ng(G)~_



_ng(G)~_



_ng(G)~_



_Vcs_ _Vcs_ _Vcs_ _Vcs_
+ +
+ +


_ns (5)_ _ns (5)_ _ns (5)_ _ns (5)_


n-channel p-channel
Figure 3.16 n- and p-channel MOSFET elements.


102 3 SEMICONDUCTOR-DEVICE ELEMENTS


omitted, because all n-channel transistors have the bulk connected to the most negative voltage and all p-channel transistors have the bulk connected to the most positive
voltage.
Up to eight geometry parameters can be specified for each MOSFET.
_Land_ _Ware_ the length and width of the conducting channel beneath the gate, between source and drain, in meters. The key letters Land Ware optional; if they are
omitted, the two values that follow _MODname_ are interpreted as length and width, in
that order. Default values can be defined as _DEFL_ and _DEFW_ in an •OPTIONS control statement (see also Section 9.5.5). The SPICE2 built-in defaults for _Land_ _Ware_
1 m; other SPICE versions may differ in the values assigned to these defaults. It is
recommended to set either _Land_ _W_ or _DEFL_ and _DEFW._
_AD_ and _AS_ are the areas, in square meters, of the drain and source diffusions of
the MOSFET. _AD_ and _AS_ multiply the bulk junction capacitance per square meter, _CJ,_
in the computation of the drain-bulk (DB) and source-bulk (SB) junction capacitances.
CJ is a model parameter defined by model _MODname._ Default values can be set at
_DEFAD_ and _DEFAS_ in an •OPTIONS statement; alternatively, in SPICE2 the defaults
of the two areas are each 100 _/Lm2._
Note that the following parameters are used only for the very accurate modeling of
MOS ICs, such as RAMs, where the operations of the memory cell, sense amplifiers,
and decoders need to be predicted reliably. This detail of geometry specification is not
necessary for first-order analysis.
_PD_ and _PS_ are the perimeters of the drain and source diffusions in meters. _PD_ and
_PS_ multiply the sidewall bulk junction capacitance per meter, _CJSW,_ in the computation
of the DB and SB junction sidewall capacitances, respectively. In SPICE2 the defaults
for _PD_ and _PS_ are zero.
_NRD_ and _NRS_ are the equivalent number of squares of the drain and source diffusions. _NRD_ and _NRS_ multiply the sheet resistance, _RSH,_ in the computation of the
parasitic drain and source series resistances, respectively. The defaults for _NRD_ and
_NRS_ are 1.
The keyword OFF initializes the transistor in the cutoff region for the initial iterations of the DC bias solution. By default MOSFETs are initialized cutoff at the limit of
turn-on, with _VGS_ = _VTO,_ the threshold voltage, _VDS_ = 0.0, and _VBS_ = -1, for the
DC solution.
The keyword IC defines the values of the terminal voltages, _VDSO, VGSO,_ and _VBSO_
at time _t_ = 0 in a time-domain analysis. _VDSO, VGSO,_ and _VBSO_ are used as initial values
only when the UIC option is present in the •TRAN statement.


3.5.1 DC Model


The most basic MOSFET model used in SPICE to describe the static BCEs of a MOSFET, the LEVEL = 1 model, is the quadratic Shichman-Hodges model (Shichman and
Hodges 1968). More complex SPICE MOSFET models, which incorporate secondorder effects, are described in Appendix A and references (Antognetti and Massobrio
1988; Vladimirescu and Liu 1981).


METAL-OXiDE-SEMICONDUCTOR FIELD EFFECT TRANSISTORS (MOSFETs) **103**


The drain-source current, _IDs,_ of an n-channel device is defined by the following
three equations for the three regions of operations cutoff, saturation, and linear, respectively:


     - for _VGS_ ::s; _VTH_



_IDS =_



_KP_ _W_ _2_
_-2_ _-(VGS_ _- VTH)_ (l + _LAMBDA._ _VDS)_ for 0 < _VGS - VTH_ :5 _VDS_
_Lefj_

_KP W_
2 _Lefj VDs(2(VGS - VTH) - VDs)(1_ + _LAMBDA._ _VDS)_

forO < _VDS_ < _VGS - VTH_


(3.29)



_whereLefj_ = _L-2.LD_ is the effective channel length corrected for the lateral diffusion,
_LD,_ of the drain and source, and


_VTH_ = _VTO_ + _GAMMA_ _( J2._ _PHI - VBs -_ _J2._ _PHI)_ (3.30)


is the threshold voltage in the presence of back-gate bias, _VBS_ < 0.0.
**VTO, KP, GAMMA, PHI,** and **LAMBDA** are the electric parameters of a MOSFET
model, representing the threshold voltage, transconductance factor, bulk threshold parameter, surface potential, and output conductance factor in saturation, respectively.
This model, similar to the JFET model, is generally applicable to FETs with minor
changes to account for the specifics of each device category. For a MOSFET the transconductance factor _KP_ depends both on the device geometry, _Wand L,_ and the process
characteristics, surface mobility, and thin-oxide thickness.
There is an additional current component, due to the pn-junction current, characterized by the saturation current, **IS,** or, equivalently, by its density, JS. The drain and
source pn junctions are reverse biased, and therefore the pn-junction currents are negligible in a first-order analysis.
The above equations are valid for _VDS_        - O. If _VDS_ changes sign, the behavior of
the MOSFET is symmetrical, the drain and the source swapping roles: _V_ GS is replaced
by _VGD, VBS_ is replaced by _VBD,_ and _VDS_ is replaced by its absolute value in the above
equations. The current _IDs_ flows in the opposite direction.
For a p-channel MOSFET the same current equations apply; the absolute values
are used for the terminal voltages and the current flows in the opposite direction.


**3.5.2** **Dynamic** **and Small-Signal Models**


The dynamic behavior of a MOSFET is governed by the charge associated with the
gate-oxide-semiconductor interface and by the charges associated with the drain and
source diffusions.


**104** 3 SEMICONDUCTOR-DEVICE ELEMENTS


Three distinct charges can be identified on the plates of the MOS capacitor: a gate,
a channel, and a bulk charge. These charges are voltage-dependent. Voltage-dependent
capacitances are always computed for the **LEVEL** = 2 and **LEVEL** = 3 models; variable
gate capacitances are computed for a **LEVEL** = I model only if the value of the thinoxide thickness parameter, _TOX,_ is specified. Details on the gate charge and capitance
formulations can be found in Appendix A.
For a first-order model it can be assumed that the three MOS charges are associated
with three constant capacitors, represented by _CGDO,_ the GD overlap capacitance per
unit channel width; _CGSO,_ the GS overlap capacitance per unit channel width; and
_CGBO,_ the GB overlap capacitance per channel length. The thin-oxide capacitance per
unit area is defined by


C = _EoxEO_ (3.31)
_ox_ _TOX_


For a first-order analysis the constant gate capacitances are specified as overlap capacitances approximated by


_CGDO_ = _CGSO_ = _~CoxL_ (3.32)

_CGBO_ = 0


where _E_ _ox_ and EO are the permitivities of Si02 and free space, respectively, and _TOX_
is the thin-oxide thickness. The actual gate capacitances, _CCD, Ccs,_ and _CCB,_ are computed i~ SPICE by multiplying _CGDO_ by _W, CGSO_ by _W,_ and _CGBO_ by _L,_ respectively.
The above approximation is appropriate for digital circuits. For analog circuits a
more careful evaluation of _CGDO_ is necessary. This capacitance has an important effect
on the bandwidth of an MOS amplifier. It is recommended to set it to zero for a transistor
biased in saturation and to the value given in Eqs. 3.32 for a transistor in the linear
region. This distinction is especially important in small-signal frequency analysis. It is
preferable to let SPICE use the voltage-dependent capacitances shown in Figure 3.17
by specifying _TOX_ in the •MODEL statement. In the three regions of operation the three
capacitances are



_CCD_ = _Ccs_ = 0, _CCB_ = _CoxWL_

_CCD_ = 0, _Ccs_ = _~CoxWL,_ _CCB_ = 0


_CCD_ = _Ccs_ = _!CoxWL,_ _CCB_ = 0



for _Vcs :::; VTH_

forO < _Vcs -_ _VTH:::;_ _VDS_

for 0 :::; _V_ _DS_ < _V_ cs - _VTH_



(3.33)



The definition of the overlap capacitances needs to be changed when voltagedependent capacitances are used. _CGDO,_ _CGSO,_ and _CGBO_ should be used to describe the actual overlap of the drain, source, and bulk by the gate, beyond the channel.
The three gate capacitances used by SPICE are computed by adding the capacitances in
Eq. 3.33 to the respective overlap capacitances:


METAL-OXiDE-SEMICONDUCTOR FIELD EFFECT TRANSISTORS (MOSFETs) **105**


14



_VCS,V_
Figure 3.17 MOSFET gate capacitances per unit channel area versus _VGs._


_CGDO_ = _CGSO_ = _!CoxLD_

(3.34)
_CGBO_ = C _foxWov_


where _LD_ is the length of the gate extension over the drain and source diffusions, C _fox_
is the field-oxide (isolation) thickness, and _Wov_ is the gate width extension beyond the
channel. Unless a very accurate simulation is needed, in which case one of the more
accurate models presented in Appendix A is recommended, one can omit the overlap
capacitances when voltage-dependent gate capacitances are used in **LEVEL** = 1.
The depletion charges are accumulated on the depletion capacitances of the two
reverse-biased junctions and are described by Eqs. 3.3:



_CBD_
_`C`_ _BD_ _`=`_
(l - _VBD/ PB)MJ_

_CBS_
(l - _VBS/ PB)MJ_



(3.35)



where _CBD, CBS, PB,_ and _MJ_ are the zero-bias bulk-drain capacitance, the zero-bias
bulk-source capacitance, the built-in bulk junction potential, and the junction grading
coefficient.
The design of LSI and VLSI circuits requires the most accurate representation of
the actual physical realization of the circuit. The DB and SB junction capacitances
have a great impact on the operation speed of an IC; SPICE2 provides the means for
an accurate specification of the junction capacitance for each device geometry and
diffusion profile. Both drain and source junction can be characterized by a bottom junction capacitance per unit area, _CJ,_ and a sidewall junction capacitance per unit length,


**106** 3 SEMICONDUCTOR-DEVICE ELEMENTS


_CJSW._ The reason for this differentiation is the smaller grading coefficient of the sidewall of the diffusion, which can make the sidewall contribution the dominant junction
capacitance.
Scaled by the device geometry parameters, _AD, AS, PD,_ and _PS,_ introduced above,
the DB and SB junction capacitances can be expressed as



_AD._ _CJ_ _PD._ _CJSW_
_CBD_ _`=`_ - - _VBDj PB)MJ_ + (1 - _VBDj PB)MJSW_

_AS . CJ_ _PS . CJSW_
_CBS_ = _-O---v-Bs-j-P-B-)M-J_ + _-O---v-Bs-j-P-B-)M-J-S-W_



(3.36)



Note that whenever both the total zero-bias junction capacitance, CBD or CBS, and the
geometry-oriented specification are available, the total capacitances take precedence.
The capacitances introduced so far are used in the small-signal analysis. In the
large-signal time-domain analysis the gate charges and bulk junction charges are computed from Eq. 3.4 using Eqs. 3.32 through 3.36; the large-signal MOSFET model is
shown in Figure 3.18.
The small-signal MOSFET model is shown in Figure 3.19. The nonlinear current
generator _IDs_ is replaced by the resistance _rds_ and transconductances _gm_ and _gmbs_ de

_nd(D)_


                     - _VBD,_ +


_ng_ (G) _IDS_ _nb_ (B)


_Q_ _GS_ _VBS'_ +


+ _VGS'_              

`S'` _Q_ _BS_


_Q_ _GB_


_Rs_


_ns_ (S)
Figure 3.18 Large-signal MOSFET model.


METAL-OXiDE-SEMICONDUCTOR FIELD EFFECT TRANSISTORS (MOSFETs) 107



_nd(D)_ _,_ " "
.,i:1

(,~ . _'.J..(_
_`R`_ _D_

_hI._,'" _J_
_CCD_ D'. _.COD_       

.•.L



f .,



"

,



_ng_ (G) _gmVgs'_ ~ _+gnrbsvbs'_ ~ _r d,_ '\ _nb_ (8)


S'



.,,1 '.


(3.37)



" f
_:l_
. Figure 3.19,Smail-signal MQSFET m,odeL
~           - _.i _I_ _~._ _-I_ _••••_ U


t . fined by the following equations:
',.



_ns(S)_



1 ~. _dI_ _Ds_
_gds_ = _rds_ _dVDS_
```
   dIDs
```

_dVGS_
```
   dIDs
```

_dVBs_



The expression of _IDS_ appropriate to the region of operation (Eqs. 3.29) must be used
when deriving _gm, gds,_ and _gmbs'_ In alLMOSFET equations terminal voltages must be
referred to nodesD' and,S' when the parasitic terminal. resistances _RD_ and _RS_ are
nonzero.
The diodes representing the drain and source junctions are modeled by the conductances _gbd_ and _gbs_ in the small-signal analysis. The values of _gbd_ and _gbs_ are computed
using Eq. 3.5 for the conductance of a diode. Usually, these diodes are turned off and

_gbd_ and _gbs_ have very small values.


108 3 SEMICONDUCTOR-DEVICE ELEMENTS


3.5.3 Model Parameters


The general form of the MOSFET model statement is


•MODEL _MODname_ NMOS/PMOS _<VTO=VTO_ _<KP=KP_ _..._       - >


In every model statement one of the keywords NMOS or PMOS, indicating the transistor
type, must be specified.
Table 3.4 summarizes the model parameters introduced so far along with the default values assigned by SPICE2. The model parameter is multiplied by the geometry
parameter listed in the Scale Factor column on the device statement. The SPICE parameters of MOSFETs are often derived from measurements of I-V characteristics of
test structures on IC wafers. The sequence is similar to the one described in Example
3.5 for a JFET, except that the characteristics are obtained from a curve tracer.


_EXAMPLE_ 3.6


The following statements are examples of MOSFET definitions in SPICE.


Ml 1 2 0 0 Mom

.MODEL Mom NMOS VTO=l.5


Ml is an NMOS transistor with no geometry data specified. The channel length, _L,_
and width, _W,_ default to 1meter; the only model parameter that is defined is the threshold voltage, VTO, and defaults are used for KP and the other parameters. LEVEL = 1
MOSFET equations are used if this parameter is absent from the • MODEL statement.
Such limited specification may be useful only for a DC analysis, where only the ratio
of _W/ L_ affects the solution, and not the individual values of Wand L. The absence of
any charge-storage elements from the above model may cause the simulator to abort a
transient analysis; see Examples 10.8 and 10.10 for details.


MN 2 1 0 0 MODN L=lOU W=20U

MP 2 1 3 3 MODP L=lOU W=40U
.MODEL MODN NMOS VTO=l KP=30U LAMBDA=.OOI CGJX)=3.45N CGS0=3.45N

.MODEL MODP PMOS VTO=-l KP=15U LAMBDA=.OOI CGJX)=3.45N CGS0=3.45N


These statements describe a CMOS inverter. The drains are connected together
at node 2, the gates are connected at node 1, the source and bulk of the NMOS are
connected to ground, node 0, and the source and bulk of the PMOS are connected to the
supply, node 3. Note that the _VTO_ specification of the PMOS incorporates the sign.


MDRIV 2 1 0 0 ENH L=lOU W=20U

MLOAD 3 2 2 0 DEP L=20U W=lOU

.MODEL ENH NMOS VTO=l LAMBDA=.005 TOX=.lU

.MODEL DEP NMOS VTO=-3 GAMMA=.5 LAMBDA=.Ol TOX=.lU


METAL-SEMICONDUCTOR FIELD EFFECT TRANSISTORS (MESFETS) 109


Table 3.4 MOSFET Model Parameters


Name Parameter Units Default Example Scale Factor

YTO Threshold voltage Y 0 1.0
KP Transconductance parameter Ay- [2] 2.0 X 10- [5] I.OE-3
GAMMA Bulk threshold parameter yl/2 0 0.5
PHI Surface potential Y 0.6 0.7
LAMBDA Channel length modulation y-I 0 I.OE-4
parameter
RD Drain ohmic resistance n 0 10
RS Source ohmic resistance n 0 10
RSH D and S diffusion sheet resistance OIsq 0 10 _`NRD`_
```
                                     NRS
```

CBD Zero-bias BD junction capacitance F 0 5P
CBS Zero-bias BS junction capacitance F 0 IP
CJ Zero-bias bulk junction bottom Fm- [2] 0 2.0E-4 _`AD`_
capacitance _`AS`_
MJ Bulk junction grading coefficient 0.5 0.5
CJSW Zero-bias bulk junction sidewall Fm- [l] 0 1.0E-9 _`PD`_
capacitance _`PS`_
MJSW Bulk junction grading coefficient 0.33 0.25
PB Bulk junction potential Y I 0.6
IS Bulk junction saturation current A 10- [14] 1.0E-I6
CGDO GD overlap capacitance per unit Fm- [1] 0 4.0E-II _W_
channel width
CGSO GS overlap capacitance per unit Fm- [l] 0 4.0E-ll _W_
channel width
CGBO GB overlap capacitance per unit Fm- [I] 0 2.0E-1O _L_
channel length
TOX Thin-oxide thickness m 00 O.lD
LD Lateral diffusion m 0 0.2D


The statements on the previous page describe an enhancement-depletion NMOS
inverter. The depletion transistor is _normally on_ and its threshold voltage is negative.


_Exercise_
Build SPICE decks for the CMOS inverter and enhancement-depletion inverter defined
above and trace the I/O transfer characteristic using the •DCstatement, introduced in
Example 3.3.


3.6 METAL-SEMICONDUCTOR FIELD EFFECT TRANSISTORS (MESFETS)


In SPICE3 the general form of a metal-semiconductor field effect transistor (MESFET)
statement is


_Zname nd ng ns MODname <area>_ <OFF> < _IC=VDSO, vGso>_


**110** 3 SEMICONDUCTOR-DEVICE ELEMENTS


The letter Z must be the first character in _Zname;_ Z identifies a MESFET only in
SPICE3. In PSpice the identification character is B. _nd, ng,_ and _ns_ are the drain, gate,
and source nodes, respectively. _MODname_ is the name of the model that defines the
parameters for this transistor. Two MESFET models are supported, n-channel (NMF)
and p-channel (PMF). The schematic representations of the two types of MESFETs are
identical to those of the corresponding types of JFETs, shown in Figure 3.13. The scale
factor _area_ is equal to the number of identical transistors connected in parallel, and defaults to 1. The keyword **OFF** initializes the transistor in the cutoff region for the initial
iterations of the DC bias solution. By default MESFETs are initialized conducting, with
_Ves_ = _VTO,_ the pinch-off voltage, and _VDS_ = 0.0 for the DC solution. The keyword
**IC** sets the terminal voltages, _VDSO_ and _Veso,_ at time _t_ = 0 in a time domain analysis. _VDSO_ and _Veso_ are used as initial values only when the **UIC** option is present in the

**. TRAN** statement.
The SPICE3 BCEs for this device are given by the Raytheon model (Statz, Newman, Smith, Pucel, and Haus, 1987). The drain-source current, _IDs,_ is given by the
following three equations for the three regions of operations, cutoff, saturation, and linear, respectively:



0 for _Ves ::; VTO_



_Ves ::; VTO_

_IDs_ = _{3(Ves_ _-_ _VTO)2_ [1 - (1 - _ALPHA_ _V~s_ J]. (l + _LAMBDA._ _VDs)_



1



for 0 < _VDs ::;_ 3/ _ALPHA_



_(3(Ves_ _-_ _VTO)2(1_ + _LAMBDA._ _VDS)_ for _VDS_ - 3/ _ALPHA_



_BETA_
(3 [=]
1 + _B(Ves_ _-_ _VTO)_ _(3.38)_



_VTO, BETA, ALPHA,_ _B,_ and _LAMBDA_ are the threshold voltage, transconductance factor, saturation voltage parameter, doping tail extending parameter, and output conductance factor in saturation, respectively.
The above equations are valid for _VDS_   - O. If _VDS_ changes sign, the behavior of
the MESFET is symmetrical, the drain and the source swapping roles: _Ves_ is replaced
by _VeD,_ and _VDS_ is replaced by its absolute value in the above equations. The current

_IDS_ flows in the opposite direction.
The dynamic behavior of a MESFET is modeled by two charges associated with
the GD and GS junctions. These charges are accumulated on the depletion capacitances
of the two reverse-biased junctions and are described by Eq. 3.3.



_C_ _es_ _=_

```
CeD =

```


_CGS_
(l - _Ves/ PB)o.5_

_CGD_
(l - _VeD/ PB)o.5_



(3.39)



_CGS, CGD,_ and _PB_ are the zero-bias gate-source capacitance, zero-bias gate-drain
capacitance, and the built-in gate junction potential, respectively. The MESFET imple

METAL-SEMICONDUCTOR FIELD EFFECT TRANSISTORS (MESFETS) **111**


mentation of these capacitances uses voltage-dependent factors that control the continuity of the equations around _V_ DS = O.
The large-signal and small-signal MESFET equivalent models are similar to the
corresponding JFET models shown in Figures 3.14 and 3.15.
The general form of the MESFET model statement is


•MODEL _MODname_ NMF/PMF _<VTO=VTO_ _<BETA=BETA_ _..._   - >


In every model statement, one of the keywords NMF or PMF must be specified for the
transistor type.
Table 3.5 summarizes the model parameters introduced so far along with the default
values assigned by SPICE3. The threshold voltage, _VTO,_ is sign-sensitive. MESFETs
operate in depletion mode, i.e., they are normally on; therefore _VTO_ is negative for
n-channel devices, NMF.


_EXAMPLE_ 3.7


Zl 1 2 3 MODZ

.MODEL MODZ NMF VTO=-3 ALPHA=l RD=20 RS=20


Zl is a normally on n-channel MESFET with parasitic series drain and source
resistances. A normally on p-channel MESFET that conducts the same current as Zl
in similar bias conditions is described by the following • MODEL statement:


.MODEL MODZ PMF VTO=3 ALPHA=l RD=20 RS=20


PSpice supports two MESFET models, both with the _MODtype_ keyword GASFET.
In addition to the Raytheon model (Statz, Newman, Smith, Pucel, and Haus, 1987)
available in SPICE3, PSpice also supports the Curtice model (Curtice 1980).


Table 3.5 MESFET Model Parameters


Name Parameter Units Default Example Scale Factor

VTO Threshold (pinch-off)voltage V -2.0 -2.5
BETA Transconductance parameter AV-2 10- `[4]` 1.0E-3 _area_
B Doping tail extending parameter V-I 0.3 0.3 _area_
ALPHA Saturation voltage parameter V-I 2 2 _area_
LAMBDA Channel length modulation V-I 0 1.0E-4
parameter
RD Drain ohmic resistance n 0 100 _l/area_
RS Source ohmic resistance n 0 100 _l/area_
CGS Zero-bias GS junction capacitance F 0 5P _area_
CGD Zero-bias GD junction capacitance F 0 IP _area_
PB Gate junction potential V 1 0.6


**112** 3 SEMICONDUCTOR-DEVICE ELEMENTS


3.7 **SUMMARY**


This chapter has described the semiconductor devices implemented in the most common SPICE programs. The SPICE analytical models and syntax for the diode, the bipolar junction transistor, and the three kinds of field effect transistors, JFET, MOSFET,
and MESFET, have been presented in detail. Examples have demonstrated the meanings and the derivations of the model parameters.
Each of the semiconductor devices is defined by an dement statement and a set of
parameters contained in a •MODELstatement. The same •MODELstatement, that is, the
same set of parameters, can be common to more than one device.
The diode is defined by the following line:


_Dname n+_ _n-_ _MODname_ _<area>_ <OFF> <IC=VDO >


The model parameters describing a diode are listed in Table 3.1 and can be specified in
statements of model typeD.
The BJT specification is


_Qname nc nb ne <ns>_ _MODname_ _<area>_ < OFF> <IC = _VBEO,VCEO>_


Two types of BJTs are supported in SPICE, NPN and PNP; the model parameters are
summarized in Table 3.2.
The format for JFETs is


_Jname_ _nd ng ns MODname_ _<area>_ <OFF> < IC=VDSO, _VGSO>_


Two types' of JFETs are available in SPICE, NJF and pJF; the model parameters can
be found in Table 3.3.
A MOSFET is defined by the following line:


_Mname ndng_ _ns nbMODname_ _«L=>L>_ < <W=> _W> <AD=AD>_ _<AS=AS>_

_+_ _<PD=PD>_ <PS= _PS> <NRD=NRD>_ _<NRS=NRS>_ <OFF>
+ <IC=VDSO, _VGSO,VBSO>_


The two types of MOSFETs supported in SPICE are the NMOSand PMOS devices; the
model parameters are listed in Table 3.4.
MESFETs are not supported in SPICE2 but are available in SPICE3, PSpice, and
most commercial SPICE programs; the syntax differs among SPICE versions. SPICE3
uses the following format:


_Zname nd ng ns MODname_ _<area>_ <OFF> <IC=VDSO, _vGSO>_


The same syntax is used also in PSpice with the sole difference that the identification
character is B. The two types of MESFET devices are NMFand PMF. The model parameters are summarized in Table 3.5.
The BJT and the MOSFET are described by very complex equations having many
parameters. The description in this chapter has not covered second-order effects. Complete equations of the semiconductor models implemented in SPICE can be found in
the book by Antognetti and Massobrio (1988) or in Appendix A.


REFERENCES **113**


**REFERENCES**


Antognetti, P., and G. Massobrio. 1988. _Semiconductor Device Modelil1;gwith. SPICE._ New
York: McGraw-Hill.
Curtice, W. R. 1980. A MESFET model for use in the design of GaAs integrated circuits. _IEEE_
_Transactions on Microwave Theory and Techniques_ MTT-28, pp. 448-456.
Getreu; 1.1976. _Modeling the Bipolar Transistor._ Beaverton, OR: Tektronix Inc.
Gray, P. R., and R. G. Meyer. 1993. _Analysis and Design of Analog Integrated Circuits._ 3d ed.
New York: John Wiley & Sons.
Grove, A. S. 1967. _Physics and Technology of Semiconductor Devices._ New York: John Wiley
& Sons.
Motorola Inc. 1988. _Motorola Semiconductors Data Book._ Phoenix, AZ: Author.
Muller, R. S., and T. I. Kamins. 1977. _Device Elettronics forlntegrated_ _Circuits._ New York:
John Wiley & Sons.. . "..  Shichman; **H.,** and D. A. Hodges. 1968. Modeling and simulation of insulated-gate fieldeffect transistor switching circuits. _IEEE Journal of Solid-State Circuits_ SC-3 (September),
pp.285-289.
Statz, H., P. Newman, I. W. Smith, R. A. Pucel, and H.A. Haus, 1987. GaAs FET device
and circuit simulation in SPICE. _IEEE Transactions on Electron Devices_ (February),
pp. 160-169.
Symmetry Design Systems. 1992. _MODPEX._ Los Altos, CA: Author.
Sze, S. M. 1981. _Physics of Semiconductor Devices._ New York: John Wiley & Sons.
Vladimirescu, A., and S. Liu. 1981. The simulation of MOS integrated circuits using SPICE2,
Univ. of California, Berkeley, ERL Memo UCBIERL M80/7 (March). :.' ;-. :,.: ".. ..,.,,~\., .-~. .,


:1' •


"



.1' 'j;



j ."



•..•.•'



" .


```
L'

```

_**Four**_


_DC_ _**ANALYSIS**_


**4.1** **ANALYSIS** **OVERVIEW**


This chapter and the following two chapters describe the different _analysis types_ performed by SPICE in its three _simulation modes,_ DC, small-signal AC, and large-signal
transient. Each simulation mode supports more than one analysis type. The specifics of
each analysis are explained in the chapters on the corresponding simulation modes.
All statements introduced in this chapter and the following two chapters, analysis
specifications and output requests, are control statements as defined in Chap. 1 and start
with a period in the first column.


**4.1.1** **Simulation Modes and Analysis Types**


The first simulation mode, DC, always computes and lists the voltages at every node
in the circuit. The DC node voltages are computed prior to an AC or transient (TRAN)
simulation. In the TRAN mode the DC solution can be specifically prohibited. DC supports the following four analysis types:


OP DC voltages and operating point information for nonlinear elements

TF Small-signal midfrequency transfer function

DC Transfer curves

SENS Sensitivity analysis


These analyses are presented in the following four sections of this chapter. The last
section describes node voltage initialization. SPICE finds the DC solution in most cases

**114**


ANALYSIS OVERVIEW **115**


without any additional information; in the situations where SPICE fails to find the DC
solution, initialization options are available.
The AC analysis described in Chap. 5 computes the frequency response of linear
circuits and of the small-signal equivalents of nonlinear circuits linearized near the DC
bias point. Two additional analysis types can be performed in the frequency domain:



**`NOISE`** Small-signal noise response analysis
```
DISTO

```

```
NOISE

```


Small-signal distortion analysis of diode and BJT circuits



In the TRAN mode SPICE computes the large-signal time-domain response of the
circuit. An initial transient solution, which is identical to the DC bias, precedes by
default a TRAN simulation. The only additional analysis in the time-domain is


**`FOUR`** Fourier analysis


The time-domain analysis is presented in Chap. 6.


**4.1.2** **Result Processingand Output Variables**


The results of the different analyses must be requested in • **PRINT** **or . PLOT** statements, introduced in Sec. 1.3.3. These statements identify circuit variables, voltages,
and currents, to be computed and stored for specific analyses. Analyses are omitted in
SPICE2 if no results are requested. SPICE3 performs the specified analyses even in
the absence of a • **PRINT or . PLOT** statement; the results are stored in a rawf ile and
can be displayed using the postprocessing utility Nutmeg. Similarly, PSpice runs the
analysis and stores the results only if a • **PRINT,** **. PLOT,** or the **proprietary.** **PROBE**
line is present in the input file; • **PROBE** saves the output results in a binary or a text
file, which is used by the graphic display program Probe.
**. PRINT** provides tabular outputs, whereas • **PLOT** generates line-printer plots of
the desired variables, as seen in Figure 1.7. The general format of the output request
statement is


**. PRINT/PLOT** _Analysis-TYPE OULvar}_ _<OULvar2 ..._        - _<ploLlimits>_


where _Analysis-TYPE_ can be **DC, AC, NOISE,** **DISTO,** **or TRAN** and is followed by up
to eight output variables _(OULvar),_ which are voltages or currents. If more than eight
output variables are desired, additional **PRINT/PLOT** statements must be used. There
is no limit on the number of output variables.
Output variables can be node voltages, branch voltages, and currents through voltage sources. A voltage output variable has the general form V _(nodel <,node2> ) ._ If
only _node}_ is present, that node voltage is stored; if two nodes are specified, the output
variable is the branch voltage across elements connected between _node}_ and _node2._
A current output variable is of the form I ( _Vname)_ where _Vname_ is an independent voltage source defined in the input circuit. The current measured by _Vname_ flows


**116** 4 DC ANALYSIS


through the source from the positive to the negative source node. PSpice provides the
convenience of identifying the current flowing through any circuit element by the expression I _<pin>_ _(Element...name)_ where _Element...name_ corresponds to an element
present in the circuit file and _pin_ must be used only for multiterminal devices, such
as transistors. I (R3 ), I (L1), and Ie (Q7) are accepted current variables in PSpice
representing the currents flowing through the resistor R1, the inductor L1, and the collector of the BJT Q7.
In AC analysis the V and the I are followed by one or more characters specifying the desired format of the complex variable. In the **NOISE** and **DISTO** analyses,
output variables are limited to the specific functions detailed in Sec. 5.3 and Sec. 5.4,
respectively.


**4.1.3** **Analysis Parameters:Temperature**


All element values specified in a SPICE deck are assumed to have been measured at a
nominal temperature, _TNOM,_ equal to 27° Celsius (300 K). The simulation of the circuit
operation is performed at the nominal temperature of 27° C. The nominal temperature
can be set to a different value using the •OPTIONS statement, described in Chap. 9.
In practical design situations the operation of the circuit must be verified over a
range of temperatures. In SPICE the circuit can be simulated at other temperatures
defined in a global statement,       - **TEMP,** with the following syntax:


**• TEMP** _tempI_ _<temp2 ..._        

The simulation is performed at temperatures _tempI,_ _temp2, ..._ when a • **TEMP** line is
present in the SPICE input file. The temperature values must be specified in degrees
Celsius. Note that if the value of the nominal temperature is not present on the • **TEMP**
line, the circuit is not simulated at _TNOM._
The effects of temperature on the values of different elements is computed by
SPICE, and the updated values are used to simulate the circuit. Resistor values are
adjusted for temperature variations by the following quadratic equation:


_value(TEMP)_ = _value(TNOM)[l_ + _tel(TEMP_ _- TNOM)_
_+_ _tc2(TEMP_ _- TNOM)2]_ _(4.1)_


where _TEMP_ is the circuit temperature, _TNOM_ is the nominal temperature, and _tel_ and
_tc2_ are the first- and second-order temperature coefficients. The behavior of semiconductor devices is affected significantly by temperature; for example, temperature appears
explicitly in the exponential terms of the _BIT_ and diode current equations (see Chap. 3),
as well as in the expressions of the saturation currents _(1s),_ built-in potentials _(cf>]),_ gain
factor _({3F),_ and pn-junction capacitance _(e])._ The detailed temperature dependence of
the model parameters of semiconductor devices is described in Appendix A.
When a circuit is analyzed at a temperature different from _TNOM,_ SPICE2lists the
TEMPERATURE- ADJUSTED VALUES for each element or model affected by tempera

OPERATING (BIAS) POINT **117**


ture. Note that SPICE3 does not support the. **TEMP** statement; the ambient temperature
must be defined on an • **OPTIONS** line.


_Exercise_
Add the statement

```
       .TEMP 100

```

to the one-transistor input file used in Example 1.3, run SPICE2, and note the differences in the model parameters and DC operating point. Which behavior of the circuit
is most affected by temperature variation?


**4.2** **OPERATING (BIAS) POINT**


The DC mode solves for the stable operating point of the circuit with only DC supplies
applied. Capacitors are open circuits and inductors are shorts in DC. The DC solution
consists of two sets of results; first, the DC bias solution, or the voltages at all nodes;
and second, the operating point information, or the current, the terminal voltages, and
the element values of the small-signal linear equivalent, computed only for the nonlinear devices in the circuit. SPICE computes and prints the bias solution prior to any
other analysis. The operating point, however, is not printed unless requested by an **.OP**
statement. The only time this information is printed without the presence of **.OP** is
when no analysis request is present in the input file. The voltages at all nodes, the total power consumption, and the current through each supply are printed as part of the
SMALL-SIGNAL BIAS SOLUTION (SSBS). Currents, terminal voltages, and smallsignal equivalent conductances of all nonlinear devices are listed in the OPERATING
POINT INFORMATION (OPI) section of the output.
The information provided by SPICE about the DC operation of a circuit is best
explained by two examples, a linear and a nonlinear circuit.


_EXAMPLE_ 4.1


Replace resistors _R_ 1 and _R_ _3_ in the bridge-T circuit of Figure 1.1, by two capacitors,
C 1 = _Cz_ = 1 _JLF._ Verify the DC solution with SPICE. The new circuit is shown in
Figure 4.1.


_**Solution**_
The DC solution for the resistive circuit was computed in Example 1.1. A capacitor
is equivalent to an open circuit in DC; therefore we expect the following DC solution:
V (1) = V (3) = 12 V; V (2) = 0 V.
The modified SPICE input file and the results of the analysis are shown in Figure 4.2. The information in the SSBS is a complete characterization of the circuit. The


**118** **4** **DC ANALYSIS**

```
      BRIDGE-T CIRCUIT

```


**1 kQ**


**Figure 4.1** **Bridge-T circuit with**
**capacitors.**



**** `CIRCUIT` `DESCRIPTION`

VI `1 0 12 AC` `1`
```
Cl 1 2 lu
C2 2 3 lu
R3 2 0 lk
R4 1 3 lk
```


 - E!'ID

```
 BRIDGE-T CIRCUIT
```

**** `SMALL` `SIGNAL` `BIAS` `SOLUTION` `TEMPERATURE` = `27.000` `DEG` `C`

```
NODE VOLTAGE NODE VOLTAGE NODE VOLTAGE NODE VOLTAGE

   1) 12.0000 2) 0.0000 3) 12.0000

  VOLTAGE SOURCE CURRENTS
  NAME CURRENT

  VI O.OOOE+OO

  TOTAL POWER DISSIPATION 0 .OOE+OO WATTS

```

**Figure** **4.2** **DC solution of bridge- T circuit with capacitors.**


OPERATING (BIAS) POINT 119


only data not computed by SPICE are the branch currents, but the node voltages and
element values are sufficient for the derivation of any current. If a specific current is
desired from SPICE, a dummy voltage source must be added in series with the element
of interest. As seen in the two DC solutions of the bridge-T circuit, Figures 1.3 and 4.2,
the currents through voltage sources are listed in the SSBS.


_EXAMPLE_ 4.2


Consider next the one-transistor amplifier of the first chapter, reproduced here in Figure
4.3. Relate the SPICE2 parameters listed under the OPI with the _BIT_ model presented
in Sec. 3.3.2. The SPICE2 results obtained in Chap. 1 are repeated in Figure 4.4 for
convenience.


_Solution_
The values of the small-signal equivalent model components of QI shown in Figure 3.9
are part of the OPI section. GMand RPI are computed according to Eqs. 3.15 and 3.17:


3
_GM_ = _IC_ = 2.1, 10- A = 8.14.10-2 mho
_Vth_ 0.0258 V


_RPI_ = _BE~:C_ = 1.23 k!1


_j_ "


RX is equal to _RB,_ the series parasitic base resistance, plus a second-order resistance
(see Appendix A for more detail), and RO is the collector-emitter output resistance. In
the absence of the Early voltage, _VAF,_ introduced in Chap. 3, RO is infinite; internally


1 kn _Rc_


+
5 v-=- _Vee_


Figure 4.3 One-transistor circuit.


**120** **4** DC ANALYSIS

```
      *******12/20/88 ******** SPICE 2G.6 3/15/83 ********17:11:05*****

      ONE-TRANSISTOR CIRCUIT (FIG. 4.3)

      **** INPUT LISTING TEMPERATURE = 27.000 DEG C

      ************************************************************************

```

      ```
      Q1 2 1 0 QMOD
      RC 2 3 1K
      RB 1 3 200K
      VCC 3 0 5
```

      ```
      .MODEL QMOD NPN
```

       ```
      .OP
```

      ```
      .WIDTH OUT=80
```

        - END
```
      *******12/20/88 ******** SPICE 2G.6 3/15/83 ********17:11:05*****

      ONE-TRANSISTOR CIRCUIT (FIG. 4.3)

```

`****` ') `SMALL` `SIGNAL` `BIAS` `SOLUTION` `TEMPERATURE` `=` `27.000` `DEG` `C`

```
      ***********************************************************************

```

```
NODE

 1)

```

```
VOLTAGE

 0.7934

```

```
NODE

```

( 2)


```
VOLTAGE

 2.8967

```

```
NODE

```

( 3)


```
VOLTAGE

 5.0000

```

```
   VOLTAGE SOURCE CURRENTS

   NAME CURRENT

   VCC -2.124D-03

   TOTAL POWER DISSIPATION 1.06D-02 WATTS
*******12/20/88 ******** SPICE 2G.6 3/15/83 ********17:11:05*****

ONE-TRANSISTOR CIRCUIT (FIG. 4.3)

**** OPERATING POINT INFORMATION TEMPERATURE = 27.000 DEG C

***********************************************************************

```

**Figure 4.4** **. OP results for one-transistor circuit.**


OPERATING (BIAS) POINT **121**



**** `BIPOLAR JUNCTION TRANSISTORS`


```
MODEL
 IB
 IC
 VBE
 VBC
 VCE
 BETADC
```

GM
```
 RPI
```

RX
```
 RO
 CPI
```

CMU
```
 CBX
 CCS
 BETAAC
```

FT


```
 Q1
QMOD
 2.10E-05
 2.10E-03
  0.793
  -2.103
  2.897
 100.000
 8.13E-02
 1.23E+03
 O.OOE+OO
 1.00E+12
 O.OOE+OO
 O.OOE+OO
 O.OOE+OO
 O.OOE+OO
 100.000
 1.29E+18

```


**Figure 4.4** _(continued)_


SPICE2 clamps the maximum resistance to _lIGMIN,_ which defaults to 10 [12] n and can
be set as an option parameter (see Chaps. 9 and 10). The small-signal capacitances, cpr
and CMU, and the corresponding cutoff frequency, FT, are also part of the bias information and are computed according to Eqs. 3.19 and 3.20. Since no values are defined for
_CJE, CJC, TF,_ or _TR,_ in the •MODEL statement the cutoff frequency, _fT,_ is infinite; this
explains the very high value of FT in Figure 4.4. The remaining capacitances, CBX and
CCS, are only relevant for second-order effects.
For more than one transistor or other nonlinear element the **OPI** is computed for
each such element.


Another example of DC operating point information is included for the depletionload NMOS inverter shown in Figure 4.5.


_EXAMPLE_ 4.3


Two important characteristic values of a logic gate are the high and low output voltages,
_VOH_ and _VOL,_ respectively. For a correctly designed enhancement-depletion (E-D) inverter, _VoH,_ which corresponds to a low _VIN,_ is equal to _VDD,_ the supply voltage. _VOL,_
however, which corresponds to high _VIN,_ depends on the model parameters of the two


**122** 4 DC ANALYSIS


5V


**Figure 4.5** Enhancement -depletion
NMOS inverter circuit.


transistors, _M[_ and _M_ _L,_ and the geometry ratio, _KR,_ of the inverter (Hodges and Jackson
1983): .


(4.2)


Find the low output voltage, _VOL,_ of the E-D inverter of Figure 4.5 using the following MOS model parameters: _VTOE_ = 1 V; _VTOD_ = -3 V; _KP_ = 20/LA/V [2] ;
_GAMMA_ = 0.5 V [1] / [2] ; and _PHI_ = _2<jJF_ = 0.6 V; where _VTOE_ and _VTOD_ are the
enhancement and depletion transistor threshold voltage, respectively. Assume that
_V_ _IN_ = _VDD_ = 5 V, _(W / L)[_ = 4, and _(W / L)L_ = 1. Verify the result with SPICE.


_**Solution**_
First calculate the threshold voltage of the depletion device taking into account the body
effect, as in Eq. 3.30:


_VTHD_ = _VTOD_ + _GAMMA_ _(_ _JPHI_ + _VOL -_ _JPHI)_

                  - 3 V + 0.14 V = - 2.86 V (4.3)


**In** the above calculation _VOL_ has only been estimated at 0.5 V in order to account for
the body effect of the depletion device. _VOL_ is calculated by equating the currents of


OPERATING (BIAS) POINT **123**


the enhancement transistor, _MI,_ and depletion transistor, _ML,_ according to Eqs. 3.29:


_1m_ = _IDL_
(4.4)


_M_ _I_ is assumed to operate in the linear region, because


_VDSI_ = _VOL_ < _VGSI -_ _VTOE_


since _VOL_ has been approximated at 0.5 V.
Substitution of the guess for _VOL_ in Eq. 4.3 yields a simple quadratic equation in

_VOL_ for Eqs. 4.4; the new solution is _VOL_ = 0.27 V. The correction in _VTHD_ has been
overestimated, but the result is very close to the SPICE solution. The current flowing
through the inverter is


These results of the SPICE2 analysis are shown in Figure 4.6. The circuit description is listed first, followed by the MOSFET MODEL PARAMETERS of transistors MI
and ML, models EMOS and DMOS. Note that only the parameter values specified in the
input file are listed, and not the default values for other parameters, such as the value of
_PHI,_ 0.6 V. For all the default values of MOSFET parameters see Table 3.4. The SSBS
and OPI list the node voltages and small-signal values of the transistors.

```
******** 12/29/88 ******** PSpice 3.02 (Mar 1987) ******** 00:11:01 ********

 E-D NMOS INVERTER

 **** CIRCUIT DESCRIPTION

****************************************************************************

```

```
MI 2 1 0 0 EMOS w=40U L=10U
ML 3 2 2 0 DMOS TtF10U L=10U
VDD 3 0 5
VIN 1 0 5
```

`.MODEL EMOS NMOS` VTO=l `KP=20U`
`.MODEL DMOS NMOS` VTO=- `3 KP=20U GAMMA=. 5`

```
.OP
```


 - END


Figure 4.6 SPICE2 input and operating point of MOS inverter.


```
 **** MOSFET MODEL PARAMETERS

           EMOS DMOS
 TYPE NMOS NMOS
 LEVEL 1.000 1. 000
 VTO 1.000 -3.000
 KP 2.00E-05 2.00E-05
 GAMMA 0.0 0.500

 **** SMALL SIGNAL BIAS SOLUTION TEMPERATURE = 27.000 DEG C

 NODE VOLTAGE NODE VOLTAGE NODE VOLTAGE NODE VOLTAGE

    1) 5.0000 2) 0.2758 3) 5.0000

  VOLTAGE SOURCE CURRENTS

   NAME CURRENT

   VDD -8.523E-005

   VIN O.OOOE+OOO

   TOTAL POWER DISSIPATION 4.26E-004 WATTS

```

`****` `OPERATING` `POINT` `INFORMATION` `TEMPERATURE` = `27.000` `DEG` `C`

```
**** MOSFETS

        MI ML
MODEL EMOS DMOS
ID 8.52E-05 8.52E-05
VGS 5.00E+00 O.OOE+OO
VDS 2.76E-01 4.72E+00
VBS O.OOE+OO -2.76E-01
VTH 1. OOE+OO -2. 92E+00
VDSAT 4.00E+00 2.92E+00
GM 2.21E-05 5.84E-05
GDS 2.98E-04 O.OOE+OO
GMB O.OOE+OO 1. 56E-05
CBD O.OOE+OO O.OOE+OO
CBS O.OOE+OO O.OOE+OO
CGSOV O.OOE+OO O.OOE+OO
CGDOV O.OOE+OO O.OOE+OO
CGBOV O.OOE+OO O.OOE+OO
CGS O.OOE+OO O.OOE+OO
CGD O.OOE+OO O.OOE+OO
CGB O.OOE+OO O.OOE+OO

```

**Figure 4.6** _**(continued)**_



**124**


DC TRANSFER CURVES **125**


The output voltage at the drain of MI agrees to two decimal points with the hand
calculation. The bias-point information contains the drain current, _Iv,_ the terminal voltages, _Vvs, VGS,_ and _VBS,_ and VTH, the back-gate bias-corrected threshold voltage. Note
that VTH for the load transistor ML is corrected to -2.92 V according to Eq. 4.3. VTH
also contains corrections due to small-size geometry for higher-level MOSFET models, as presented in more detail in the works by Antognetti and Massobrio (1988) and
Vladimirescu and Liu (1981) and Appendix A.
The small-signal characteristics for a MOSFET correspond to the small-signal
model of Figure 3.19 and are GDS, GM, GMBS, CBS, CBD, CGS, CGD, and CGB, as well
as the overlap capacitances.


**4.3** **DC TRANSFER CURVES**


This analysis computes the DC states of a circuit while a voltage or current source is
swept over a given interval. The following statement defines the source and the range
of swept values:


         - DC _V/InameI_ _startI stopI step] <V/Iname2 start2 stop2 step2>_


The voltage or current source names _VnameI, Vname2_ or _InameI, Iname2_ must be
defined in another independent source statement. SPICE allows a second source to be
varied as an outer variable. In addition to the voltage and current of an independent
source, SPICE2 and other SPICE versions allow the user to vary the value of a resistor, _Rname,_ or the temperature, _TEMP._ Any node voltage or current through a voltage
source can be defined as an output variable. The value of the output variable is evaluated
by sweeping the variables in the following order:


v/i2_value = start2
for (v/i2_value :5 stop2, v/i2_value = v/i2_value + step2)
v/iLvalue = startl
for (v/iLvalue :5 stopl, v/iLvalue = v/iLvalue + step1)
OULvar = f (viiLvalue,v/i2_value)


The value _viiI _value_ of source _VllnameI_ is swept first over the interval from _startI_ to
_stopI_ for each value, _vli2_value,_ of _Vllname2._ Source _Vllname]_ is also called the inner
variable and source _Vllname2,_ the outer variable. The variation of two sources does
not result in a comprehensive line-printer plot; the program generates one plot for each
value of the second source, the outer variable, rather than gather all curves in a single
plot. The graphic display tools Nutmeg and Probe can overcome this problem.
The output variables of interest must be requested as either a tabular print or a plot


**.PRINT** **DC** _OULvarI_ _<OULvar2_ _>_

**. PLOT DC** _OUT_varI <OULvar2_       - _<ploUimI,ploUim2>_


**126** 4 DC ANALYSIS


**In** SPICE2 if no DC output variable is defined in either print or plot format, the DC
sweep analysis is omitted.


_**Example**_
```
      .DC VIN 0.5 0.8 0.25
```

.PRINT DC V(6) V(lO,11)

. PLOT DC I (VICQ9)


The above three statements are part of a SPICE input file requiring the computation
of DC voltage and current transfer curves. The first line specifies that voltage source
VIN is to be swept from 0.5 Y to 0.8 Y in steps of 0.25 V. The second statement produces
a tabular output listing of the values of the voltage at node 6 and the voltage difference
between nodes 10 and 11. The third statement generates a line-printer plot of the current
flowing through the voltage source VICQ9, a dummy voltage source connected at the
collector of a transistor, _Q9,_ to measure the values of _Ie._
Two very common applications for using DC transfer curves are described in the
following examples.


_**EXAMPLE 4.4**_


Use PSpice and Probe to represent graphically the _IDs_ = _f(VDS,_ _VGs)_ characteristics of
the junction field effect transistor 2N4221; use the _Motorola Semiconductors Data Book_
(Motorola Inc. 1988) for the electrical characteristics. A different SPICE simulator and
plotting package can be used.


_**Solution**_
The measurement setup is shown in Figure 4.7, and from the Motorola data book we
can derive the following model parameters: _VTO_ = _VGS(ofj)_ = -3.5 Y; _BETA_ _=_
4.1, 10- [4] _A/y_ _[2]_ _;LAMBDA_ = 0.002 _y-1,RD_ = 200. The derivation of the SPICE
model parameters from data book characteristics is described in Example 3.5.


**Figure** **4.7** Measurement setup for JFET
_IDS_ = _f(V_ _Ds,_ _Yes)_ characteristics with
SPICE deck.


DC TRANSFER CURVES **127**


The SPICE input description is listed below. Note that no • **PRINT or . PLOT** lines
are necessary for graphical results in PSpice; all that is needed is a • **PROBE** statement.
Eqs. 3.25 are used to compute the current _IDS_ for values of _VDS_ from 0 to 25 V in steps
of 1 V at four values of _V_ _GS,_ _-_ 3 V, - 2 V, - 1 V, and 0 V. The range of values and
increments for the two bias sources, _VD_ and _V_ G, are defined by the •DCstatement.

```
I-V CHARACTERISTICS OF JFET 2N4221
```

```
Jl 2 1 0 MODJ
VD 2 0 25
```

VG 1 0 -2

```
.MODEL MODJ NJF VTO=-3.5 BETA=4.1E-4 LAMBDA=O.002 RD=200
```

```
*.OP
.DC VD 0 25 1 VG -3 0 1
* ONLY FOR PSPICE
.PROBE
* OTHER SPICE
*.PRINT DC I(VD)
.END

```

The output characteristics of the transistor computed by SPICE are shown in Figure 4.8. Note that in spite of using a very simple model with just basic parameters, the


5


4



«
E



3


2





5 10 15 `20` `25`


**Figure 4.8** Simulated _IDS_ = _f(VDS,_ _VGs)_ characteristics of a JFET.


**128** 4 DC ANALYSIS


computed I-V characteristics are close to those in the data book. More accurate model
parameters can be obtained using parameter extraction programs, such as _Parts_ from
MicroSim.


Another common use of DC transfer curves is for the design of logic gates, which
require a thorough characterization of the noise margins.


_EXAMPLE_ 4.5


Find the noise margins _NMH_ and _NML_ of the NMOS inverter in Figure 4.5; the gate of
transistor _M1_ is swept from 0 to 5 V. Use the parameters of Example 4.3.


_**Solution**_
The following two statements must be added to the input circuit description in Figure 4.6:

```
       .DC VIN 0 5 0.25
       .PLOT DC V(2)

```

The resulting SPICE2 plot is shown in Figure 4.9. The four voltages _VOH, VOL, VIH,_
and _VIL,_ defining the high and low noise margins, _NMH_ and _NML,_ respectively, are
marked on the plots. The input voltages _VIH_ and _VIL_ are defined by the points where
the slope of the voltage transfer characteristic is unity (Hodges and Jackson 1983). The
four voltages are: _VOH_ = 5 V, _VOL_ = 0.28 V, _VIH_ = 1.5 V, and _VIL_ = 2.5 V. These
result in


_NMH_ = _VOH -_ _VIH_ = 3.5 V


and


_NML_ = _VIL -_ _VOL_ = 2.22 V


The above values guarantee a proper operation of the E-D NMOS inverter when connected with other logic gates implemented in the same technology that is, in NMOS.
The effect of changes in the geometry of the transistors, that is, in _Wand_ _L,_ can be
easily observed in a repetition of the above analysis.
This example also shows the usefulness of a line-printer plot for an accurate reading
of the output voltages for given input voltages.


SMALL-SIGNAL TRANSFER FUNCTION **129**

```
E-D NMOS INVERTER

```

`****` `DC TRANSFER CURVES` `TEMPERATURE` = `27.000 DEG C`

```
 VIN V(2)
(*)----------- O.OOOOE+OO 2.0000E+OO 4.0000E+00 6.0000E+00 8.0000E+00

```

```
   O.OOOE+OO 5.000E+00
   2.500E-Ol 5.000E+00
   5.000E-Ol 5.000E+00
   7.500E-Ol 5.000E+00
   1.000E+00 5.000E+00
   1.250E+00 4.943E+00
```

_VIR_ `1.500E+00` `4.763E+00`
```
   1.750E+00 4.432E+00
   2.000E+00 3.866E+00
   2.250E+00 2.546E+00
```

_VIL_ `2.500E+00` `9.240E-Ol`
```
   2.750E+00 7.101E-Ol
   3.000E+00 5.923E-Ol
   3.250E+00 5.124E-Ol
   3.500E+00 4.541E-Ol
   3.750E+00 4.087E-Ol
   4.000E+00 3.721E-Ol
   4.250E+00 3.419E-Ol
   4.500E+00 3.165E-Ol
   4.750E+00 2.947E-Ol
   5.000E+00 2.758E-Ol

```



  
 
 
 





```
 VOL

```











       - .




Figure 4.9 DC transfer characteristic of NMOS inverter.


**4.4** **SMALL-SIGNAL TRANSFER FUNCTION**


At the completion of the DC bias solution the linearized network of a nonlinear input
circuit is available. For example, for a BJT SPICE has computed the values of all the
elements of the _small-signal BIT model_ shown in Figure 3.9 and listed in Figure 4.4.
The two-port characteristics of the linearized circuit can be obtained by using the


**. TF** _OUT_var V/Iname_


control statement. The output variable can assume any of the forms described for output variables on **PRINT** and **PLOT** DC statements. _VlIname_ identifies an independent
voltage or current source connected at the input of the two ports defined by the above
statement.
SPICE2 computes the gain and the input and output resistances of the two-port
circuit defined by the. **TF** statement. The gain can be a voltage or current gain, _dVo/ dVi_
or _dIo/ dIi,_ a transconductance, _dIo/ dVi,_ or a transresistance, _dVo/ dh_


**130** 4 DC ANALYSIS


An important assumption of • **TF** is that the midfrequency behavior of the circuit
is to be computed. This assumption is valid for frequencies at which charge-storage
effects can be neglected; that is, coupling capacitors are shorted and high-frequency
capacitors are open. Coupling capacitors are used to decouple amplifier stages from
each other and from signal generators for proper bias. Their values range from 1 nF
to 1 p,F. High-frequency capacitors limit the bandwidth at high frequencies and are
exemplified by transistor internal capacitances, such as C 7T and _C!L_ for a BJT and _Cos_
and _COD_ for a MOSFET. Inductors at midfrequency are assumed to be shorted or open
depending on which end of the frequency range they affect.
SPICE treats _all capacitors_ as open and _all inductors_ as shorted in the DC analysis.
Therefore, the validity of the • **TF** analysis is limited to circuits that contain only highfrequency capacitors and low-frequency inductors. A pure resistive network is assumed
in the transfer function solution.
The inclusion of a small-signal transfer function in a large-signal DC analysis needs
a few more explanations. In general, the voltage or current at any node is


where _VN_ is the DC bias value, _V_ _n_ is the amplitude, and _cjJ_ is the phase shift of
the AC signal. In the large-signal time-domain analysis _Vn_ can have any value; in
the frequency-domain analysis the assumption that the signal is small limits _Vn_ to
_Vth,_ the thermal voltage. With this assumption the AC response can be computed on
a linear network, which is a valid approximation of the nonlinear circuit as long as
it does not deviate significantly from its bias point. The additional midfrequency assumption simplifies the AC component of the signal to a real rather than complex
value.


_EXAMPLE_ 4.6


Find the two-port midfrequency characteristics of the one-transistor amplifier of Figure
4.3. Verify the results using the. **TF** analysis of SPICE2.


_**Solution**_
The midfrequency small-signal equivalent circuit of the one-transistor amplifier is
shown in Figure 4.10. The values of the linearized network can be computed using Eqs.
3.15 through 3.20 or taken directly from the OPI of transistor QI, listed in Figure 4.4.
In order that a • **TF** analysis can be performed, an input signal source must be
added to the circuit in Figure 4.3. A source in SPICE has also a DC component, which
can perturb the DC bias of the circuit; the addition of a voltage input source at the
base of QI, node 1, would change the operating point of the transistor. The easiest approach to adding a signal source without perturbing the DC state is to use a current
source _Ii_ that has a DC value of zero at the input. This source represents the AC input
signal _ii._


SMALL-SIGNAL TRANSFER FUNCTION **131**

**Figure 4.10** Small-signal midfrequency equivalent of
one-transistor amplifier.


The transfer function characteristics of the one-transistor circuit for a voltage output, _V2,_ at the collector of Ql, and a current input, _Ii,_ are the transresistance, _a_ _r,_ the
input resistance, _Ri,_ and output resistance, _R_ _a:_


_Va_ _V2_ _RB_
_ar =_ _f3F_ _Rc_ `(4.5)`
_ii_ _Ii_ _RB_ + _r71'_


_Vi_
_Ri_ _=_ _RB_ II _r71'_ `(4.6)`
_ii_


_Va_
_Ra_ _=_ _Rc_ II _r_ _a_ = _Rc_ `(4.7)`
_ia_


The voltage gain can be obtained from the transresistance transfer function:


_Va_ _`a`_ _r_
_a_ _v_ _=_ (4.8)

_Vi_ _Ri_


The following two statements must be added to the input description of Figure 4.4
for performing the transfer function analysis in SPICE2:


II 0 1
.TF V(2) II


The modified input circuit and the SPICE2 results of the analysis are shown in Figure
4.11. Note in the SSBS that the zero-valued input current source, II, does not disturb
the operating point of the circuit. The results confirm the above hand calculations.


**132** 4 DC ANALYSIS

```
      ONE-TRANSISTOR CIRCUIT (FIG. 4.3)
      **** INPUT LISTING

```

       ```
      Q1 2 1 0 QMOD
      RC 2 3 1K
      RB 1 3 200K
      VCC 3 0 5
```

       II 0 1

       ```
      .MODEL QMOD NPN
```

       .TF V(2) II

       ```
      .WIDTH OUT=80
      .END

```

```
TEMPERATURE = 27.000 DEG C

```

```
**** SMALL SIGNAL BIAS SOLUTION TEMPERATURE = 27.000 DEG C

```

```
NODE VOLTAGE

 3) 5.0000

```

```
NODE

  1)

```

```
VOLTAGE

 0.7934

```

```
NODE VOLTAGE

 2) 2.8967

```

```
VOLTAGE SOURCE CURRENTS

NAME CURRENT

VCC -2.124D-03

TOTAL POWER DISSIPATION 1.06D-02 WATTS

```

```
**** SMALL-SIGNAL CHARACTERISTICS
```

V(2) _III_
```
  INPUT RESISTANCE AT II
  OUTPUT RESISTANCE AT V (2)

```

```
= -9.939Dt04
= 1.222Dt03
= 1.000Dt03

```


**Figure 4.11** **. TF analysis results for a one-transistorcircuit.**


_**Exercise**_
**Confirm the value of the voltage gain,** _av,_ **derived above in Eq. 4.8, using a voltage**
**transfer function. A voltage transfer function can be obtained by replacing resistor** _**RB**_
**with a Thevenin equivalent at node I and specifying the added voltage source as input**
**in the . TF statement.**


SENSITIVITY ANALYSIS 133


4.5 SENSITIVITY ANALYSIS


Sensitivity analysis offers insight into the effect of the values of circuit elements and
variations of model parameters on selected output variables and hence on circuit performance. The sensitivity analysis request has the following form:


        - SENS _OULvarl_ _<OULvar2_ _..._        

where output variables _OUT_var 1, OUT_var2, ..._ are defined in the same manner as
for the •PRINT and •PLOT statements. The sensitivities with respect to every element
in the circuit and all DC model parameters of diodes and BITs are computed for each
output variable defined in the. SENS statement. No sensitivities with respect to model
parameters of IFET or MOSFET transistors are available. SPICE3 does not support this
type of analysis.
There are two sensitivity numbers listed for each parameter value: the absolute
sensitivity, _avj apj,_ and the relative sensitivity, _(avj apj)(pj/_ 100). These values reflect the sensitivities of DC voltages and currents with respect to perturbations in circuit
element values. No sensitivity analysis is available in SPICE2 for AC or time-domain
response.


_EXAMPLE 4.7_


Use SPICE2 to compute the sensitivity of the current provided by the current mirror
(Gray and Meyer 1993) shown in Figure 4.12 with respect to the circuit parameters.
Assume that _{3F_ = 100 and assign the default values to the remaining BIT model parameters.


_Solution_
The current supplied by this current source is


_Ie2 =_ _IREF_ 1.02lA = 0.98 rnA
1 + 2/ _{3F_

_IREF =_ _Vee_ _-_ _VBE(on)_ 5 - 0.7 V 1 rnA
_`REF`_ 4.3.10 [3] n


The input specification, operating point, and sensitivity results of the SPICE2
simulation are listed in Figure 4.13. First, note in the OPI section that the value of
_Ie2_ is very close to the above estimate. Second, consider the sensitivity results in the
DC SENSITIVITY ANALYSIS section. The same data are computed for each output
variable on the • SENS statement. In this example a single output variable has been requested, and all results appear under the header DC SENSITIVITIES OF OUTPUT
I (VMEAS). The four-column tabular output lists the ELEMENT NAME, ELEMENT
VALUE, ELEMENT SENSITIVITY, the absolute sensitivity in amperes or volts per

**Figure 4.12** Current mirror
current source.


unit of the respective element, and the NORMALIZED SENSITIVITY in amperes or
volts per I % variation in the value of the respective element.
The most informative data are the normalized sensitivities. For this small circuit it
is easy to spot that a I % change in the value of any of the following elements causes
roughly a 1O-ILA variation in _I_ _C2:_ the reference resistor, _REF,_ the supply, _Vcc,_ and _IS,_
the saturation current of transistors Ql and _Q2._ An increase of _REF_ and _IS_ causes _I_ C2 to

```
CURRENT MIRROR CURRENT SOURCE
```

```
REF 3 2 4.3k
Ql 2 2 0 QMOD
Q2 1 2 0 QMOD
VMEAS 3 1
VCC 3 0 5
```

```
.MODEL QMOD NPN BF=100 VA=50
```

```
.OP
.SENS I (VMEAS)
```

```
.WIDI'H OUI'=80
```

 - END


**Figure 4.13** SPICE2 sensitivity results for the current mirror.


`****` `SMALL SIGNAL BIAS SOLUTION` `TEMPERATURE` = `27.000 DEG C`

```
NODE VOLTAGE NODE VOLTAGE NODE VOLTAGE NODE VOLTAGE

   1) 5.0000 2) 0.7733 ( 3) 5.0000

   VOLTAGE SOURCE CURRENTS

   NAME CURRENT

   VMEAS 1.045E-003
     VCC -2.028E-003

  TOTAL POWER DISSIPATION 1.01E-002 WATTS

```

`****` `OPERATING POINT INFORMATION` `TEMPERATURE` = `27.000 DEG C`

```
**** BIPOLAR JUNCTION TRANSISTORS
NAME Ql Q2
MODEL QMOD QMOD
IB 9.64E-06 9.64E-06
IC 9.64E-04 1.05E-03
VEE 7.73E-Ol 7.73E-Ol
VEC O.OOE+OO -4.23E+00
VCE 7.73E-Ol 5.00E+00

```

`****` `DC SENSITIVITY ANALYSIS` `TEMPERATURE` = `27.000 DEG C`
```
DC SENSITIVITIES OF OUTPUT I(VMEAS)
     ELEMENT ELEMENT ELEMENT NORMALIZED
      NAME VALUE SENSITIVITY SENSITIVITY
                      (AMPS/UNIT) (AMPS/PERCENT)

      REF 4.300E+03 -2.415E-07 -1.038E-05
      VMEAS O.OOOE+OO -1.927E-05 O.OOOE+OO
      VCC 5.000E+00 2.649E-04 1.325E-05
Ql
      RB O.OOOE+OO O.OOOE+OO O.OOOE+OO
      RC O.OOOE+OO O.OOOE+OO O.OOOE+OO
      RE O.OOOE+OO O.OOOE+OO O.OOOE+OO
      BF 1.000E+02 1.018E-07 1.018E-07
      ISE O.OOOE+OO O.OOOE+OO O.OOOE+OO
      BR 1.OOOE+OO O.OOOE+OO O.OOOE+OO
      ISC O.OOOE+OO O.OOOE+OO O.OOOE+OO
      IS 1.000E-16 -1.028E+l3 -1.028E-05
      NE 1.500E+00 O.OOOE+OO O.OOOE+OO
      NC 2.000E+00 O.OOOE+OO O.OOOE+OO
      IKF O.OOOE+OO O.OOOE+OO O.OOOE+OO
      IKR O.OOOE+OO O.OOOE+OO O.OOOE+OO
      VAF 5.000E+Ol O.OOOE+OO O.OOOE+OO
      VAR O.OOOE+OO O.OOOE+OO O.OOOE+OO

```

**Figure 4.13** _**(continued)**_
**135**


**136** 4 DC ANALYSIS

```
       Q2
```

RB
```
           RC
```

RE
```
           BF
             ISE
             BR
            ISC
           IS
```

NE
```
           NC
             IKF
             IKR
           VAF
           VAR

```

**Figure 4.13** _(continued)_


```
 O.OOOE+OO
 O.OOOE+OO
 O.OOOE+OO
 1.018E-07
 O.OOOE+OO
-2.056E-18
 O.OOOE+OO
 1.035E-05
 O.OOOE+OO
 O.OOOE+OO
 O.OOOE+OO
 O.OOOE+OO
-8.147E-07
 O.OOOE+OO

```

```
O.OOOE+OO
O.OOOE+OO
O.OOOE+OO
1.000E+02
O.OOOE+OO
1.OOOE+OO
O.OOOE+OO
1.000E-16
1.500E+OO
2.000E+OO
O.OOOE+OO
O.OOOE+OO
5.000E+Ol
O.OOOE+OO

```

```
 O.OOOE+OO
 O.OOOE+OO
 O.OOOE+OO
 1.018E-07
 O.OOOE+OO
-2.056E-16
 O.OOOE+OO
 1.035E+13
 O.OOOE+OO
 O.OOOE+OO
 O.OOOE+OO
 O.OOOE+OO
-1.629E-06
 O.OOOE+OO

```


decrease, whereas an increase in _Vee_ brings about an increase in _Iez._ The effect of a
perturbation in _BF_ is far less important.
The number of requested output variables in sensitivity analysis should be kept
small, because a large amount of information is generated by this analysis.


**4.6** **NODE VOLTAGE INITIALIZATION**


All nonlinear electrical simulation programs compute the solution iteratively. The iterative process starts with an initial guess of the voltages. Initially SPICE assumes that
all node voltages are zero. In most cases the user does not need to specify any information about initial voltages. There are exceptions when SPICE cannot find the solution
in .the default number of 100 iterations. For these situations a node voltage initialization
statement is available with the following general format:

**.NODESET** _V(nodel)=valueI_ _<V(node2)=value2 ..._ _>_


The effect of this statement is to assign _valueI_ to the voltage of node _nadel, value2_ to
node _node2,_ and so on, in the first few solution iterations.
The final solution may differ from the values specified by • **NODESET.** SPICE2 uses
the initial values only as a guidance until it finds a first solution; the search for the DC
voltages continues, however, with the initialization constraint removed until the final
solution is reached. The final solution is probably in agreement with the • **NODESET**
values, if they are correct, but it must not be identical with them.
A good example of the use of the        - **NODESET** statement is the DC analysis of
bistable circuits. The following example shows the effect        - **NODESET** has on the final
solution.


NODE VOLTAGE INITIALIZATION **137**


_EXAMPLE_ 4.8


Find the DC solution of the flip-flop circuit shown in Figure 4.14. Use the same MOSFET model parameters as in Example 4.3.


_**Solution**_
The input specification and the bias point obtained from SPICE2 are shown in Figure
4.15. The flip-flop or bistable circuit, of Figure 4.14 has two stable operating points:
the first is with _MIl_ ON and _M12_ OFF, and the second is with _MIl_ OFF and _M12_ ON.
The solution found by SPICE2 has both inverters biased identically, with both _MIl_ and
_M_ _12_ conducting. This is a metastable state, which in reality would not last. **In** reality
the two inverters are not physically identical, and upon connecting the supply, _VDD,_ one
inverter would assume the ON state, and the other would be OFF.
The physical imbalance can be reproduced in SPICE2 by initializing the drain voltage of _MIl_ to 5 V (V (2) = 5) and the drain voltage of _M12_ to 0.25 V (V (1) = 0.25),
as listed in the modified input in Figure 4.16. The latter value is roughly equal to _VOL_
estimated in Example 4.3 for the same inverter. The solution obtained by SPICE2 in
the presence of the • **NODESET** statement and shown also in Figure 4.16 is according
to expectations. Note that the voltage at node **1,** V (1) = 0.2758, which is equal to the
solution found in Example 4.3, is a corrected value of the initial guess. The same result can be obtained by adding the keyword **OFF** to the _MIl_ line; this is equivalent to
initializing transistor _MIl_ in the OFF state.


Another approach to node voltage initialization,   - **IC,** is presented in Section
6.3 in conjunction with the time-domain analysis .• **IC** can be used to find the DC bias


**Figure 4.14** MOS flip-flop.


**138** **4** DC ANALYSIS

```
      NMOS FLIP-FLOP
```

       ```
      .WIDTH OUT=80
      .OPTION NOPAGE
```

       ```
      MIl 2 1 0 0 EMOS w=40U L=10U
      ML1 3 2 2 0 DMOS W=10U L=10U
      MI2 1 2 0 0 EMOS w=40U L=10U
      ML2 3 1 1 0 DMOS W=10U L=10U
      VDD 3 0 5
```

       ```
      .MODEL EMOS NMOS VTO=l KP=20U
      .MODEL DMOS NMOS VTO=-3 KP=20U GAMMA=.5
```

       ```
      .OP
```

       ```
      .END

```

**** `SMALL` `SIGNAL` `BIAS` `SOLUTION` `TEMPERATURE` `=` `27.000` `DEG` `C`

```
       NODE VOLTAGE NODE VOLTAGE NODE VOLTAGE NODE VOLTAGE

         1) 2.2701 2) 2.2701 3) 5.0000

```

**Figure 4.15** **SPICE2 bias solution of a MDS flip-flop without .** NODESET.

```
      NMOS FLIP-FLOP
```

** `CIRCUIT` `DESCRIPTION` `COMES` `HERE`

      ```
      .NODESET V(1)=0.25 V(2)=5
      .OP
```

       ```
      .END

```

**** `SMALL` `SIGNAL` `BIAS` `SOLUTION` `TEMPERATURE` `= 27.000` `DEG` `C`

```
       NODE VOLTAGE NODE VOLTAGE NODE VOLTAGE NODE VOLTAGE

         1) 0.2758 2) 5.0000 3) 5.0000

```

**Figure 4.16** **SPICE2 bias solution of a MOS flip-flop with .** NODESET.


SUMMARY **139**


solution; the major difference from . **NODESET** is that node voltages are forced to the
values specified by the user in the • **IC** statement and are not corrected after an initial
pass.


**4.7** **SUMMARY**
. .
This chapter has presented an overview of the SPICE analysis modes and has described
in detail the an,alysistypes of the bc mode. Analysis parameters, 'output variables, and
result processing are also outlined as part ofthe analysis overview. Examples have
shown how to apply the various DC analyses to specific circuit problems.
The DC analysis types-operating point, transfer curves, small-signal transfer
function, and sensitivity-are specified by the following control lines:

```
       .OP
```

**. DC** _V/Iname1 startl stopl stepl <V/Iname2 start2 stop2 step2>_

**. TF** _OULvar_ _V/Iname_

**.SENS** _OUT_varl <OULvar2 ... >_


With the exception of the DC operating point information, results are stored in
the output file only for specified circuit variables, _OUT_var,_ which can be voltages or
currents:


v _(nodel <,node2> )_
I _(Vname)_


The output variables for a •DC transfer curve analysis can be saved either in tabular
or line-printer plot format using the • **PRINT or . PLOT** control statement, respectively.
The general format of the output request is


**. PRINT/PLOT** _Analysis-TYPE OUT_varl <OUT_var2..._        - _<ploUimits>_


**In** the DC mode, _Analysis-TYPE_ can be only DC.
The ambient temperature for the circuit analysis is defined by


**. TEMP** _templ <temp2..._        

All circuit element values and model parameter values are defined at the nominal temperature, _TNOM,_ which defaults to 27°e.
Node voltages can be initialized for a DC computation using the following statement:


**.NODESET** _V(nodel)=valuel_ _<V(node2)=value2 ... >_


Note that the final values of the voltages at the nodes _nodel, node2, ..._ may differ from
the initialization values.


**140** 4 DC ANALYSIS


**, REFERENCES**


Antognetti, P., and G. Massobrio. 1988. _Semiconductor Device Modeling with SPICE._ New
York: McGraw-Hill.
Gray, P. R., and R. G. Meyer. 1993. _Analysis and Design of Analog Integrated Circuits._ 3d ed.
New York: John Wiley & Sons.
Hodges, D. A., and H. G. Jackson. 1983. _Analysis and Design of Digital Integrated Circuits_
New York: McGraw-Hill.
Motorola Inc. 1988. _Motorola Semiconductors Data Book._ Phoenix, AZ: Author.
Vladimirescu, A., and S. Liu. 1981. The simulation of MOS integrated circuits using SPICE2.
Memo UCBIERL _M8017_ (March).


_**Five**_


_AC_ _**ANALYSIS**_


**5.1** **INTRODUCTION**


In AC mode SPICE computes the frequency response of linear circuits. Small input
signals, with amplitudes less than the thermal voltage, _Vth_ = _kT /_ _q,_ are assumed for
nonlinear circuits that are linearized around the DC operating point. In AC the node
admittances are complex, frequency-dependent entities of the form


Y = G + _jwC_ + _1_ (5.l)
_jwL_


where _w_ = 27T _f_ is the angular frequency measured in radians per second andfis the
frequency in Hertz. In the frequency domain the voltages and currents of the circuit are
also complex numbers, called phasors:


v = _VR_ + _jVI_ = IVie [N]

IVI = _J~_ + _Vi_


4J = arctan ( ~~) (5.2)


Phasors consist of a real part, _V_ _R,_ and an imaginary part, _VI,_ and can also be expressed
as magnitude, lVI, and phase, 4J. The periodicity factor, sinwt, is implicitly assumed
for all variables in an AC analysis.


**141**


**142** 5 AC ANALYSIS


SPICE2 supports several small-signal analysis types in the frequency domain.
These are **.AC,** for a frequency sweep, presented in Sec. 5.2, • **NOISE,** for input and
output noise computation, presented in Sec. 5.3, **and. DISTO,** for analysis of distortion
due to semiconductor device nonlinearities, presented in Sec. 5.4. SPICE3 also offers
a pole-zero analysis, • **PZ,** which is described in Sec. 5.5.
Prior to an AC analysis SPICE always computes the DC operating point, which
becomes the reference for linearizing nonlinear circuit elements.


**5.2** **AC FREQUENCY** **SWEEP**


This analysis computes the values of node voltages in the circuit over a specified frequency interval. The following statement specifies the frequency interval and scale:


**•AC** _Interval numpts fstart fstop_


where _Interval_ is one of the three keywords that indicate whether the frequency varies
by decade (DEC), by octave (OCT), or linearly (LIN), _betweenfstart,_ the starting frequency, and _fstop,_ the final frequency. The variable _numpts_ specifies the number of
frequency points used per interval; for the linear interval _numpts_ is the total number of
frequency values _betweenfstart_ andfstop. This analysis provides meaningful results if
there is at least one independent source with a specified AC value in the input circuit.


_EXAMPLE_ 5.1


Describe the differences in the AC analysis for the three types of intervals.


_**Solution**_
The following three • **AC** statements cover the same frequency range but cause circuit
evaluations at different frequency points:

```
       .AC DEC 10 1K 1MEG
       .AC OCT 4 1K 1MEG
       .AC LIN 1000 1K 1MEG

```

The first statement divides the frequency interval between 1 kHz and 1 MHz into
three subintervals, with the endpoint of each subinterval being _h_ = 10 II, where _f1_ is
the starting frequency of the subinterval. The 10 frequency values in each subinterval
are selected on a logarithmic scale. The circuit is evaluated at 30 frequencies.
The second statement divides the frequency range into subintervals defined by the
following relation between endpoints: _h_ = _2f1._ Ten subintervals are needed, since
_fstop_ = _1000fstart_ and 2 [10] = 1024. The points in each interval are selected on a
logarithmic scale, four per octave. A total of 41 circuit evaluations are performed, with
the last analysis at 1.024 MHz.


AC FREQUENCY SWEEP 143


The third statement divides the frequency range in 1000 equal parts, and the frequency varies linearly _betweenfstart andfstop._ One thousand evaluations are necessary
in this analysis.
The decade is the most commonly used frequency interval, because it is consistent
with a Bode plot of the circuit response.


The results of an AC analysis can be viewed in either tabular or line-printer format
by adding one or more of the following statements:


•PRINT AC _ACOULvarl_ _<ACOULvar2_   
  - PLOT AC _AC_OUT_varl <ACOUT_var2_   - _<ploLliml, ploLlim2>_


Output variables for the AC analysis, _AC_OUT_varl, . .._ contain additional information besides the type, V or I, and the node numbers. The extra characters contained
in the output variable's name differentiate among various representations of complex
numbers, as in Eqs. 5.2. The accepted names for _ACOUT_var_ are the following:



VRor IR

VI or II


VMor IM

VP or IP


VDBor IDB



Real part of complex value


Imaginary part of complex value


Magnitude of complex number, IVI or III

Phase of complex number


Decibel value of magnitude, 20 loglO(IVI) or 20 loglO(!II)



As in DC analysis a current output variable is specified as _l(Vname)_ where _Vname_ can
be any voltage source in the circuit description.
At least one. PRINT AC or •PLOT AC statement is necessary in order for SPICE2
to perform the analysis. SPICE3 does not require an output statement, and PSpice needs
either a PRINT/PLOT line or a . PROBE line.


_EXAMPLE_ 5.2


Derive the transfer function _V3/ Vj_ of the bridge- T circuit shown in Figure 4.1, sketch
its Bode plot, and verify with an .AC analysis performed with SPICE.


_Solution_
The transfer function can be derived from the KVL and the BCE relations. For _R =_
Rj = _R_ _2_ and C = Cj = C 2 it is equal to:


_R_ _[2]_ _C_ _[2]_ _S_ _[2]_ + _2RCs_ + 1
(5.3)
_R2C2s2_ + _3RCs_ + 1


**144** 5 AC ANALYSIS


where _s_ is the complex frequency; _s_ = (J" + _jw._ The quadratic equations in the numeratorand denominator must be solved for the zeros and poles, respectively, in order
to be able to represent the Bode plot (Dorf 1989). The two zeros are equal and are

ZI = Z2 = -10 [3] rad/s, corresponding to 159 Hz. The two poles surround the double
Zeroon the negative real frequency axis and are



_PI_


_P2_ _=_



-3 + _J5_ 1
_2_ _RC_

-3 - _J5_ 1
_2_ _RC_




- 3.82, 10 [2] rad/ s -7 -61Hz



The locations of the poles and zeros point to a dip in the frequency characteristic centered around 159 Hz. Because it attenuates signals of a given frequency, this circuit is
also called a notch filter.
The SPICE input for the circuit is listed below. Note that a decadic interval is specified and the transfer function requested is from 10 Hz to 10 kHz. When this example
is run on PSpice, the • **PROBE** line should be added in order to save all the phasors of
the circuit. The • **PLOT** **AC** statement requests a line-printer plot, similar to the one of
Figure 1.7, of the magnitude in decibels, VDB ( 3 ), and the phase, VP ( 3 ), of the voltage
at node 3 to be saved in the output file.

```
BRIDGE-T CIRCUIT
*
V1 1 0 12 AC 1
C1 1 2 1u
C2 2 3 1u
R3 2 0 1k
R4 1 3 1k
```

```
.AC DEC 10 10 10k
.PLOT AC VDB(3) VP(3)
.WIDTH OUT=80
* PSPICE ONLY
*.PROBE
```

. END


The Bode plot of VDB (3) and VP (3) is reproduced in Figure 5.1. The graphical representation validates the above hand calculations. In addition to the frequency
sweep, a pole-zero analysis can be performed in SPICE3; see also Sec. 5.5.


0


-1
lD
"0
"0.a cD `-2`
'c
Clro
::2:
```
  -3

  -4

```


AC FREQUENCY SWEEP **145**


10


`5` OJ
::TQ)
(J)

5"
0 0CD
'" CD
`-5` CD (J)


-10



100 1000


Frequency, Hz
**Figure 5.1** Magnitude and phase of the bridge-T transfer function.


_**EXAMPLES.3**_


Find the frequency variation of the current gain of the one-transistor amplifier of Figure 4.3 by running an • **AC** analysis. Identify important frequency points. Add the values of the BE and BC junction capacitances to the model parameters: _CIE_ = IpF,
_CIC_ = 2pF.


_**Solution**_
The transfer function of interest is


_gm_ = _f3(jw)_ (5.4)
_g'Tr_ + _jw(_ ~~_C'T_~~ _r_ + _CIl-)_


Several statements must be added to the SPICE2 input for the one-transistor amplifier
in Figure 4.3. The equivalent small-signal circuit for the frequency sweep of the current
gain is shown in Figure 5.2 and the modified SPICE2 input in Figure 5.3.
First, the input signal source _Ii_ must be connected to the base of _Ql,_ node 1:


IIIOACI


This source has a zero DC current and therefore does not disturb the DC bias point. The
AC amplitude of lA at the input scales the resulting complex voltages and currents to
represent the transfer functions with respect to the input. A value different from **1, A**


**146** 5 AC ANALYSIS



_mom_

_Ii_
# I



+




  

_**gmVbe**_ _R_ _c_ _VMEAS_
+


```
C

```


_Ii_ _R_ _`B`_ _r"_
CT"




         -         -         -         -         -         w ~
**Figure 5.2** Current-gain amplifier: _(a)_ amplifier circuit; _(b)_ small-signal equivalent.


```
*******01/14/89 ******** SPICE 2G.6

ONE-TRANSISTOR CIRCUIT (FIG. 5.2)

```

```
3/15/83 ********17:36:16*****

```

```
**** INPUT LISTING TEMPERATURE = 27.000 DEG C

***********************************************************************
```

 ```
Q1 2 1 0 QMOD
RC 2 3 1K
RB 1 3 200K
```

VCC 3 0 5
```
II01AC1
VMEAS 4 2
CSHUNT 4 0 .1U
```

 ```
 .MODEL QMOD NPN CJE=lP CJC=2P
```

 ```
 .OP
 .AC DEC 10 O.lMEG lOG
```

 ```
 .PLOT AC IDB (VMEAS) IP (VMEAS)
 .WIDTH OUT=80
 .END

```

**Figure 5.3** SPICE2 one-transistor current-gain circuit with bias information.


`****` `BJT MODEL PARAMETERS` `TEMPERATURE` = `27.000 DEC C`

```
       QMOD
TYPE NPN
IS 1.00D-16
BF 100.000
NF 1.000
BR 1.000
NR 1.000
CJE 1.000-12
CJC 2.00D-12

**** SMALL SIGNAL BIAS SOLUTION TEMPERATURE =27.000 DEG C

```

```
NODE VOLTAGE

 4) 2.8967

```

```
NODE VOLTAGE

 3) 5.0000

```

```
NODE VOLTAGE

 1) 0.7934

```

```
NODE VOLTAGE

 2) 2.8967

```

```
VOLTAGE SOURCE CURRENTS

```


NAME

```
VCC
VMEAS

```

```
 CURRENT

- 2.124D-03
 O.OOODtOO

```

```
         TOTAL POWER DISSIPATION 1.06D-02 WATTS

       **** OPERATING POINT INFORMATION TEMPERATURE = 27.000 DEG C

       **** BIPOLAR JUNCTION TRANSISTORS

              Q1
       MODEL QMOD
```

.,'
```
       IB 2.10B-05
       IC 2.10E-03
       VBE 0.793
       VBC -2.103
       VCE 2.897
       BETADC 100.000
       GM 8.13E-02
       RPI 1.23E+03
       RX O.OOE+OO
       RO 1.00E+12
       CPI 1.72E-12
       CMU 1.29E-12
       CBX O.OOE+OO
       CCS O.OOE+OO
       BETAAC 100.000
       FT 4.30E+09

```

**Figure 5.3** _**(continued)**_
,/



**147**


**148** 5 AC ANALYSIS


or V, for the AC input amplitude proves useful when the output of a circuit needs to be
calibrated at 1 V, or 0 dB.
The zero-DC offset current source connected above and in Example 4.6 is very
useful for adding AC input signals or for purposely introducing an open circuit in DC
without SPICE2 flagging the error LESS THAN TWO ELEMENTS CONNECTED AT

_NODEx._
Second, the AC component of the output current _1_ _0_ must be separated from the DC
component and measured. A decoupling capacitor, _CSHUNT,_ connected to the collector
in parallel with _Re_ is equivalent to a short at high frequencies and an open circuit at
DC. A dummy voltage source, _VMEAS_ must be added in series with _CSHUNT_ to measure
the output current, 1 0•
Third, the zero-bias junction capacitance values must be added to the • **MODEL**
statement of the npn transistor. These capacitances together with the diffusion capacitances, which are omitted in this example, limit the gain bandwidth of the transistor.
Fourth, an AC control statement is needed. The frequency range of interest can be
estimated roughly by locating the pole of the current gain at


1 1 / 9 /
_w{3_ = _r_ rad s = 0.27.10 rad s (5.5)
_7T_ _[(C]_ _7T_ [+] [ C,..J] [ =] [ 1.23.10][3][.3.10-][12]


The value of _r_ 7T has been taken from the bias point computation in Figure 4.4, and
the zero-bias junction capacitances values have been used for C7T and CIL" This pole
corresponds to a -3-dB frequency of 43 MHz. The unity-gain frequency _iT,_ defined
in Eq. 3.20, is two orders of magnitude higher:



027.10 [9]
_iT_ = _{3F/[3_ = 100. . 27T Hz = 4.3 GHz


The frequency interval of interest is therefore between 10 MHz and 10 GHz:

```
.AC DEC 10 10MEG lOG

```

Last, the output control statement must be added:

```
.PLOT AC IDB(VMEAS) IP(VMEAS)

```


(5.6)



It produces a Bode plot of the magnitude in decibels and phase in degrees of the current
transfer function, Eq. 5.4.
The input circuit with the bias point information is listed in Figure 5.3, and the
Bode plot is shown in Figure 5.4.
In the OPERATING POINT INFORMATION _(OPI),_ section note that the values
CPI and CMU have been modified using the actual junction voltages VEE and VEC according to Eqs. 3.14, 3.18, and 3.19, C 7T has increased, because _VEE_ is positive, and _CJL_
has decreased, because _V_ _Be_ is negative. Also listed in this section is the value of the
unity-gain frequency, _iT._ This value is very close to the one computed in Eq. 5.6.


NOISE ANALYSIS **149**

```
  45

```

IDB (VMEAS)
```
  40 0

```

""0 al `35` `-20` "1J :T

""0"c :2: •• alOl(lj `2530` `-40-60` <0 .C1> III(J) C-C1> m C1> (J)


```
         20 -80

         15
                                 10 100

```

Frequency, MHz

**Figure 5.4** Bode plot for the one-transistor current-gain circuit.


The next step is to check the values of _f{3_ and _iT_ in the AC plot. The pole position,
_f{3,_ is located where


(5.7)


which translated into decibels is equal to - 3 dB below the midfrequency magnitude of
_f3F._ The phase of the current gain at _/r3_ is -45°. From the AC plot the midfrequency
magnitude of the current gain is 39.93 dB, which is approximately equal to the value
of _f3F_ = 100. The magnitude drops to 37.28 dB and the phase to -40° at 39.81 MHz.
(These accurate values are obtained with a • **PRINT AC** statement.)
The unity-gain frequency is located where the magnitude curve crosses the O-dB
mark. This frequency is between 3.98 GHz and 5 GHz. Both _/r3_ and _iT_ derived from
the AC plot confirm the above hand calculations.


**5.3** **NOISE** **ANALYSIS**


There is a lower limit to the amplitude of a signal that can be processed by electronic
circuits. This limit is imposed by the _noise_ that is generated in electronic components.
Noise characterization of a circuit can be performed by adding to each SPICE component a noise generator.
Noise generation has a random character and can be due to a number of phenomena.
The most common is the _thermal noise_ generated in resistors. Semiconductor devices
produce _shot noise, flicker noise,_ and _burst noise_ (Gray and Meyer 1993). A common


**150** 5 AC ANALYSIS


origin of the noise phenomenon is the conduction of electric current by individual carriers, electrons and holes, in semiconductor circuits. The various types of noise have
different frequency behaviors; some types cover the entire frequency spectrum uniformly and are also known as _white noise,_ whereas other types are greater at one end
of the spectrum than at the other.
SPICE models noise in resistors and all semiconductor devices. Capacitors, inductors, and controlled sources are noise-free. The noise current or noise voltage generators
associated with different elements are characterized by a mean-square value, _{i_ or _v_ _[2]_ _,_
respectively. A mean-square value is used for noise sources because the phenomena
underlying the charge-flow mechanism are random. The noise generators of the different elements in a circuit are uncorrelated. The total effect of all the noise sources at
the output of the circuit is obtained by adding all the mean-square values of the noisy
elements reflected at the output:


_n_

_V~ut_ = ~ _vt_ (5.8)
i=1


Noise-source values are proportional to the frequency bandwidth, _I::..f,_ of the measurement. A useful measure is the spectral density, _v_ _[2]_ _/ I::..f_ or _{i/_ _I::..f,_ of the noise source.
The spectral density is measured in V [2] /Hz or A [2] /Hz.
The best known noise behavior of an electronic component is the generation of
thermal noise in a resistor. The theoretical mean square of the noise voltage source in
series with the noise-free resistor (see Figure 5.5) is given by


Vk = _4kTR/1f_ (5.9)


where _k,_ equal to 8.62.10- [5] eV/K, is Boltzman's constant; Tis the absolute temperature,
measured in degrees Kelvin; _R_ is the resistance; and _I::..f_ is the frequency bandwidth


G IR.2


**Figure 5.5** Noise source
of a resistor.


NOISE ANALYSIS **151**


of the measurement. Another way of representing the noise contribution is to connect a
current generator in parallel with mean-square value


_i_ _[2]_ _`R-`_ _-_ _4kTGtif_ (5.10)


with G = 1/ _R,_ as shown in Figure 5.5. The latter approach is used in SPICE because
of the ease of adding the contribution of current generators in nodal equations.
The major source of noise in semiconductor devices is associated with the flow of
DC current and is known as _shot noise._ The small-signal equivalent model of a _BIT_
with the shot noise sources of the base and collector currents, _i~,_ and _i~,_ is shown in
Figure 5.6. The mean-square value of each source is proportional to the corresponding
DC current, _IB_ or _Ie:_



_i~_ = _2qI_ _B_ _tif_
G = _2q_ _[I]_ _e_ _tif_



(5.11)


(5.12)



The mean-square values of the noise sources are small compared to the thermal
voltage, _Vth,_ and therefore the analysis can be performed on the linear equivalent of
a nonlinear circuit. The noise analysis is performed by SPICE in conjunction with an
.AC request; both the .AC and the •NOISE control statements must be present in the
input file. SPICE computes the output noise voltage at a specified output and an equivalent input noise voltage or current, depending on whether the circuit input is defined
by a voltage or current source, respectively. The equivalent input noise is obtained by
dividing the output noise by the transfer function of the circuit and represents the measure of all noise sources concentrated in a single noise source at the input. Additionally,
a report on each noise source's contribution can be generated by SPICE2 at specified
frequencies. This report can produce a large amount of printout.
The general form of the •NOISE control statement is


.NOISE V _(nl<,n2»_ _V/Iname nums_

which defines the two-port connections of the circuit for the noise computation; _V(nl_ <,
_n2»_ defines the output port as a voltage between nodes _nl_ and _n2._ If only one node


B


+

_Ii_ _r"_


Figure 5.6 Noise sources of the one-transistor amplifier.


152 5 AC ANALYSIS


is specified, the output is between it and ground. The input of the two-port circuit
is identified by an input source, VII _name,_ which can be a voltage or current source
and must be present in the circuit description. SPICE2 can list the individual contribution of each noise generator at given frequencies; a summary of each noise source
value is listed in the result file once every _nums_ frequency points in the _intervalfstart_
to _fstop,_ the frequency interval specified in the .AC statement. The number of noisesource summaries for a DECinterval with _numpts_ frequency points per decade and a
number of frequency decades in the _intervalfstart_ to _fstop_ equal to _decades_ is equal to
_decades'_ _numptsj nums_ + 1. A zero or the absence of a value for _nums_ disables the
individual noise-source report.
The results of a noise analysis can be requested in tabular form with a •PRINT
statement or as a line-printer plot with a •PLOT statement. The general form of the
output request is


•PRINT NOISE ONOISE < (MtDB) > <INOISE < (MtDB) > >

.PLOT NOISE ONOISE«MtDB)        - <INOISE«MtDB»>


ONOISE represents the total noise voltage, _V(nl_ <, _n2»,_ at the output nodes defined in
the •NOISE statement, and INOISE is the equivalent input noise, voltage or current,
at _Viiname,_ also defined by the .NOISE line. At least one resulting noise value must
appear on a •PRINT or •PLOT NOISE statement. The optional qualifiers differentiate
between magnitude, M, which is the default, and decibels, DB.The output noise and the
input noise are computed at all frequencies betweenfstart _andfstop,_ as specified in the
•ACstatement.


_EXAMPLE 5.4_

```
       .AC DEC 10 1K 100MEG
       .NOISE V(ll) VIN1 10

```

The above two statements define the frequency interval, from _fstart_ = 1 kHz to
_fstop_ = 100 MHz; define the two-port circuit, of which the input is VINl and the
output is node 11; and request six noise-source summaries, one for each decade. No
output is generated in the absence of a •PRINT or •PLOT statement for ACor NOISE.
If, in addition, the value 10 is missing from the •NOISE statement, then SPICE2 does
not generate any output related to the two statements.
The addition of the statement

```
       .PLOT NOISE ONOISE

```

to the above two statements causes SPICE2 to produce a line-printer plot of the total
_root-mean-square (rms)_ value of the output voltage noise at node 11.


NOISE ANALYSIS **153**


_**EXAMPLE**_ _5.5_


Compute the contribution of each noise source to the output voltage noise, the total
output noise, and the equivalent input noise for the one-transistor amplifier in Figure
5.2 without the _VMEAS, CSHUNT_ net. Check your results with SPICE2.


_**Solution**_
The noise sources are shown in the small-signal equivalent circuit of the one-transistor
amplifier in Figure 5.6. The values of all noise sources can be computed using the
definitions ofthermal and shot noise, Eqs. 5.9 to 5.12:


~ _a_ _R}_ = _4kTRB_ = 1.6, 10- [20] .2. 105 _y_ _[2]_ _/Hz_ = 3.2, 10- [15] _y_ _2/Hz_


2
_~R;_ = _4kTRc_ = 1.6, 10- [20] . 10 [3] _y_ _[2]_ _/Hz_ = 1.6, 10- [17] _y_ _[2]_ _/HZ_


.2 _2_
_~f_ = _2qIB_ = 2.1.6.10-19.2.1.10-5 _A_ _[2]_ _/Hz_ = 6.72.10- [24] _A_ _/Hz_

_~f_ '2 = _2qIc_ = 2.1.6, 10- [19 ] .2.1 . 10- [3] _A_ _[2]_ _/Hz_ = 6.72 . 10- [22] _A2/Hz_


The contribution of each of the above sources to the output noise voltage is calculated next. The contribution of the noise sources connected at the base of the transistor
can be obtained by multiplying the mean-square values of _i~b_ and _i~_ by the square of the
transfer function _VolIi._ The value of the transfer function at mid-frequency, as defined

in Sec. 4.4, is


The contribution of the noise sources connected to the collector is obtained by multiplying _i~c_ and _i~_ by the square of the output resistance. All contributions to the output
noise voltage are spectral densities of the mean-square values.
First, the contributions of the two BJT noise currents are evaluated:


_72R2_
_l~f_ = 6.72.10- [16] _y_ _[2]_ _/Hz_


_~A2_
_l~/_ = 6.72.10-14 _y2/Hz_


**154** 5 AC ANALYSIS


The noise contributed by the base current at the output is significant because the current
amplification available in BITs is high. For this reason low-noise amplifiers often use
PETs in the input stage.
Second, the noise seen at the output due to _R_ _c_ and _RB_ is:


_Va3_ 2
_!J.j_


The total mean-square output noise voltage v~ is the sum of the mean-square values of
all contributions, resulting in


2 I 4
_Va_ ___ ""2                   - 6 9'10- [14] y2/
_!J.j_ _-_ _!J.j ~_ _Von_ _-_ .7 Hz


or 2.6. 10- [7] Y/ Jlh, expressed as an rms value.
The following two statements must be added to the SPICE2 input used in the AC
sweep (Example 5.3), in order to have a noise analysis performed:

```
       .NOISE V(2) II 10
       .PLOT NOISE ONOISE INOISE

```

The element lines VMEAS and CSHUNT must be deleted since an output voltage must be
sampled. The • **NOISE** statement defines node 2 as the noise output and current source
I I as the noise input. One summary report of each noise source is computed for each
frequency decade. A frequency sweep of the total output noise voltage and equivalent
input noise current is also requested.
The input circuit, the summary report printed by SPICE2 of the noise analysis at
100 kHz, and the frequency variation of the rms values of _va/_ _!J.j_ and _iieq/_ _!J.j_ computed
from 100 kHz to 10 GHz are listed in Figure 5.7.
Below the NOISE ANALYSIS header are the mean-square values of all individual noise sources computed at the output. The FREQUENCY precedes each such report.
The RESISTOR SQUARED NOISE VOLTAGES are in agreement with the hand calculations. All noise sources associated with a **BJT** and their values are listed under
TRANSISTOR SQUARED NOISE VOLTAGES. The parasitic terminal resistors, **RB,**
**RC,** and **RE,** generate thermal noise, which is equal to zero in this case because no
parasitic resistances have been specified in the •MODEL statement. The shot noise contributions from IB and IC are in agreement with the hand calculations. The last noise
source of a _**BIT,**_ FN, is the _flicker_ _noise_ component, which is described in more detail
in the reference text by Gray and Meyer (1993).
Each NOISE ANALYSIS summary ends with the mean-square and rms values of
TOTAL OUTPUT NOISE VOLTAGE; TRANSFER FUNCTION VALUE: V(2l/II


```
*******02/03/89 ******** SPICE 2G.6

ONE-TRANSISTOR CIRCUIT (FIG. 5.2)

```


**NOISE** **ANALYSIS** **155**

```
3/15/83 ********11:40:54*****

```


******** `INPUT` `LISTING` `TEMPERATURE` `=` `27.000` `DEG` `C`

```
***********************************************************************
```

 ```
Q1 2 1 0 QMOD
RC 2 3 1K
RB 1 3 200K
VCC 3 0 5
```

II 0 1 AC 1

```
.MODEL QMOD NPN CJE=lP CJC=2P
```

```
.OP
.AC DEC 10 O.lMEG lOG
.NOISE V(2) II 10
```

```
.PLOT NOISE ONOISE INOISE
.WIDTH OUT=80
.END
*******02/03/89 ******** SPICE 2G.6 3/15/83 ********11:40:54*****

ONE-TRANSISTOR CIRCUIT (FIG. 5.2)

```

******** `NOISE` `ANALYSIS` `TEMPERATURE` `=` `27.000` `DEG` `C`

```
***********************************************************************

   FREQUENCY = 1.000D+05 HZ

```


********

```
TOTAL

```

```
RESISTOR SQUARED NOISE VOLTAGES (SQ V/HZ)

     RC RB
   1.646D-17 8.130D-16

```


******** `TRANSISTOR` `SQUARED` `NOISE` `VOLTAGES` `(SQ V/HZ)`


```
RB
RC
RE
IB
IC
```

FN
```
TOTAL

```

```
  Q1
O.OOOD+OO
O.OOOD+OO
O.OOOD+OO
6.612D-14
6.693D-16
O.OOOD+OO
6.679D-14

```

```
**** TOTAL OUTPUT NOISE VOLTAGE

   TRANSFER FUNCTION VALUE:
    V(2)/II
   EQUIVALENT INPUT NOISE AT II

```

```
 6.762D-14 SQ V/HZ
2.600D-07 V/RT HZ

9.904D+04
2.625D-12 /RT HZ

```

_**(continued**_ _**on next page)**_



**Figure 5.7** **Results of one-transistor** **amplifier noise analysis.**


```
*******02/03/89 ******** SPICE 2G.6 3/15/83 ********11:40:54*****
ONE-TRANSISTOR CIRCUIT (FIG. 5.2)
```

`****` `INPUT` `LISTING` `TEMPERATURE` = `27.000` `DEG` `C`


```
***********************************************************************
 LEGEND:
*: ONOISE
```

**+:** `INOISE`
```
   FREQ ONOISE
*)------------- 1.000D-10 1.000D-09 1.000D-08

```

```
+)------------- 1.000D-12

1.000D+05 2.600D-07
1.259D+05 2.595D-07
1.585D+05 2.587D-07
1.995D+05 2.574D-07
2.512D+05 2.554D-07
3.162D+05 2.523D-07
3.981D+05 2.476D-07
5.012D+05 2.407D-07
6.310D+05 2.309D-07
7.943D+05 2.175D-07
1.000D+06 2.003D-07
1.259D+06 1.799D-07
1.585D+06 1.574D-07
1.995D+06 1.343D-07
2.512D+06 1.123,D-07
3.162D+06 9.245D-08
3.981D+06 7.520D-08
5.012D+06 6.067D-08
6.310D+06 4.868D-08
7.943D+06 3.892D-08
1.000D+07 3.105D-08
1.259D+07 2.473D-08
1.585D+07 1.968D-08
1.995D+07 1.566D-08
2.512D+07 1.245D-08
3.162D+07 9.905D-09
3.981D+07 7.883D-09
5.012D+07 6.278D-09
6.310D+07 5.007D-09
7. 943D+07. 4. 002D-09
1.000D+08 3.209D-09
1.259D+08 2.587D-09
1.585D+08 2.102D-09
1.995D+08 1.727D-09
2.512D+08 1.441D-09
3.162D+08 1.226D-09
3.981D+08 1.069D-09
5.012D+08 9.564D-10
6.310D+08 8.774D-10
7.943D+08 8.230D-10
1.000D+09 7.855D-10
1.259D+09 7.590D-10
1.585D+09 7.388D-10
1.'995D+09 7.211D-10
2.512D+09 7.028D-10
3.162D+09 6.807D-10
3.981D+09 6.521D-10
5.012D+09 6.147D-10
6.310D+09 5.675D-10
7.943D+09 5.111D-10
1.000D+10 4.485D-10

```

**Figure 5.7** _**(continued)**_


```
 1.000D-09 1.000D-08 1.000D-07 1.000D-06
```

- - - [- - -] - [- - - - - - - - - -] - - - - - - ```
 3.162D-12 1.000D-ll 3.162D-ll 1.000D-10
```

- - - - - - - - - - - - [- -][ -][ - -]
```
  + *
  + *
  + *
  + *
  + *
  + *
  + *
  + *
  + *
  + *
  + *
  + *
  + *
  + *
  + .*
  + *
  + *
  + *
  + *
  + *
  + *
  + *
  + *
  + *
  + .*
  + *
  + * .
  + *
  + *
  + *
  + *
  + *
```

**+.** `*`
**+.** `*`
```
   + *
   +*
   *+
   * +
   * . +
   * . +
   * . +
  * +
  * +
  * +
  * +
  * +
 * +
 * +
 * +
 * +
* +
```

    - - - -     - - - - - - - - 


**156**


------- -----~--~------

DISTORTION ANALYSIS **157**


at the corresponding frequency; and the EQUIVALENT INPUT NOISE AT II. One
such summary is printed also for I MHz, 10 MHz, 100 MHz, I GHz, and 10 GHz; these
summaries have been omitted from Figure 5.7.
In the frequency plot entitled AC ANALYSIS, the output noise voltage, ONOISE, is
seen to fall off above 1 MHz, and the equivalent input noise, INOI SE, increases starting
at 158 MHz. The falloff of the output noise voltage is due to the 3 dB/octave roll-off
of the transfer function, _Avi,_ and the increase in equivalent input noise, proportional to
/2, is due to the frequency dependence of the current gain, (3 _(jw)._


_Exercise_
Explain the difference between the - 3-dB frequency obtained in the AC frequency
sweep, Example 5.3, and the - 3-dB frequency obtained in the above analysis.


**5.4** **DISTORTION** **ANALYSIS**


The signal applied to an active circuit is distorted because of a number of causes such
as nonlinear elements and limiting. For small signals the cause of small distortions is
the nonlinear I-V characteristic of semiconductor devices. SPICE2 and SPICE3 compute several harmonic distortion characteristics using AC small-signal analysis. This
analysis is not available in PSpice.
The distortion measures derived below are computed for nearly linear circuits, operating at the bias point and at midfrequency, where capacitances and inductances can
be neglected. The output signal, _So,_ a voltage or a current, can be expressed as a power
series of the input signal, _Si:_


(5.13)


where _ai, a2, a3, ..._ are constants. _al_ is the transfer function at midfrequency computed
by SPICE2 as part of the • **TF** or • **AC** analysis.
Harmonic distortion is generated in the circuit when one or more sinusoidal signals
are applied at the input, such as


When _Si_ is replaced by SI _coswltin_ Eg. 5.13, signals of frequencies _2Wl_ and _3Wl_ (and
higher) are generated, representing the _second_ and _third harmonic_ _distortion_ terms.
When a second signal is also present in the input signal,


_Si_ = SI _COSWjt_ + _S2cosw2t_ (5.14)


_intermodulation_ _distortion_ terms of frequencies _(WI_ + _W2)_ and _(WI - W2)_ are generated as well. These terms are called _sum_ and _difference_ _second-order_ _intermodulation_


**158** 5 AC ANALYSIS


components. The third-order term in the power series of Eq. 5.13 produces third-order
intermodulation terms at frequencies _(2wz_ :t _wd_ and _(2w]_ :t _wz)._
The following quantities are computed by SPICE2 as a measure of the different
distortion components. _HD2_ is the fractional second-harmonic distortion, of frequency
_2w]_ in the absence of the second signal, and is equal to


_HD2_ = amplitude of second-harmonic distortion signal
(5.15)
amplitude of fundamental


The expression of _HD2_ as a function of the power series coefficients is derived by
replacing 8i in Eq. 5.13 by 8] _cosw]t_ and ordering the terms of the fundamental and
the harmonics.
The normalized third-harmonic distortion magnitude, _HD3,_ is computed similarly,
using the amplitude of the third-harmonic distortion signal.
The second-order sum and difference intermodulation components, _81M2_ and
_DIM2,_ respectively, are computed from the following equation and under the assumption that two signals are present at the input:


_1M2_ = amplitude of second-order intermodulation component
(5.16)
amplitude of fundamental


The last distortion measure computed by SPICE2 is _DIM3,_ the normalized thirdorder intermodulation component of frequency _(2w] - wz)._
Associated with each component of the small-signal equivalent model of a transistor is a distortion contribution at the output of the circuit. Each distortion contribution
is computed as distortion power in a designated load resistor; the total harmonic distortion of a given order is obtained by summing up all individual contributions. The small
distortions measures defined above are computed by SPICE2 in conjunction with an
AC small-signal analysis; both an • **AC** and a • **DISTO** statement must be present in the
input file.
The general form of the distortion control statement is

**.DISTO** _RLname <nums <hi_ II _<Pre!_ <8z»»

_RLname_ is the name of the load resistor for computing the power contribution of the
distortion. A resistor with the same name must be present in the input file. A summary of each distortion source in the circuit is listed in the result file once every _nums_
frequency points in the interval from _fstart_ to _fstop,_ the frequency interval specified
in the       - **AC** statement. The number of summaries can be related to the type of frequency interval, specified in the **.AC** statement; for a **DEC** interval with _numpts_ frequency points per decade, and _decades_ decades in the interval from _fstart_ to _fstop,_
_decades'_ _numptsl nums_ + 1 summaries are printed. A zero or the absence of a value
for _nums_ disables the report on individual distortion sources.
The expressions _hi_ II and 8z define the frequency, _h,_ and amplitude, 8z, of the
second input signal, 8z _coswzt,_ in Eq. 5.14 for the evaluation of the intermodulation
distortion terms. The frequency of the first signal, _f],_ is the frequency being swept in


DISTORTION ANALYSIS **159**


the AC analysis. If _hi_ _fl_ is not specified, a value of _hi_ It = 0.9 is used by SPICE2
and 52 defaults to 1.
The variable _P ref_ is the power used as reference in the computation of the
distortion-power terms in resistor _RLname._ The power of the output signal, _Va,_ measured in the load resistor _RL_ is


(5.17)


By default SPICE2 uses 1 mW for _P_ _ref._ For a given value of _RL_ both the amplitude _Va_
and 51 can be calculated, which serve as reference for deriving the distortion measures
_HD2, HD3, ..._ according to Eqs. 5.15 and 5.16. Example 5.7 provides more insight into
the derivation of the distortion components of the one-transistor amplifier.
The frequency sweep of the distortion components can be requested in tabular form
with a • **PRINT** statement or as a line-printer plot with a • **PLOT** statement. The general
form of the output request is


**.PRINT** **DISTO** `HD2«x) > HD3«x)>` `SIM2«x) > DIM2«x) >`
+ `DIM3«x) >`

**.PLOT** **DISTO** `HD2«x) > HD3«x»` `SIM2«x) > DIM2«x)` `>`
+ `DIM3<` _(x) >_


**HD2, HD3, SIM2, DIM2,** and **DIM3** have the meanings defined above, and _x_ stands
for any of **R,** for real; I for imaginary; **M,** for magnitude, which is the default; P, for
phase; and **DB,** for logarithmic representation. At least one distortion term must appear
on a • **PRINT** or • **PLOT DISTO** statement. The distortion terms are computed at all
frequencies _betweenfstart_ _andfstop_ as specified in the **.AC** statement.


_EXAMPLE_ 5.6

```
.AC DEC 10 1K 100MEG
.DISTO ROUT 20 0.95 1M 0.5

```

The above two statements request the computation of the small distortion measures
in the load resistor ROUT over a frequency interval from 1kHz to 100 MHz. The output
produced by SPICE2 will consist of three summaries of all distortion sources and the
total distortion terms **HD2, HD3, SIM2, DIM2,** and **DIM3** at 1 kHz, 100 kHz, and 10
MHz. The value 20 in the • **DISTO** statement establishes the summary to be printed
once every 20 frequency points resulting in the three summary frequencies mentioned
above; according to the **.AC** statement specification there are 10 frequency points per
decade.
The rest of the data in the • **DISTO** statement define the second signal and reference
output power level, _Pret._ The frequency of the second signal _12_ is set to _0.95fl,_ and


**160** 5 AC ANALYSIS


the amplitude is 0.5. _Pref_ is used to scale the distortion terms that the output voltage
amplitude of the fundamental is equal to


If _P_ _ref_ = I mW, the logarithmic values of the distortion components can be expressed
in terms of _dBm,_ a unit often used in telecommunications:


_dBm_ distortion = _20logHD_


where 1 mW corresponds to 0 dBm. It should be noted that referencing distortion to the
output power level uniquely determines the amplitude of the input signal producing that
distortion. The value of _P_ _ref_ can contradict the AC amplitude of the input source, which
is usually IV. The resulting distortion components reflect the actual input amplitude
corresponding to _P_ _ref._ The computation of the distortion terms is presented in more
detail in the following example.
The results of the • **AC** and • **DISTO** statements are detailed summaries of all distortion sources in the circuit. If only the total distortion is of interest, _nums_ is set to zero
in the • **DISTO** statement and a • **PRINT** or • **PLOT** **DISTO** statement is added, such as

```
       .PRINT DISTO HD2 HD2(P) DIM2 DIM2(P)

```

which lists the magnitude and phase of the second harmonic distortion, **HD2,** and the
second intermodulation difference distortion, **DIM2,** for all computed frequency points
between 1 kHz and 100 MHz.


_EXAMPLE_ 5.7


Compute all distortion measures introduced above for the one-transistor amplifier (Figure 4.3) and check the results using SPICE2.


_**Solution**_
Expressions for the different distortion terms can be derived based on the exponential
I-V characteristic of the _BIT._ The one-transistor circuit is simplified, as shown in Figure 5.8, by removal of the bias base resistor, _RB,_ and replacement of it by a bias source
of value _VBE_ = 0.7934, equal to the BE voltage obtained with the base resistor such
that the quiescent collector current, _Ie_ = 2.1 rnA, is preserved. This simplification
is necessary because distortion is a strong function of the input source resistance. A
voltage signal source of amplitude _Vbel_ is also connected at the input. The total voltage
applied at the base of Ql, _VBE,_ can be expressed as


_VBE_ = _VBE_ + _Vbe_ = _VBE_ + _Vbel_ coswt (5.18)


(1 V) COS rot



DISTORTION ANALYSIS **161**


+


5V _Vee_
-=


+

_VBE_ 0.794 V
-=I

**FigureS.S** Simplified one-transistor
circuit for distortion analysis.


The resulting total collector current, _ie,_ has a DC component, _Ie,_ and an AC component, _Ie:_


_ie_ = _Ie_ + _Iecoswt_ (5.19)


The total collector curren~, _ie,_ is an exponential function of the total base-emitter voltage, _VBE,_


(5.20)


where _VBE_ has been replaced by the sum of its components. Because of the assumption
of small nonlinearities, the exponential in Eq. 5.20 can be expanded in a power series:
"



_._ _Vi_ _IVi_ _IVi_
_1<::_ _. .'_ := _Ie_ 1[ + - _Vth_ + - 2 (                    - _Vth_ ) [2] + - 6 ()3                    - _Vth_ + ... ]
,
where _Vi_ is tlleinput s~gnal,equal to _Vbel-_ ~e follows'.from Eqs. 5.19 and 5.21:


_Ie_ _._ I _Ie_ 2 1 _Ie_ _3_
_Ie_ = _ie - Ie_ = _-V Vi_ + '2 _V2 Vi_ +"6 _V_ _3_ _Vi_ + ...
_th_ _th_ _th_



(5.21)


**162** 5 AC ANALYSIS


The coefficients _ai_ ofthe power series in Eq. 5.13 can be set equal to the coefficients in
the above power series, assuming that Si = _Vi_ and _So_ = _Ie._ The distortion terms follow
naturally:


(5.22a)


or, using the relation _So_ = _ajSi,_ _HD2_ can be rewritten as



_HD2_ = ~ . _a2_ S = ~ . _Ie_
2 ai _0_ 4 _Ie_



(5.22b)



**In** order to evaluate the above expressions, _Vi_ or _Ie_ must be calculated. Both values
result from the equation of the output power in _R_ _e_


_`V`_ _[2]_ I
_Po_ = = _i;Re_ = _Pre!_ = 1 mW
_ut:_


_Vo_ = _J2RePre!_ = 1.4 V


= = 1.4 rnA
_Ie_ _J2~;!_


The amplitude of the input signal _Vi_ is


_Ie_ _Ie_ 1.4 rnA
_Vi_ = aj = _gm_ = 0.081 mho = 17mV


The second-harmonic distortion is obtained by substituting for either _Vi_ or _Ie_ in Eq.
5.22a or Eq. 5.22b, respectively:


1 _Ie_ _1. 1.4 __. 0 16
_HD2_ = -- _4Ie_ = 4 _2.1i'_


The remaining distortion terms can be derived similarly:



1 ( _Vi_ )2 1 _(Ie_ )2
_HD3_ = 24' _Vth_ = 24' _Ie_ = 0.018


1 _Vi_ 1 _Ie_
_SIM2_ = _DIM2_ = - . - = - . - = 0.333
_2_ _Vth_ 2 _Ie_



(5.23)


(5.24)


DISTORTION ANALYSIS


1 _(Vi)2_ 1 _(Ie)2_
_DIM3_ = 8". _Vth_ = 8". _Ie_ = 0.054



**163**


(5.25)



The input statements for the distortion analysis of the one-transistor amplifier
of Figure 5.8 and the distortion measures at 1 kHz computed by SPICE2 are listed in
Figure 5.9. Note _that/start and/stop_ in the **.AC** statement have been set equal since only


```
*******03/06/89 ******** SPICE 2G.6

ONE-TRANSISTOR CIRCUIT (FIG. 5.8)
**** INPUT LISTING

```

```
3/15/83 ********11:10:26*****

 TEMPERATURE = 27.000 DEG C

```

```
***********************************************************************
```

```
Q1 2 1 0 QMOD
RC 2 3 1K
*RB 1 3 200K
VCC 3 0 5
```

```
VEE 4 0 793.4M
VEE1 1 4 AC 1
```

```
.MODEL QMOD NPN
*+ CJE=lP CJC=2P
```

```
.OP
.AC LIN 1 1K 1K
.DISTO RC
```

```
.PRINT DISTO HD2 HD3 SIM2 DIM2 DIM3
.PRINT DISTO HD2 (DB) HD3 (DB) SIM2 (DB) DIM2 (DB) DIM3 (DB)
.WIDTH OUT=80
.END

**** AC ANALYSIS TEMPERATURE = 27.000 DEG C

```

```
  FREQ

1.000E+03

```

```
HD2 HD3 SIM2 DIM2 DIM3

1.683E-01 1.889E-02 3.367E-01 3.367E-01 5.668E-02

```

```
**** AC ANALYSIS TEMPERATURE = 27.000 DEG C

```

```
 FREQ

1.000E+03

```

```
HD2 (DB) HD3 (DB) SIM2 (DB) DIM2 (DB) DIM3 (DB)

-1. 548E+01 -3.447E+01 -9.455E+00 -9.455E+00 -2.493E+01

```


**Figure 5.9** SPICE2 distortion analysis results.


**164** 5 AC ANALYSIS


the total distortion terms at midfrequency are of interest. The distortion terms computed
by SPICE2 are in good agreement with the values calculated by hand according to Eqs.
5.22 through 5.25. The distortion terms in dBm are listed in the SPICE2 output as well.


5.5 **POLE-ZERO ANALYSIS**


The frequency sweep, •AC, introduced above yields the frequency response of circuits
in the form of a graph. The locations of poles and zeros can in general be inferred from
a Bode plot. In many applications, such as filters or feedback circuits, the succession of
several poles and zeros makes reading their locations from a frequency plot difficult and
makes it necessary to obtain the actual values. SPICE3 and high-end SPICE versions,
such as SpicePLUS and HSPICE, provide a pole-zero analysis.
The pole-zero analysis computes the transfer function of the circuit represented as
a two-port circuit:


_H(s)_ = _Vo(s)_ = _a (s-zd(s-zz)"'(s-Zn)_
(5.26)
_Sj(s)_ _(s - PI)(S_ _- pz) ... (s -_ _Pm)_


where _s_ = _j_ _w,_ V 0 is the output voltage, and Sj is the input signal, which can be either
a current or a voltage. The output for this analysis is always a voltage.
The general form of the pole-zero statement in SPICE3 is


         - PZ _ni_ I _ni2 no_ 1 _no2_ CURNOL POL/ZERIPZ


where _nil_ and _ni2_ are the input nodes and _nol_ and _no2_ are the output nodes of the
two-port representation. The field following the node specification defines the type of
the input; CUR for current input and VOL for voltage input. One of the keywords must
be present. The last field specifies whether the poles (POL), zeros (ZER), or both poles
and zeros (PZ), should be computed. One of the three keywords must be present. In
interactive mode the same command with the omission of the leading period must be
typed at the SPICE3 shell prompt.
The results are stored in the output file if the following line is added to the input
circuit:


. PRINT PZ ALL


The same command without the leading period can be issued in interactive mode.
A noteworthy difference between the frequency sweep and the pole-zero analysis
is that in the former case one analysis computes the transfer function from input to any
node in the circuit, whereas in the latter case a separate analysis must be performed
each time the two-port representation is redefined.
The pole-zero analysis is very useful for relatively small circuits; for circuits containing more than 20 charge storage elements the results must be interpreted carefully.


SUMMARY **165**


The bridge-T circuit, which has exemplified the **.AC** frequency sweep, is used
below for finding the poles and zeros and double- checking the Bode plots.


_**EXAMPLES.8**_


Use SPICE3 to compute the poles and zeros of the bridge-T filter; compare the results
with the hand calculations in Example 5.2 and the Bode plot produced by SPICE.


_**Solution**_
The SPICE3 input and results for the pole-zero analysis are shown in Figure 5.10 on
page 166. Note that the • **AC** statement has been replaced by a • **PZ** line defining the
input of the two-port representation between nodes 1 and 0 and the output between
nodes 3 and O. Furthermore, the input is defined as a voltage. The output signal is
always assumed to be a voltage.
The output contains the two real poles and zeros of the transfer function, which are
identical to the hand calculations carried out in Example 5.2. Note that the pole-zero
algorithm usually runs into difficulties when the transfer function is complex and has
multiple poles or zeros.


**5.6** **SUMMARY**


This chapter has described the analyses performed by SPICE in the AC mode. The
control statements for each analysis have been introduced as well as the specifications
of output variables and result-processing requests. Several examples have been used to
show how to apply the various AC analyses to practical circuit problems. The implications of small-signal analysis for nonlinear circuits in the AC mode has been addressed
in the examples.
The AC analysis types, frequency sweep, noise and distortion analysis, and polezero computations are specified by the following control lines:


**•AC** _Interval numpts fstart fstop_

•NOISE _V(nI<,n2»_ _V/Iname nums_

**.DISTO** _RLname <nums <hl!J_ _<Pre! <52»»_

**. PZ** _ni_ 1 _ni2 no_ 1 _no2_ **CURNOL** **POL/ZERIPZ** (SPICE3)


Noise and distortion are frequency-domain analyses; therefore these statements must
be used in conjunction with an • **AC** line.
With the exception of the **PZ** analysis, results are stored in the output file only for
specified circuit variables, _AC_OULvar,_ which can be complex voltages or currents:


_Vx (nodeI <,node2»_
_Ix (Vname)_


**166** 5 AC ANALYSIS

```
    BRID3E T FILTER
```

    ```
    VI 1 0 12 AC 1
    Cl 1 2 1U
    C2 2 3 1U
    R3 2 0 lK
    R4 1 3 lK
```

    ```
    .OP
    .PZ 1 0 3 0 VOL PZ
    .PRINT PZ ALL
```

    
     - END

```
    Circuit: BRID3E T FILTER

    Circuit: BRID3E T FILTER
    Date: Fri Apr 19 14:55:55 1991

    Operating point information:

       Node Voltage

```


V(3)

V(2)
V(l)


```
1.000000e+Ol
O.OOOOOOe+OO
1.000000e+Ol

```

```
    Source Current

    vl#branch O.OOOOOOe+OO

Index pole(l)

```

```
bridge T filter
pole-zero analysis Fri Apr 19 14:55:55 1991

     pole(2)

```



- `-2.618034e+03,` `O.OOOOOOe+OO` `-3.819660e+02,` `O.OOOOOOe+OO`

```
                    bridge T filter
                    pole-zero analysis Fri Apr 19 14:55:55 1991

```

```
Index zero(l)

```

```
zero(2)

```



- `-1.000000e+03,` `O.OOOOOOe+OO` `-1.000000e+03,` `O.OOOOOOe+OO`


**Figure 5.10** Input and results for pole-zero analysis of bridge-T circuit.


SUMMARY **167**


where _x_ defines the output format of the complex variable; accepted formats are Rand
**I,** for real and imaginary part, respectively; Mand **P,** for magnitude and phase, respectively; and **DB,** for the decibel value of the magnitude.
The output variables of a frequency-domain analysis can be saved either in tabular
or line-peinter-plot format using the • **PRINT or . PLOT** control statement, respectively.
The general format of the output request is

**.PRINT/PLOT** **AC** _AC-OUT_varl <AC_OULvar2 ..._   - _<ploLlimits>_


**REFERENCES**


Dorf, R. C., 1989. _Introduction to Electric Circuits._ New York: John Wi1~y&: Sons.
Gray, P. R., and R. G. Meyer. 1993. _Analysis and Design of Analog Integrated Circuits,_ 3d ed.
New York: John Wiley & Sons. ' .


"


_J_


,.


..• I


':r,


_**Six**_


_**TIME-DOMAIN**_ _**ANALYSIS**_


**6.1** **ANALYSIS DESCRIPTION**


The transient analysis of SPICE2 computes the time response of a circuit. This analysis mode takes into account all nonlinearities of the circuit. The input signals applied
to the circuit can be any of the time-dependent functions described in Chap. 2: pulse,
exponential, sinusoidal, piecewise linear, and single-frequency FM. In contrast, in AC
analysis only sinusoidal signals with small amplitudes, for which circuits can be considered linear, are used.
Time-domain analysis computes, in addition to voltages and currents of timeinvariant elements, the variation of charges, _q,_ and fluxes, _e/>,_ associated with capacitors and inductors. These are described by the branch-constitutive equations (BCEs)
for capacitors and inductors defined in Sees. 2.2.3 and 2.2.5:


= _Cdvc_
_ic =_ _[dq]_ (6.1)
_dt_ _dt_

_VL =_ _[de/>]_ [ =] _[ L]_ _[diL]_ (6.2)
_dt_ _dt_


where _ic_ and _Vc_ are the current and voltage of capacitor C and _iL_ and _VL_ are the current
and voltage of inductor _L._ The BCE for resistors, Ohm's law, is time-invariant.
Two analysis types are supported in SPICE for the time-domain solution:


TRAN Computes the voltage and current waveforms over a given time interval

FOUR Computes the Fourier coefficients, or spectral components, of periodic signals


**168**


TRANSIENT ANALYSIS **169**


An additional utility for transient analysis, • **IC** _(initial_ _conditions),_ is used for
specifying the initial voltages at selected or all nodes. An INITIAL TRANSIENT
SOLUTION _(ITS)_ precedes a time-domain analysis unless it is specifically disabled.
It is a DC solution at _t_ = O.


**6.2** **TRANSIENT ANALYSIS**


The following statement is required by SPICE to perform a transient analysis:


**. TRAN** _TSTEP TSTOP <TSTART_ _<TMAX>_        - <UIC>


The analysis is performed over the time interval from 0 to _TSTOp'_ but results can be
output starting from a user-defined time, _TSTART,_ to _TSTOP; TSTARTis_ assumed to be

       - if it is not specified. _TSTEP_ is the time interval used for printing or plotting the results
requested by a • **PRINT** or a • **PLOT.** Note that SPICE2 and most programs derived
from it use a different internal time step for solving the circuit equations, which is
automatically adjusted by the program for accuracy. By default the internal time step is
bound by the smaller of _(TSTOP-TSTART)/50_ or 2. _TSTEP._ Although in most cases the
SPICE internal time-step selection algorithm is accurate enough, there are situations
when for better accuracy a user may want to restrict the maximum time step. This can
be achieved by specifying the value of the maximum allowed internal time step _TMAX._
The data on a • **TRAN** statement are order-sensitive, and a value for _TSTART_ must always
precede _TMAX._
The time-domain solution is preceded by a DC solution, the ITS, which computes
the initial values of voltages and currents necessary for the integration of the BCEs, Eqs.
6.1 and 6.2, or Eqs. 2.5 and 2.10. A user can avoid the initial transient, DC, solution by
concluding **the. TRAN** statement with the keyword **UIC** _(use initial conditions)._ In this
case the initial value of every voltage and current is 0 except those voltages and currents
initialized with the **IC** keyword in the element definition lines or the • **IC** statement.
One scenario where **UIC** is useful is the computation of the steady-state solution without
the transient response leading to it. For a correct solution the user must define the correct
initial values for all charge-storage elements in the circuit.


_EXAMPLE_ 6.1


Explain the meaning of the following transient analysis statements:

```
      .TRAN In lOOn
      .TRAN O.lu 100u 90u
      .TRAN 100u 1m 0 lOu
```

`.TRAN` `IOn` `lu` mc
```
      .PRINT TRAN V(6) I (VCC)
      .PLOT TRAN V(6) V(2,1) (0,5)

```

**170** 6 TIME-DOMAIN ANALYSIS


_**Solution**_
The first statement specifies that a time-domain analysis is to be performed from time

      - to 100 ns and that the results are to be output at a l-ns interval. The second statement
requests that the analysis be performed to 100 Jl-sand that the results between 90 Jl-Sand
100 Jl-s be output at a 0.1- Jl-Sinterval. The third statement requests a long analysis to
lms with results output every 100Jl-s but limits the internal time step to lOJl-s. Finally,
the fourth. **THAN** statement requires SPICE to omit the initial transient, or DC, solution
by concluding the statement with the **Ule** keyword.
The desired voltages and currents resulting from a transient analysis are identified
in a • **PRINT** or • **PLOT** statement. The keyword **THAN** must be present to identify the
analysis type. The time interval and time step for the prints and plots are those specified
on the • **THAN** statement. At least one • **PRINT** or • **PLOT** statement must be present in
the input file for the analysis to be performed. In this example the values of V ( 6) and
the current through voltage source vee are printed and V ( 6) and V ( 2, 1) are plotted
with a common voltage scale with values from 0 to 5 V at the output.


_EXAMPLE_ 6.2


Compute the time-domain response of an RLC parallel circuit that at _t_ = 0 is connected
to a constant current source as shown in Figure 6.1. Verify the solution with SPICE.


_**Solution**_
The KCL applied to node 1 yields the following equation:



_._ _Vc_ _I_
_C_ _[dvc]_ _dt_ + _lL_ + _If_ = S


The BCE of the inductor, Eq. 6.2, yields a substitution for _iL :_


_diL_
_L-_ = _Vc_
_dt_



(6.3)


(6.4)



leading after differentiation with respect to time to the following second-order differential equation in _vc:_


(6.5)


The solution of this equation is of the form



_vc(t)_ = _Ae_ _[pt]_


```
(6.6)

```

TRANSIENT ANALYSIS **171**



_t=_ 0


_R_
10kQ


**Figure 6.1** Parallel RLC circuit.


which put in the differential equation above leads to the _characteristic_ _equation:_


pZ + _2a p_ + _w5_ = 0


where


_a_ = _1_ = 5. 10 [4] S-I
_2RC_


1
_Wo_ = -- = 10 [6] rad/s
_jLC_


The solution of the quadratic equation is



(6.7)


(6.8)



_PI,_ Z = _-a::!:: Ja_ _[Z]_ _-_ _W5_ = _-a::!:: J-(W5_ _-_ a [Z] ) = _-a::!:: jWd_ _(6.9)_


which is put in Eq. 6.6 to obtain _vdt):_


(6.10)


_a_ is the _damping/actor,_ and _Wd_ is the _damped radian/requency_ (Nilsson 1990). Coefficients _A_ I and Az are found from the initial conditions; at _t_ = 0, vdO) = 0 and therefore
Az = _-AI. Al_ is obtained by putting vdO) in Eq. 6.3:


**172** 6 TIME-DOMAIN ANALYSIS


The time-dependent function _vc(t)_ is


1 _I_ _-at._ _._
_Vc_ _t_ ( ) = -c _se_ sm _Wd_ _t_ (6.11)
_Wd_


The angular frequency, _w,_ is close to _Wo_ because _a_ is negligible by comparison; therefore the period is


27r
_T_ = - = 6.28/Ls (6.12)
_Wo_

```
      PARALLEL RLC CIRCUIT
```

      ```
      IS 0 1 PWL 0 0 IN 1M 1 1M
      L 101M
     C lOIN
     RIO 10K
```

       ```
       .TRAN lU 1000
       .PLOT TRAN V(l)
```

. END


The SPICE input file for this circuit entitled, PARALLEL RLC CIRCUIT, is
shown above. A transient analysis for 100 /Ls is requested corresponding to approximately 16 periods according to the above calculations. The waveform computed by
SPICE2 is shown in Figure 6.2 and has the damped sinusoidal shape predicted by
Eq. 6.11. The complex algorithms in SPIcI~2 (see Sec. 9.4) can be verified to predict
waveforms in agreement with the above hand-derived solution for this simple problem.
According to Eq. 6.11, the amplitude of the oscillation at _wot_ = 7r/2 (for example, at
_t_ = 7r/2 /LSfor _Wo_ = 10 [6] rad/s) is


After solving for _vc(t),_ one can put _Vc_ of Eq. 6.4 in Eq. 6.3 to obtain a second-order
differential equation in _iL(t):_


(6.13)


This equation differs from Eq. 6.5 for _vc(t)_ in that the right-hand side is nonzero. The
solution consists of the damped sinusoidal term, which is the natural solution, and an


1.5


1.0


0.5


,.G 0.0


-0.5


-1.0

```
            20

```

Time, JlS
Figure 6.2 The waveform _vc(t)_ computed by SPICE.


additional forced solution:


```
60

```


TRANSIENT ANALYSIS 173

```
      80

```

(6.14)



The SPICE waveform for _iL(t)_ is shown in Figure 6.3. It can be seen that once
the oscillations die out the inductor current assumes the forced solution, which is equal
to the input current of 1 rnA. The natural solution, therefore, represents the transient
response, whereas the forced solution is the steady-state response.
A few comments can be made at this point. In order to observe the oscillations in
a circuit, we use a step function at _t_ = 0+ described as a PWL current source. An
alternate way to achieve the same result is to use a DC current source at the input and
to omit an INITIAL TRANSIENT SOLUTION by specifying the ure option in the

 - TRAN statement. This second approach is equivalent to applying a step function at
_t_ = 0+ since all currents and voltages at _t_ = 0 are zero.


_Exercise:_
Show that no oscillation can be observed in the SPICE solution if the ure keyword is
not used when _Is_ is a DC source. Explain the result.


The previous example demonstrated the use of the transient analysis in SPICE
for computing the response of a linear RLC circuit. The example also outlined the


**174** 6 TIME-DOMAIN ANALYSIS


1.5


«
E 1.0
._~


0.5


Time, I!S
Figure 6.3 Thewaveform _h(t)_ computedby SPICE.


connection between the equations describing the electrical circuit and the analysis parameters and solution computed by SPICE. The importance of the different analysis
parameters is exemplified best by oscillators. The following example demonstrates the
use of SPICE for computing the response of a Colpitts oscillator.


_EXAMPLE_ 6.3


Verify the oscillation condition and find the amplitude and frequency of the Colpitts
, oscillator shown in Figure 6.4 using SPICE.


_**Solution**_
The passive RLC circuit in Example 6.2 cannot sustain oscillations, which are damped
by the factor _e-_ _[at]_ _._ Oscillations can be sustained only if the real part of the natural
frequencies computed from Eq. 6.7 is positive, or in other words, the circuit has righthand-plane poles. This can be achieved with a gain block connected in a feedback con~
figuration (Pederson and Mayaram 1990). In the frequency domain the overall transfer
function, _A(s),_ of a gain block, _a(s)_ (where s = _(T_ + _jw_ is the complex frequency),
connected in a feedback loop,f, which is shown in Figure 6.5 is equal to the following
(Gray and Meyer 1993):


_a(s)_
(6.15)
1 + _a(s)f_


0



TRANSIENT ANALYSIS **175**


_i('_ _i_ _e_ _v"_ 0

+
_**i**_ _**f= i**_ _**e**_


C,
CD     
_L_
_`RE`_ _`R`_ _L_

_`RB`_ C2




 _VEE_
`-10 V`    - _Vee_
10V
Figure 6.4 Colpitts oscillator.


The loop gain of the system, _T(s),_ where _T(s)_ = _a(s)f,_ must encircle the point (-1,
0) in the complex frequency plane as shown in Figure 6.6 in order for the circuit to
oscillate. The plot in Figure 6.6 is known as the _Nyquist diagram._
The Colpitts oscillator shown in Figure 6.4 has the common-base (CB) transistor
amplifier, QI connected in a feedback loop. The feedback network consists of capacitors
C, and C2. The signal fed back to the input is


(6.16)


where _n_ can be referred to as the capacitive turns ratio and is equal to the inverse of the
feedback factor, f:


I
_n=_ _f_ 10 (6.17)



s,
I
I
I
I
I _f_ I
I `L` _Als)_ `~` I


Figure 6.5 Feedback amplifier.



S"


**176** 6 TIME-DOMAIN ANALYSIS



_T(joo) =a_ (joo)J= _ _gm_ _[2]_ _L(j_ (0)
_n_


_n_



1m _T(joo)_

```
 00=0
```

_Re T(joo)_



**Figure 6.6** Nyquist diagram.


The small-signal gain _a(_ s) of the CB transistor is


The circuit is unstable, and oscillations are initiated when the loop gain is


_T(jwo)_ = _a(jwo)f_ = - _gmRL_ = -1
_n_



(6.18)


(6.19)



where _Wo_ is the resonant frequency of the tank circuit in the collector of transistor _QI :_



1
_Wo_ _=_
_JLC_



1
----;::====== rad/ s = 21.1 . 10 [6] rad/ s (6.20)
_J5'_ 10- [6] .450, 10- [12]


(6.21)



with



This corresponds to an oscillation frequency _fo_ = 3.36 MHz. When oscillations build
up, the small-signal approximation is no longer valid and the equivalent large-signal _G_ _m_
must be considered, which is less than _gm._ A good approach to ensuring steady-state
oscillations (Meyer 1979) is to dimension _R_ _L_ so that the initial loop gain is


(6.22)


The gain of the circuit including feedback is



TRANSIENT ANALYSIS **177**


(6.23)



The denominator can be compared with the characteristic equation of the parallel RLC
circuit, Eq. 6.7. It has a pair of complex poles leading to a time-domain solution, Eq.
6.11, of the form


(6.24)


where, in this example,



ex = _1 (1_ _gmRL)_
_2RC_ _n_



(6.25)



and represents the damping factor. If _gmRd n_ - 1, corresponding to complex poles in
the right half-plane, the predicted solution, Eq. 6.24, is a growing sinusoid that reaches
a steady-state amplitude constrained by circuit biasing and loading.
The above equation is very important for understanding at what rate the oscillations
build up. The analysis of oscillators with SPICE can be tricky for certain circuits because a large number of periods must be simulated before oscillations can be observed.
The oscillation buildup can be related to the quality factor, _Q,_ of a parallel tuned circuit,
defined by



_R_
_Q_ = = _woCR_
_woL_


Putting _Q_ in Eq. 6.24 leads to the following expression of the circuit response:


_vo(t)_ IX _eKwot/Q_ _sinwot_



(6.26)


(6.27)



where _K_ is a constant dependent on the actual oscillator configuration. The above expression shows that the higher the _Q_ of the tuned circuit, the longer it takes to reach
steady-state oscillations. Eq. 6.27 is also valid for series resonant circuits with the appropriate change in the definition of _Q._
In order to complete the circuit specification, we need to bias the circuit; this can
be achieved by setting the emitter current, _hE,_ using a negative supply, _VEE,_ and a resistor, _RE:_


_VEE_ = -lOV


**178** 6 TIME-DOMAIN ANALYSIS


_RE_ = 4.65 kO


_gm_ = 0.076 A/V


_- VEE -_ _VBE_ = 099(10 - 0.8) V
_Ie_ = _adEE_ = _aF_ _RE_ _._ 4.65. 103 n l.96mA


With the above values the minimum value of _RL_ for which, according to Eq. 6.22, the
circuit oscillates is


The SPICE input COLPITTS OSCILLATOR is listed below; note that the negative
supply is implemented as a step function using the **PULSE** source. It is always desirable
to kick the circuit in order for the program to find the oscillatory solution. The step
function used in simulation is similar to the real situation of connecting a circuit to a
supply before proper operation can be observed. The value chosen for _RL_ is 750 n.
The simulation is carried out for ten periods, to 3 f.LS, with results to be printed in the
output file every 20 ns. Note that for the graphical output of Nutmeg or Probe, the
time step is used only to set a default upper bound on the internal integration time
interval.

```
      COLPITTS OSCILLATOR
```

      ```
      RB101
      Q1 9 1 3 Mom
      VC1 2 9 0
      VCC 4 0 10
      RL 4 2 750
      C1 2 3 500P
      C2 4 3 4.5N
      L 4 2 5U
      RE 3 6 4.65K
      VEE 6 0 -10 PULSE -15 -10 0 0 0 1
```

      ```
      .MODEL Mom NPN RC=10
```

      ```
      .TRAN 20N 3U
      .PLOT TRAN V(2) I (VC1)
      .OPTIONS LIMPTS=5000 ITL5=0 ACCT
```

       - END


The results of the simulation, the collector voltage, _vo,_ of QI, are shown in graphical
form in Figure 6.7. The amplitude of oscillations at the collector, _Vo,_ or V ( 2) in SPICE,


13


12


11


} 10


9


8


7



0.5



TRANSIENT ANALYSIS **179**


2.5



Time, IlS

**Figure 6.7** Colpitts oscillator: collector voltage, _vo,_ of QI.


can be verified at _wo:_


= 0.89.750.2. 1.9. 10- [3] V = 2.54 V



(6.28)



The incremental part of the collector current, _Ie,_ is approximated by a Fourier series
(Pederson and Mayaram 1990) in which the ratio of the modified Bessel functions,
_Iii 1_ _0,_ is a function of _b_ = _Vt/Vth_ and is equal to 0.95 for _Vt/Vth_ - 6. A power-series
representation cannot be used because of the large value of _Vi_ compared to _Vth'_ The
amplitude of _Va_ derived above is in good agreement with the waveform in Figure 6.7.
The waveform can be seen to be a piecewise linear approximation of a sinusoid.
The points actually computed by SPICE are apparent on the graph. **In** order to obtain a
smoother sinusoid, the maximum integration time step used by SPICE must be limited.
This is achieved by specifying the _TMAX_ parameter on the • **TRAN** statement:

```
.TRAN 20N 3D 0 lON

```

The new waveform resulting after replacement of the **initial.** **TRAN** line with the above
line is shown in Figure 6.8 and can be observed to be much smoother.


**180** 6 TIME-DOMAIN ANALYSIS


13


12


11


    ,." 10


9


8


7


Time,IlS
**Figure 6.8** Colpitts oscillator: more time points used for V ( 2 ) .


_Exercise_
Verify that oscillations can be observed for _RL_ = 395 n **but** not for _RL_ = 100 n. This
exercise should prove the validity of the oscillation condition derived above.


**6.3** **INITIAL CONDITIONS**


The solution of the time response of electric circuits starts with the time-zero values, or
initial conditions, as shown in Example 6.2. A transient analysis in SPICE is preceded
by an INITIAL TRANSIENT SOLUTION, which computes the initial conditions. The
steady-state time-domain solution of more complex circuits is reached faster if the user
initializes voltages across capacitors, currents through inductors, semiconductor-device
junction voltages, and node voltages. As described in Sec. 4.6, the • **NODESET** statement helps the DC solution to be found faster. Similarly, user-defined initial conditions
enhance the accuracy and offer quicker access to the desired solution. Most SPICE
programs support two types of user-specified initial conditions.
First, initial values for node voltages can be set with the following statement:

**.Ie v** _(node]) =value] <V(node2) =value2 ... >_


This command sets the time-zero voltage at _node]_ to _value],_ that at _node2_ to _value2,_
and so on. Initial values of charges on capacitors and semiconductor devices are also
computed based on these initial voltages. Note that unlike voltages initialized by


INITIAL CONDITIONS **181**


- NODESET, which are used only as initial guesses for the iterative process and then
released to converge to a final solution, voltages defined by the • IC statement do not
change in the final INITIAL TRANSIENT SOLUTION.
The effect of the   - IC statement differs depending on whether the UIC parameter is present on the. TRAN line. In the absence of UIC an INITIAL TRANSIENT
SOLUTION for the entire circuit is computed with the initialized nodes kept at the specified voltages. If UIC is specified on the •TRAN line, all the values in the time-zero
solution except the initialized node voltages are zero. As many node voltages should be
initialized as possible when the UIC parameter is set.
Second, initial conditions for capacitors, inductors, controlled sources, transmission
lines, and se Il1 iconductor devices can b,e set on a device-by-device basis using the IC
keyword. These values are used only in conjunction with UIC and have no effect on the
INITIAL TRANSIENT SOLUTION. When initial values are specified both on devices
and in an • IC stateme~t, the device-based values take precedence:
Table 6.1 summarizes the. effect of the different combinations of initial conditions,
namely, the • IC statement, the device-based Ie, and the UIC keyword, on the circuit
solution. In this table _ITS_ stands for _initial transient solution,_ which is different from
the small-signal bias solution (SSBS), which is the result of an .OP request.


_**EXAMPLE 6.4**_


Use a device-based IC to set the initial current _iL(O)_ = 1 rnA through the inductor of
the parallel RLC circuit in Figure 6.1.


_Solution_
According to Table 6.1, a device-based IC effects the solution only when UIC is present
in the •TRAN statement. Therefore the SPICE input file in Example 6.2 is modified as
shown below. The third modification in the RLC description listed below is the replacement of the PWL source used for _Is_ with a DC current, which in the presence of UIC
has the effect of a step function.


Table 6.1 Effects o( IC Combinations

UIC .IC Device-based IC SPICE2/3 Initialization

no no no ITS is equivalent to SSBS
no no yes ITS is equivalent to SSBS; device-based ICS have no
influence
no yes no ITS uses •IC voltages; is different from SSBS
no yes yes ITS uses . IC voltages; is different from SSBS; devicebased ICs have no influence
yes no no No ITS; all initial values are zero
yes no yes No ITS; uses device-based IC; rest of initial values are zero
yes yes no No ITS; uses . IC; rest of initial values are zero
yes yes yes No ITS; uses device-based IC first, . IC next; rest of
initial values are zero


**182** 6 TIME-DOMAIN ANALYSIS


`PARALLEL` `RLC` `CIRCUIT` _WI_ `INITIAL` `CONDITION`
```
      IS 0 1 1MA
      L 101MB IC=lMA
      C101NF
      R 1 0 10K
      .TRAN 1US 100US UIC
```

.pwr `TRAN` `V(l)`
```
      .END

```

The SPICE analysis results in a constant current _iL(t)_ = 1rnA without the damped
oscillations observed in Example 6.2. The explanation for this result is that the specified initial condition corresponds to the steady-state solution. This constitutes a very
important observation: The fastest way to find the steady-state response of a circuit is
to initialize as many elements as possible in the state they are expected to reach.
Note that omission of the keyword **urc** from the • **TRAN** statement results in
damped oscillations, because device-based rcs have no effect, as shown in Table 6.1.


The above example demonstrates the use of the device-based **rc** and its applicability for finding the steady-state response. In the analysis of oscillators initial conditions
must be used in order to shorten the simulation time during the build-up phase (the
higher the _Q_ of the circuit, the longer this phase lasts, according to Eq. 6.27). The next
example will demonstrate the use of • **rc** for the correct initialization of a ring oscillator.


_**fXAMPLf6.5**_


Use SPICE to simulate the behavior of the three-stage enhancement-depletion (E-D)
MOS ring oscillator shown in Figure 6.9. The enhancement and depletion transistors
have the following device and model parameters:

Enhancement NMOS: W = 40 _j.Lm;_ _L_ = 10 _j.Lm;_ _VTO_ = 1.8 Y;
_KP_ = 40 j.LA/y [2] ; _LAMBDA_ = 0.001 y-I, _CGSO_ = 20 pF/m.
Depletion NMOS: W = 5 _j.Lm;_ _L_ = 10 _j.Lm;_ _VTO_ = - 3 y;
_KP_ = 40 j.LA/y2; _LAMBDA_ = 0.001 y-I.


_**Solution**_
Following is the SPICE input for this circuit:

```
      RING OSCILLATOR MOS
```

      VDD 11 0 5
```
      M1 1 3 0 0 ENH L=10U w=40U
      M2 2 1 0 0 ENH L=10U w=40U
      M3 3 2 0 0 ENH L=10U w=40U

```

INITIAL CONDITIONS **183**


_~_ _VDD_
~ 5V


**Figure** 6.9 NMOS ring oscillator.

```
M4 11 1 1 0 DEP L=10U W=5U
M5 11 2 2 0 DEP L=10U W=5U
M6 11 3 3 0 DEP L=10U W=5U
```

```
.MODEL DEP NMOS LEVEL=l VTO=-3 LAMBDA=.OOl KP=.4E-4
.MODEL ENH NMOS LEVEL=l VTO=1.8 CGS0=20N LAMBDA=.OOl KP=.4E-4
```

```
.TRAN .0lU .5U
.PLOT TRAN V(l) V(2) V(3) (0,5)
```

 - END


If the circuit is analyzed as is, no oscillations are observed; the outputs of the three
inverters, nodes 1,2, and 3, settle at 2.5 V. An initial imbalance is necessary for oscillations to build up; this can be achieved by initializing the outputs of the inverters at
high or low values, 5 V or 0 V, with an • **IC** line:

```
.IC V(1)=5 V(2)=0

```

Resimulation of the circuit including the above line produces the waveforms shown
in the graph of Figure 6.10.


Note that the data in the   - **IC** statement are used to compute the INITIAL
TRANSIENT SOLUTION in the absence of the **UIC** parameter. The values in the initial solution are not always identical to the values in the • **IC** statement, because initial
conditions are set up in SPICE by connecting a Thevenin equivalent with a voltage


**184** 6 TIME-DOMAIN ANALYSIS


`200` `300` 400


Time, ns
**Figure 6.10** Waveforms at the outputs of the inverters in the ring oscillator.


equal to the initial value and a 1-0 resistor to the initialized node. The Thevenin equivalent nets are removed only at the first time point in the transient analysis.


**6.4** **FOURIER** **ANALYSIS**


A periodic signal can be decomposed into a number of sinusoidal components of frequencies that are multiples of the fundamental frequency. These components of the signal are also referred to as spectral or harmonic components. In other words, a periodic
signal can be represented by a Fourier series (Nilsson 1990):


1 _n_
_v(t)_ = _2ao_ + _L(ak_ _coskwt_ + _bk_ sinkwt) (6.29)

_k=!_


where _!ao_ is the DC component and the coefficients _ah bk_ of the series are defined by

_2_ _ft+T_
_ao_ = _T_ _t_ _v(t)dt_



_2 ft+T_
_ak_ = _T_ _t_ _v(t) cos(kwt)dt_

_2 ft+T_
_bk_ = _T_ _t_ _v(t) sin(kwt)dt_



(6.30)


FOURIER ANALYSIS **185**


The coefficients _ak_ and _b_ _k_ give the magnitude of the signal of frequency _kw,_ or the
kth harmonic component. Only a single-tone sinusoid has a single spectral component,
which is at the oscillation frequency.
**In** electrical engineering a different formulation, having only one periodic component, is used for the Fourier series:



1 _n_
_v(t)_ = _"2ao +.~Ak_ _cos(kwt_ _-_ _cPk)_

k=l


where the amplitude, Ab and the phase, cPb are given by



(6.31)


(6.32)



**In** the time-domain mode SPICE can compute the spectral components, magnitude and phase, of a given signal if the following line is present along 'with the • **TRAN**
statement:


**• FOUR** _freq OUT_varl <OULvar2_ _..._   
**In** the above _statementfreq_ is the fundamental frequency and _OULvarl,_ - _ULvar2,_
... are voltages and currents the spectral components of which are to be computed.
SPICE2 and PSpice compute the first nine spectral components for each of the signals
listed on the • **FOUR** line. SPICE3 allows the user to define the number of harmonics to
be computed. Only one • **FOUR** line can be used during an analysis.
A few remarks are necessary about the accuracy of the Fourier analysis in SPICE.
Because of the assumption of periodicity, the Fourier coefficients defined above are
computed based on the values of _OULvar_ during the last period, that is for the interval _(TSTOP-l/freq, TSTOP)._ For an accurate spectral analysis enough periods must be
simulated that the circuit reaches the steady state. The Fourier coefficients defined in
Eqs. 6.30 are evaluated based on the values for _OULvar_ computed at discrete time
points; thus for good accuracy the maximum time step must be limited, using _TMAX_
on the • **TRAN** line.


_**Example**_
```
.FOUR lMeg V(3) I (VDD)

```

This line added to a SPICE deck causes the computation of the spectral components of the voltage at node 3 and of the current through the voltage source _VDD._ The
frequencies of the harmonics are multiples of the fundamental frequency of 1 MHz.


**186** 6 TIME.DOMAIN ANALYSIS


_EXAMPLE_ 6.6


Verify the spectral values computed by SPICE2 for the output signal of the CMOS
square-wave clock generator shown in Figure 6.11. The two transistors are described
by the following model and device parameters:


NMOS: _VTO_ = 1 V; _KP_ = 20 /LAJV2; _CGSO_ = _CGDO_ = 0.2 nF/m; _CGBO_ = 2 nF/m.

PMOS: _VTO=_ -1 V; _KP=_ 10 /LAJV2; _CGSO= CGDO=0.2_ nF/m;
_CGBO_ = 2 nF/m.

Ml: _W_ = 20 _/Lm;_ _L_ = 5 _/-Lm._

M2: _W_ = 40 _/Lm;_ _L_ = 5 _/Lm._


A sinusoidal voltage source is applied at the input with a peak- to-peak amplitude of 5
V and a frequency of 20 MHz.


_**Solution**_
Because the CMOS inverter is nonlinear, the output signal contains harmonics of the
20-MHz input sinusoid. The following line requests the computation of the harmonics
for the output signal V ( 2 ) :

```
       .FOUR 20MEG V(2)

```

_{;;\_ _VDD_

        - 5V


**Figure 6.11** CMOS inverter.


FOURIER ANALYSIS **187**


The period of the output signal is 50 ns, and the analysis is requested for two periods,
until 100 ns; simulation of two periods is sufficient for this circuit because no oscillations need to settle. The SPICE deck,for this ex'ample is


CMOS INVERTER

M1 2 1 0 0 NMOS W=20U L=5U

M2 2 1 3 3 PMOS W=40U L=5U

VDD 3 0 5

VIN 1 0 SIN 2.5 2.5 20MEG

.MODEL NMOS NMOS LEVEL=l VTO=l KP=20U
+ CGID=. 2N .CGSO=. 2N CGBO=2N

.MODEL PMOS PMOS LEVEL=l VTO=-l KP=10U
+ CGID=. 2N CGSO=. 2N CGB0=2N
```
.OP
```

.TRAN 1N lOON

.FOUR 20MEG V(2)
.PLOT TRAN V(2) V(l) (-1,5)

. PLOT TRAN I (VDD)

. END


The output waveform, V (2 ), is a square wave, as showI1 in Figure 6.12. Note that
if the above deck were used the output voltage would display some ringing, which is
due to numerical inaccuracy. This problem can be corrected by SPICE2 analysis option
parameters, described in Sees 9.4.2 and 9.5. For this circuit it is necessary to add the

line


.OPTION RELTOL = 1E-4


in order to obtain the waveform in Figure 6.12. The results of the Fourier analysis are
listed in Figure 6.13. The DC component computed by SPICE2 is 2.5 V, the amplitude
of the fundamental is 3.15 V, and all the even harmonics are negligible. The results
of the Fourier analysis are listed according to the formulation in Eq. 6.31; the magnitudes of the spectral components, _Ak>_ are listed under FOURIER COMPONENT, and
the phases, _cPk>_ appear in the PHASE (DEG) column. **In** the Fourier analysis output two
additional columns list the amplitudes of the spectral components normalized to the
amplitude, _A_ l, of the fundamental, and the phases normalized to cPl'
The Fourier series coefficients can be easily checked with Eqs. 6.29 and 6.30. The
output signal, _vo(t)_ (V (2) ), shown in Figure 6.12 can be expressed as follows:


_T_
_vo(t)_ = 0 for 0 <                    - _t_ < -2


_T_
for - :5 _t_ < _T_
2


**188** **6** **TIME-DOMAIN** **ANALYSIS**


5


4


       - `3`
g

       - `2`










|Col1|Col2|
|---|---|
|||
|'\|_r_<br>'\|
|||
|||
|||
|||
|\.<br>J<br>\..<br>_J_<br>|\.<br>J<br>\..<br>_J_<br>|



**`20`** **`40`** **`60`** **80**


**Time, ns**

**Figure 6.12** **Square-wave** **signal** V ( 2) **at the output of the CMOS inverter.**


**** `FOURIER` `ANALYSIS` `TEMPERATURE` = `27.000` `DEG` `C`

```
FOURIER COMPONENTS OF TRANSIENT RESPONSE V (2)
```

`DC COMPONENT` = `2.503637E+00` .
```
HARMONIC FREQUENCY FOURIER NORMALIZED PHASE NORMALIZED
  NO (HZ) COMPONENT COMPONENT (DEG) PHASE (DEG)

   1 2.000E+07 3.147E+00 1,000E+00 1.794E+02 O.OOOE+OO
   2 4.000E+07 S.05SE-03 2.561E-03 1. 19SE+02 - 5.962E+01
   3 6.000E+07 9.612E-01 3.055E-01 1.791E+02 - 2.S9SE-01
   4 S.000E+07 9.945E-03 3.160E-03 1.425E+02 - 3.694E+01
   5 1.000E+OS 4.951E-01 1.573E-01 1.791E+02 - 2.692E-01
   6 1.200E+OS 1.249E-02 3.970E-03 1. 593E+02 - 2.009E+01
   7 1.400E+OS 2.946E-01 9.362E-02 1.799E+02 4.797E-01
   S 1.600E+OS 1.555E-02 4.941E-03 1.716E+02 - 7.74SE+00
   9 1. SOOE+OS 1.907E-01 6.061E-02 -1. 7S2E+02 - 3.576E+02

```

`TOTAL` `HARMONIC` `DISTORTION` = `3.613225E+01` `PERCENT`


**Figure 6.13** **Fourier analysis results for the square-wave** **voltage** V ( 2 ) .


FOURIER ANALYSIS **189**


The DC component, _Ao,_ is


1 1 _(T_ 1
_Ao_ = _2ao_ = _l'_ Jo _vo(t)dt_ = 25 V = 2.5 V


Before deriving the coefficients of the harmonics, note that the function is of odd
symmetry:


_J(t)_ = _-J(-t)_


Thus all coefficients _ak_ are zero. _vo(t)_ also possesses half-wave symmetry; that is,


_J(t)_ = - _J(t_ _- T/2)_


making all coefficients _b_ _k_ with even _k_ equal to zero (Nilsson 1990). The first three
harmonics, _bl> b2,_ and _b3,_ are derived by solving the integral in Eqs. 6.30 for the two
values of _vo(t)_ corresponding to the half-periods of the waveform in Figure 6.12:


_2 (T_ 2 _(T_ _1_ _2_
_bi_ = _l'_ Jo _vo(t) sin(wt)dt_ = _1'VDD_ Jo _sin(wt)dt_


_2_ _T_ _(2'1T)_ _TI2_ _2.5_
= _-1"_ _2'1TVDDCOS T_ _t_ 10 = --;;-V = 3.18 V


_b2_ = 0


_b3_ = _2VDD_ = 1.06 V
```
                3'1T

```

The above coefficients scaled by the appropriate DC value are generally valid for any
square wave. The small discrepancies with the SPICE2 Fourier coefficients can be attributed to the imperfection of the square wave V ( 2 ).


A useful application of the Fourier analysis is the evaluation of large-signal distortion. The TOTAL HARMONIC DISTORTION _(THD)_ computed by SPICE is equal to


(6.33)


In the design of many circuits the _THD_ must be kept below a specified limit. The second and third NORMALIZED COMPONENTS listed among the Fourier analysis results


**190** 6 TIME-DOMAIN ANALYSIS


correspond to _HD2_ and _HD3_ in the AC small-signal distortion analysis presented in
Chapter 5. If the results of the two analyses are compared, the Fourier components
should be scaled by the reference power, _Pref,_ in the load resistor to match the values
of _HD2_ and _HD3._ More detail on the two types of distortion analysis can be found in
Chapter 8.
Sinusoidal oscillators for various applications must have a small content of harmonics. It is instructive to compute the harmonic content in the output voltage of the
Colpitts oscillator.


_EXAMPLE_ 6.7


Use Fourier analysis to find the total harmonic distortion of the output signal of the
Colpitts oscillator in Figure 6.4.


_**Solution**_
For an accurate estimate of the harmonics, the circuit needs to be simulated for more
than the 10 periods used in Example 6.3. We will perform a transient analysis for 10

JLS corresponding to 33 periods; the • **TRAN** line in the input file is replaced by the
following line:

```
      .TRAN 15N lOU 9.3U 15N

```

The waveform is saved for displaying only the last two periods, and limiting _TMAX_
to 15 ns ensures that at least 20 time points are used in each period to evaluate the
response.
The following statement defines the frequency of the fundamental and the output
variable for which the spectral components are desired:

```
      .FOUR 3.36MEG V(2)

```

The frequency of the fundamental must be specified as accurately as possible, because
an error as small as 1% can make a difference in the values of the Fourier coefficients.
The output ofthe Fourier analysis from SPICE2 is listed in Figure 6.14. Note that
the amplitude of the fundamental found by the Fourier analysis agrees with the value
computed by hand in Example 6.3, Eq. 6.28. The _THD_ of the sinusoidal signal produced
is 8.25%.


A few comments are necessary regarding the implementation of Fourier analysis
in SPICE3. Although the limit of only nine harmonics imposed by SPICE2 and most
other SPICE versions is not a problem for most circuits, this limitation can become an
impediment in finding the intermodulation _(1M)_ terms for such circuits as mixers. In


SUMMARY **191**


**** `FOURIER ANALYSIS` `TEMPERATURE` = `27.000 DEG C`

```
FOURIER COMPONENTS OF TRANSIENT RESPONSE V (2)

 DC COMPONENT = 1.000407E+00l

 HARMONIC FREQUENCY FOURIER NORMALIZED PHASE NORMALIZED
  NO (HZ) COMPONENT COMPONENT (DEG) PHASE (DEG)

```

```
-8.683E+00I O.OOOE+OOO
-1.545E+002 -6.769E+00I
-1.471E+002 -6.027E+00I
-1.374E+002 -5.054E+00I
-1.257E+002 -3.886E+00I
-1.111E+002 -2.426E+00I
-9.404E+00I -7.206E+000
-7.896E+00I 7.869E+000
-6.880E+00I 1.803E+00l

```


1
2
3
4
5
6

7
8
9


```
3.360E+006 2.523E+000 1.000E+000
6.720E+006 1.890E-00l 7.490E-002
1.008E+007 7.725E-002 3.062E-002
1.344E+007 3.532E-002 1.400E-002
1.680E+007 1.602E-002 6.420E-003
2.016E+007 7.680E-003 3.044E-003
2.352E+007 4.226E-003 1.675E-003
2.688E+007 2.962E-003 1.174E-003
3.024E+007 2.516E-003 9.971E-004

```


`TOTAL HARMONIC DISTORTION` = `8.245843E+000 PERCENT`


Figure 6.14 Fourieranalysisof the Colpittsoscillator.


SPICE3 the user can define the number of harmonics to be computed by issuing the
following set command in the SPICE3 shell:


spice3> set nfreqs=n


where nfreqs is the keyword and _n_ is the desired number of harmonics. The default
for _n_ is 9.
Another variable that can be set by the user in SPICE3 is the degree of the polynomial used to interpolate the waveform. In order to request polynomial interpolation of
higher degree, the following command must be issued at the SPICE3 shell prompt:


spice3> set polydegree=n


where polydegree is the keyword and _n_ is the degree.


6.5 **SUMMARY**


This chapter presented the analyses performed by SPICE in the time domain. The control statements for each analysis were introduced as well as the specifications of output
variables and result-processing requests. Emphasis was placed on exemplifying the
transient and steady-state responses of both a linear and a nonlinear circuit and comparing the manual derivation with SPICE simulations.


**192** 6 TIME-DOMAIN ANALYSIS


SPICE supports two analysis types in the time domain, transient and Fourier analysis, which are specified by the following control lines:


**. TRAN** _TSTEP TSTOP <TSTART <TMAX>_        - <UIC>

**.FOUR** _freq OULvar]_ _<OULvar2_ _... >_


The. **IC** (initial conditions) statement is a third control statement introduced in this
chapter used for specifying the known node voltages at time _t_ = 0:

**. IC** V _(node] )=valuel_ <V _(node2) =value2 ..._          

Initial conditions can also be defined for individual elements; terminal voltages and initial currents can be used to initialize charge-storage and nonlinear elements. Elementbased initial conditions are taken into account only in conjunction with the **UIC** (use
initial conditions) option in the • **TRAN** statement. Table 6.1 summarizes the ways of
setting initial conditions.
The waveforms of voltages and currents computed in a transient analysis must be
saved by use of the. **PRINT** or • **PLOT** control statement, in tabular or line-printer-plot
format, respectively. The general format of the output request that must accompany a

**• TRAN** line is


**. PRINT/PLOT** **TRAN** _OUT_var] <OULvar2_ _..._        - _<ploLlimits>_


The seven detailed examples in this chapter also highlighted the relation between
large-signal time-domain analysis and small-signal AC analysis.


**REFERENCES**


Gray, P. R., and R. G. Meyer. 1993. _Analysis and Design of Analog Integrated Circuits,_ 3d. ed.
New York: John Wiley & Sons.
Meyer, R. G. 1979. Nonlinear integrated circuits. In _EE 240 Class Notes._ Berkeley: University
of California.
Nilsson, 1. W. 1990. _Electric Circuits,_ 3d ed. Reading, MA: Addison-Wesley.
Pederson, D.O., and K. Mayaram. 1990. _Integrated Circuits for Communication._ Boston:
Kluwer Academic Publishers.


```
  Seven

```

_**FUNCTIONAL**_
_**AND**_ _**HIERARCHICAL**_
_**SIMULATION**_


**7.1** **HIGH-LEVEL CIRCUIT DESCRIPTION**


The example circuits presented in previous chapters use circuit elements, such as resistors, capacitors, and transistors, that have a one-to-one correspondence with components
on electronic circuit boards or ICs. Such a description is generally referred to as a _struc-_
_tural_ representation of the circuit. The simulation of a structural circuit produces very
accurate results, but may take a long time. The analysis time grows proportionally to
the number of components and is dominated by semiconductor elements, which are described by complex nonlinear equations. The analysis time sets a limit on the size of circuits that can be simulated at the structural level. Although circuits with several hundred
to a few thousand components can be analyzed with SPICE on current PCs and engineering workstations, alternate ways of modeling circuits can increase design productivity.
The most common approach is to group several components in a block according
to the function performed. According to this criterion, we can distinguish gain blocks,
oscillators, integrators, differentiators, NAND and NOR blocks, adder blocks, and so
on. Then, the SPICE description needs to be an equivalent circuit that achieves the same
function as the component-level implementation. This functional model can be built
with fewer components and with special SPICE elements, such as controlled sources.
Simulation times for circuits with functional models are considerably shorter than those
for detailed circuits.


**193**


**194** 7 FUNCTIONAL AND HIERARCHICAL SIMULATION


SPICE provides a _subcircuit_ capability, which allows a user to define a subnet or
a block and then instantiate it repeatedly in the overall circuit. For example, the functional, or transistor-level, schematic of a NAND gate can be defined once and then
instantiated repeatedly to form complex digital or mixed analog/digital circuits. This
SPICE feature and its application for large circuits is described in Sec. 7.2.
When the SPICE input of large circuits is prepared, the netlist description can be
very long and difficult to understand. A hierarchical approach to describing large circuits is recommended; with this approach a designer can quickly recognize the top-level
block diagram of the circuit from the SPICE description. The subcircuit definition capability of the SPICE input language provides the means for hierarchical descriptions.
An example of SPICE hierarchical definition is described in Sec. 7.2. **In** a hierarchical
description various blocks can be described at different levels of accuracy.
The simplest representation of the function of a given block is an _ideal model._
Ideal functional blocks are introduced in Sec. 7.3 for both analog and digital circuits.
Ideal blocks are very simple and result in short simulation times but may not provide
sufficient accuracy or adequate SPICE convergence, as described in Chap. 10.
More complex models for SPICE simulation can be developed, which reproduce
detailed characteristics of the circuit, such as limited output swing, finite bandwidth,
and other range restrictions. These models combine SPICE primitives (Chap. 2) and
arbitrary functions (Sec. 7.4.1) to _formjunctional models._ A few examples of functional
models are presented in Sec. 7.4.
All details of the operation of circuit blocks or entire ICs can be built into SPICE
primitives. The macro-model can incorporate all or a part of the first- and second-order
effects of a circuit with a considerably smaller number of elements, resulting in significantly shorter simulation times. An operational amplifier macro-model commonly used
by many suppliers of SPICE models for standard parts is described in Sec. 7.5.


**7.2** **SPICESUBCIRCUIT AND CIRCUIT HIERARCHY**


**7.2.1** **.SUBCKT Definition**


A circuit block that appears more than once in the overall circuit and consists of SPICE
primitives can be defined as a _subcircuit_ (Vladimirescu, Zhang, Newton, Pederson, and
Sangiovanni-Vincentelli 1981). The block can then be referenced as a single component, the _subcircuit instance,_ and connected throughout the circuit. There is a similarity between **the.** **SUBCKT** definition and the **.MODEL** definition. Whereas a **.MODEL**
statement defines a set of parameters to be collectively used by a number of devices,
the • **SUBCKT** definition represents a circuit topology, which can be connected through
its external pins or nodes anywhere in the circuit.
The elements that form the sub circuit block are preceded by the following control
statement:

**. SUBCKT** _SUBname node} <node2 ..._       

SPICE SUBCIRCUIT AND CIRCUIT HIERARCHY **195**


where _SUBname_ uniquely identifies the subcircuit and _nodel, node2, ..._ are the external nodes that can be connected to the external circuit. There is no limit to the number
of external nodes. The rest of the nodes in the subcircuit definition are referred to as
internal nodes. The internal nodes cannot be connected or referenced in the top-level
circuit. The ground node, node 0, is global from the top circuit through all subcircuits.
The completion of the subcircuit definition is marked by the following line:


**. ENDS** _<SUBname>_


Repetition of _SUBname_ is not required, except for nested subcircuit definitions, but is
recommended for the ease of checking the correctness of the circuit description.
In addition to SPICE elements, a number of control statements can be used within a
subcircuit definition. Local •MODEL lines introduce models that can be referenced only
by elements that belong to the subcircuit. Other • **SUBCKT** definitions can be nested inside a subcircuit; nested subcircuits can only be referenced from the subcircuit in which
they are defined. No other control lines, that is, analysis, print/plot, or initialization requests, are allowed in a subcircuit definition. One difficulty created by this restriction is
related to initializing node voltages. Although device initial conditions can be defined
for elements inside a subcircuit, no • **NODESET** **or .** **IC** statement can be used to set the
starting voltages on internal nodes. This limitation is overcome by declaring all nodes
that require initialization as external nodes on the • **SUBCKT** line.


**7.2.2** **Subcircuit Instance**


A subcircuit block is placed in the circuit by an _X-element_ call, or subcircuit call, defined
by the following line:


_Xname xnodel <xnode2 ..._        - _SUBname_


The letter X must appear in the first column to identify a subcircuit instance; the number
of nodes must be equal to those on the corresponding subcircuit definition, _SUBname._
_xnode l, xnode2, ...,_ are the numbers or names of the nodes that are to correspond with
the nodes _nodel, node2, ..._ of **the.** **SUBCKT** line, at the circuit level where _SUBname_
is instantiated.
Subcircuit definition and calls can be exemplified by a hierarchical description of
the three-stage ring oscillator in the previous chapter, Example 6.5. The new SPICE
description, using inverters rather than the detailed schematic of the circuit as in Figure
6.9 is listed in Figure 7.1. The corresponding circuit diagram is shown in Figure 7.2.


**7.2.3** **Circuit Hierarchy**


The SPICE subcircuit capability offers the designer the ability to describe a complex
circuit in a hierarchical fashion. Any number of hierarchical levels can be defined. The


196 7 FUNCTIONAL AND HIERARCHICAL SIMULATION


`RING OSCILLATOR` _WI_ `MOS INVERTERS`

       ```
      Xl 1 2 5 INVERTER
      X2 2 3 5 INVERTER
      X3 3 1 5 INVERTER
```

       ```
      VDD 5 0 5
```

      ```
      .SUBCKT INVERTER 1 2 3
```

      - `NODES: VIN, VOUT, VDD`
```
      M1 2 1 0 0 ENH L=10U W=40U
      M2 3 2 2 0 DEP L=10U W=5U
```

       ```
      .MODEL DEP NMOS LEVEL=l VTO=-3 LAMBDA=.OOl KP=.4E-4
      .MODEL ENH NMOS LEVEL=l VTO=l.8 CGS0=20N LAMBDA=.OOl KP=.4E-4
```

      ```
      .ENDS INVERTER
```

       ```
      .IC V(l)=5 V(2)=0
      .TRAN .0lD .5U
      .PLOT TRAN V(l) V(2) V(3) (0, 5)
      .WIDTH OUT=80
      .END

```

Figure 7.1 SPICE input for ring oscillator with MOS inverters using .SUBCKT.


hierarchical description of an adder built from NAND gates is presented in this section
as an example of the proper application of the SPICE      - SUBCKT statement.


_EXAMPLE 7.1_


Use sub circuits and hierarchy to create the SPICE input of the 4-bit adder built with
TIL NAND gates that is shown in Figure 7.3 (Vladimirescu 1982). Partition the adder
at the following levels: NAND gate, I-bit adder, and 4-bit adder. Run SPICE to find
the DC operating point of the I-bit adder and interpret the results.


_Solution_
The first step is to write the SPICE netlist of the TIL NAND gate in Figure _7.3.a._ This
description is listed between the . SUBCKT NAND and . ENDS NAND lines. The external nodes, or terminals, of the NAND gate are the two inputs INl and IN2, the output,
OUT, and the supply connection, VCC. These are the only pins needed for connecting a
NAND gate in an external circuit and correspond to the pins available in a 7400-series
TILle.


SPICE SUBClRCUIT AND CIRCUIT HIERARCHY **197**


**Figure 7.2** Ring oscillator with MOS inverters.


Next, a description of the I-bit adder is created by specifying how the nine NAND
gates in the schematic in Figure _7.3.b_ are connected. The NAND gates are instantiated
in the I-bit description using the X element. This new circuit is labeled as subcircuit
ONEBIT and is used at the next level of the hierarchy to define the 4-bit adder. The
external nodes of ONEBIT are the two inputs, A and B, the carry-in bit, CIN, the output,
OUT, and carry-out bit, COUT, as well as the supply, vee. When digital circuits are
described in the following sections of this chapter, node names are uppercase, such as
A and OUT, the voltages or analog signals at these nodes are indicated by an uppercase
_V,_ as in _VA_ and _VOUT,_ and the boolean (digital) variables associated with the terminals
are lowercase, such as _a_ and _out._
Four ONEBIT subcircuits are connected according to Figure _7.3.c_ to form the
4-bit adder. Four instances (X) of ONEBIT are needed to define the FOURBIT subcircuit. The hierarchical SPICE definitions of the 4-bit and I-bit adders and the NAND
gate are listed in Figure 7.4. All the top-level input and output pins of the 4-bit adder are


**198** 7 FUNCTIONAL AND HIERARCHICAL SIMULATION


IN1


IN2


_(a)_


A
B


_(b)_



OUT



I~
~OUT

IN2


. GOUT


GINOUT
----;;0- A
OUT B GOUT



**`r-----------------------------------------i`** _FOURRIT_
I _RITO_ _BITI_ _BIT2_ _BITJ_ I
I
GIN GOUT GIN GOUT GIN GOUTI


BITO A BIT1 A BIT2 A I BIT3
BOUT BOUT B OUT I
**`-----------`** **------** `-----~`


_(c)_

**Figure** 7.3 Hierarchy of 4-bit adder: _(a)_ TTL NAND gate; _(b)_ I-bit adder with symbol;
_(c)_ 4-bit adder.


**SPICE SUBCIRCUIT AND CIRCUIT HIERARCHY** **199**


**connected to signal sources or resistors, respectively. The 4-bit adder circuit defined in**
**Figure 7.4 has three levels of hierarchy.**
**The DC operating point of the I-bit adder can be found by running the SPICE deck**
**shown in Figure 7.5 with the subcircuit definitions listed in Figure 7.4 for** NAND **and**
ONEBIT. **The SPICE2 output in Figure 7.5 seems confusing at first. A long list** of node

```
ADDER - 4 BIT ALL-NAND-GATE BINARY ADDER
```

```
.SUBCKT NAND 1 2 3 4
```

- `NODES:` `IN1` `IN2` `OUT` `VCC`
```
Q1 9 5 1 QMOD
D1CLAMP 0 1 DMOD
Q2 9 5 2 QMOD
D2CLAMP 0 2 DMOD
RB 4 5 4K
R1 4 6 1. 6K
Q3 6 9 8 QMOD
R2 8 0 1K
RC 4 7 130
Q4 7 6 10 QMOD
DVBEDROP 10 3 DMOD
Q5 3 8 0 QMOD
.ENDS NAND
```

```
.SUBCKT ONEBIT 1 2 3 4 5 6
```

- `NODES:` `A B CIN` `OUT` `COUT` `VCC`
```
Xl 1 2 7 6 NAND
X2 1 7 8 6 NAND
X3 2 7 9 6 NAND
X4 8 9 10 6 NAND
X5 3 10 11 6 NAND
X6 3 11 12 6 NAND
X7 10 11 13 6 NAND
X8 12 13 4 6 NAND
X9 11 7 5 6 NAND
.ENDS ONEBIT
```

```
.SUBCKT FOURBIT 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
```

- `NODES:` `INPUT` `- BlTO(2)` `/ BIT1(2)` `/ BIT2(2)` `/ BIT3(2),`

- `OUTPUT` `- BITO` `/ BIT1` `/ BIT2` `/ BIT3,` `CARRY-IN,` `CARRY-OUT,` `VCC`
```
Xl 1 2 13 9 16 15 ONEBIT
X2 3 4 16 10 17 15 ONEBIT
X3 5 6 17 11 18 15 ONEBIT
X4 7 8 18 12 14 15 ONEBIT
```

`.ENDS` `FOURBIT` _**(continued**_ _**on next page)**_


**Figure 7.4** **Hierarchical SPICE definition of a 4-bit adder.**


**200**


```
***
*** DEFINE NOMINAL CIRCUIT
***
Xl 1 2 3 4 5 6 7 8 9 10 11 12 0 13 99 FOURBIT
RBITO 9 0 1K
RBIT1 10 0 1K
RBIT2 11 0 1K
RBIT3 12 0 1K
RCOUT 13 0 1K
VCC 99 0 DC 5V
VIN1A 1 0 PULSE(O 3 0 10NS 10NS 10NS SONS)
VIN1B 2 0 PULSE(O 3 0 10NS 10NS 20NS lOONS)
VIN2A 3 0 PULSE(O 3 0 10NS 10NS 40NS 200NS)
VIN2B 4 0 PULSE(O 3 0 10NS 10NS 80NS 400NS)
VIN3A 5 0 PULSE(O 3 0 10NS 10NS 160NS 800NS)
VIN3B 6 0 PULSE(O 3 0 10NS 10NS 320NS 1600NS)
VIN4A 7 0 PULSE(O 3 0 10NS 10NS 640NS 3200NS)
VIN4B 8 0 PULSE(O 3 0 10NS 10NS 1280NS 6400NS)
```

```
.MODEL DMOD D
.MODEL QMOD NPN(BF=75 RB=100 CJE=lPF CJC=3PF)
.OP
.OPT ACCT
.END

```

**Figure 7.4** _**(continued)**_

```
******* 02/24/92 ***** SPICE 2G.6 3/15/83 ******** 17:44:45 *******

ADDER - 1 BIT ALL-NAND-GATE BINARY ADDER

**** INPUT LISTING TEMPERATURE 27.000 DEG C

***************************************************************************

.SUBCKT NAND 1 2 3 4
```

- `NODES:` `IN1, IN2, OUT, VCC`
```
Q1 9 5 1 QMOD
D1CLAMP,0 1 DMOD
Q2 9 5 2 QMOD
D2CLAMP 0 2 DMOD
RB 4 5 4K
R1 4 6 1.6K.
Q3 6 9 8 QMOD
```

R2 8 0 1K
```
RC 4 7 130
Q4 7 6 10 QMOD
DVBEDROP 10 3 DMOD
Q5 3 8 0 QMOD
.ENDS NAND

```

**Figure 7.5** **SPICE2 output for I-bit adder.**


```
 .SUBCKT ONEBIT 1 2 3 4 5 6
* NODES: A, B, CIN, OUT, COUT, VCC
Xl 1 2 7 6 NAND
X2 1 7 8 6 NAND
X3 2 7 9 6 NAND
X4 8 9 10 6 NAND
x5 3 10 11 6 NAND
X6 3 11 12 6 NAND
X7 10 11 13 6 NAND
X8 12 13 4 6 NAND
X9 11 7 5 6 NAND
 .ENDS ONEBIT
***
*** DEFINE NOMINAL CIRCUIT
***
Xl 1 2 9 0 13 99 ONEBIT
RBITO 9 0 1K
RCOUT 13 0 1K
.MODEL DMOD D
.MODEL QMOD NPN(BF=75 RB=100 CJE=lPF CJC=3PF)
VCC 99 0 DC 5V
VIN1A 1 0 PULSE(O 3 0 10NS 10NS 10NS 50NS)
VIN1B 2 0 PULSE(O 3 0 10NS 10NS 20NS lOONS)
```

 
 ```
.OP
.OPT ACCT NODE
.WIDTH OUT=80
.END
******* 02/24/92 ******** SPICE 2G.6 3/15/83 ******** 17:44:45 ****

ADDER - 1 BIT ALL-NAND-GATE BINARY ADDER

**** ELEMENT NODE TABLE TEMPERATURE = 27 .000 DEG C

***************************************************************************

    1 VIN1A DlCLAMP* DlCLAMP* Q1.X1.X1 Q1.X2.X1
    2 VIN1B D2CLAMh DlCLAMP* Q2.X1.X1 Q1.X3.X1
    9 RBITO DlCLAMh DlCLAMP* Q1.X5.X1 Q1.X6.X1
   13 RCOUT DVBEDRO* Q5.X9.X1
   99 RB.Xl.X1 Rl. Xl. Xl RC.X1.X1 RB.X2.X1 Rl.X2.X1 RC.X2.X1 RB.X3.X1
       Rl.X3.X1 RC.X3.X1 RB.X4.X1 R1.X4.X1 RC.X4.X1 RB.X5.X1 Rl.X5.X1
       RC.X5.X1 RB.X6.X1 R1.X6.X1 RC.X6.X1 RB.X7.X1 R1.X7.X1 RC.X7.X1
       RB.X8.X1 Rl.X8.X1 RC.X8.X1 RB.X9.X1 R1.X9.X1 RC.X9.X1 VCC
   100 DVBEDRO* D2CLAMP* D2CLAMP* D2CLAMP* Q5.X1.X1 Q2.X2.X1 Q2.X3.X1
       Q2.X9.X1
   101 DVBEDRO* D1CLAMP* Q5.X2.X1 Q1.X4.X1
   102 DVBEDRO* D2CLAMP* Q5.X3.X1 Q2.X4.X1

```

**Figure 7.5** _**(continued)**_


_**')1\1**_


```
  103 DVBEDRO* D2CLAMP* D1CLAMP* Q5.X4.X1 Q2.X5.X1 Q1.X7.X1
  104 DVBEDRO* D2CLAMP* D2CLAMP* D1CLAMP* Q5.X5.X1 Q2.X6.X1 Q2.X7.X1
       Q1.X9.X1
  105 DVBEDRO* D1CLAMP* Q5.X6.X1 Q1.XB.X1
  106 DVBEDRO* D2CLAMP* Q5.X7.X1 Q2.XB.X1
  107 Q1.X1.X1 Q2.X1.X1 Q3.X1.X1
  lOB RB.X1.X1 Q1.X1.X1 Q2.X1.X1
  109 R1.X1.X1 Q3.X1.X1 Q4.X1.X1
  110 R2.X1.X1 Q3.X1.X1 Q5.X1.X1
  111 RC.X1.X1 Q4.X1.X1
  112 DVBEDRO* Q4.X1.X1
  113 Q1.X2.X1 Q2.X2.X1 Q3.X2.X1
  114 RB.X2.X1 Q1.X2.X1 Q2.X2.X1
  115 R1.X2.X1 Q3.X2.X1 Q4.X2.X1
  116 R2.X2.X1 Q3.X2.X1 Q5.X2.X1
  117 RC.X2.X1 Q4.X2.X1
  11B DVBEDRO* Q4.X2.X1
  119 Q1.X3.X1 Q2.X3.X1 Q3.X3.X1
  120 RB.X3.X1 Q1.X3.X1 Q2.X3.X1
  121 R1.X3.X1 Q3.X3.X1 Q4.X3.X1
  122 R2.X3.X1 Q3.X3.X1 Q5.X3.X1
  123 RC.X3.X1 Q4.X3.X1
  124 DVBEDRO* Q4.X3.X1
  125 Q1.X4.X1 Q2.X4.X1 Q3.X4.X1
  126 RB.X4.X1 Q1.X4.X1 Q2.X4.X1
  127 R1.X4.X1 Q3.X4.X1 Q4.X4.X1
  128 R2.X4.X1 Q3.X4.X1 Q5.X4.X1
  129 RC.X4.X1 Q4.X4.X1
  130 DVBEDRO* Q4.X4.X1
  131 Q1.X5.X1 Q2.X5.X1 Q3.X5.X1
  132 RB.X5.X1 Q1.X5.X1 Q2.X5.X1
  133 R1.X5.X1 Q3.X5.X1 Q4.X5.X1
  134 R2.X5.X1 Q3.X5.X1 Q5.X5.X1
  135 RC.X5.X1 Q4.X5.X1
  136 DVBEDRO* Q4.X5.X1
  137 Q1.X6.X1 Q2.X6.X1 Q3.X6.X1
  138 RB.X6.X1 Q1.X6.X1 Q2.X6.X1
  139 R1.X6.X1 Q3.X6.X1 Q4.X6.X1
  140 R2.X6.X1 Q3.X6.X1 Q5.X6.X1
  141 RC.X6.X1 Q4.X6.X1
  142 DVBEDRO* Q4.X6.X1
  143 Q1.X7.X1 Q2.X7.X1 Q3.X7.X1
  144 RB.X7.X1 Q1.X7.X1 Q2.X7.X1
  145 R1.X7.X1 Q3.X7.X1 Q4.X7.X1
  146 R2.X7.X1 Q3.X7.X1 Q5.X7.X1
  147 RC.X7.X1 Q4.X7.X1
  14B DVBEDRO* Q4.X7.X1
  149 Q1.X8.X1 Q2.X8.X1 Q3.XB.X1
  150 RB.X8.X1 Q1.X8.X1 Q2.XB.X1

```

**Figure 7.5** _**(continued)**_



**202**


SPICE SUBCIRCUIT AND CIRCUIT HIERARCHY **203**

```
  151 R1.X8.X1 Q3.X8.X1 Q4.X8.X1
  152 R2.X8.X1 Q3.X8.X1 Q5.X8.X1
  153 RC.X8.X1 Q4.X8.X1
  154 DVBEDRO* Q4.X8.X1
  155 Q1.X9.X1 Q2.X9.X1 Q3.X9.X1
  156 RB.X9.X1 Q1.X9.X1 Q2.X9.X1
  157 R1.X9.X1 Q3.X9.X1 Q4.X9.X1
  158 R2.X9.X1 Q3.X9.X1 Q5.X9.X1
  159 RC.X9.X1 Q4.X9.X1
  160 DVBEDRO* Q4.X9.X1
******* 02/24/92 ******** SPICE 2G.6 3/15/83 ******** 17:44:45 ****

ADDER - 1 BIT ALL-NAND-GATE BINARY ADDER

```

`****` `SMALL SIGNAL BIAS SOLUTION` `TEMPERATURE` = `27.000 DEG C`

```
***************************************************************************

NODE VOLTAGE NODE VOLTAGE NODE VOLTAGE NODE VOLTAGE

```

`1)` `0.0000` ( `2)` `0.0000` ( `9)` `0.7616` `( 13)` `0.0178`
```
( 99) 5.0000 (100) 3.5278 (101) 3.6308 (102) 3.6308
(103) 0.0309 (104) 3.5339 (105) 3.4928 (106) 3.6303
(107) 0.0179 (108) 0.8268 (109) 4.9724 (110) 0.0000
(111) 4.8320 (112) 4.1899 (113) 0.0363 (114) 0.8448
(115) 4.9941 (116) 0.0000 (117) 4.9642 (118) 4.2529
(119) 0.0363 (120) 0.8448 (121) 4.9941 (122) 0.0000
(123) 4.9642 (124) 4.2529 (125) 1.9994 (126) 2.7685
(127) 1.1122 (128) 1.0745 (129) 4.9998 (130) 0.5122
(131) 0.0672 (132) 0.8752 (133) 4.9745 (134) 0.0000
(135) 4.8444 (136) 4.1940 (137) 0.7979 (138) 1.5919
(139) 4.8567 (140) 0.0870 (141) 4.9639 (142) 4.1152
(143) 0.0672 (144) 0.8752 (145) 4.9941 (146) 0.0000
(147) 4.9639 (148) 4.2526 (149) 1.9763 (150) 2.7459
(151) 1.0877 (152) 1.0500 (153) 4.9998 (154) 0.4845
(155) 1.9897 (156) 2.7590 (157) 1.1020 (158) 1.0642
(159) 4.9998 (160) 0.5005

  VOLTAGE SOURCE CURRENTS

  NAME CURRENT

  VCC -1.8760-02
  VIN1A 2.0750-03
  VIN1B 2.0750-03

   TOTAL POWER DISSIPATION 9.380-02 WATTS

```

**Figure 7.5** _(continued)_


**204** 7 FUNCTIONAL AND HIERARCHICAL SIMULATION


numbers appears in the SMALL-SIGNAL BIAS SOLUTION _(SSBS)_ section. In order
to understand the.meaning of these newly created node numbers the user must request
the **NODE** option on an • **OPTION** line:


. OPTION NODE


For more detail on SPICE options see Chap. 9, especially the summary in Sec. 9.5.
The ELEMENT NODE TABLE generated by SPICE2 is also part ofthe output listed
in Figure 7.5. A practice that distinguishes the top-level circuit nodes from those generated by the program due to subcircuit expansion is to make the last node number in
the top-level circuit easy to identify. In the adder example the last node number is 99;
therefore all three-digit numbers are introduced due to subcircuit expansion and the
meaning of each node can be derived from the ELEMENT NODE TABLE.
The name of an element connected at a node is formed by concatenating the names
of the X calls at every level of hierarchy to the element name of a SPICE primitive
appearing at the bottom of the hierarchy, in this case the NAND gate definition level.
The composite names are limited to eight characters in SPICE2, making it difficult to
trace the hierarchy path of elements having long names. The composite name starts
with the component name followed by the subcircuit instance names that call it; the
names at different levels of hierarchy are separated by periods. Component RB. X2 . Xl
is the resistor RBof the X2 NAND instance that is part of the I-bit adder Xl. PSpice
uses the composite node names in the SSBS printout.


Once a hierarchy of a circuit is established, a designer can choose among several
levels of detail and accuracy for each hierarchical block. Describing a block by the detailed structural schematic is always straightforward if the schematic is known, but it
may not be economical. The operational amplifier, which is widely used in many designs and is considered a basic circuit element due to its availability in IC implementation can be described as an ideal, functional, macro-model or as a detailed model.
Because the detailed design of an opamp is complex, including from 20 to 50 transistors, it is advisable to select the representation with only those characteristics that are
relevant for a given design. This process is similar to using simpler or more complex
transistor models by selectively specifying values of model parameters representing
certain second-order effects.
The following sections present several approaches to defining SPICE models for
more complex blocks, both analog and digital.


7.3 **IDEAL MODELS**


Ideal models are the simplest and computationally most efficient. As described in the
following sections, for both analog and digital circuits an ideal model provides only
the single most relevant function of a device; for example, an opamp is a gain block and


IDEAL MODELS **205**


a transistor is a switch. Although very efficient in simulation ideal models can cause
problems in SPICE analyses due to the ideality.


**7.3.1** **Operational Amplifiers**


The main characteristics of an opamp are very high gain, very high input resistance, and
low output resistance. An ideal opamp can be reduced to a gain block with infinite input
resistance and zero output resistance, as shown in Figure 7.6. The principle of the virtual
short can be applied in the analysis of circuits with ideal opamps (Dorf 1989; Oldham
and Schwartz 1987; Paul 1989; Sedra and Smith 1990). This assumption consists of


_Vid_ = 0


(7.1)


A commonly used circuit configuration of the opamp is shown in Figure 7.7. The
output voltage in the frequency domain is given by


(7.2)


This feedback connection is often used to implement integrators, differentiators, filters, and amplifiers. An ideal integrator can be built with the circuit in Figure 7.7 by
replacing Z _f_ with a capacitor C _f_ and _Zi_ with a resistor _Ri._ The correct operation as
an integrator can be checked with SPICE both in the time domain and the frequency
domain.


**Figure 7.6** Idealopamp.


**206** 7 FUNCTIONAL AND HIERARCHICAL SIMULATION


Figure 7.7 Opamp in feedback configuration.


_**EXAMPLE**_ _7.2_


Check the operation as a bandpass filter of the circuit shown in Figure 7.8. Use the
ideal opamp description with _a_ _v_ = 10 [5] and the following values for the resistors and
capacitors: _Ri_ = 100 0,; C = I _nF;Rf_ = 10 ko'; _Cf_ = I nF.


_**Solution**_
The SPICE input is listed below. Note that the ideal opamp is defined as a subcircuit (. SUBCKT) that contains just a voltage-controlled voltage source, as shown in
Figure 7.6.


`BAND-PASS FILTER` _WI_ `IDEAL OPAMP`

       ```
      XOP1 0 1 2 OPAMP
      RI 3 4 100
      CI 1 3 1N
      RF 1 2 10K
      CF 1 2 1N
      VID40AC1
```

       

Figure 7.8 Bandpass filter.


IDEAL MODELS **207**

```
.SUBCKT OPAMP 1 2 3
EGAIN 3 0 1 2 1E5
.ENDS
.AC DEC 10 10 1G
.PRINT AC VDB(2) VP(2)
.WIDTH OUT=80
.END

```

The transfer function of this active filter is obtained through substitution of the
expressions for _Zi_ and _Zf_ in Eq. 7.2:



_H(jw)_ = V [o] =
**Vid**



__ Rf_ _._ _jw_


_i_
_R_ _(_
_RfCf_ _~w_ + _RfCf_ 1)( _jw_ + _Riq_ 1)



(7.3)



In the pass-band, where 1/ _(RfCf)_ « _w_ « 1/ _(RiCi),_ the transfer function becomes


(7.4)


The limits of the pass-band for this active filter are defined by the two poles:


_PI_


_P2_ _=_ -10 [7] rad/s (7.5)
_RiCi_


The magnitude and phase resulting from the SPICE frequency analysis are plotted
in Figure 7.9. The Bode plot produced by SPICE is in agreement with the behavior
predicted by Eqs. 7.3-7.5; that is, the pass-band extends from 15.9 kHz to 1.59 MHz.


The ideal opamp model presented above is a useful concept for instructional purposes and quick hand calculations. Its use in SPICE simulations should be limited due
to the potential numerical problems that can be caused by the approximations involved.
A very important nonideality factor to consider in large-signal analyses is the supply voltage, which limits the excursion of the output signal, as shown by the transfer
characteristic, _Va_ versus _Vid,_ in Figure _7.10.Q._ The output voltage of the open-loop ideal
opamp model, however, can rise to thousands of volts, possibly causing simulation problems depending on the circuit. The desired large-signal transfer characteristic can be
achieved by adding a voltage limiter to the output stage.


**208** 7 FUNCTIONAL AND HIERARCHICAL SIMULATION


         

lD `-25`
-c
ai
-g -50
~
g'
:a: `-75`


-100


```
-------------0

```


-100 "'C
::T
Dl
~

`-200` 0
-300 coCD m CD _en_


```
-200

```


-300



-400



10 [2] 10 [3] 10 [4] 10 [5] 10 [6] 10 [7] 10 [8]


Frequency, Hz

**Figure 7.9** Magnitude and phase of _Va_ of bandpass filter.



_vee_



_Vo_


_Ve_
## 1



_Ve_
_R_ _o_
+
+

_**Vid**_ _R;_ _g;v;d_ t _Ree_ `C` e _Vd_ _°dVd_


_`D`_ _2_


        -         
_(b)_
_VEE_
### r



_Ve_
_R_ _o_
+ +
_Vo_
+
_**Vid**_



_`D`_ _2_




- 


_(a)_ _(b)_
_VEE_



_Vee_


_**Vid**_ _Vo_


_VEE_
_(c)_


**Figure 7.10** Nonideal operational amplifier: _(a) Va_ versus _Vid_ transfer characteristic;
_(b)_ opamp model; _(c)_ opamp symbol.


IDEAL MODELS **209**


Two additional nonideality factors that should be added to the opamp model in order
to avoid very high currents are input and output resistances, _Rill_ and _R_ _o._
The ideal opamp also assumes that the frequency bandwidth is infinite; in reality the
bandwidth of the opamp is finite and is defined by an internal compensation capacitor.
A simple but nonideal opamp model that includes the above properties is presented
in Figure _7.IO.b,_ and the revised symbol is in Figure 7.IO.c. An intermediate stage has
been added to this model to include the single-pole roll-off of the frequency characteristic. The pole is defined by the intermediate stage at 10 Hz, which corresponds to a value
Ce = 1.59. 10- [2] F and _Re_ = 1 O. Note that the simple nonideal opamp model has
five terminals, which include the two power supplies, _Vee_ and _VEE._ The corresponding
SPICE sub circuit description using typical values is listed below .

```
       .SUBCKT OPAMP 1 2 3 4 5
```

       - `TERMINALS:` `IN+` `IN-` `OUT` `VCC` `VEE`
```
      RIN 1 2 1MEG
```

       - `GAIN` `STAGE`
```
      GI 0 6 1 2 1
      RCC 6 0 1
      CC 6 0 1. 59E-2
```

       - `OUTPUT` `STAGE`
```
      EGAIN 7 0 6 0 1E5
      RO 7 3 100
      VC 8 3 0.7
      VE 3 9 0.7
      D1 8 4 DMOD
      D2 5 9 DMOD
       .MODEL DMOD D RS=l
       .ENDS

```

**7.3.2** **Logic Gates and Digital Circuits**


Many circuits simulated with SPICE have both analog and digital functions. If the analog blocks are required to be characterized with very high accuracy, the digital functions
might not be critical to the performance of the circuit but might need to be included for
verifying the correct operation of the overall circuit. **In** this case simplified versions of
the logic blocks can be used. The simplest and computationally most efficient are the
ideal models.
Ideal models oflogic gates can be implemented with switches. Ideal logic gate models can be easily derived from the NMOS implementation (Hodges and Jackson 1983).
The MOS transistor in this implementation acts as a voltage-controlled switch. The
ideal models ofthe NAND, AND, NOR, OR, and XOR gates using voltage-controlled
switches and positive logic are shown in Figure 7.11. These ideal models of logic
gates can be used to simulate circuits in SPICE3 and PSpice but not in SPICE2.


210 7 FUNCTIONAL AND HIERARCHICAL SIMULATION


Computationally efficient models for logic gates accepted by SPICE2 can be implemented as functional models using controlled sources. These models are presented in
Sec. 7.4.


_**EXAMPLE**_ _7.3_


Derive the most efficient implementation of the I-bit adder (Figure _7.3.b)_ using the
ideal gates shown in Figure 7.11. Compute the response to signals _a,_ _b,_ and Ci in Figure
7.12. using SPICE; compare the results and the run time with those obtained with the
detailed model of Figure _7.3.b,_ the SPICE input of which is listed in Fig. 7.5.


_Solution_
The Boolean function, s, implemented by the I-bit adder with carry-in Ci and carry-out

_Co,_ is


s = _a_ + _b_ + Ci

_Co_ = _(a_ + _b)ci_ + _a . b_ (7.6)


The logic diagram of the adder is drawn in Figure 7.13 and the corresponding SPICE3
input is given in Figure 7.14. The computed waveforms s and _Co_ for both the ideal and
the detailed implementations (see listing in Figure 7.5) are displayed with the input signals on the same graph in Figure 7.12, for convenient verification of correct operation.
The analysis time for the ideal circuit in SPICE3 on a SUN 4/110 workstation
is 1.2 s (no hysteresis), whereas that of the all-NAND implementation is 146 s. In
PSpice on an IBM PSI2-80 with a 386 processor at 16 MHz the run times 37.9 sand


_V_ _o_



NAND AND
Figure 7.11 Ideal logic gates.



NOR OR XOR


_a_


_b_


_s_ (ideal)


_Co_ (ideal)


_s_ (full)


_Co_ (full)



IDEAL MODELS **211**


50 100 150



Time. ns
**Figure 7.12** I-bit adder simulation: input signals _G,_ _b,_ and _Cj_ and output s and _Co_ for ideal
and full models.


617 s, respectively. Note that the waveforms obtained with the two representations are
different; the ideal model predicts more changes in the output signals, s and _Co,_ than the
detailed circuit. The difference between the operations of the two circuits can be traced
to the instantaneous switching of the ideal version after each change in input, compared
to the delayed response of the transistor-level version: the ideal circuit lacks of charge


_a_

      
_b_


      **Figure 7.13** Logic diagram of the I-bit adder.


```
1-BIT ADDER WITH SWITCHES
```

```
.SUBCKT OR 1 2 3 4
```

- `TERMINALS` `A B OUT VCC`
RL 3 0 1K
```
Sl 3 4 1 0 SW
S2 3 4 2 0 SW
.ENDS OR
```

```
.SUBCKT AND 1 2 3 4
```

- `TERMINALS A B OUT VCC`
RL 3 0 1K
```
Sl 4 5 1 0 SW
S2 5 3 2 0 SW
.ENDS AND
```

```
.SUBCKT XOR 1 2 3 4
```

- `TERMINALS` `A B OUT VCC`
RL 3 0 1K
```
Sl 4 3 1 2 SW
S2 4 3 2 1 SW
.ENDS XOR
```

```
.SUBCKT ONEBIT 1 2 3 4 5 6
```

- `TERMINALS:` `A B CIN OUT COUT VCC`
```
Xl 1 2 7 6 XOR
X2 1 2 8 6 AND
X3 7 3 4 6 XOR
X4 3 7 9 6 AND
X5 8 9 5 6 OR
.ENDS ONEBIT
```

** `MAIN CIRCUIT`

 ```
Xl 1 2 3 9 13 99 ONEBIT
RINA 1 0 1K
RINB 2 0 1K
RCIN 3 0 1K
RBITO 9 0 1K
RCOUT 13 0 1K
VCC 99 0 5
VINA 1 0 PULSE 0 3 0 10N 10N 10N 50N
VINB 2 0 PULSE 0 3 0 10N 10N 20N lOON
VCIN 3 0 PULSE 0 3 lOON 10N 10N lOON 200N
```

 ```
.MODEL SW VSWITCH RON=l ROFF=lMEG VON=2. 5 VOFF=2. 5
```

 ```
.TRAN 2N 200N
.END

```

**Figure 7.14** **SPICE3 description of I-Bit adder.**



**212**


FUNCTIONAL MODELS **213**


storage. Besides predicting incorrect behavior, ideal circuit models can also lead to an
analysis failure in SPICE.


This sec;tionhas introduced the concept of ideal elements. With the hierarchical
specification features of SPICE input language, it is possibleto have one description of
the top-level circuit and use different levels of detail in the component building blocks
or subcircuits. This app~oachwas exemplified above for a full adder~mplemented with
ideal gates rather than the all-NAND TTL transistor-level implementation used in Example 7.1. The savings in simulation time are very important. On the other hand, ideal
models can,be inappropriate for some analyses, as pointed out by the shortcomings of
the ideal opamp.


7.4 F~NCTIONAL **MODELS**


Several ideal subcircuit definitions were introduced in the p~eyious'section that perform the main function of the circuit blocks they model in a SPICE analysis. These
subcircuits are built with just a few SPICE primitives, such as controlled sources, the
equivalent of a gain block, switches, and other components. The circuit structure, or
topology, ofthesesubcircuits is similar to that of the transistor-level implementation.
This section describes how the function of a circuit bl~ck c~mbe modeled using
controlled sources that are nonlinear or of arbitrary functional form. In a departure from
the above circuit models, which are structural, functional models achieve the same operation as the blocks they represent with just a few controlled soUrces connected in a
network having no resemblance to the original one.
In the following subsections a few examples of functional models are provided that
are developed based on the different capabilities of the controlled sources available in
the versions of SPICE under consideration.


**7.4.1** **Nonlinear (Arbitrary-Function) Controlled Sourcesin SPICE3**


A single type of nonlinear controlled source, which covers all possible cases, is supported in SPICE3. Linear sources are treated in the same way as in SPICE2. The general
format for nonlinear controlled sources is


_Bname node} node2 V/I=expr_


B in the first column identifies the controlled source as nonlinear, and _name_ can be an
arbitrary long string, as ~an any element name in SPICE3. The controlled source is
connected between nodes _node}_ and _node2_ and is either a voltage or a current source
depending on whether the character at the left of the equal sign is V or **I,** respectively.
The variable _expr_ is an arbitrary function of the node voltages and currents in the
circllit All common ~l~m~ntm;v flm~tiom: ~~n h~ 1I~~cl in _pynr'_ tr~n~rpntlpnt~l,:>vn


**214** 7 FUNCTIONAL AND HIERARCHICAL SIMULATION


log, ln, and sqrt; trigonometric, sin, cos, tan, asin, acos, and atan; and hyperbolie, sinh, cosh, tanh, asinh, acosh, and atanh. The nonlinear function applies
only to the time domain; in the frequency domain the source assumes a constant voltage or current value equal to the small-signal value in the DC operating point (see Sec.
7.4.2, Eqs. 7.13 to 7.15). PSpice supports, in addition to polynomial sources, nonlinear
controlled sources equivalent to those in SPICE3 and identified as G or E sources depending on whether the output is current or voltage, respectively. These sources are described in the "Analog Behavioral Modeling" section in the PSpice manual (Microsim
Corporation 1991).
Controlled sources described by arbitrary functions enable the user to define functional or behavioral models. It is important to understand that the SPICE algorithms
require nonlinear functions to be continuous and bound. Rapidly growing functions,
such as _exp(x)_ and _tan(x),_ can cause convergence problems, and discontinuous functions, such as 1/ _x,_ can cause an arithmetic exception. A sound approach is to check
that the variables of the functions are in a safe range.
The following example describes how a voltage-controlled oscillator can be modeled in SPICE3 using B-type controlled sources.


_**EXAMPLE 7.4**_


Define a functional model of a voltage-controlled oscillator (VCO) in SPICE3 using B
sources.


_**Solution**_
A VCO generates a signal whose frequency, _Wose,_ is controlled by an input voltage, _Vc:_


_Wose(t)_ = _Wo_ + _Kvc(t)_ = _Wo_ (1 + _K'vc(t))_ (7.7)


where _K_ is the VCO gain in rad. V-1s- [1] and _Wo_ is the signal frequency of the freerunning oscillator when the controlling voltage is zero.
The function for the B source must express the instantaneous value at any time
point; therefore, for a VCO this function is


_vose_ = _Vose_ sin _()ose_ (7.8)



where



_()ose_ = _J:_ _Wose dt_ = _wot_ + _K_ _J:_ Vc _dt_ = _Wo_ _I:_ (1 + _K'vc)dt_ _(7.9)_



Assume that the controlling voltage, _vc,_ ramps up from 0 V to 1 V in the first half
of the time interval and then decreases back to 0 V in the second half of the interval. Vc
is implemented as an independent PWL source whose value must be integrated to obtain


FUNCTIONAL MODELS **215**


the second term of Eq. 7.9. The SPICE3 B-source expression does not allow explicit
_time_ dependence; a PWL voltage source, which varies linearly with time, can be used.
Under the assumption that _fa_ = 10kHz and _K'_ = I V-I, the SPICE3 input circuit
is listed below:

```
      VCO FUNCTIONAL MODEL FOR SPICE3
```

       ```
       * CONTROL VOLTAGE
```

       ```
      VC 1 0 PWL 0 0 0.5 1 1 0
      RIN 1 0 1
```

       ```
      * V(2) IS INTEGRAL IN EQ. 7.9
```

       ```
      BINT 0 2 I=l+V(l)
      CINT 2 0 1
```

       ```
      BVCO 3 0 V=5*SIN(2*PI*10*V(2))
      ROUT 3 0 1
```

       ```
       .PLOT TRAN V(3) V(2)
       .TRAN 0.01 102M UIC
       .END

```

Note that V ( 2) in the expression of BVCO equals the integral of the current through
capacitor CINT and represents the time integral of (1 + _K'vc)_ (see Eq. 7.9). The model
introduced in this example for a VCO is known as _afunctional,_ or _behavioral,_ model.
The waveforms of the controlling voltage, Vc = V (1), and the VCO output, _Vase_
V (3), are shown in Figure 7.15.


**7.4.2** **Analog Function Blocks**


The circuits presented in these sections implement the desired function with the polynomial controlled source (introduced in Chap. 2) in SPICE2 and the arbitrary-function
controlled source in SPICE3 and PSpice.
The nonlinear controlled source can be used to implement a number of arithmetic
functions, such as addition, subtraction, multiplication, and division (Epler 1987). Note
that the results of these operations are analog, rather than digital, or binary, as was the
case in Examples 7.1 and 7.3. Addition and multiplication can be achieved with the
following polynomial, VCVS:

```
      EADD 3 0 POLY (2) 1 0 2 0 0 1 1
      EMULT 3 0 POLY (2) 1 0 2 0 0 0 0 0 1

```

**216** 7 FUNCTIONAL AND HIERARCHICAL SIMULATION


```
   4

   2

```

"C :Eai a
Ci
« E

```
  -2

  -4

```


|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|.|Col10|Col11|Col12|
|---|---|---|---|---|---|---|---|---|---|---|---|
|||||||||||||
|I-f\_ v_|_ ase_<br>_"_||II||/I|||II||_f\_||
|||||||||||||
|||||||||||||
|||||||||||||
|||||||||||||
|ve<br>||||||||||||
|-||||||||||||
|||||||||||||
|-<br>-<br>V<br>V<br>V<br>V<br>V<br>V<br>V<br>V<br>V<br><br> <br>|-<br>-<br>V<br>V<br>V<br>V<br>V<br>V<br>V<br>V<br>V<br><br> <br>|-<br>-<br>V<br>V<br>V<br>V<br>V<br>V<br>V<br>V<br>V<br><br> <br>|-<br>-<br>V<br>V<br>V<br>V<br>V<br>V<br>V<br>V<br>V<br><br> <br>|-<br>-<br>V<br>V<br>V<br>V<br>V<br>V<br>V<br>V<br>V<br><br> <br>|-<br>-<br>V<br>V<br>V<br>V<br>V<br>V<br>V<br>V<br>V<br><br> <br>|-<br>-<br>V<br>V<br>V<br>V<br>V<br>V<br>V<br>V<br>V<br><br> <br>|-<br>-<br>V<br>V<br>V<br>V<br>V<br>V<br>V<br>V<br>V<br><br> <br>|-<br>-<br>V<br>V<br>V<br>V<br>V<br>V<br>V<br>V<br>V<br><br> <br>|-<br>-<br>V<br>V<br>V<br>V<br>V<br>V<br>V<br>V<br>V<br><br> <br>|-<br>-<br>V<br>V<br>V<br>V<br>V<br>V<br>V<br>V<br>V<br><br> <br>|-<br>-<br>V<br>V<br>V<br>V<br>V<br>V<br>V<br>V<br>V<br><br> <br>|


`200` 400 `600` `800`



Time, ms
Figure 7.15 Waveforms _Vase_ and _Vc_ for veo functional model.


The functions implemented by the two elements are


_V3_ = _VI_ + _V2_

_V3_ = _VI V2_



(7.10)


(7.11)



where _VI, V2,_ and _V3_ are the voltages at nodes 1,2 and 3, referenced to ground, which
is node O.For details on the **POLY** coefficient specification see Sec. 2.3.2.
A divider is slightly more complex and requires two poly sources, as shown in
Figure 7.16. The SPICE specification ofthe two VCCSs needed is

```
GV130101
GV2V3 0 3 POLY (2) 2 0 3 0 0 0 0 0 1

```


CD
+0--_v,_
-0--

(2)
+0--_v2_
-0--Figure 7.16 Divider circuit.



+


FUNCTIONAL MODELS **217**


The resulting output voltage, _V3,_ is the quotient _VI/V2_ because of the equality of the
currents of the two.VCCSs imposed by the KCL:


(7.12)


Note that the large output resistor is needed to satisfy the SPICE topology checker,
which would otherwise flag the two controlled current sources in series as an error.
An important observation regarding the use of nonlinear controlled sources is that
the desired function, such as multiplication or division, is performed only in a DC or
time-domain large-signal analysis but not in a small-signal AC analysis. The cause of
this is the small-signal nature of AC analysis, which 'uses the differential of a nonlinear
function in the DC operating point and not the function itself. The value of the function
expressed by a nonlinear controlled source _f (x_ + ax) when a small signal ax is added
to the quiescent value of the controlling signal _x_ is


(7.13)


Therefore, the controlled source function tJ.,J in sinaU~signalanalysis is a linear function
given by ., " I." . .
.'
_,_ _df"_
_D.j,=-D.x_
_, "dx_ ..


The derivative offis computed in DC bias-point analysis in a way similar to the evaluation of small-signal conductances of semiconductor devices (see Secs. 3.2, 3.3.2, 3.4,
and 3.5.2). A controlled source with two arguments, Xl and _X2,_ is evaluated in AC analysis accordip.g to


(7.14)


. .
The addition and multiplication functions implemented with polynomial controlled
sources are evaluated according to the following equalitie~ in AC analysis:



_fs_ == Xl + _X2,_

_fM_ = XIX2,



_D.fs_ = D.XI + _D._ _X2_

_D.fM_ = X2D.XI _+'XID._ _X2_



(7.15)



Another useful function that can be implemented with polynomial sources is a meterfor the instantaneous and cumulative power over the time interval of transient analysis. The setup is shown in Figure 7.17 and uses a CCCS to transform the current of the
bias source, _V_ _DD,_ into a voltage with the correct sign and a VCVS to obtain the product
_-iDD VDD._ The voltage _V3_ represents the instantaneous power, and _V4_ is the cumulative


**218** 7 FUNCTIONAL AND HIERARCHICAL SIMULATION


**Figure 7.17** Power-measuring circuit.


power from 0 to the current time:




- lQ 0



lQ



IF



(7.16)


The average power at any time point can be obtained by dividing _V4_ as given in Eg.
7.16, by the current time, which can be measured by a PWL voltage source whose
value increases proportionally with the analysis time.
The ease of defining functional models is greatly enhanced by the arbitrary controlled sources available in SPICE3 and PSpice. A good example is the limiter circuit
that was used in the previous section at the output of a nonideal opamp block. The output characteristic shown in Figure 7.18 is similar to that of a differential amplifier (Gray
and Meyer 1993) and is expressed by



_avvid_
_V_ _o_ = _Vee_ tanh _-V_
ee


20


10



",0
°


-10


-20


-1.0 -:0.5 ° 0.5 1.0


**Figure 7.18** Output of tanh _x_ limiter functional block.



(7.17)


FUNCTIONAL MODELS **219**


In general the function tanhx is ideally suited to implementing a limiter; for small
values of the argument it is approximately equal to the argument, according to the series
expansion:


I 3 2 5
tanhx = _x - -x_ + _-x_ _- ..._ (7.18)
3 15


Its absolute value is limited at 1 for large values of the argument. The limiter built
with the arbitrary controlled source defined by Eq. 7.17 allows the output voltage _V_ _o_ to
follow the input voltage _Vid_ amplified by _av_ as long as _avvid_ is smaller than the supply
voltage and then limits _Vo_ to the supply when _avvid_ surpasses the supply voltage. The
functional description of a differential amplifier built with an emitter-coupled pair (Gray
and Meyer 1993) is as follows:


_V_ _o_ = _exRchE_ tanh - _(_ _2~thV"d)_ (7.19)


where _hE_ is the sum of the emitter currents, _ex_ is the CB gain factor, and _Rc_ is the
collector resistance, which is equal for the two input transistors of a differential pair.
A functional limiter can be built also for SPICE2, but it takes more components
(Mateescu 1991). The behavior of arctan _x_ is similar to that of tanh _x,_ assuming values
between 0 and 7r when _x_ varies from -00 to 00, and it can be represented by conventional
polynomial sources, because the derivative of the arctangent is


_d_ _u'_

                     - arctanu = (7.20)
_dt_ 1 + _u_ _[2]_


Therefore the limiter can be built by implementing the right-hand side of Eq. 7.20 and
then integrating it to obtain

_V_ _o_ = _2V_ _[cc]_ (f __U_'_dT_ ___ _~)_ (7.21)
7r Jo 1 + _u_ _[2]_ _2_


where


The functional limiter for SPICE2 is shown in Figure 7.19. The behavior of arctan _x_ is
identical to that of tanh _x,_ that is, for small values of the argument it can be approximated
by the value of the argument, and for large values of the argument it is limited to a
constant value.


**220** 7 FUNCTIONAL AND HIERARCHICAL SIMULATION


   - `CD`


**Figure 7.19** Circuit diagram of arctan _x_ limiter.


The voltages at nodes 2, 5, 6, 7, and 9 are given in the following equations.


7T _avVid_
_V2_ = _U_ = -'-_2_ _Vee_


_V9_ = _u'_


_u'_



_I_



_t_ _`u'`_
_V6_ = _---dT_

    - 1 + _u_ _[2]_



_V7_ __ 2Vee-_ _--_ _(It_ _---_ _u'_ _d_ T ___ 7T)7T 0 1 + _u_ _[2]_ _2_



Each section in Figure 7.19 performs a specific function, such as division, differentiation, or integration, toward the realization of Eq. 7.21. The differentiator is built with
an ideal opamp. Each section is also identified by comments in the SPICE2 input listed
in Figure 7.20. The voltages representing the values ofthe integral, its arguments, and
the limiting output function are plotted in Figure 7.21.
Functional models must be used with care to avoid arithmetic exceptions such
as division by zero. Another important point is to initialize differentiators and integra

FUNCTIONAL MODELS **221**

```
ARCTAN (X) LIMITER
```

 ```
VIN 1 0 PWL 0 -1M 2 1M
RIN 1 0 lMEG
```

 
 - `COMPUTE THE ARGUMENT U, EQ. 7.21`

 ```
GV 0 2 1 0 lE5

G2 2 0 2 0 9.54
R2 2 0 lE12
```

** `DIFFERENTIATION` `CKT TO COMPUTE U'`

 ```
E3 3 0 201
C3 3 4 1 1('=-10.48
R3 4 0 lE12
EDIF 9 004 lE3
RDIF 4 9 1
RO 9 0 lE12

                 A
```

** `COMPUTE U'/(I+U` `2)`

 ```
GVP05901
G5 5 0 POLY (2) 2 0 5 0 0 0 1 0 0 0 0 1
R5 5 0 lE12
```

 
 - `INTEGRATION CKT, COMPUTES INTEGRAL OF V (5)`

 ```
G6 0 6 5 0 1
R6 6 0 lE12
C6 6 0 1
```

** `LEVEL-SHIFT AND SCALE`

 ```
E7 7 0 POLY (1) 6 0 -15 9.54
R7 7 0 1
```

```
.TRAN .01 2 0 UIC
.PRINT TRAN V(5) V(6) V(7)
.END

```

**Figure 7.20** **SPICE deck for arctan** _**x**_ **limiter.**


**tors in the expected initial states in order to avoid convergence** **failures. The capacitor**
**of the differentiator,** _C3,_ **used in the arctan** _**x**_ **function is initialized with the appropriate**
**voltage at** _**t**_ **= 0 in order to prevent a convergence** **failure due to a large voltage at the**
**input of the ideal opamp.**


**222** 7 FUNCTIONAL AND HIERARCHICAL SIMULATION


5


    - 0
,.""


-5


-10


-15


-1.0 -0.5 0 0.5 1.0


_V;d=_ V(1),mV


**Figure 7.21** Simulation results of SPICE2limiter.


So far we have defined a number of functional blocks, such as the adder, the multiplier, the integrator, and the differentiator; these can be saved in a library and then used
in any circuit where such blocks are needed.
A functional block that proves very useful in many simulations is a frequencydomain transfer function. Some proprietary SPICE simulators, such as PSpice and
SpicePLUS (Valid Logic Systems 1991), support a frequency-domain transfer function. With this capability a variety of filters can be described by the locations of poles
and zeros.
With an arbitrary frequency-domain transfer function block one could define the
parallel RLC circuit of Example 6.2 by the following transfer function:


_Ls_

(7.22)
_LCs_ _[2]_ + _Ls/R_ + 1


The PSpice input specification for this block is

```
       .PARAM L=lMH C=lNF R=10K
      EFILTR 1 0 LAPLACE {I(VIN)}={L*s/(L*C*s*s+L/R*s+l)}

```

This block can replace the RLC lumped-element representation in Example 6.2. Both
a frequency- and a time-domain analysis can be performed with this block.


FUNCTIONAL MODELS 223


_Exercise_
Show that the time-domain response of the above block to a current step function calculated by PSpice is identical to the response of the lumped RLC circuit in Figure 6.2.


7.4.3 **Digital** **Function** **Blocks**


In Sec. 7.3, on ideal building blocks, digital gates were implemented with simple circuits that are structurally similar to actual implementations but use ideal elements, such
as switches. All digital gates can be described at a functional level with polynomial
sources (Sitkowski 1990). The elements presented below implement the analog operation of digital circuits, that is, logic levels 0 and 1 are expressed in voltages corresponding to positive logic.
The structure of a universal gate is shown in Figure 7.22. The supply and input
resistors are chosen to model the behavior of a TTL gate. The operation of this model is
based on the correspondence of the logical AND operation to multiplication. The AND
function is implemented by the VCVS EAND, which contains only the term _VA VB:_

```
      EAND OUT 0 POLY (2) A 0 BOO 0 0 0 0.2

```

Assuming that _VA_ and _VB_ take values between 0 and 5 V,the product must be scaled by
0.2 so that the output voltage _V_ _OUT_ is 5 V when both inputs are at a logical 1. In order
to model the OR function, DeMorgan's theorem (Mano 1976) is applied to transform
the OR function into an AND function, which can be implemented as above:



100Q



(7.23)



_a+b=ii.Jj_


vc


3.12 kQ


_E_
1GQ


```
OUT

```


A


B



3.12 kQ


1GQ



+



Figure 7.22 Universal gate functional model.


**224** 7 FUNCTIONAL AND HIERARCHICAL SIMULATION


The inversion of the input signals is achieved by referencing the two input signals, _VA_
an9 _VB,_ to _Vee_ rather than to ground; the inversion of the output function, the NAND
function, is achieved by inverting the polarity of the controlled source and subtracting
5 V from the result. According to Eq. 7.23, the OR function becomes

```
      EaR 0 OUT POLY(2) A VC B VC -5 0 0 0 0.2

```

The NAND function needs only to have the output inverted, and the NOR function needs
only the inputs inverted, with respect to the AND function, according to Eq. 7.23:

```
      ENAND 0 OUT POLY(2) A 0 B 0 -5 0 0 0 0.2
      ENNOR OUT 0 POLY(2) A VC B VC 0 0 0 0 0.2

```

The XOR and XNOR functions are implemented according to the definition


_a_ E9 _b_ = _iib_ + _ab_ (7.24)


These functions need four variables, _a, ii,_ _b,_ and _b,_ and therefore a four-dimensional
polynomial is used. Each variable and its inverse introduce two controlling voltages;
that is, input _a_ is _VA_ and input _ii_ is _Vee -_ _VA'_ The SPICE definitions of the VCVS for
the XOR and XNOR functions are, respectively,

```
      EXOR OUT 0 POLY(4) VC ABO A 0 VC BOO 0 0 0 0 0.2 0 0 0 0 0 0 0.2
      EXNOR 0 OUT POLY (4) VC ABO A 0 VC B -5 0 0 0 0 0 0.2 0 0 0 0 0 0 0.2

```

The order of the coefficients follows the rule introduced in Sec. 2.3.2. The only terms
of the polynomial used in both functions are the product of variables I and 2, _iib,_ and
the product of variables 3 and 4, _ab,_ leading to the following expression of the XOR
function


_VOUT_ = _O.2(Vee -_ _VAWB_ + _O.2(Vee -_ _VBWA_


The two terms require the definition of coefficients _P6_ and _P13_ for both XOR and XNOR.
The XNOR function is implemented by switching the polarity of the VCVS. Note that
for SPICE2 the node names used above must be replaced by numbers:
i


**7.4.4** **Equation Solution**


The operation of electrical systems as well as nonelectric systems, such as mechanical,
hydraulic, and electro-mechanical systems, are described by complex nonlinear differential equations. In order to simulate these devices with SPICE it is necessary to create
a model or, equivalently, to cast the component equation in a form that the program
can understand and solve. The functional models defined above can be combined in
creative ways to solve most complex equations describing not only electrical but also
other physical systems.


FUNCTIONAL MODELS 225


_**EXAMPLE**_ _7.5_


With the functional blocks defined above develop a circuit that can be used in SPICE
to model the turn-on I-V characteristic of a fluorescent discharge lamp. The relationship between the current, _I,_ and the voltage, _V,_ of the lamp is defined by the following
equation:


           - _dG_ = _aI_ _[2]_ + _bIV_ + c _V_ _[2]_ + _d_ _(I-_ )3 + _e -(I_ )2 + _f -_ _I_ (7.25)
_~_ _V_ _V_ _V_


where G is the conductance of the lamp. Create a model for both an arbitrary controlled
source as well as a polynomial controlled source implementation. After designing the
complete model defined by Eq. 7.25, simulate the turn-on characteristic for a lamp with
the following parameters:


_a_ = 2.422, _f_ = 271.7


The rest of parameters, _b,_ c, and _d,_ equal zero.


_Solution_
The main part of the model is the defining equation of the conductance G, Eq. 7.25;
it can be implemented as a nonlinear controlled voltage source, BRHS, which sums
the terms on the right-hand side of Eq. 7.25. The lamp is represented by a nonlinear
controlled current source, BLAMP, the current of which is


_I_ = GO';;!)' _V_


where _G(V, I)_ is the voltage at node G1, equal to the integral of the right-hand side of
Eq. 7.25. The circuit is shown in Figure 7.23. The corresponding SPICE3 description
is shown in Figure 7.24.
A SPICE2 model can be developed using functional blocks, such as multipliers and
dividers, which implement the terms of the right-hand side of Eq. 7.25, which are then
added. The result is integrated to obtain _V(G_ 1). Note that for PSpice the definitions of
G and of the arbitrary controlled sources BRHS and BLAMP need to be changed to the
following syntax:

```
ERHS 6 0 VALUE={2.422*PWR(I(VA),2)-S.186E4*PWR((I(VA)/V(2)),2)
+ +271.7*(I(VA)!V(2))}
GLAMP 4 5 VALUE={ V(Gl) W(IN) }

```

The I-V characteristic of the lamp obtained from SPICE3 is plotted in Figure 7.25
and corresponds to the operation known from text books.


**226** 7 FUNCTIONAL AND HIERARCHICAL SIMULATION


0 _R_ _a_ CD @
+
J
1

_vB_ `ClO` _R_ _`7`_ BLAMP _`EVS`_ + _R_ _`6`_
100 pF 10MQ _1= VGl VIN_

_VA_


+
0

     
                             

@)


BRHS


**Figure 7.23** Fluorescent lamp functional model.

```
      FLUORESCENT LAMP
      VA 8 0 DC 201 SIN ( 2.01E+02 2E+02 6E+01 -1.2E-02 0 )
      VB 7 8 PWL ( 0 0 0.1 100 )
      C10 4 5 lOOP
      BRHS 6 0 V=2.422*(I(VA)A2)-5.186E04*((I(VA)!V(2))A2)+271.7*(I(VA)!V(2))
      R8 7 4 978M
      R7 5 4 10MEG
      R6 0 IN 1K
      BLAMP 4 5 I=V(G1)*V(IN)
      EV5IN0451
      L3 0 3.55. 7M
      XF2 6 G1 INT1M
      .SUBCKT INTEG 1 2
      RIN1 1 4 2
      RIN2 1 4 2
      G1 2 0 4 0 -1
      R1 2 0 1E12
      C1 2 0 1
      .ENDS INTEG
      VI 5 3 0.0
      .IC V(G1)=1 V(IN)=201
      .TRAN 0.005 .1 0 .5M UIC
      .END

```

**Figure 7.24** SPICE3 input for the fluorescent lamp functional model.


MACRO-MODELS 227


_V1N,V_
Figure 7.25 1-V characteristic of fluorescent lamp.


7.5 **MACRO-MODELS**


A number of concepts have been introduced so far in this chapter on higher-level modeling. The approaches have varied from structural simplifications of the circuit using
ideal elements to pure functional blocks, which synthesize the input/output relationship
of the circuit.
This section introduces the most general and powerful modeling concept, called
_macro-modeling._ Macro-models combine functional elements with accurate nonlinear
models for some elements, such as transistors and diodes, in order to obtain the behavior of the original circuit from a simplified circuit that can be simulated several times
faster.
This concept was first applied to opamps (Boyle, Cohn, Pederson, and Solomon
1974), which contain ten to a hundred transistors in a detailed representation. Since the
introduction in IC realization in the late 1960s, opamps have been widely used in such
circuits as active filters, phase-locked loops, and control systems. A SPICE simulation
of a circuit with more-than a couple of opamps can be very expensive, and the development of macro-models that implement all or part of the data-book characteristics of a
given opamp is crucial. The next section describes a common opamp macro-model. The
components used to model specific characteristics are identified, and their evaluation
from the data sheet is highlighted.


**228** 7 FUNCTIONAL AND HIERARCHICAL SIMULATION


**7.5.1** **The Opamp Macro-Model**


The macro-model developed by Boyle et al. (1974) is described in this section. Unlike the ideal opamp described in Sec. 7.3.1, the macro-model attempts to provide an
accurate representation of differential and common-mode gain versus frequency characteristics, input and output characteristics, and accurate large-signal characteristics,
such as offset, voltage swing, short-circuit current limiting, and slew rate. The approach
described below can be applied to model a broad class of opamps.
The macro-model derivation for the _JLA741_ is outlined below according to Boyle
et al. (1974). The detailed circuit, containing 26 BJTs, is shown in Figure 7.26. The
schematic ofthe macro-model is shown in Figure 7.27. The macro-model ofthe _JLA 741_
opamp is divided into three distinct stages, the input, gain, and output stages; the three
stages are modeled separately to implement all the data-sheet characteristics. These
characteristics are presented in Table 7.1.
The number of transistors in the macro-model has been reduced to only two, which
are necessary to model the correct input characteristics. The gain stage is built with
linear elements, and four diodes are used in the output stage for limiting the voltage
excursion and the short-circuit current. At the conclusion of this section the switching
and frequency-domain characteristics of the macro-model compared with those of the
detailed circuit are shown in Figures 7.31 and 7.33.
The input stage must be designed to reproduce characteristics such as DC offset,
slew rate, and frequency roll-off. The element values and model parameters of _Q!_ and
Qz must be derived from the opamp data sheet, Table 7.1. The gain factor, _f3F,_ of the
two transistors, model parameter _BF,_ is derived from the DC offset and the slew rate.
_I_ _Cl,_ equal to _I_ _ez,_ is established by the positive-going slew rate, S; and compensation
capacitor Cz:


(7.26)


_IB_ of _Q!_ and Qz is taken from the data sheet, and an imbalance is introduced to account
for the offset input current, _IBos:_


_I_ _[BI]_ _-_ _-_ _I_ + _B_ _IBos_ _2'_ (7.27)


_f3F1_ and _f3F2_ are derived from Eqs. 7.26 and 7.27; the input offset voltage, _Vos,_ is due
to an inequality in the two saturation currents, _Is!_ and _IS2,_ according to the following
equation:


(7.28)


which leads to the values of the model parameter _IS_ of _Q!_ and Qz.


_+Vcc_
@
@


@
_-VEE_



@
_Qg_


39kn<Rs


_R4_ _R_ _1_ _R3_



_`C`_ _f_



_`B`_ 1 _`A`_


@



Input Intermediate Output
stage stage stage



~~
1.0



Biasing
reference
network
**Figure 7.26** Detailed _JLA741_ circuit.


~
W
Q
_(Vee!_

    

v.
**I** **I**



_V_ _e_ _-=-_
```
Rc2

```

0
_`R`_ _p_ _`D3`_

_Vb_ @ C 2 _VC_ @ _`Ral`_ Vs
..
CD


```
             D1 D2 D4

```

_`R2`_ @
\{2. _GbVb_ H@
#### r


```
D1 D2 D4

```


_**GemVe**_ **I** I _GaVa_ 1 _GbVb_

Gevs
1 1
**1** **1** -=- -=- '1 -=- f -=##### r



0(+)



_L1EE_
( ~
c,!


0
1
(V _(-VEE)_



\. y---------~) \. y--------)\. y-------~)


Inputstage Interstage Outputstage

**Figure 7.27** p,A741 macro-model.


MACRO-MODELS **231**


**Table 7.1** _fLA741_ Performance Characteristics

**Device-Level**
**Parameter** **Data Sheet** **Model** **Macro-Model**


_Cz_ (pF) 30 30 30
S; _(V/fLs)_ 0.67 0.9 0.899
Si _(V/fLS)_ 0.62 0.72 0.718

_IB_ (nA) 80 256 255

_IBos_ (nA) 20 0.7 <1

_Vos_ (mV) 1 0.283 0.265

_avd_ 2.10 [5] 4.17.10 [5] 4.16.10 [5]

_avd_ (l kHz) 10 [3] 1.219.10 [3] 1.217.10 [3]

!1c/J(degrees) 20 16.8 16.3

CMRR(dB) 90 106 106

_Rout_ (n) 75 566 566

_Roose_ (n) 76.8 76.8

_Is~_ (rnA) 25 25.9 26.2

_Is~_ (rnA) 25 25.9 26.2

_V+(V)_ 14 14.2 14.2

_V-_ (V) -13.5 -12.7 -12.7


The emitter resistor, _RE_ is chosen so that it matches the output resistance of a transistor with an Early voltage, _VAF,_ of 200 V:


(7.29)


where _hE_ is the sum of the collector and base currents of QI and _Q2._
The frequency response is established by resistors _Rei_ and _Rc2_ in the input stage
and components of the gain stage. The frequency of the dominant pole, _f3dB,_ set by the
compensation capacitor C2 and by _G_ _a_ = _I/ReI,_ is given by


(7.30)


_Rei_ and _Rc2_ can be derived from the equality



1
_Rei_ = _Rc2_ = 2 -r ~~.~~ C
_7TJOdB_ 2



(7.31)


**232** 7 FUNCTIONAL AND HIERARCHICAL SIMULATION


where _fOdB_ is the O-dB frequency from the data sheet; _fOdB_ can be approximated for a
roll-off of 6dB/octave by


(7.32)


There are two more capacitors in the input stage, _CE_ and C 1• The first is included
to model a smaller negative-going slew rate _Sii_ according to the following equality:


\ (7.33)


C 1 models the excess phase at _fOdB_ by introducing a second pole at


(7.34)


With the phase shift !i.<jJ given in the data sheet, C 1 results as


(7.35)


The gain stage is designed to provide the correct differential mode, DM, and common mode, CM, gains. This is achieved by a correct sizing of the transconductances

_Gem_ and _Gb'_ The two gains, _aYd_ and _aye,_ are defined by the following equalities:



_`R`_ _2_
_aYd_ = `R` cl

_aye_ = _GemR2_


_whereR2_ = lOOk!1andGa = l/Rcl.ThevalueofGemisbasedonthecommon-mode
rejection ratio, _CMRR_ = _ayd/_ _aye,_ and is equal to



(7.36)


(7.37)



1

(7.38)
_Gem_ = _(CMRR)R_ ~~_cl_~~


Transconductance _Gb_ defines the correct open-loop DM gain, _ayd,_ and is given by


(7.39)


where _R_ _o_ _2_ is approximately equal to the DC output resistance given in the data sheet.


MACRO-MODELS **.233**


The design of the output stage of the macro-model requires the dimensioning of
diodes D1 and D2 and resistor _R_ _a_ _1_ for current limiting and diodes D3 and D4 and bias
sources _V_ c and _VE_ for proper output voltage limiting.
The complete list of the parameters of the macro-model is provided in Table 7.2,
reproduced from Boyle et a1.(1974); for the detailed derivation of this model see that
paper.


_**EXAMPLE 7.6**_


Compare the voltage-follower slew-rate performance and the open-loop f~equency response to _fOdB_ between the complete _p,A741_ circuit shown in Figure 7.26 and the macromodel in Figure 7.27 with the component values from Table 7.2.


_**Solution**_
First, write the SPICE netlist for the detailed _p,A741,_ called subcircuit UA741, and for
the macro-model, called UA7 41MAC. The two subcircuit definitions are listed in Figure
7.28. Both subcircuits have five external terminals, the two inputs, the output, and the
two supplies.
The circuit for the slew-rate performance is shown in Figure 7.29, and the SPICE
input is shown in Figure 7.30. Note that two unconnected voltage followers; Xl and X2,
are used in order to compare the output voltages, _V3_ and _V6,_ for the two opamp models;
Xl is represented by the macro-model, UA7 41MAC, and X2 is described by the complete
circuit, UA741, listed in Figure 7.28. A 20-p,s pulse from - 5 V to 5 V is applied to
the positive input ports of both opamps. The offset voltages _Vas_ corresponding to each
model are applied as DC biases at the inputs of the two opamps. The two waveforms
of _VOUT_ are plotted in Figure 7.31 and can be seen to match very well.


**Table 7.2** _p,A741_ Macro-Model Parameters

**Parameter** **Value** **Parameter** **Value**



_lSI_ (A) 8.10- [16] _Rp(kO)_ 15.363



b(A) 8.0925.10- [16] _Ga({.Lmho)_ 229.774



(31 52.6726 _Gem(nmho)_ 1.1516



(3z 52.7962 Gb(mho) 37.0978



_leE ({.LA)_ 27.512 _Rol(O)_ 76.8



Rei (0) 4352 _Roz(O)_ 489.2



_Rei_ (0) 2391.9 _Ism_ (A) 3.8218 .1O- [3Z]



_RE (MO)_ 7.2696 _Ism_ (A) 8. 10- [16]



_CE_ (pF) 7.5 _Rc(mO)_ 0.1986

CI (pF) 4.5288 Gc (mho) 5034.3

Rz _(KO)_ 100 _Vc_ (V) 1.6042

Cz (pF) 30 _VE_ (V) 3.1042


**234** 7 FUNCTIONAL AND HIERARCHICAL SIMULATION

```
      *************************************
```

      - `DETAILED CIRCUIT FROM BOYLE PAPER`       ```
      *************************************
      .SUBCKT UA741 1 2 24 27 26
```

      - `NODES:` 1m- `IN- OUT VCC VEE`
```
      R1 10 26 1K
      R2 9 26 50K
      R3 11 26 1K
      R4 12 26 3K
      R5 15 17 39K
      R6 23 24 50
      R7 24 25 25
      R8 18 26 100
      R9 14 26 50K
      R10 21 20 40K
      R11 13 26 50K
      CaMP 22 8 30PF
      Q1 3 1 4 BNP1
      Q2 3 2 5 BNP1
      Q3 7 6 4 BPN1
      Q4 8 6 5 BPN1
      Q5 7 9 10 BNP1
      Q6 8 9 11 BNP1
      Q7 27 7 9 BNP1
      Q8 3 3 27 BPN1
      Q9 6 3 27 BPN1
      Q10 6 15 12 BNP1
      Q11 15 15 26 BNP1
      Q12 17 17 27 BPN1
      Q13A 28 17 27 BPN3
      Q13B 22 17 27 BPN4
      Q14 27 28 23 BNP2
      Q15 28 23 24 BNP1
      Q16 27 8 14 BNP1
      Q17 22 14 18 BNP1
      Q18 28 21 20 BNP1
      Q19 28 28 21 BNP1
      Q20 26 20 25 BPN2
      Q21 13 25 24 BPN1
      Q22 8 13 26 BNP1
      Q23A 26 22 20 BPN5
      Q23B 26 22 8 BPN6
      Q24 13 13 26 BNP1
```

       ```
      .MODEL BNP1 NPN BF=209 BR=2.5 RB=670 RC=300 CCS=1.417P TF=1.15N TR=405N
```
+ `CJE=0.65P CJC=0.36P IS=1.26E-15 VA=178.6 C2=1653 IK=1.611M NE=2 PE=0.6`
+ `ME=0.33 PC=0.45 MC=0.33`


**Figure 7.28** Detailed description and macro-model of the _JLA741_ opamp.


**MACRO-MODELS** **235**

```
.MODEL BNP2 NPN BF=400 BR=6.1 RB=185 RC=15 CCS=3.455P TF=0.76N TR=243N
```

+ `CJE=2.8P` `CJC=1.55P` `lS=0.395E-15` `VA=267` `C2=1543` `lK=10M` `NE=2` `PE=0.6`
```
+ ME=0.33 PC=0.45 MC=0.33
.MODEL BPN1 PNP BF=75 BR=3.8 RB=500 RC=150 CCS=2.259P TF=27.4N TR=2540N
```

+ `CJE=0.10P` `CJC=1.05P` `lS=3.15E-15` `VA=55.11` `C2=1764` `lK=270U` `NE=2` `PE=0.45`
+ `ME=0.33` `PC=0.45` `MC=0.33`
```
.MODEL BPN2 PNP BF=117 BR=4.8 RB=80 RC=156 TF=27.4N TR=2540N
```

+ `CJE=4.05P` `CJC=2.80P` `lS=17.6E-15` `VA=57.94` `C2=478.4` `lK=590.7U` `NE=2` `PE=0.6`
+ `ME=0.25` `PC=0.6` `MC=0.25`
```
.MODEL BPN3 PNP BF=13. 8 BR=1. 4 RB=100 RC=80 CCS=2 .126P TF=27. 4N TR=55N
```

+ `CJE=0.10P` `CJC=0.3P` `lS=2.25E-15` `VA=83.55` `C2=84.37K` `lK=5M` `NE=2` `PE=0.45`
+ `ME=0.33` `PC=0.45` `MC=0.33`
```
.MODEL BPN4 PNP BF=14.8 BR=1.5 RB=160 RC=120 CCS=2.126P TF=27.4N TR=220N
```

+ `CJE=0.10P` `CJC=0.90P` `lS=2.25E-15` `VA=83.55` `C2=84.37K` `lK=171.8U` `NE=2` `PE=0.45`
+ `ME=0.33` `PC=0.45` `MC=0.33`
```
.MODEL BPN5 PNP BF=80 BR=1.5 RB=1100 RC=170 TF=26.5N TR=9550N
+ CJE=0.10P CJC=2.40P lS=0.79E-15 VA=79.45 C2=1219 lK=80.55U NE=2 PE=0.6
+ ME=0.25 PC=0.6 MC=0.25
.MODEL BPN6 PNP BF=19 BR=1.0 RB=650 RC=100 TF=26.5N TR=2120N
```

+ `CJE=1.90P` `CJC=2.40P` `lS=0.63E-17` `VA=167.1` `C2=57.49K` `lK=80.55U` `NE=2` `PE=0.6`
+ `ME=0.25` `PC=0.6` `MC=0.25`

```
.ENDS UA741
*********************
```

- `UA741` `MACRO-MODEL` ```
*********************
.SUBCKT UA741MAC 3 2 6 7 4
```

- `NODES:` `IN+` `IN-` `OUT` `VCC` `VEE`
```
Q1 8 2 10 QMODl
Q2 9 3 11 QMOD2
RC1 7 8 4352
RC2 7 9 4352
RE1 1 10 2391. 9
RE2 1 11 2391. 9
RE 1 0 7.27MEG
CE 1 07.5P
lEE 1 4 27.512U
C1 8 9 4.5288P
RP 7 4 15.363K
GCM 0 12 1 0 1.1516N
GA 12 0 8 9 229.774U
R2 12 0 lOOK
C2 12 13 30P
GB 13 0 12 0 37.0978
R02 13 0 489.2
R01 13 6 76.8
Dl 13 14 DMODl

```

**Figure 7.28** _**(continued)**_


**236** 7 FUNCTIONAL AND HIERARCHICAL SIMULATION

```
      D2 14 13 DMODl
      *EC 0 14 6 0 1
      GC 0 14 6 0 5034.3
      RC 14 0 0.1986M
      D3 6 15 DMOD3
      D4 16 6 DMOD3
      VC 7 15 1.6042
      VE 16 4 3.1042
```

      ```
      .MODEL QMOD1 NPN IS=8E-16 BF=52.6726
      .MODEL QMOD2 NPN IS=8.0925E-16 BF=52.7962
      .MODEL DMOD1 D IS=3.8218E-32
      .MODEL DMOD3 D IS=8E-16
      .ENDS

```

**Figure 7.28** _(continued)_


**Figure 7.29** Voltage follower configuration for
slew-rate comparison.

```
      UA741 SLEW RATE
```

      ```
      * MACRO-MODEL
      Xl 1 3 3 4 5 UA741MAC
      * FULL MODEL
      X2 2 6 6 4 5 UA741
      VIN1 10 0 DC -.2765M PULSE -5 SOlON 10N 20U 100U AC 1
      VIN2 11 0 DC -.2834M PULSE -5 SOlON 10N 20U 100U AC 1
      RIN1 10 1 100
      RIN2 11 2 100
      VCC 4 0 15
      VEE 5 0 -15
```

       ```
      .TRAN .25U SOU
      .OPTIONS ACCT
      .END

```

**Figure 7.30** SPICE input for voltage-follower configuration for slew-rate comparison.


4


2


s `0`
,,0

```
  -2

  -4

```


MACRO-MODELS 237


10 `20` `30` `40`


Time, lIS



Figure 7.31 Slew-rate results for opamp models.


The SPICE input for the frequency response is modified, as shown in Figure 7.32,
so that the two opamps, Xl and X2, are in an open-loop configuration, the pulse is replaced by an AC source, and the frequency range is set from below the dominant pole
defined by the compensation capacitor to six orders of magnitude above that value. The
magnitudes ofthe two output signals are plotted in Figure 7.33. The two models track

```
UA741 FREQUENCY RESPONSE
```

** `MACRO-MODEL`
```
Xl 1 0 3 4 5 UA741MAC
```

 - `FULL MODEL`
```
X2 2 0 6 4 5 UA741
```

 ```
VIN1 1 0 DC -.2765M AC 1
VIN2 2 0 DC -.2834M AC 1
VCC 4 0 15
VEE 5 0 -15
```

 
 ```
 .TF V(3) VIN1
 .TF V(6) VIN2
 .AC DEC 10 .1 1G
```

. END


Figure 7.32 SPICE input for open-loop frequency response comparison.


**238** 7 FUNCTIONAL AND HIERARCHICAL SIMULATION

```
       100

        50
```

OJ
"0

"0<Ii
:J `0`
**'2** Ol
t1l
::2:
```
       -50

       -100

```

Frequency, Hz

Figure 7.33 Open-loop frequency response comparison.


each other very well up to 1 MHz, after which secondary poles and zeros come into
play.


The above characterization is useful for identifying the range of the macro-model's
validity for different applications. The reductions in circuit complexity and simulation
time are important advantages for macro-models. Separate runs for individual opamps
show that the complete circuit has 79 nodes and 38 components, versus 16 nodes and
26 elements for the macro-model. In addition, the complete circuit has 26 BITs, versus
only 2 for the macro-model. This ratio is very important, because in SPICE the transistor
is the most time-consuming component to evaluate.
The accounting information option of SPICE, ACCT (see Sec. 9.5.1), offers detailed
information on the two circuits. This option also shows that the run time for the openloop DC operating point is 1.17 sand 21 iterations for the complete _,uA_ 741 circuit
and 0.25 sand 32 iterations for the macro-model. The gains in analysis time become
significant for the transient analysis, where the complete circuit requires 56 s versus
only 5 s for the macro-model, a performance gain of 11. These results were obtained
from SPICE2 running on a SUN 4/110 workstation. The same analysis performed by
PSpice 01). an IBM PS/2 Model 80 equipped with a 16 MHz 386 processor requires 209
s for the complete circuit versus 14 s for the macro-model. The performance gain is
achieved in the analysis of the macro-model circuit partly because fewer time points
and iterations are required by this solution; see Chap. 9 for more details. The simpler
circuit takes only half the number of iterations used by the full opamp circuit.


SUMMARY **239**


An important conclusion to the modeling practices described in this chapter is that
SPICE can accommodate different levels of accuracy in the representations of circuits.
It is up to the user to decide which behavior of a circuit block is important and needs to
be modeled for the correct operation of an entire circuit. For the opamp macro-model
varying degrees of accuracy can be implemented, from the ideal model in Figure 7.6 to
the complex macro-model of Figure 7.27.
With the reduction in complexity, the savings in run time are of major significance.
Whereas the detailed macro-model can save up to an order of magnitude in run time, a
nearly ideal model of an opamp can run up to two orders of magnitude faster.


**7.6** **SUMMARY**


This chapter has introduced several concepts pertaining to modeling and simulating
electric circuits and systems, which are applicable as well to nonelectrical physical systems. This approach to modeling and simulation is known as _high-level,_ or _behavioral,_
in contrast to the _structural_ representation common to circuit schematics.
The first step in defining circuit representational levels is to identify a hierarchy
when describing a more complex circuit. The SPICE language provides constructs for
identifying subcircuits and instantiating them in the circuit description.
The _subcircuit definition,_ a global statement, and the _subcircuit instance_ are defined
by the following syntax:

**• SUBCKT** _SUBname nodel <node2 ..._        circuit elements


        - ENDS

_Xname xnodel_ <xnode2 ...       - _SUBname_


These statements can be nested to create several levels in a hierarchical circuit description, as exemplified by several digital building blocks.
High-level circuit representations have been presented in three categories depending on the level of accuracy. Ideal models describe the single most relevant function of
a device and can be used for computational efficiency in circuits where the ideal blocks
are not critical for the circuit performance. Ideal opamps can be used in active filters,
and ideal logic gates save analysis time in mixed analog/digital circuits.
Functional models implement complex analytical current-voltage expressions
with one or more nonlinear controlled sources. The arbitrary controlled source introduced in SPICE3 and the equivalent or more powerful capabilities in PSpice, SpicePLUSlProfile, HSPICE (Meta-Software Inc. 1991) and Saber (Analogy Inc.,1991)
make it possible to model circuit blocks such as limiters, voltage-controlled oscillators,
and phase-locked loops with just a few components. Devices described by complex
equations, which need not be electrical, can also be simulated using arbitrary controlled
sources. A number of useful functional blocks can be defined using the polynomial controlled sources available in all SPICE simulators.
Macro-models can achieve the accuracy of a detailed circuit with important savings
in analysis time by combining structural elements, such as transistors and capacitors,


**240** 7 FUNCTIONAL AND HIERARCHICAL SIMULATION


with functional blocks implemented with controlled sources. Well-designed macromodels can be simulated up to an order of magnitude faster than the detailed model
with little if any loss in accuracy.
Both analog and digital circuit examples have been presented in this chapter to
highlight the diverse approaches to high-level modeling.
A cautionary note at the conclusion of this chapter regarding the accuracy of the
results using high-level representations: the analysis is only as accurate as the models
used! Erroneous operation as well as analysis difficulties can result from using idealized
models, as shown in one ofthe examples, as well as in Secs. 10.2.2, 10.3, and lOA.


**REFERENCES**


Boyle, G. R., B. M. Cohn, D. O. Pederson, and 1.E. Solomon. 1974. Macromodeling of integrated
circuit operational amplifiers. _IEEE Journal of Solid-State Circuits_ (December).
Dorf, R. C. 1989. _Introduction to Electric Circuits._ New York: John Wiley & Sons.
Epler, B. 1987. SPICE2 application notes for dependent sources. _IEEE Circuits and Devices_
_Magazine_ 3 (September).
Gray, P. R., and R. G. Meyer. 1993. _Analysis and Design of Analog Integrated Circuits,_ 3d ed.
New York: John Wiley & Sons.
Hodges, D. A., and H. G. Jackson. 1983. _Analysis and Design of Digital Integrated Circuits._
New York: McGraw-Hill.
Mano, M. M. 1976. _Computer System Architecture._ Englewood Cliffs, NJ: Prentice Hall.
Mateescu, A. 1991. Personal communication.
Meta-Software Inc. 1991. _HSPICE Users Guide._ Campbell, CA: Author.
Microsim Corporation. 1992. _PSpice, Circuit Analysis Users Guide, Version 5.0._ Irvine, CA:
Author.
Oldham, W. G., and Schwartz. 1987. _Introduction to Electronics._ New York: McGraw-Hill.
Paul, C. R. 1989. _Analysis of Linear Circuits._ New York: McGraw-Hill.
_Saber Users Guide._ Release 3.0. Analogy Inc. 1990. Beaverton, OR: Author. Sedra, A. S., and
K. C. Smith. 1990. _Microelectronic Circuits._ Philadelphia: W. B. Saunders.
Sitkowski, M. 1990. Simulation and modeling-The macro-modeling of logic functions for the
SPICE simulator. _IEEE Circuits and Devices Magazine_ 6 (September).
Valid Logic Systems. 1991. _Analog Workbench Reference._ Vol. 2. San Jose, CA: Author.
Vladimirescu, A. 1982. LSI circuit simulation on Vector computers. Univ. of California, Berkeley, ERL Memo UCBIERL M82175 (October).
Vladimirescu, A., K. Zhang, A. R. Newton, D. O. Pederson, and A. L. Sangiovanni- Vincentelli.
_1981. SPICE version_ 2G _User's Guide._ Dept. of Electrical Engineering and Computer Science, Univ. of California, Berkeley (August).


_**Eight**_


_**DISTORTION**_ _**ANALYSIS**_


**8.1** **DISTORTION** **IN SEMICONDUCTOR** **CIRCUITS**


This chapter describes in detail the evaluation of distortion in electronic circuits with
SPICE. Emphasis is placed on the small-signal distortion analysis in SPICE2, which
is a powerful tool for designing electronic circuits and ICs. The main features of the
small-signal distortion analysis were presented in Sec. 5.4.
The distortion analysis presented in Chap. 5 was limited to frequency-independent
circuits. A more rigorous analysis of distortion components for a single-transistor amplifier and a mixer circuit is carried out in this chapter, in Sec. 8.2. SPICE2 provides
more distortion information about a circuit than shown in Chap. 5. The total distortion
measures are broken down in the SPICE2 output into contributions for each nonlinearity
of each diode or BJT in the circuit as exemplified in Sec. 8.2.2.
The signal amplitude is often larger than the limit for small signals. Therefore, it
is important to understand how to use large-signal time-domain analysis to derive the
same distortion measures computed by the small-signal analysis. Sec. 8.3 describes the
application of Fourier analysis for verifying the results of the one-transistor amplifier
and for deriving the intermodulation component for a mixer.


**8.2** **SMALL-SIGNAL DISTORTION** **ANALYSIS**


In Chap. 5 the distortion measures were derived for a _nearly linear frequency-indepen-_
_dent circuit._ In this section the effect of frequency-dependent circuit elements is considered in the derivation of the distortion measures.


**241**


**242** 8 DISTORTION ANALYSIS


The SPICE2 capability of reporting individual distortion sources is explained and
the additional feature of the AC analysis that provides a frequency sweep of the distortion coefficients is exemplified.


**8.2.1** **High-Frequency Distortion**


In the absence of frequency-dependent elements, a power series is used to express the
high-order terms of the signal at the output of a nonlinear circuit. A more general series
expansion of a signal is derived below for computing the distortion terms. The approach
consists of expressing the transfer function of a circuit containing both small nonlinearities and frequency-dependent elements (Meyer 1979; Pederson and Mayaram 1990).
In Figure 8.1 two frequency-dependent linear circuit blocks, both filters, are added
to the nonlinear gain block _A._ The two linear filters have transfer functions _F(j w)_ and
_J(jw),_ respectively.
The higher-order terms in the output signal, _So,_ are obtained by taking into account
all three transfer functions. The output, _Soa,_ of the nonlinear gain block, _A,_ is a power
series of the input to _A, Sia:_


(8.1)


_Sia_ is the result of passing the input signal, Si,



Si = SI _cosw1t_ + _S2cosw2t_



(8.2)



through _F(jw)_ to get


.where _IF(j_ w)1 is the magnitude and _cPw_ is the phase of the transfer function. A new
operator is introduced, 0, to simplify the above expression of _Sia_ to



_Sia_ = _F(jW)oSi_



(8.4)



_F(jOJ)_



_J(_ _jOJ)_



**Figure 8.1** Nonlinear gain block with input and output filters.


SMALL-SIGNAL DISTORTION ANALYSIS **243**


The meaning of applying _F_ through the operator 0 on the input signal _Si_ is to multiply
the amplitude _Sn_ of each frequency component in _Si_ by _IF(jwn)1_ and shift its phase
by _cf>wn._
The signal at the output of the nonlinear gain block is a power series of the input
signal; limited to three terms and up to three signal frequencies, _Wa, Wb,_ and _We,_ the
output becomes


_Saa_ = _Saa]_ + _Saa2_ + _Saa3_

_= a]F(jwa)_ 0 _Si_ + _a2F(jwa)F(jWb)_ 0 Sf + _a3F(jWa)F(jWb)F(jWe)_ 0 Sf (8.5)


The detailed expressions of _Saa], Saa2,_ and _Saa3,_ which are listed below for an input signal with two frequencies, _W]_ and _W2,_ are useful for deriving the distortion components
in the following section:


_Saa] =a][IF(jw])IS]_ _cosa]_ + _IF(jW2)IS2_ _cosa2]_


_Saa2_ = _~{[IF(jw])12Sr(COS2a]_ + 1) + _IF(jW2)12Si(cos2a2_ + 1)]


_+_ _2IF(jwdIIF(jW2)IS]S2[_ _cos(a]_ + _(2)_ + _cos(a]_ _- (2)]}_
_a_ _(8.6)_
_Saa3_ = _;{[IF(jw])13Sr(COS3a]_ + 3cosad + _IF(jW2)13Si(cos3a2_ + _3cos(2)]_


_+_ _3!F(jwdIS]IF(jW2)12Si[2cosa]_ + _COS(2a2 - ad_ + _COS(2a2_ + _a])]_
_+_ _3IF(jw])!2SrIF(jW2)IS2[2cosa2_ + _cos(2a]_ _- (2)_ + _cos(2a]_ + _(2)]}_


In the above equations _a]_ and _a2_ represent


_a]_ = _WIt_ + _cf>w]_

(8.7)
_a2_ = _W2t_ + _cf>w2_


The signal at the output, _So,_ is obtained by including the contribution of the second
frequency-dependent block, _J(jw):_

_So_ = _a]F(jwa)J(jwa)_ 0 _Si_ + _a2F(jwa)F(jWb)J(jWa,_ _jWb)_ 0 Sf
_+_ _a3F(jWa)F(jWb)F(jwe)J(jwa,_ _jWb, jwe)_ 0 Sf (8.8)


The argument of _J_ in Eq. 8.8 is the frequency of a given spectral component which in
tum is a linear combination of the input frequencies _Wa, Wb, We._ The above result is generally valid for circuits with memoryless nonlinearities and linear frequency-dependent
elements. The above power series expansion of the output signal is also known as a
Volterra series (Narayanan 1967).


**244** 8 DISTORTION ANALYSIS


The different distortion measures introduced in Chap. 5 can be derived as ratios of
the second- or third-order terms in Eqs. 8.8 and by an appropriate assignment of _::tWl_
and _::tW2_ to _Wa, Wb,_ and _We._
**In** conclusion, the distortion terms of a signal at the output of a frequency-dependent
circuit with small nonlinearities can be found by writing the overall transfer function
and replacing the nonlinear signals by series expansions. Transfer functions of first,
second, and third order can be isolated to compute the distortions of corresponding
order. The following section exemplifies the use of this approach.


**8.2.2** **Distortion in a One-Transistor Amplifier**


Consider the one-transistor amplifier of Figure 5.8 with a series base resistance, **RB,**
of 100 n and junction capacitances **CJE** and **CJC** added to the • **MODEL** statement, as
listed in Figure 8.2. The DC bias solution and the small-signal parameters of _Ql_ are
recomputed and the results are in Figure 8.2. The linear equivalent of the one-transistor


```
******* 04/07/89 ******** SPICE 2G.6

ONE-TRANSISTOR CIRCUIT (Figure 5.8)

```

```
3/15/83******** 16:14:42 *****

```

```
***** INPUT LISTING TEMPERATURE = 27.000 DEG C

*************************************************************************
```

```
Q1 2 1 0 QMOD
```

RL 2 3 1K
```
VCC 3 0 5
```

```
VEE 4 0 793.4M
VI 1 4 AC 1
```

```
.MODEL QMOD NPN RB=100
```
+ `CJE=lP`
+ `CJC=2P`
```
.OP
.AC LIN 1 1MEG 1MEG
.DISTO RL 1
```

```
.PRINT DISTO HD2 HD3 SIM2 DIM2 DIM3
.WIDTH OUT=80
.OPTION NOPAGE
.END

```

**Figure 8.2** One-transistor amplifier input and DC bias point.


```
**** BIT MODEL PARAMETERS
        QMOD
TYPE NPN
IS 1.00D-16
BF 100.000
NF 1.000
BR 1.000
NR 1.000
RB 100.000
CJE 1.00D-12
CJC 2.00D-12

**** SMALL SIGNAL BIAS SOLUTION

NODE VOLTAGE NODE VOLTAGE

  1) 0.7934 ( 2) 3.0522

   VOLTAGE SOURCE CURRENTS

   NAME CURRENT
   VCC -1.948D-03
   VBE -1.948D-05
   VI -1.948D-05

```


`TEMPERATURE` = `27.000` `DEG C`


`TEMPERATURE` = `27.000` `DEG C`

```
NODE VOLTAGE

( 3) 5.0000

```

```
   TOTAL POWER DISSIPATION 9.75D-03 WATTS

```

`****` `OPERATING` `POINT` `INFORMATION` `TEMPERATURE` = `27.000` `DEG C`


```
****

```

```
BIPOLAR JUNCTION TRANSISTORS
    Q1
   QMOD
   1.95E-05
   1.95E-03
     0.793
    -2.259
     3.052
    100.000
   7.53E-02
   1.33E+03
   1.00E+02
   1.00E+12
   1.72E-12
   1.26E-12
   O.OOE+OO
   O.OOE+OO
    100.000
   4.02E+09

```

```
MODEL
```

IE
```
IC
VBE
VBC
VCE
BETADC

```


8M
```
RPI
```

RX
```
RO
CPI

```


CMU
```
CBX
CCS
BETAAC
```

FT



**Figure 8.2** _**(continued)**_



**245**


**246** 8 DISTORTION ANALYSIS


`r---------r~---------lQ` 1



_:_ _R_ _[B]_ B' e~ c I~ _i_ _o_

I
I +
I



+



_n_ _o_
_r_ _en_ _IVb'_ _r_ _!_



I I
I                  -                  -                  - I
I I
I
l- ~


**Figure** 8.3 Small-signal equivalent of the one-transistor amplifier.


amplifier is shown in Figure 8.3. More detail than just the total distortion figures is
obtained from SPICE2 when a summary interval, equal to 1in the deck shown in Figure
8.2, is specified in the. **DISTO** statement; see Sec. 5.4. The distortion contribution in the
load resistor is computed for every element in Figure 8.3 associated with a nonlinearity
of the transistor.
The distortion summary computed by SPICE2 at 1 MHz is listed in Figure 8.4.
Note that the addition of the base resistance and the two charge nonlinearities do not
significantly affect the absolute values of the second- and third-order distortion terms,
HD2 and HD3, and the second-order intermodulation terms, SIM2 and DIM2, which are
listed under the AC ANALYS I S header, as compared to the results obtained at 1kHz in
Sec. 5.4 (Figure 5.9).
The DISTORTION ANALYSIS summary report lists five groups of BJT
DISTORTION COMPONENTS. Each group starts with a header identifying the type
of distortion, such as 2ND HARMONIC DISTORTION, and the fundamental frequency, FREQ1, for one input signal or FREQl and FREQ2 for two input signals;
the DISTORT I ON FREQUENCY and MAG and PHS of the transfer functions for the input
signals are listed on the following line.
The BJT DISTORTION COMPONENTS are due to the nonlinear voltage dependencies of _Ie, IB, QBE,_ and _QBe,_ as defined in Eqs. 3.10 through 3.14. The total currents,
_ie_ and _iB,_ can be expressed as Taylor series around the DC operating values, _Ie_ and _IB,_
in the same manner as derived in Eqs. 5.19 through 5.21 for an approximation of _ie._ The
elements _g1T' gJL' gm, go, C1T,_ and _CJL_ in the linear equivalent in Figure 8.3 represent the
partial derivatives of _IB, Ie, QBE,_ and _QBe_ in the first-order terms of the corresponding
Taylor expansions.
The higher-order terms of this series constitute distortion sources, as described in
Chap. 5. The contribution of each second or third derivative in the Taylor series to the
output distortion is listed in the corresponding column of the SPICE2 printout.
Note that the current equations for _Ie_ and _IB_ in distortion analysis use not the
Gummel-Poon formulation given in Appendix A, but the more simple Ebers-Moll


******** `DISTORTION` `ANALYSIS` `TEMPERATURE` `27.000` `DEG` `C`


`2ND` `HARMONIC` `DISTORTION` `FREQI` = `1.00D+06` `HZ`

```
   DISTORTION FREQUENCY 2.00D+06 HZ MAG 6.989D+Ol PHS 176.26

BJT DISTORTION COMPONENTS
NAME GM GPI GO GMU GM02
Ql MAG 1.800D-Ol 1.261D-02 1.356D-08 1.000D-20 3.600D-I0
      PHS 166.19 -14.02 -14.73 0.00 -14.27 0.00 0.00
        CB CBR CJE CJC TOTAL
      MAG 1.000D-20 1.000D-20 4.473D-06 5.016D-03 1.674D-Ol
      PHS 75.98 75.10 164.49

   HD2 MAGNITUDE 1. 674D-Ol PHASE 164.49 -15.53 DB

```

`3RD` `HARMONIC` `DISTORTION` `FREQI` = `1.00D+06` `HZ`

```
   DISTORTION FREQUENCY 3.00D+06 HZ MAG 6.989D+Ol PHS 176.26

```

```
BJT DISTORTION
NAME
Ql MAG

```

```
  GO
1.267D-07
 -22.30
  CJE
3.678D-07
 -55.64

```

```
 GM02
5.598D-ll
 -38.68
 GM203
6.468D-ll
 -21.10

```

```
 GM023 TOTAL
4.871D-09 1.842D-02
 -21.56 120.61

```

```
  GMU
1.000D-20
  0.00
  CJC
4.019D-03
 62.75

```

```
MAG
PHS

MAG
PHS

```

```
  COMPONENTS
  GM GPI
1.789D-02 1.253D-03
 132.40 -47.92
  CB CBR
1.000D-20 1.000D-20
  0.00 0.00

```

```
HD3 MAGNITUDE 1.842D-02 PHASE 120.61 -34.69 DB

```

```
  2ND ORDER INTERMODULATION DIFFERENCE COMPONENT
```

`FREQ2` = `9.00D+05` `HZ`
```
  DISTORTION FREQUENCY 1.00D+05 HZ
MAG 6.992D+Ol PHS 176.63

```

```
BJT DISTORTION
NAME
Ql MAG

```

```
     COMPONENTS
     GM GPI
MAG 3.632D-Ol 2.544D-02
PHS 179.31 -0.70
     CB CBR
MAG 1.000D-20 1.000D-20
PHS 0.00 0.00

```

```
  GO
2.735D-08
 -0.74
  CJE
4.512D-07
 89.30

```

```
  GMU
1.000D-20
  0.00
  CJC
5.061D-04
 89.25

```


`FREQI` = `1.00D+06` `HZ`

```
 MAG 6.989D+Ol PHS 176.26

 GM02
7.264D-I0
```

-0.71
```
 TOTAL
3.377D-Ol
 179.22

```

```
MAG
PHS

```

```
   IM2D MAGNITUDE 3.377D-Ol PHASE 179.22 -9.43 DB

```

`2ND` `ORDER` `INTERMODULATION` `SUM` `COMPONENT` `FREQI` = `1.00D+06` `HZ`
`FREQ2` = `9.00D+05` `HZ`

```
   DISTORTION FREQUENCY 1.90D+06 HZ MAG 6.989D+Ol PHS 176.26
 MAG 6.992D+Ol PHS 176.63

BJT DISTORTION COMPONENTS

NAME GM GPI GO GMU GM02
Ql MAG 3.604D-Ol 2.524D-02 2.714D-08 1.000D-20 7.209D-I0
      PHS 166.88 -13.32 -14.00 0.00 -13.56
          CB CBR CJE CJC TOTAL
     MAG 1.000D-20 1.000D-20 8.509D-06 9.543D-03 3.352D-Ol
      PHS 0.00 0.00 76.68 75.84 165.26

   IM2S MAGNITUDE 3.352D-Ol PHASE 165.26 -9.50 DB
```

_**(continued**_ _**on next page)**_


**Figure** **8.4** **SPICE2.** **DISTO summary for the one-transistor** **amplifier.**


**247**


**248** **8** **DISTORTION ANALYSIS**


`3RD ORDER INTERMODULATION DIFFERENCE COMPONENT` `FREQ1` = `1.000+06` `HZ`
```
     FREQ2 = 9.000+05 HZ

     DISTORTION FREQUENCY 1.100+06 HZ MAG 6.9890+01 PHS 176.26
   MAG 6.9920+01 PHS 176.63

  BJT DISTORTION COMPONENTS

  NAME GM GPI GO GMU GM02
  Q1 MAG 5.164D-02 3.616D-03 3.867D-07 1.000D-20 1.685D-10
       PHS 162.25 -17.86 -8.22 0.00 -14.24
           CB CBR CJE CJC GM203 GM023 TOTAL
       MAG 1.000D-20 1.000D-20 2.388D-07 4.515D-03 1.973D-10 1.486D-08 4.883D-02
       PHS 0.00 0.00 -66.39 79.97 -7.78 -7.95 157.01

      1M3 MAGNITUDE 4.883D-02 PHASE 157.01 -26.23 DB

     APPROXIMATE CROSS MODULATION COMPONENTS

```

```
  MAGNITUDE 1.844D-01
  MAGNITUDE 6.4400-02

AC ANALYSIS

    HD2 H03

```

```
             -14.68 DB
             -23.82 DB

```

`TEMPERATURE` = `27.000 DEG C`

```
SIM2 DIM2 DIM3

```


********


```
CMA
CMP

FREQ

```

```
1.000E+06 1.674E-01 1.842E-02 3.352E-01 3.377E-01 4.883E-02

```

**Figure 8.4** _**(continued)**_



**formulation including the Early effect from Eqs. 3.10 through 3.12. For completeness**
**the equations of** _**Ic**_ **and** _**IB**_ **used in SPICE2 for computing distortion are included here:**



_**Ic**_ **=** _**(lcc**_ _**-**_ _**ICE)**_ **(1 -** _**IBC**_
:1~)


_**(lcc**_ _**-**_ _**ICE)**_ _**IBC**_


_**= Is**_ _(ev8dVth_ _-_ _eV8c1vth_ **)(1 -** _**%R**_ _(eV8c1Vth -_ 1) **(8.9)**
:1~)


_**IB**_ **=** _**IBE**_ **+** _**IBC**_


**where** _**Icc,**_ _**ICE, IBC,**_ **and** _**IBE**_ **have the same meanings as in Eqs. 3.10 and 3.11.**
**The current components for low- and high-level injection have been neglected in**
**order to simplify the derivation of higher-order terms and focus the results on the main**
**nonlinear distortion sources. Also, because of model simplicity at the time of the im-**
**plementation, the emission coefficients** _**NF**_ **and** _**NR**_ **are set equal to 1.**
**The base and collector currents are functions of two variables,** _**VBE**_ **and** _**VBC.**_ **The**
**total currents and voltages, such as** _**VBE,**_ **are made up of a DC component, such as** _**VBE,**_
**and an incremental component, such as** _Vbe:_


**(8.10)**


Similarly,



SMALL-SIGNAL DISTORTION ANALYSIS **249**


(8.11)



where _IB_ is defined by Eqs. 8.9. The incremental component _ib_ has the following Taylor
series expansion:


_ib_ = _ig7T_ + _igIJ-_ = _g7TVbe_ + _g7T2v~e_ + _g7T3vbe_ + ... + _gIJ-Vbe_

_+_ _gIJ-2_ _[V]_ _be_ 2 + _gIJ-3_ _[V]_ _be_ 3 + ... (8.12)


where


_alB_ 1 _dlcc_
_g7T =_ --_aVBE_ _{3FdVBE_


_alB_ I _dIcE_
_gIJ-_ --_avBC_ _{3RdVBC_
(8.13)
I _a_ _[2]_ _lB_ 1 _d_ _[2]_ _lBC_

_g7T2_
_2av~E_ 2 _dV~E_

1 _a_ _[2]_ _lB_ 1 _d_ _[2]_ _lBE_
_gIJ-2 =_ _2av~c_ _2dV~c_


and so on. The values listed under GPI and GMUin the HD2 group represent the contributions to the total distortion due to the second-order terms _g7T2_ and _gIJ-2_ in _ib._ Note that
a value of 10- [20] represents zero distortion contribution.
**In** the same way distortion contributions can be associated with the Taylor coefficients of the expansion of ic:


_._ _alc_ _alc_ 1 _(a_ _[2]_ _lc_ 2 _a_ _[2]_ _lc_ _a_ _[2]_ _lc_ 2)
Ie = _-V_ _Vbe_ + _-av_ _Vbe_ + -2 _--2-vbe_ + 2 _av_ _av_ _VbeVbe_ + _--2-vbe_
_a BE_ _BC_ _aVBE_ _BE_ _BC_ _aVBC_


(8.14)


where iP) and i~2)represent the first- and second-order terms, respectively, of the ic
series. Note that _Vbe_ and _Vbe_ are the independent variables in the above equation; the
input and output voltages of the transistor equivalent network shown in Figure 8.3,
however, are _Vbe_ and _Vee,_ respectively. A change of variable


(8.15)


**250** 8 DISTORTION ANALYSIS


leads to the following expression for the first- and second-order components of _ic:_


(8.16)


where


_alcT_ _alcT_ _alc_
--+-- _---go_
_aVBE_ _aVBC_ _aVBE_

_alcT_ _alc_
--- = _----g_
_aVBC_ _aVBC_ _f.L_


GM,GO, and GM02 in the SPICE2 output represent the second-order distortions


(8.17)


respectively.
Next consider the distortion due to the charge components, The nonlinear charge
formulations are described by Eqs. 3.2 and 3.4. The current through a nonlinear capacitance can be expressed in a power series:


(8.18)


Here _C(V)_ has two possible formulations,


(8.19)


SMALL-SIGNAL DISTORTION ANALYSIS **251**


for the diffusion capacitances defined by Eq. 3.3 and


Co               - _ClO_
(8.20)
J                       - [1 - _(Vl_ + _Vj)/ cPl]Ml_


for the junction capacitances, respectively. _ID_ represents the diffusion current, _Icc_ or
_ICE,_ and _Vl_ is the junction voltage. In the small-signal equivalent _C1T_ and _Cf.L_ include
both types of capacitances; the printout of the distortion components separates them,
however. CB and CBR represent the contributions due to _CDE_ and _CDC,_ defined by
Eqs.3.l8:


_a_ _[2]_ _QDE_
_Cde2 =_ = _TF._ _gm2_
_aV~E_
(8.21)
_a_ _[2]_ _QDc_
_Cdc2 =_ = _TR._ _ga2_
_av~c_


CJE and CJC represent the distortion contributions due to the junction capacitances,
defined by Eqs. 3.14:



_Cje2 =_ _[dClE]_



_dVBE_



(8.22)
_dClc_



_Cjc2 =_
_dVBc_



respectively.
It is instructive to derive by hand the different distortion components for the
one-transistor amplifier in order to understand the meaning of the SPICE2 distortion
summary report. The approach used in Sec. 8.2.1 to find the transfer function of the
frequency-dependent and nonlinear blocks of Figure 8.1 is used in this derivation. A
source of small distortion can be associated with each nonlinear term (Chisholm and
Nagel 1973) in Eqs. 8.13 and 8.17, namely, _IBE, IBc, Icc,_ _ICE_ and the different charge
terms in Eqs. 8.21 and 8.22. The distortion in the load resistor, _RL,_ due to each nonlinearity is evaluated by considering only one distortion source at a time. The total
distortion at the output of the linear circuit is obtained by superposition of all individual
contributions. Note that the circuit distortion is additive in a vector sense; that is, two
distortion generators of equal magnitude and opposing phase cancel each other.
Start out by writing the transfer function for the small-signal circuit in Figure 8.3.
Kirchhoff's current law (KCL) is applied at nodes B' and C to yield



_Vi -_ _Vb'_ _._ _._ 0
_RB_ + _1f.L_ _-_ _11T =_


_i_ _a_ _-_ _i_ _gm_ _-_ _if.L_ = 0



(8.23)


**252** 8 DISTORTION ANALYSIS


These are general equations, which must be satisfied for the terms of different orders in
the Taylor series expansion of the currents and voltages. Similarly to _Si_ in Eq. 8.2 the
input signal, _Vi,_ consists of two sinusoids of frequencies WI and _W2_ and amplitudes _Vii_
and _V_ _i2:_


(8.24)


The derivation is simplified by splitting the circuit in Figure 8.3 into two disconnected
subnetworks, shown in Figure 8.5. The input equivalent of _gIL'_ _CIL,_ is multiplied by
the voltage gain, _avl,_ from the output to the internal base; gIL is very small and can be
neglected.
In the following derivation second-order distortion figures are computed first. Each
distortion source contribution derived below has a one-to-one correspondence with a
distortion component in the SPICE2 summary.
Consider the nonlinearity due to _IBc,_ represented by _ig1T_ in Eq. 8.12, the distortion contribution of which appears in the GPI column in the printout. The current _i1T,_ in
Eqs. 8.23, has a nonlinear component, _ig1T_ (Eqs. 8.12), and a linear component, _iC1T:_


(8.25)


Because _ig1T_ is nonlinear _Vb'_ can be expressed as a power series of the input signal, _Vi:_


(8.26)


where al represents the transfer function from the input to the internal base, B'. The
coefficients of the above series are derived by satisfying the KCL (Eqs. 8.23) for first-,
second-, and third-order terms.
Substitution of the first-order terms in Eqs. 8.23 yields


from which the following expression for al can be obtained:


(8.27)


It is calculated by substituting the following circuit component values:


_R_ _B_ = 1000.

_g1T_ = 7.5 X 10- [4] mho

_C_ _1T_ = l.72pF


SMALL-SIGNAL DISTORTION ANALYSIS **253**


**`r---------------------------,`** _Q_ _1_
I I .
B I _R_ _[B]_ B' C I~

I
I +
I +
I
I
I
I
I
I
I
`L` I `~` I


**Figure 8.5** Small-signal equivalent using Miller's theorem.


_CJ.L_ = 1.26 pF

_avi_ = _gmRL_ = 0.075 X 10 [3] = 75


Next, the first of Eqs. 8.23 is written for the second-order terms of the currents and
voltages:


Note that _Vi_ has no terms of second or higher order; _a2_ can be expressed from the above
equation:


_g'1T2RBal(jwI)al_ _(jW2)_
(8.28)
1 + _g'1TRB_ + _j(WI_ + _(2)RB(C'1T_ + _avi CJ.L)_


where _a2_ is a function of WI and _W2,_ and different combinations of the two must be used
depending on which distortion measure is evaluated.
The values of _a2_ represent the second-order distortion at the internal base due to
_g'1T'_ that is, the _IBe_ nonlinearity. The contribution at the output, in resistor _RL,_ can be
obtained by multiplying the second-order component in the _vb'_ series by the gain:


(8.29)


The expressions of _HD2, SIM2,_ and _DIM2,_ due to _g'1T'_ result from the second-order
terms in Eqs. 8.6 and 8.8 evaluated for _a2( jWI,_ _jwd,_ _a2( jWI,_ _j(2),_ anda2( _jWI,_ _- j(2),_
respectively.


1 _Vag_ (2) _'1T_
_HD2g'1T_ = -2 _-2-Van_ (8.30)
_Va_


**254** 8 DISTORTION ANALYSIS


where _Vo_ is the gain referenced to the input for an input signal of amplitude IV, and _Von_
is the normalized output voltage corresponding to 1 mW power in _RL. a2(jwl,_ _jWl)_ is


. . 0.0145 . 10 [2] (0.93 - _jO.053)2_
_a2(jwl,jwl)_ = - 1.075 + _j6.28_ _._ (2.106).10 [2] (1.72 + 75.3 .1.26)10- [12]

= -1.24(0.92               - _jO.212)_


where


1 _g-rr._ _/_ 2
_g-rr2_ = -- = 0.0145 A V
_2 V_ _th_


Substitution in Eq. 8.30 yields the amplitude and phase of _HD2g_ _-rr:_


_IHD2_ _g-rr1_ = 0.0126


These values are in excellent agreement with the values computed by SPICE2 in the

GPI column ofthe 2ND HARMONIC DISTORTION category.
The second-order intermodu1ation components are calculated similarly; for _SIM2_
evaluate


. . 1.45(0.93 - _jO.053)2_
_a2(jwl,_ _j_ _[W]_ _2)_ = - 1.075 + _j6.28_ _._ (1.9 . 106) . 10 [2 ] . (1.72 + 75.3 . 1.26)10- [12]
_= a2(jwbjwd_


where _WI_ + _W2_ = _1.9wl,_ corresponding to 1.9MHz. The distortion signal at the output,
_vog-rr,_ is calculated for _a2(jwl,_ _jW2),_ and its value is substituted into the definition of
_SIM2_ ofEq. 5.16:



1 _vog-rr jWl,_ (2) ( . _jW2_ ')
_SIM2g-rr_ = 2 2 _Von_
_Vo_


The magnitude and phase of _SIM2_ are


_ISIM2g-rr1_ = 0.0256


_LSIM2g-rr_ = -13°



(8.31)


SMALL-SIGNAL DISTORTION ANALYSIS **255**


The difference intermodulation component is derived similarly by substituting


1.45(0.93 - _jO.053)(0.93_ + _jO.047)_
1.075 + _j6.28'_ (0.1.10 [6] ). IO [z] (1.72 + 75.3, 1.26)1O- [1Z]


-1.25(0.93            - _jO.012)_


in Eq. 8.29, where _WI_ _-_ Wz is 27Tx 0.1 MHz. The magnitude and phase of _DIM2_ are


_IDIM2g1T1_ = 0.0255

_LDIM2g1T_ = -0.7°


Note that the _1M2_ components agree with the SPICE2 results and the magnitudes are
equal to 2. _HD2_ as predicted in the frequency-independent case in Example 5.7.
The harmonic distortion due to the nonlinearity of _Ie_ is summarized in the SPICE2
output in the columns GM, GO, and GM02. The equivalent distortion sources generating
these three contributions to the second harmonic are defined in Eqs. 8.17, based on the
Taylor series expansion of _ie_ around the operating point/c, Eq. 8.14.
The following equations are used to derive _HD2_ _gm,_ the second harmonic component due to the _gm_ distortion source. _ic_ is expressed as a power series of _Vb':_


(8.32)


and _Va_ is a power series of _Vb':_


(8.33)


with


The first- and second-order terms of _i_ _c_ and _Va_ are used in the KCL, the second of Eqs.
8.23, to find _b_ _1_ and _bz:_



_gmRL_
1 + _jWICfoLRL_


_gmZRL_
1 + _j(WI_ + _wz)CfoLRL_



(8.34)


**256** 8 DISTORTION ANALYSIS


where _gm2_ is computed according to the Taylor series coefficients, Eqs. 8.17:


1 _gm_ _/_ 2
_gm2_ = 2 _V_
_th_ [=] [ 1.45 A V]


_h2_ represents the contribution of _gm_ to the second harmonic in the output voltage:


(2) _ _h_ _2_
_Vogm_ _-_ _2Vb'_


The distortion at the output is computed according to Eq. 8.29:



_HD2_ _gm_



1 _vogm_ (2)
_-2-2-Von_ (8.35)
_V_ _o_



resulting in the following values:


_IHD2_ _gm_ _i_ = 0.181


_LHD2_ _gm_ = 1660


At first glance the distortion due to _go_ should be zero since no value has been specified for the Early voltage, _VAF._ The second harmonic contribution is found in the GO
column of the SPICE2 output and is equal to 1.36 X 10- [8] . This result can be explained
by the conductance _GMIN_ added in parallel to each junction (see Sec. 10.2.1), equal
by default to 10- [12] mho. The resulting value can be verified replacing the second-order
terms in the KCL (Eq. 8.23) at the output node and using only the _go_ terms of the _ic_
series:


(8.36)


A new value is obtained for _h_ _2,_ which now represents the distortion at the output due
to _go:_


(8.37)


where the _go_ term has been neglected and


SMALL-SIGNAL DISTORTION ANALYSIS **257**


The second harmonic distortion coefficient, _HD2go,_ follows:


_IHD2go_ _i_ = 1.4 x 10- [8]


The distortion contribution due to the second-order cross-term _gmo2_ in the _ic_ series,
Eq. 8.16, is nonzero'because of the _GMIN_ conductance. The value listed under GM02
in Figure 8.4 can be verified through the above approach.
The distortion components due to _QBE_ and _QBC,_ represented by C1/"and CIL in Figure 8.3, are evaluated next. Only the junction capacitanc~s **CJE** anq **CJC** are defined
for transistor Ql in this example; that is, no **TF** **or** **TR** parameters are specified, and
therefore the nonlinearity in C1/"or C IL can be expressed in the single power series


(8.38)


based on Eqs. 8.18 and 8.20 and the series


11 `2`
--- = 1 + _ax_ + _2!a(a_ _- l)x_ + ...
(l + _x)"_


For the evaluation of the distortion contribution of _Cje,_ Eqs. 8.23 and 8.26, which were
used in calculating the distortion contributions of _g1/"'_ remain valid, but Eqs. 8.12 and
8.25, expressing currents _i_ _g_ _1/"_ andic1/"' must be changed to


(8.39)


(8.40)


The values of _C1/"O,_ Cirl. and _C1/"2,_ which correspond to _CjO, Cjl,_ and _Cj2_ in Eq. 8.38,
are not computed,\ccording to Eq. 8.38 because the BE junction is forward biased, with
_VBE_ - _FC._ _VJE,_ and SPICE uses the following approximation:


_C1/"O_ = _C_ _[je]_ = (l :-: _CJE FC)MJE_ _[MJE_ 1 + _VJE(l_ __ FC) (VBE -_ _FC._ _VJE)_ _]_ (8.4l)


described in Sec. 10.2.2; the graphical interpretation of the above approximation is
shown in Figure 10.7. The coefficients _Cjl_ and _Cj2_ in the power series of _Cj,_ Eq. 8.38,
are the first and second derivatives of _Cj_ with respect to _VJ,_ respectively. The derivatives of Eq. 8.41 lead to the coefficients for Eq. 8.40:



C - C .. - _crE_ _MJE_

1/"1   - _jel_ _-_ _VJE(l_ _- FC._ _VJE)(MJE+l)_


_C1/"2_ = _Cje2_ = 0



(8.42)


**258** 8 DISTORTION ANALYSIS


Eqs. 8.23 and 8.40 are used to compute the values of the coefficients _aI, a2,_ and _a3_
of the _Vb'_ series, Eq. 8.26. The first-order equation and, therefore, _al_ are the same as
for _g",.._ The second-order terms inserted into the first of Eqs. 8.23 yield the following
expression for _a2:_


_j(WI_ + _W2)C",.IRB_
(8.43)
(l + _jWl C",.ORB)(l_ + _jW2C",.oRB)[l_ + _j(WI_ + _w2)C",.oRBl_


The amplitude and phase of the second-order distortion, _HD2c",.,_ due to C",. are


_IHD2c",.1_ = 4.5 . 10- [6]

_LHD2c",._ = 77°


which are in excellent agreement with the SPICE2 values.
The distortion contribution due to _CJL_ will be derived next. First, calculate the distortion due to _CJLi,_ the reflection of _CJL_ to the input circuit, as shown in Figure 8.5. The
first of Eqs. 8.23 is used with _i_ _JL_ expressed by the following series due to the nonlinearity in the junction capacitance C _JL:_


___ _dVb'_ 2 _dv~,_ 3 _dv~,_
_i_ _JL -_ C _JLOa_ _V_ 1 _-----;[t_ + C _JL_ 1 _av_ 1 _(if_ + C _JL2av_ 1 _-----;[t_


_= jWICJLOavIVb'_ + _j(WI_ + _W2)CJLla;IV~'_ + _j(WI_ + _W2_ + _w3)CJL2a~lv~,_ _(8.44)_


where _V_ _o_ has been replaced by _avlvb"_
C _JLO_ is equal to _Cjc,_ the capacitance of the reverse-biased BC junction, and has the
following derivatives _Cjcl_ and _Cjc2:_


1 _MIC_
_CJLl_ = _C_ _[jcl]_ _"2.cJLOVIC_ _-_ _VBC_
2 1 _+MIC_
_CJL2_ = _C_ _[jc]_ _2_ = _3_ _[CJL1 ]_ _VIC_ _-_ _VBc_


Substitution of second-order terms in Eqs. 8.23 yields the following value for _a2_ in
Eq.8.26:


(8.46)


The second-order distortion component _HD2cJLi_ has the following magnitude:


SMALL-SIGNAL DISTORTION ANALYSIS **259**


The second part of the distortion due to CIJ. is evaluated from the output circuit in
Figure 8.5. The nonlinearity of _ilJ._ is assumed to be due only to _vo,_ which is a power
series of _Vb':_


_Vo_ = _b]Vb'_ + _bzv~,_ + _b3V~,_

(8.47)
_ilJ._ = _jW]CIJ.OVo_ + _j(W]_ + _WZ)CIJ.]V~_ + _j(W]_ + _Wz_ + _W3)CIJ.ZV~_


The assumption that the input circuit is linear represents an approximation made in
order to avoid the more complex solution, which involves the power series of both _vb'_
and _Vo_ simultaneously. Substitution of the first- and second-order terms in Eqs. 8.23
yields the following values of the coefficients _b]_ and _b_ _z:_


(8.48)


(8.49)


The second-order distortion due to the CIJ. component connected at the output node is
obtained from Eqs. 8.47 after inserting the value of _bz_ from Eq. 8.49:


The contribution due to CIJ. at the output is the sum of the two coefficients


This value is in agreement with the value found in the SPICE listing of Figure 8.4 in
the CJC column.
The section 2ND HARMONIC DISTORTION is concluded by the line HD2
MAGNITUDE 1.674D-01 PHASE 164.49 = -15.53 DB, which gives the total second-harmonic distortion in the load resistor obtained by adding all the complex
numbers representing the individual distortion components. The magnitude 0.167 is
very close to the value of _HD2_ obtained in Sec. 5.4 for the transistor with no frequencydependent elements. Because 1MHz is a relatively low frequency, the distortion due to
the nonlinear capacitances CIJ. and C 7T is negligible compared to the nonlinear resistive
contributions, _gm_ and _g7T'_ Similarly, the total second-order intermodulation sum and
difference components track the values of Chap. 5 and equal 2 X _HD2._
The third-order distortion can be computed following the same steps as above. Because the number of terms involved is higher, the derivation is more difficult and prone
to errors due to some approximations made in hand calculations.
The third-order distortion due to the _IBe_ component of the base current can be
computed by replacing the third-order terms of Eqs. 8.25 and 8.26 into KCL, Eqs. 8.23.


**260** 8 DISTORTION ANALYSIS


Coefficient _a3_ in the _Vb'_ series, Eq. 8.26, results:


_a3( jWl,_ _jW2, jW3)_

_- g71"3RBal (jwl)al_ _(jw2)al_ _(jw3)_ _-_ _2g71"2RBal (jwl)a2(_ _jWl,_ _j_ _[W]_ _2)_
(8.50)
I + _g71"RB_ + _j(Wl_ + _W2_ + _w3)RB(C71"_ + _avl CJL)_


where the possible values of _W3_ are :tWl or _:tW2._ The _HD3_ contribution at the output
is obtained by multiplying _a3_ by the gain _avl:_


(8.51)


and the third-order distortion due to _g71"_ is given by


(8.52)


The magnitude of this distortion yields


which is in agreement with the SPICE2 value for GPI in the 3RD HARMONIC

DISTORTION section.
The third-order distortion component due to _gm_ is computed similarly, by the insertion of the third-order terms in Eqs. 8.32 and 8.33 into KCL, Eq. 8.23, for the output
section of the transistor model. The third-order coefficient in the power series for _Va_
results:


(8.53)


where _W3_ can be :tWl or _:tW2_ depending on the distortion component to be derived, and


(8.54)


The third-order distortion contribution due to _gm_ in the output voltage is


(8.55)


which translates into the following magnitude for _HD3:_


_IHD3gm_ _i_ = 2.22 X 10- [2]


SMALL-SIGNAL DISTORTION ANALYSIS **261**


_HD3_ _gm_ is evaluated according to Eq. 8.52 where the _gm_ contribution replac'es that of _g1T_
in _VO'_ This value is larger than the 1.79 X 10- [2] predicted by SPICE; for the third-order
distortion it is harder to separate in hand calculations the different distortion components
contributed by _Ie._
Two additional distortion components, GM2 03 and GM02 3, can be noticed in the
summary report for third-order distortion. They represent the distortion due to the following partial derivatives in the Taylor series expansion of _ie:_


_a_ _[3]_ _`1`_ _e_
_gm203_ (8.56)
_aV~EaVBe_


_a_ _[3]_ _`1`_ _e_
_gmo23_ (8.57)
_aVBEaV~e_


The total third"order distortion _HD3_ is the magnitude of the vector sum of all components, equal to 1.84 X 10- [2], and is very close to the value obtained in Chap. 5 for the
circuit with pure resistive nonlinearities and without parasitic base resistance.
An important distortion measure is the third-order intermodulation, denoted _1M3,_
which represents the spectral component at 2Wl - _W2_ = _21T_ X 1.1 MHz. The term with
this frequency in Eqs. 8.6 represents the _1M3_ component. Assuming that _F(_ _jWl)_
_F(_ _jW2),_ the _1M3_ distortion can be related to _HD3_ as follows:


(8.58)


as long as frequency-dependent effects are not important. In our example this assumption is generally valid, and the value _1M3_ = 4.88 X 10- [2] computed by SPICE relates to
_HD3_ approximately according to Eq. 8.58 with 52 equal to 1 if not otherwise specified
on the • **DrSTO** line.
The last distortion category computed by SPICE as part of the summary is
that of the APPROXIMATE CROSS MODULATION COMPONENTS. Cross modulation (Meyer, Shensha, and Eschenbach 1972) occurs when one of the two input signals
in Eq. 8.2 is modulated in amplitude and the other is not:


(8.59)


where _m_ is the modulation index. Because of the nonlinearities in the circuit, amplitude
modulation is transferred to the signal WI, the carrier signal. In the third-order term in
Eqs. 8.6 the following cross-modulation term is generated:


(8.60)


**262** 8 DISTORTION ANALYSIS


The _cross modulation index, CM,_ is defined as the ratio of the transferred amplitude
modulation to the original fractional modulation,


(8.61)


for equal amplitudes of the two input signals, _Vi]_ = _Vi_ _2._ This definition is valid for
memoryless, or resistive, nonlinearities only. For frequency-dependent nonlinear circuits the phase shifts of the different transfer functions must be considered in defining
a frequency-domain cross-modulation factor, _CMF:_


(8.62)


where _H3( jw!, jW2, - j(2)_ is the third-order transfer function for the modulated _w!_
component (see Eqs. 8.6 and 8.8). At high frequencies the amplitude crossmodulation,
CMA, corresponds to _CM_ at low frequencies (defined by Eq. 8.61) and is equal to


_CMA_ = _CMF._ cos<p (8.63)


where


A _phase cross-modulation factor,_ CMP, can be defined as the ratio of the transferred
phase modulation to the original fractional amplitude modulation:


_CMP_ = _CMFsin<p_ (8.64)


The values computed by SPICE2 are based on the relation between _CMF_ and the
third-order intermodulation distortion, _1M3._ From comparison of Eq. 8.62 and the definition of _1M3,_ Eq. 8.58, the following equality results:


_CMF_ = _4.IM3_ (8.65)


The above equality is used in SPICE2 to compute the amplitude and phase crossmodulation terms:



_CMA_ = _411M31 COS(<PIM3- <Po)_

_CMP_ = _411M31_ sin(<pIM3- _<Po)_



(8.66)


(8.67)



where _<PIM3_ and _<Po_ are the phase of _1M3_ and the phase of the signal at the output, respectively.


LARGE-SIGNAL DISTORTION ANALYSIS **263**


**8.3** **LARGE-SIGNAL DISTORTION ANALYSIS**


A good approach for estimating the total harmonic distortion is to run a large-signal
time-domain analysis and then use the       - **FOUR** analysis introduced in Sec. 6.4. The
Fourier analysis computes the first 10 spectral components in SPICE2 and a userspecified number of harmonics in SPICE3. Large-signal analysis provides more accurate results than AC small-signal analysis because of the removal of the linearity, or
small-signal, assumption. The computation of the spectral components, however, can
introduce errors due to the approximation of the waveform based on the values stored
for the discrete timepoints used in the transient analysis. Also, the Fourier analysis does
not offer the evaluation of intermodulation distortion in the presence of two input signals
and the distortion contribution by type of nonlinearity available with the small-signal
**. nrSTO** analysis.


**8.3.1** **One-Transistor Amplifier Distortion**


It is a useful exercise to check the distortion measures computed by SPICE2 using
**. nrSTO** for the one-transistor amplifier in the above section.
The most important issue is to scale the amplitude of the sinusoidal input signal
properly so that the circuit dissipates the same power in the load resistor as specified in
the • **nrSTO** statement. The distortion components for the above circuit were computed
for 1mW power in _RL,_ or 0 dBm. The amplitude of the output voltage, _Vo,_ corresponding
to this specification is


(8.68)


The gain predicted by the AC analysis for this circuit (see the results in Figure 8.4) is


_a_ _v_ = ~ = 69.9


which leads to an input amplitude of



_Vi_ = _V_ _[o]_ = 20.2mV
_av_

```
ONE-TRANSISTOR CIRCUIT (Figure 5.8)
```

```
Ql 2 1 0 QMOD
```

RL 2 3 lK
vce `3 0 5`



(8.69)


**264** 8 DISTORTION ANALYSIS


       ```
      VEE 4 0 793.4M
      VI 1 4 SIN 0 20.2M lMEG AC 1
```

       ```
      .MODEL QMOD NPN
```
+ `RB=lOO`
+ `CJE=lP`
```
     + CJC=2P
```

       ```
      .OP
      *.AC LIN 1 lMEG lMEG
      *.DIS'IORL 1
```

       ```
      .TRAN IN 2U 0 IN
      .PLOT TRAN V(2)
      .FOURIER lMEG V(2)
      .WIDTH OUT=80
      .OPT NOPAGE REL'IOL=lE-4 ITL5=O LIMPTS=5000

```

        - END


The SPICE input is shown above; the circuit has the sinusoidal input signal _Vi_
with a DC offset, _VBE,_ of 793.4 mV necessary to bias the circuit, an amplitude of 20.2
mY, and a frequency of IMHz. Note the large number of time steps specified on the
**. TRAN** line, 2000, as well as the value of _TMAX,_ the maximum time step the program is
allowed to use in order to estimate the spectral components over the last period. Before
checking the results of the Fourier analysis, one needs to double-check that the value
of the gain computed in the AC analysis is accurate, that is, the amplitude of _Vo_ should
be 1.41 V. The measurements show that this value is 1.46 V. This value points to a gain
of 72.7, which inserted into Eq. 8.69 leads to the following value of _Vi:_


_Vi_ = 19.4mV



,



The discrepancy in the value of the gain can be explained by the fact that the input
voltage is very close to the value of _Vth,_ the thermal voltage, where the accuracy of the
linear approximation declines.
The results of the analysis with _Vi_ = 19.4 mV are shown in Figure 8.6. First check
the value of the first spectral component at 1 MHz, which must be 1.41 V for proper calibration of the spectral components. The second- and third-order harmonic distortions are


_HD2_ = 0.154


_HD3_ = 0,0162


which are close to but slightly less than the values obtained from the • **DISTO** analysis.


LARGE-SIGNAL DISTORTION ANALYSIS **265**


**** `FOURIER ANALYSIS` `TEMPERATURE` = `27.000 DEG C`


```
FOURIER COMPONENTS OF TRANSIENT RESPONSE V(2)
```

`IX:COMPONENT` = `2.831DtOO`
```
HARMONIC FREQUENCY FOURIER NORMALIZED
  NO (HZ) COMPONENT COMPONENT
   1 1.000Dt06 1.412DtOO 1.000000
   2 2.000Dt06 2.1790-01 0.154288
   3 3.000Dt06 2.2880-02 0.016205
   4 4.000Dt06 5.9760-03 0.004232
   5 5.000Dt06 1.8310-03 0.001296
   6 6.000Dt06 5.2410-04 0.000371
   7 7.000Dt06 1.4840-04 0.000105
   8 8.000D+06 4.0550-05 0.000029
   9 9.000Dt06 1.0620-05 0.000008

```

```
  PHASE
  (DEG)
 175.453
 71.477
 -69.935
 127.044
 -4.229
-131.263
 102.947
 -21.846
-146.013

```

```
 NORMALIZED
PHASE (DEG)
    0.000
  -103.976
  -245.388
  -48.409
  -179.682
  -306.715
  -72.505
  -197.299
  -321.466

```


`TOTAL HARMONIC DISTORTION` =


**Figure 8.6** Fourier analysis results.


**8.3.2** **Single-Device** **Mixer Analysis**


```
15.520066 PERCENT

```


Mixer circuits are commonly used in radio receivers. The radio signal, _w_ _s,_ and a local signal generated in the receiver, _Wlo,_ are fed to a mixer circuit. The local oscillator
frequency is tunable so that the difference between the two signal frequencies is approximately constant.
The mixer operates as an analog multiplier by generating spectral components of
frequencies _Wlo_ :t _w_ _s'_ The mixer is followed by a bandpass filter tuned to the difference
frequency, which rejects the sum and other frequency components. The difference frequency is called the intermediate frequency, _Wi!._
A typical single-transistor mixer circuit is shown in Figure 8.7. _C], L],_ and the load
resistor, _R],_ in parallel form a bandpass filter at the output of the mixer. Two voltage
sources are connected at the input: _Vw_ sets the bias at the base of transistor, _Q],_ and
generates the local oscillator signal (LO), and _Vs_ is defined as the input signal (5):


The two signals add up to an input voltage Vi consisting of two frequencies:


(8.70)


**266** 8 DISTORTION ANALYSIS


Figure 8.7 Single-transistor
mixer.


The transfer characteristic of the BIT is approximately equal to


(8.71)


where leis the quiescent DC value of the collector current. There are two possible series
expansions for an exponential. In Eq. 5.21 and in the above sections a power series was
used under the assumption of a small signal, namely _v;j_ _Vth_ < < 1.
A difference-frequency component is present in the output current, _ie,_ according
to the small-signal derivation of Sec. 8.2.1:


_=_ _Ie_ [1 + ... + _az Vlo Vs_ COS(Wlo            - _ws)t_ + ... ] (8.72)


LARGE-SIGNAL DISTORTION ANALYSIS **267**


where _Vi_ is the total input signal for the mixer circuit. This _1M2_ component represents
the **IF** signal, which is the output of interest in a mixer:


(8.73)


**In** the case of a mixer or a multiplier the small-signal assumption is not always true.
If the amplitude of an input sinusoid is not small with respect to _Vth,_ the exponential
can be expanded in a Fourier series with Bessel function coefficients (Pederson and
Mayaram 1990):



where



exp(Vscos _wst/Vth)_ = _Io(s)_ + 21] _(s)_ cos _wst_ + .

(8.74)
_exp(Vlo_ cos _wlot/_ _Vth)_ = _fo(l)_ + 21] (l) cos _wlot_ + .


s =


_I_ _`=`_



and _In_ _(x)_ are modified Bessel functions of order _n,_ which can be found in mathematical
tables. After substitution ofthe series ofEq. 8.74 into Eq. 8.71 and use of trigonometric
identities, the output collector current is


_ie_ = _IcIo(s)Io(l)_ + ... + _2Ie1] (s)1]_ _(I)_ _COS(Wlo - ws)t_ + ...



(8.75)



where



1] _(s)1](l)_ _]_
_= IDe_ [ 1 + ... + 2 _Io(s)Io(l)_ _COS(Wlo - ws)t_ + ...


_IDe_ = _IcIo(s)Io(l)_



is the dynamic average value of the collector current. A difference-frequency spectral
component _(Wlo_ _-_ _w_ _s),_ the **IF** component, is generated as well as other components
not included above; all spectral components except the **IF** component must be rejected
by the output filter. The **IF** component in Eq. 8.75 derived through a Fourier series
expansion is more general than the expression in Eq. 8.72 or that in 8.73, obtained from
small-signal analysis. For small signals Eqs. 8.72 and 8.75 are identical.
Assume the following values for the amplitudes and frequencies of the two signals:
_Vlo_ = 100 mV, _flo_ = 1.1 MHz, _Vs_ = 1mV, and _fs_ = I MHz. _Vlo_ is a large signal and


**268** 8 DISTORTION ANALYSIS


therefore Eq. 8.75 must be used to calculate the IF component. The ratios of Bessel
coefficients are found in math tables:


_h(l)_ = 095
fo(l) .


_h(s)_ s 1 _V_ _s_
_lo(s)_ 2 2 _Vth_


The difference component of the collector current becomes


_iCij_ = _0.951Dc-_ _V_ _s_ _COSWijt_ (8.76)
_th_ _v_


The correct design of a mixer requires that the amplitude of the IF output voltage

_Vij_ be much larger than any other voltage. The selection of this value is made difficult
by the fact that the amplitude of the local oscillator, _Via,_ is much larger than the radio
signal, _Vs'_ The Q of the parallel RLC filter must be dimensioned so that the rejection,
_Rej,_ at _Wla_ is sufficient to boost the IF component.
From the Fourier series,


_._ _h(l)_
_ICla_ = _21_ _Dc_ _lo(l) COSwia_ _[t]_ (8.77)


arid using _iCij_ as given in Eq. 8.76 the ratio of the LO component to the IF component
is given by


_iCla_ = 2 _Vth_ (8.78)

_iCij_ _Vs_


which in this example is over 50.
The rejection of a given frequency component, _Re_ _j (w),_ for a single-tuned parallel
RLC filter is given by


(8.79)


where


1
_Wa_ _=_ _jLC_


is the resonant frequency and Q is the quality factor defined in Eq. 6.26.


LARGE-SIGNAL DISTORTION ANALYSIS **269**


The ratio of interest between the voltage amplitudes of the IF and LO components is


_Voil_ ___ 2 _VthR.(_ _)_
_--_ _-_ _-_ _e]_ _Wlo_ (8.80)
_Volo_ _Vs_


If Q = 40 for the tuned circuit of Figure 8.7, the rejection of the LO component is
_Rej_ = 440, leading to an IF voltage component 8.49 times larger than the amplitude
of the local oscillator at the output _Volo'_
The SPICE circuit description and the resulting DC operating point are shown in
Figure 8.8. The IF and LO frequency components can be checked by requesting a • FOUR
analysis. There is a limit of only nine harmonics printed by SPICE2 including the fundamental. In order to have SPICE2 compute the amplitudes of both the IF and LO components, two separate runs must be performed. The first set of input commands is

```
.TRAN .2U 620U 600U 45N
.FOUR lOOK V(3)
.PLOT TRAN V(3)

```

```
*******12/13/90 ******** SPICE 2G.6

ONE TRANSISTOR MIXER CIRCUIT
**** INPUT LISTING

```

```
3/15/83 ********18:44:38*****

 TEMPERATURE = 27.000 DEG C

```

```
***********************************************************************

Q1 3 2 0 Mom
R1 3 4 15K
C1 3 4 4.244NF
L1 3 4 596.83UH
.MODEL Mom NPN
```

```
* SUPPLY, SIGNAL AND LOCAL OSCILLATOR
```

```
VCC 4 0 10
VS 2 1 0 SIN 0 1MV 1MEG
VLO 1 0 0 SIN 0.78 100MV 1.lMEG AC 1
```

```
.TRAN .2U 620U 600U 45N
.FOURIER lOOK V(3)
*.TRAN 45N 601.8U 600U 45N
*.FOURIER 1.lM V(3)
.PLOT TRAN V(3)
.WIDTH OUT=80
.OPTIONS RELTOL=lE-4 ITL5=0
.END

```

Figure 8.8 SPICE2 input and DC bias point for mixer circuit.


**270** **8** **DISTORTION ANALYSIS**


`****` `BIT MODEL` `PARAMETERS` `TEMPERATURE` = `27.000` `DEG C`

```
              MODl
      TYPE NPN
      IS 1.00D-16
      BF 100.000
      NF 1.000
      BR 1.000
      NR 1.000

```

`****` `SMALL` `SIGNAL` `BIAS` `SOLUTION` `TEMPERATURE` = `27.000` `DEG C`


```
NODE VOLTAGE

 4) 10.0000

```

```
NODE VOLTAGE

 2) 0.7800

```

```
NODE VOLTAGE

 3) 10.0000

```

```
  VOLTAGE SOURCE CURRENTS

  NAME CURRENT

  VCC -1.251D-03
  VLO -1.251D-05

  TOTAL POWER DISSIPATION 1.25D-02 WATTS

```

`****` `OPERATING` `POINT` `INFORMATION` `TEMPERATURE` = `27.000` `DEG C`

```
**** BIPOLAR JUNCTION TRANSISTORS

```

```
MODEL
```

IE
```
IC
VEE
VEC
VCE
BETADC
```

8M
```
RPI
```

RX
```
RO
CPI
CMU
CBX
CCS
BETAAC
FT

```

```
 Q1
MODl
1.25E-05
1.25E-03
  0.780
 -9.220
 10.000
 100.000
4.84E-02
2.07E+03
O.OOE+OO
1.00E+12
O.OOE+OO
O.OOE+OO
O.OOE+OO
O.OOE+OO
 100.000
7.70E+17

```


**Figure 8.8** _**(continued)**_


**LARGE-SIGNAL** **DISTORTION** **ANALYSIS** **271**


**15**


8 **10**
:>


**605**


**Time. ~s**
**Figure 8.9** **IF component waveform.**


**which request SPICE2 to plot the waveform** **of** V ( 3), **the collector voltage,** **for the**
**last two periods** _**(T**_ _**ij**_ **= lO,us) after 60 cycles** **have been computed to assure that**
**the circuit has reached steady state. The** **. FOUR statement requests the harmonics**
**of the 100-kHz spectral component. The IF waveforms** **modulated by the LO signal**


**** `FOURIER` `ANALYSIS` `TEMPERATURE` = `27.000` `DEG` `C`

```
 FOURIER COMPONENTS OF TRANSIENT RESPONSE V(3)
```

`DC COMPONENT` = `1. 000Dt01`
```
 HARMONIC FREQUENCY FOURIER NORMALIZED PHASE NORMALIZED
   NO (HZ) COMPONENT COMPONENT (DEG) PHASE (DEG)

   1 1.000Dt05 6.225DtOO 1.000000 -89.950 0.000
   2 2.000Dt05 5.624D-03 0.000903 5.330 95.280
   3 3.000Dt05 1.593D-03 0.000256 42.211 132.161
   4 4.000Dt05 1.347D-03 0.000216 -157.027 -67.077
   5 5.000Dt05 1.059D-03 0.000170 -61.888 28.062
   6 6.000Dt05 1.054D-03 0.000169 19.929 109.879
   7 7.000Dt05 1.509D-03 0.000242 100.348 190.298
   8 8.000Dt05 5.607D-04 0.000090 62.290 152.240
   9 9.000Dt05 1.819D-03 0.000292 -75.714 14.236

```

`TOTAL` `HARMONIC` `DISTORTION` = `0.106690` `PERCENT`


**Figure 8.10** **Fourier coefficients** **of the IF component.**


**272** 8 DISTORTION ANALYSIS


are shown in Figure 8.9, the Fourier analysis results are listed in Figure 8.10. The amplitude of _Voif_ computed by SPICE2 is 6.225 V.This value can be verified by hand
uS,ingEq. 8.76:



(8.81)



where



_Vs_
_Voif_ = _IcifR_ _i_ = _0.95IDe-_ _v_ _th_ Ri
10- [3]
= 0.95 . (1.25 . 10- [2] A) 0.025815 . 10 [3] n = 6.9 V


_IDe_ = _Iefo(s)Io(l)_ = (1.25 . 10- [3] A) . 10 = 1.25. 10- [2] A



with _Ie_ given by SPICE2, and _fo(l)_ = 10, and _Io(s)_ = **1,** from tables of Bessel functions.
The • **TRAN** and • **FOUR** statements for the next run must be changed in order to
observe the 1.I-MHz LO spectral component:

```
.TRAN 45N 610.909U 609.090U 45N
.FOUR 1.lMEG V(3)

```

As in the IF signal plot, the last two periods of the 1.1-MHz LO signal waveform
are shown in Figure 8.11; the resulting Fourier coefficients for the _WZ_ _o_ signal are listed


'* :>



609.5


**Figure 8.11** Waveform of the LO signal.



610.0


Time, ).Is



610.5


LARGE-SIGNAL DISTORTION ANALYSIS 273


in Figure 8.12. The value computed by SPICE2 for _Volo,_ 0.89 V, is larger than that
predicted by Eq. 8.80:


1.9. 1.25 . 10- [2 ]                   - 15 . 10 [3]
440 V = 0.81 V (8.82)


The approach of finding the high-frequency component of a modulated signal from a
Fourier analysis with this component as fundamental is very inaccurate. The amplitude
of the IF component can vary by 100% depending on which time interval of the IF
signal's period the computation is performed. Note that the above .TRAN analyses were
run with a maximum internal time step _TMAX_ = 45 ns, which represents 1I20th of the
highest-frequency component of interest in the signal. It is necessary to provide at least
20 points for one period of a sine wave for the calculation of the Fourier coefficients to
be accurate.
Better accuracy can be obtained from a program that can compute more than nine
harmonics. SPICE3 allows a user to define the number of Fourier components computed; in this example both the IF and the LO magnitudes result from a single analysis
as the fundamental and the eleventh harmonic. The results of the SPICE3 Fourier analysis are listed in Figure 8.13.
The SPICE3 Fourier analysis verifies the ratio _VOitiVolo_ = 8.5 predicted above.
More details about Fourier and distortion analysis in SPICE3 can be found in the latest
user's guide (Johnson, Quarles, Newton, Pederson, and Sangiovanni- Vincentelli 1992).
The same result can be arrived at by using the •DISTO small-signal analysis as
long as the circuit behaves fairly linearly. Since _Vlo_ is not much larger than _Vth,_ it is


**** `FOURIER ANALYSIS` `TEMPERATURE` = `27.000 DEG C`

```
FOURIER COMPONENTS OF TRANSIENT RESPONSE V (3)
```

`DC COMPONENT` = `4.099DtOO`
```
HARMONIC FREQUENCY FOURIER NORMALIZED PHASE NORMALIZED
  NO (HZ) COMPONENT COMPONENT (DEG) PHASE (DEG)

  1 1.100Dt06 8.892D-01 1.000000 110.885 0.000
  2 2.200Dt06 7.609D-02 0.085574 -0.298 -111.184
  3 3.300Dt06 1.344D-01 0.151106 -140.456 -251.342
  4 4.400Dt06 9.763D-02 0.109789 -169.624 -280.510
  5 5.500Dt06 6.168D-02 0.069368 -165.533 -276.418
  6 6.600Dt06 5.23ID-02 0.058822 -156.038 -266.923
  7 7.700Dt06 4.618D-02 0.051932 -151.451 -262.337
  8 8.800Dt06 4.095D-02 0.046057 -146.867 -257.752
  9 9.900Dt06 3.701D-02 0.041623 -142.171 -253.056

```

`TOTAL HARMONIC DISTORTION` = `23.881368` `PERCENT`


Figure 8.12 Fourier components of the LO signal.


274 8 DISTORTION ANALYSIS

```
      1> spice3d2
      Spice 1 -> source 1xtor_mixer.ckt

      Circuit: one transistor mixer circuit

      Spice 2 -> run
      Spice 3 -> set nfreqs=12
      Spice 4 -> fourier lOOk v(3)
      Fourier analysis for v(3) :
       No. Harmonics: 12, THO: 11.7802 %, Gridsize: 200, Interpolation Degree: 1

      Harmonic Frequency Magnitude Phase Norm. Mag Norm. Phase
```

-------- `---------` `---------` `---------` `-----------`
```
      0 0 9.99887 0 0 0
      1 100000 6.224 -89.993 1 0
      2 200000 0.00663444 11.4065 0.00106594 101.4
      3 300000 0.00102807 71.4975 0.000165179 161.491
      4 400000 0.00222051 -168.16 0.000356766 -78.163
      5 500000 0.00106634 -79.296 0.000171327 10.6968
      6 600000 0.00140642 9.06029 0.000225968 99.0534
      7 700000 0.00115581 100.742 0.000185701 190.735
      8 800000 0.00095327 -158.17 0.00015316 -68.176
      9 900000 0.0016788 -71.311 0.00026973 18.6825
      10 1et06 0.0181946 84.4315 0.0029233 174.425
      11 1.1et06 0.732933 90.1382 0.117759 180.131

      Spice 5 -> quit
      Spice-3d2 done

```

Figure 8.13 Fourier components computed by SPICE3 for the mixer circuit.


instructive to verify the results of the. DISTO analysis. The IF component is the _DIM2_
second-order difference intermodulation component. The SPICE2 input and the results
of the. AC and. DISTO analyses are listed in Figure 8.14. It is important to provide the
correct information in the •DISTO statement.
First, the reference power is calculated for an input amplitude _Vlo_ = 100 mV



_Pre!_ = _-:i~Rl_ 1 = "2 1( 4.84.10- [3] )2 15.10 [3] mW = 175 mW


where


with _8m_ = 4.84 X 10- [2] mho as computed by SPICE in Figure 8.8.



(8.83)


```
*******12/13/90 ******** SPICE 2G.6
ONE TRANSISTOR MIXER CIRCUIT
**** INPUT LISTING

```

```
3/15/83 ********18:44~38*****

 TEMPERATURE = 27.000 DEG C

```

```
***********************************************************************
Q1 3 2 0 MODI
R1 3 4 15K
C1 3 4 4.?44NF .
L1 34 '596.83UH
.MODEL Mom NPN
```

```
* SUPPLY, SIGNAL AND LOCAL OSCILLATOR
```

```
VCC 4 0 10
*VS 2 1 0 SIN 0 75.5UV 1MEG
VLO 2 5 SIN 0.78 100MV 1.1MEG AC 1
```

```
.DISTO R1 0 .90909 175M .01
:AC LIN 11 'lOOK 1.lMBG '
.PRINT AC VM(3)
.PRINT DISTO DIM2 SIM2 HD2 HD3 DIM3
.WIDTH OUT=80
.OPTIONS RELTOL=lE-4 ITL5=0
.END
```

.
```
**** ACANALYSIS TEMPERATURE = 27.000 DEG C

```

```
  FREQ
1.000E+05
2.000E+05
3.000E+05
4.000E+05
5.000E+05,
6.000E+05
7.000E+05
8.000E+05
9.000E+05
1.000E+06
1.100E+06

```

```
VM(3)
7.255E+02
'1.209E+01
6.802E+00
4.837E+00
3.779E+00
3.109E+00
2.645E+00
2.303E+00
2.041E+00
1.832E+00
'1.663E+00

```

```
**** AC ANALYSIS TEMPERATURE =, 27.000 DEG C

   FREQ DIM2 SIM2,HD2 HD3 DIM3
 1. 000E+05 4.424E-05 3.484E-04 1. 609E-02 5.778E-03 2.647E-03
 2.000E+05 3.268E-01 4.887E-01 2.317E+01 5.753E+02 '5'.841E+01
 3.000E+05 1.618E+00 9.891E-01 4.707E+01 2.121E+03 1.906E+02
 4.000E+05 4.551E+00 1.447E+00 6.895E+01 4.399E+03 3.803E+02
 5.000E+05 1.019E+01 1.885E+00 8.986E+01 7.361E+03 6.256E+02
 6.000E+05 2.040E+01 2.312E+00 1.103E+02 1.099E+04 9.259E+02
 7.000E+05 3.882E+01 2.733E+00 1.303E+02 1. 530E+04 1.281E+03
 8.000E+05 7.388E+01 3.149E+00 1.502E+02. 2.026E+04 1. 691E+03
 9.000E+05 1. 507E+02 3.563E+00 1.700E+02 2.589E+04 2.155E+03
 1.000E+06 3.931E+02 3.976E+00 1.897E+02 3.218E+04 2.675E+03
 1.100E+06 3.676E+03 4.386E+00 2.093E+02 3.914E+04 3.249E+03

```

**Figure 8.14** **Small-signal** **distortion analysis results for mixer.** **275**


**276** 8 DISTORTION ANALYSIS


For the • **DISTO** specification the radio signal S is defined with respect to the LO
signal; the amplitude _Vs_ is .01 _Via_ and the frequency _Ws_ is 0.909 _Wla._ The following
changes must be made to the SPICE2 input used by the previous analyses (see Figure
8.8). First, the input signal source, _Vi,_ is commented out, since only one AC source,
_Via,_ is needed to run the AC analysis. Second, the • **AC** and • **DISTO** lines replace the
**•TRAN and.** **FOUR** lines; see the **INPUT** **LISTING** in Figure 8.14.
The ratio _Vail /Vala_ can be obtained from the value of _DIM2_ computed by SPICE
at 1.1 MHz. SPICE2 computes _DIM2_ according to


(8.84)


where _a]_ is the gain, _a2_ is the second-order coefficient in the power series, and _Van_ is
the normalized voltage amplitude at the output:


(8.85)


The gain _a]_ is frequency-dependent, and at 1.1 MHz it is found in the AC ANALYSIS
listing for VM ( 3) equal to 1.66. _a2_ can be evaluated by solving equations similar to
Eqs. 8.23 and Eqs. 8.32 through 8.34:


(8.86)


The value of _DIM2_ computed by SPICE2 is 3.68x 10 [3] . From Eqs. 8.73, 8.80, and
8.84 the ratio of the IF to the LO signal at the output can be derived:


_a2_ _ViaV_ _[s]_ = _DIM2_ _[a]_ _]_ _Via_ = 3.68. 103 1.66 . 0.1 = 8.4 (8.87)

_a]_ _Via_ _Van_ _72.5_


which is the same as the result obtained from large-signal Fourier analysis and hand
calculations.
It is advantageous to use the • **DISTO** analysis whenever the circuit behaves linearly because the       - **DISTO** and       - **AC** analyses are much faster than the       - **TRAN** and

**• FOUR** analyses. The results obtained using      - **DISTO** are correct for this example because the only distortion of the signal is due to the transistor nonlinearities.


**8.4** **SUMMARY**


This chapter has described in detail how to evaluate distortion in electronic circuits
using both small-signal AC and large-signal Fourier analysis in SPICE. The purpose
has been to familiarize the user with the methodology of evaluating distortion, which
can be applied with any SPICE program, regardless of whether the program supports
small-signal distortion analysis.


REFERENCES **277**


All the capabilities of the small-signal • **DISTO** analysis of SPICE2 introduced in
Chap. 5 have been presented here. Frequency-dependent elements were included in
the general derivation of the spectral component calculation. The summary option of
**. DISTO** was exercised in SPICE2 and the meanings of all the results were explained.
Commonly used distortion measures were related to the results obtained from SPICE2
for a single-transistor amplifier.
**In** the second part of the chapter large-signal time-domain analysis and • **FOUR**
analysis were applied to evaluate the same distortion measures derived with smallsignal analysis. The Fourier components computed by SPICE correspond to the distortion components of the same order. Special consideration must be given to the accuracy
of the • **FOUR** analysis, that is, to the number of time points computed by the simulator
during the last period of the signal. The relationship between small-signal and largesignal analysis results was exemplified for a single-transistor mixer. This example also
pointed to the advantages of the **small-signal.** **DISTO** analysis over **the.** **FOUR** analysis
for circuits with two nearly linear input signals.


**REFERENCES**


Chisholm, S. H., and L. W. Nagel. 1973. Efficient computer simulation of distortion in Electronic
circuits. _IEEE Transactions on Circuit Theory_ (November).
Johnson, B., T. Quarles, A. R. Newton, D. O. Pederson, and A. Sangiovanni-Vincentelli. 1992
(April). _SPICE3 Version 3f User's Manual._ Berkeley: Dept. of Electrical Engineering and
Computer Science, Univ. of California.
Meyer, R. G. 1979. Distortion analysis of solid-state circuits. In _Nonlinear Analog Circuits EECS_
_240 Class Notes._ Berkeley: Dept. of Electrical Engineering and Computer Science, Univ. of
California.
Meyer, R. G., M. J. Shensa, and R. Eschenbach. 1972. Cross modulation and intermodulation in
amplifiers at high frequencies. _IEEE Journal of Solid-State Circuits_ SC-7 (February).
Narayanan, S. 1967. Transistor distortion analysis using Volterra series representation. _Bell Sys-_
_tem Technical Journal_ (May-June).
Pederson, D.O., and K. Mayaram. 1990. _Integrated Circuits for Communication._ Boston:
Kluwer Academic.


_**Nine**_


_**SPICE ALGORITHMS**_
_**AND**_ _**OPTIONS**_


,
**9.1** **OVERVIEW OF ALGORITHMS**


A number of algorithms have proven well suited for the solution of the equations of
electrical circuits and are implemented not only in SPICE simulators but in most circuit
simulators in existence today. The various types of BCEs for electrical elements were
described in Chaps. 2 and 3. The most general equations have been shown to be ordinary
differential equations, ODE, with nonlinear BCEs, which must be solved in the time
domain.
The solution process implemented in SPICE for the time-domain solution is shown
in Figure 9.1. Generally the program first solves for a stable DC operating point. The solution starts with an initial guess of the operating point, which is followed by iterations
for solving the DC nonlinear equations. The iterative process is represented by the inner
loop in Figure 9.1. The solution the iterative process converges to represents either the
small-signal bias solution (SSBS) or the initial transient solution (ITS); see Chaps. 4
and 6, respectively. This is the time zero solution. The iterative process is repeated for
every time point at which the circuit equations are solved in transient analysis. The algorithms used in SPICE for the DC solutions of linear and nonlinear circuits are presented
in Secs. 9.2 and 9.3, respectively.
The time-domain solution, which is represented as the outer loop in Figure 9.1, uses
numerical integration to transform the set of ODEs into a set of nonlinear equations.
The time-domain analysis is replaced by a sequence of quasi-static solutions. These
techniques are described in Sec. 9.4.

```
278

```

OVERVIEW OF ALGORITHMS **279**


Define new trial
operating point

```
       No

```


Discretize differential
equations in time


```
No

```


Initial trial
operating point


Linearize semiconductor
device around trial operating point


Load linear conductances
in circuit matrix


Solve linear equations


Convergence?


Yes


Increment time


End of time interval?


Yes



Stop
**Figure 9.1** SPICEsolutionalgorithm.


A circuit simulator is defined by the following sequence of specific algorithms;
an implicit numerical integration method that transforms the nonlinear differential
equations into nonlinear algebraic equations, linearization of these through a modified Newton-Raphson iterative algorithm, and finally Gaussian elimination and sparse
matrix techniques that solve the linear equations. Simulators using these techniques,
such as SPICE2, SPICE3, and their derivatives, are known as third-generation circuit
simulators. The solution approach implemented in these simulators is also referred to
as direct methods. These algorithms are described in detail by McCalla (1988) and
Nagel (1975) and in overview papers, such as those by McCalla and Pederson (1971)
and Hachtel and Sangiovanni-Vincentelli (1981).
An important characteristic of SPICE is the _analysis options,_ which enable the
user to select among several numerical methods and analysis tolerances. SPICE should
not be treated as a black box that always provides the right answer to no matter what
circuit. The choice of algorithms and tolerances is based on a large set of examples,


**280** 9 SPICEALGORITHMS AND OPTIONS


and the majority of the circuits run well using the default settings. This chapter is intended to relate the analysis options accessible to the user with the solution algorithms.
A good understanding of this chapter is important for overcoming the analysis failures
commonly referred to as convergence problems.
The general form of the option statement is


**. OPTIONS** _OPTl=Namel/vall_ _<OPT2=Name2/val2> ..._


_OPTl, OPT2, ..._ are options recognized by the SPICE program. The option is followed
either by a name, _Namel, Name2, ..._ or a number, _vall, val2, ..._ The most important
options control the solution algorithms and tolerances and are introduced in this chapter.
Each version of SPICE has a few options that differ from the ones in SPICE2, but the
fundamental options for algorithms, tolerances, and iteration limits can be found in most
versions. The analysis options introduced throughout this chapter are summarized at
the end.


**9.2** **DC SOLUTION OF LINEAR CIRCUITS**


This section describes the circuit equation formulation as well as the solution algorithms for linear systems. The linear-equation solution algorithms described here are
used for the DC solution of linear circuits and for the the AC solution, which always
involves linear circuits. The DC equations are formulated with real numbers, and the
AC equations use complex numbers.
The matrix formulation for connectivity and nodal equations in SPICE is presented
in Sec. 9.2.1 together with the solution algorithm. An extended version of nodal analysis (Dort 1989; Nilsson 1990; Paul 1989), called modified nodal analysis (MNA), is
used in SPICE to represent the circuit. Gaussian elimination and the associated factorization into lower triangular and upper triangular matrices, the LV factorization, are
implemented in SPICE for the solution of a linear system of simultaneous equations.
An important characteristic of the circuit admittance matrix, its sparsity, and its impact
on the analysis is also described in this section.
Certain characteristics of the MNA formulation and Gaussian elimination associated with computer limitations of the representation of real numbers can lead to a loss of
accuracy and a wrong solution. These pitfalls are detailed in Sec. 9.2.2. Two important
issues are detailed there: the reordering of equations for accuracy and sparsity and the
SPICE options available to the user for controlling the linear solution process.


**9.2.1** **Circuit Equation Formulation: Modified** **Nodal Equations**


In Example 1.1 the DC solution of the bridge-T circuit (Figure 1.1) is derived from
the nodal equations written for each node. In the evaluation of the node voltages, the
value of the grounded voltage source, _VB/AS,_ was assigned, by inspection, to _VI,_ the voltage at node 1. Thus only two nodal equations in two unknowns must be solved; Eqs. 1.1


DC SOLUTION OF LINEAR CIRCUITS **281**


and 1.2 are reproduced here:


node2: -GI . _VI_ +(GI + G2 + _G3)V2_ _-G3_ _. V3_ = 0
(9.1)
node3: _-G4_ _. VI_ _-G3_ _. V2 +(G3_ + _G4)V3_ = 0


Eq. 9.1 can be expressed as a matrix equation:


(9.2)
GV = I


where G is the conductance matrix of the circuit, V is the unknown node voltage vector, and I is the right-hand-side (RHS) current vector. Representation by matrices and
vectors is well suited for programming and therefore is the methodology of choice in
SPICE. The conductance matrix, G, is easily set up by adding all conductances incident into a node to each diagonal term and subtracting the conductances connecting two
nodes from the corresponding off-diagonal terms.
One problem in formulating the conductance matrix, G, is that a voltage source cannot easily be included in the set of nodal equations: the conductance of an ideal voltage
source is infinite, and its current is unknown. A voltage source connected between two
circuit nodes complicates this issue even more and raises the need for a consistent formulation suited for programming. The problem is exemplified by the modified bridge- T
circuit shown in Figure 9.2, which contains an additional voltage source, _VA,_ in series


with _R4._
This problem led the developers of SPICE to extend the set of nodal equations to
include voltage-source equations represented by currents in the unknown vector and
by voltages in the RHS vector. This approach, modified nodal analysis, is therefore an
extension of nodal analysis in that the node voltage equations are augmented by current
equations for the voltage-defined elements (Nagel and Rohrer 1971; Ho, Ruehli, and


Brennan 1975).



0 + _VA_

```
R4
```

14
-0 CD



0



+



_VA_



_`R`_ _3_


_VB_ _`R`_ _2_


Figure 9.2 Modified bridge-T circuit.


**282** 9 SPICEALGORITHMS AND OPTIONS


The complete set of equations can now be written for the bridge- T circuit in Figure
9.2, including the voltage sources:


node 1: (G I + _G4)VI_ _-GIV2_ _-G4V4_ +II =0

node 2: _-GIVI_ +(G I + G2 + _G3)V2_ _-G3V3_ =0

node 3: _-G3V2_ _+G3 V3_ _-/4_ =0
(9.3)
node 4: _-G4VI"_ _+G4V4_ _+/4_ =0

_VB:_ _VI_ _= VB_

_VA:_ _-V3_ _+V4_ _= VA_


In partitioned matrix form the equations become


GJ _+G4_ -G I 0 _-G4:_ 1 0 _VI_ 0

-GJ G I + G2 + G3 _-G3_ 0 :0 I 0 _V2_ 0
0 _-G3_ G3 0 :0 -1 _V3_ 0

(9.4)
_-G4_ 0 0 G4 :0 1 _V4_ 0
```
        -----------------------------~----```

1 0 0 0 :0 0 II _VB_
0 0 -1 1 :0 0 _14_ _VA_


The above MNA equations can be rewritten in abbreviated form:


where C and E are the vectors of the current and voltage sources, respectively.
So far the discussion has treated only voltage sources as being difficult to include
into a set of nodal equations. Another circuit element that presents the same problem is
the inductor, because it is a short in DC, and therefore the voltage across it is zero and
the conductance is infinite. The inductor is also a voltage-defined element in SPICE
and is included as a current equation in the MNA formulation. The total number of
equations, _N,_ used to represent a circuit in SPICE is


(9.5)


where _n_ is the number of circuit nodes excluding ground, _nv_ is the number of independent voltage sources, and _nz_ is the number of inductors. Note that all controlled sources
except the voltage-controlled current source (VCCS), which is a transconductance, also


DC SOLUTION OF LINEAR CIRCUITS **283**


introduce current equations. For complete details on the MNA matrix representation of
different elements consult McCalla's book (1988).
The MNA set of equations that needs to be solved, Eq. 9.4, can be expressed as a

matrix equation:


Ax = b `(9.6)`


The solution vector, x, can be computed by inverting matrix A. This approach is very
time-consuming, and Gaussian elimination (Forsythe and Moler 1967) is preferred for
numerical solutions.
The Gaussian elimination procedure uses scaling of each equation followed by subtraction from the remaining equations in order to eliminate unknowns one by one until
A is reduced to an upper triangular matrix. The solution can then be found by computing each element of vector x in reverse order (the back-substitution phase). For a 3 X 3
system of linear equations,


_e_ _[(O) . [ a(O)]_ I. 11 _a(O)_ 12


_a(O)_ _a(O)_
_e_ _[(O).]_ 2. 21 22

_a(O)_ _a(O)_ (9.7)
_e_ _[(O).]_ 3. 31 32


the steps leading to the solution are outlined as follows. The equations are designated
by _e\O), eiO),_ and _e~O)._ The superscripts, both in the equation designators and the matrix
elements, represent the step of the elimination process. First, _XI_ can be eliminated from

_e(O)_ and _e(O)_ by subtracting _e(O)_ multiplied by _a(O)/a(O)_ from /0) and subtracting _e(O)_
2 3 I ° 21 11 2 I
multiplied by _a(O)/a(O)_ 31 11 from / 3 J..


_e(l)_ _-_ _e(O)_
I                  - I


_e(l)_ _-_ /0) _ _(a(O)/a(O))/O)_
2                   - 2 21 11 I

_e(l)_ _-_ _e(O) -_ _(a(O)/a(O))e(O)_ (9.8)
3                   - 3 31 11 I


Second, _X2_ is eliminated from _e~l)_ by subtracting _ei1)_ multiplied by _aWl_ _aW_ from _e~1):_


(9.9)


**284** 9 SPICEALGORITHMS AND OPTIONS


which yields an upper triangular equation system:


_e(2) ._ I' r _a(O)_ 11 _a(O)_ 12 _a(O)_ 13 _[_ XI _]_ r _b(O)_ I 1

_e(2)._ 0 _a(l)_ _a(l)_ _X2_ = _b(l)_
2 . 22 23 2

_e(2) ._ 0 0 _a(2)_ _X3_ _b(2)_
3 . 33 3


Third, back-substitution leads to the following solution:



(9.10)


(9.11)



A variant of Gaussian elimination is _LV factorization._ This procedure transforms the
circuit matrix A into a lower, **L,** and an upper, **U,** triangular matrix. Equation 9.6 can
be rewritten as


**LUx** = b (9.12)


The first step of the method is to factorize A into Land **U,** which for the third-order
system become


(9.13)


where U is the result of Gaussian elimination and L stores the scale factors at each
elimination step. The second phase of the solution is the forward substitution, which
results in a new RHS:


(9.14)


The last step is back-substitution, which computes the elements of the unknown vector, x:


(9.15)


Note that inverting Land U is trivial because they are triangular. The advantage of **LU**
factorization over Gaussian elimination is that the circuit can be solved repeatedly for


DC SOLUTION OF LINEAR CIRCUITS **285**


different excitation vectors, that is, different right-hand sides. This property is useful in
certain SPICE analyses, such as sensitivity, noise, and distortion analyses.
An important observation about the conductance matrix G (Eq. 9.4) is that it is
diagonally dominant and many off-diagonal terms are zero. The simple explanation of
this is that off-diagonal terms are generated by conductances connected between pairs
of nodes, and usually a node is connected to only two or three neighboring nodes. In
the conductance matrix of a circuit having a few tens of nodes, only two or three out of
a few tens of off-diagonal terms are nonzero; in other words the conductance matrix is
_sparse._ The sparsity is maintained in the current-equation submatrix R (Eq. 9.4), where
many diagonal elements are also zero. This issue is addressed in the following section
on accuracy. The MNA matrix of the bridge-T circuit, Eq. 9.4, has 20 zero elements of
a total of 36 elements in the matrix. The sparsity of the matrix can be defined as


number of elements equal to zero
_sparsity_ = ------------- (9.16)
total number of elements in matrix


The sparsity is 55.6% in this example. The number obtained from SPICE for the sparsity
of this circuit in the accounting summary, option **ACCT** (Sec. 9.5), differs from the above
number because SPICE includes the ground node in the computation, raising the total
number of elements to 49. The zero-element count in SPICE is taken after reordering.
Sparsity is a very useful feature, which can be exploited for reducing data storage and
computation. The next section explains the need for careful reordering of the equations
for maintaining accuracy and sparsity at the same time.


**9.2.2** **Accuracy and SPICEOptions**


Accuracy problems in the solution of a linear circuit can be classified as either topological or numerical. The voltage-defined elements, such as voltage sources and inductors,
generate zero diagonal elements linked to the current equation (Ho, Ruehli, and Brennan
1975). This problem can be corrected in the setup phase based on a topological reordering, also referred to as _preordering._ In SPICE the row in the MNA matrix corresponding
to the current equation of a voltage source is swapped with the node voltage equation
corresponding to the positive terminal of the same voltage source (Cohen 1981).
A second problem, which is also topological in nature, is a cut set of voltage-defined
elements. This leads to a cancellation of a diagonal element value during the factorization process. Earlier versions of SPICE2, up to version F, which used only topological
reordering, could not correct this problem. A reordering algorithm has been proposed
(Hajj, Yang, and Trick 1981) that finds an equation sequence free of topological problems. This additional topological reordering scheme is, however, not necessary once
the numerical reordering known as _pivoting_ is used. All SPICE2 version G releases use
pivoting in the sparse matrix solution (Boyle 1978; Vladimirescu 1978).


**286** 9 SPICEALGORITHMS AND OPTIONS


A circuit that cannot be solved only through preordering is shown in Figure 9.3.
The MNA matrix of the circuit is


`1/5` `-1/5` 0 0 0 0 _`V]`_ I

`-1/5` `1/5` 0 0 `1` 0 _`V2`_ 0
0 0 `1/2` `-1/2` `-1` 0 _`V`_ _3_ 0
0 0 `-1/2` `1/2` 0 `1` _`V4`_ 0
0 `1` `-1` 0 0 0 _h_ 0
0 0 0 `1` 0 0 _`Iv`_ 3 `(9.17)`


After preordering, which swaps row _h_ with node 2 and row _Iv_ with node 4, and reordering to maintain sparsity, described below, the circuit matrix becomes


`1` 0 0 0 0 0

`1/2` `1` 0 0 0 `-1/2`
0 0 `1/5` `-1/5` 0 0
0 0 `-1/5` `1/5` `1` 0

`-1/2` 0 0 0 `-1` `1/2`
0 0 0 `' 1` 0 `-1`


Matrix equations 3 and 4 form a diagonal block


[ G] _-G] ]_
_-G]_ G]


where G] = !; during the LV factorization a zero is created on the diagonal at row 4.
This example shows the need of a reordering scheme based on the matrix entries at each
step of the LV decomposition.



_R1_
G) CD
    


_L1_ _R_ _2_
0 0



50 1H 20
~
_IL_



_Iv_ 3V _VA_
t




  -  **Figure 9.3** Circuit exemplifying diagonal cancellation.


DC SOLUTION OF LINEAR CIRCUITS 287


Not all problems associated with the solution of theMNA matrix are topological,
however. Another problem is that computers only have finite precision. The limit of the
number of digits in the mantissa of a floating-point number, up to 15 decimal digits for
a double-precision, Or 64-bit, real number, in IEEE floating-point format, can lead to
the loss of significance of a matrix term relative to another during the solution of the
linear equations.
The simple circuit (Freret 1976) shown in Figure 9.4 demonstrates this point. It is
assumed that the computer can represent only four digits of floating~point accuracy. It is
easy to imagine that having a switch element (see Chap. 2) A circuit can have resistors
with a range from i mn to 1 Gn, that is, 12 orders of magnitude. The equations of the
circuit are




[ -1 [1] 1.0001-1] [ _V_ _VI]_ _z_ _-_ _._ [1]0


The hypothetical computer in this case, however, rounds off element _Qzz_ to


_a22_ = G I + _G_ _z_ = 1.000



(9.18)



due to the four-digit limitation. As in the previous example, a zero is created on the
diagonal during Gaussian'elimination, resulting in erroneous values of infinity for _VI_
and _V_ _z._ This problem is due to the insufficient accuracy of the computer and cannot be
corrected by reordering. The conductance matrix of the circuit is singular.
Another accuracy problem, also due to the limited number of digits, can be caused
by the Gaussian elimination process. This case is exemplified by the circuit in Figure
9.5. The nodal equations for this circuit are


GI _VI_ + _gz Vz_ = _I_

_- gl VI_ + _Gz Vz_ = 0 (9.19)


1 Q


10 kQ


Figure 9.4 Circuit exemplify- Figure 9.S Circuit exemplifying rounding error.
ing limited floating-point range.


**288** 9 SPICEALGORITHMS AND OPTIONS


Substitution of the values of the conductances, G I and _G2,_ and the transconductances,
gl and _g2,_ yields the following system of equations:


After one elimination step the system becomes


with the following solution on a computer with four-digit accuracy:


which is obviously incorrect. If the rows of the equation are swapped before factorization in order to bring the largest element onto the diagonal, the system of equations
becomes


with the more realistic solution


The accuracy of this solution is still affected by the limited number of digits; the solution
is correct, however, for the available number representation. The exact solution is


_V2_ = 0.9999

VI = 0.9999


This type of accuracy loss can also be observed in the case of a series of high-gain
stages conne,cted in a feedback loop, such as a ring oscillator; the off-diagonal elements
are transconductances, which grow as a power-law function of the gain factors during
factorization and can eventually swamp out the diagonal term. A ring oscillator similar to that in Figure 6.9 but implemented with bipolar transistors is shown in Figure
9.6. Replacement of the transistors with a linearized model during each iteration, as


DC SOLUTION OF LINEAR CIRCUITS 289


_R_ _R_
10 kn 10 kn


t _I_


Figure 9.6 BJT ring oscillator exemplifying rounding error.


described in Sec. 9.3, leads to the following system of equations:




[



G + _g1T2_ 0

_gm2_ G + _g1T3_

  - _gm3_



_gml_ _][VI]_ _[Ieql]_

  - _V2_ = _Ieq2_

G + _g1T1_ _V3_ _Ieq3_ (9.20)



The solutions of the node voltages, _VI, V2,_ and _V3,_ should be identical, but they
differ if the above system is solved as is, because the self-conductance of each node, or
diagonal term, loses its contribution during the elimination process.


_Exercise_
Assume that _gm_ = 3.607 X 10- [2] mho, _g1T_ = 3.607 X 10- [4] mho, _R_ = 10 kO, and _Ieq_ _=_
2.192 X 10- [2] A. Carry out the Gaussian elimination steps to find the solution for _VI, V_ _2,_
and _V_ _3_ with four-digit accuracy.


Another numerical problem occurs when the matrix entries at a certain step of the
elimination process become very small, with the ratio between the largest value in the
remainder matrix and the largest value in the initial matrix being of more orders of
magnitude than can be represented by the computer.
A parameter, PIVTOL, is used in SPICE that defines the lowest threshold for accepting an element as a diagonal element, or a _pivot._ If an element larger than this
value is not found in the remainder matrix at any step, then the matrix is declared singular and SPICE aborts the analysis. The default for this parameter, _PIVTOL_ = 10- [13],
was chosen under the assumption that for typical circuits the maximum conductance
is 1 mho and that, at least 13 digits of accuracy are used by computers to store the matrix


**290** 9 SPICEALGORITHMS AND OPTIONS


entries. Note that SPICE lists the value of the largest element in the remainder matrix in
the *ERROR*: MAXIMUM ENTRY IN THIS COLUMN AT STEP _number value_ IS
LESS THAN PIVTOL message (see Appendix B for error messages). If this value is
nonzero, _PIVTOL_ can be reset using the • **OPTION** statement to accommodate it. The
solution obtained afterward can be correct, but the user must double-check the circuit
for possible high-impedance nodes, very high ratios of conductance values, and so on.
The above examples demonstrate that a topological reordering is not sufficient and
that the order of the MNA sparse matrix has to be based on actual values generated by
the circuit as well. Sometimes it is even necessary to reorder during the iterative process.
Reordering based on selecting the largest element for the diagonal, called _pivoting,_ is
essential for an accurate solution to a set of equations if the original values can be altered
significantly by the factorization process. The larger the circuit, the more important
pivoting becomes, because of the accumulation of rounding error in the solution process.
A detailed presentation of numerical accuracy issues can also be found in the thesis by
Cohen (1981).
As part of numerical reordering, a partial pivoting strategy, which picks the largest
element in the column or row, or a full pivoting strategy, which selects the largest element in the remainder of the matrix, can be chosen. The second constraint mentioned in
the previous section is preservation of the sparsity of the matrix. The Markowitz algorithm is used in SPICE to select, among a number of acceptable pivots, the one that introduces the fewest _jill-in_ terms. Fill-ins are the matrix terms that are zero at the beginning
of the factorization process and become nonzero during LV decomposition. According
to the Markowitz algorithm, the best element to be picked as the next pivot is the one that
has the minimum number of off-diagonal entries in the row and column as measured by


_m_ = _(r -_ _1)(c -_ 1) (9.21)


where rand c are the numbers of nonzero entries of a row and a column, respectively.
In SPICE2 the topological aspects are considered in the setup phase when the sparsematrix pointers are defined. The numerical reordering is based on two criteria: partial
pivoting for accuracy and the Markowitz algorithm for minimum fill-in. Reordering is
performed at the very first iteration after the actual MNA values have been loaded.
The selection of a pivot in SPICE proceeds as follows. Pivoting is performed on the
diagonal elements; if no pivot can be found on the diagonal the rest of the submatrix
is searched. First, the largest element is found in the remainder matrix, and then the
diagonal element with the best Markowitz number is checked as to whether it satisfies
the following magnitude test:


_aii_ _:::::_ _PIVREL._ _aiMax_ (9.22)


where _aiMax_ is the maximum entry at the _ith_ elimination step and **PIVREL** is a SPICE
option parameter, which defaults to 10- [3] . Therefore SPICE accepts as pivot the element
that introduces the fewest fill-ins as long as it is not _PIVREL_ orders of magnitude smaller
than the largest element at that elimination step. An increase of _PIVREL_ forces a better

DC SOLUTION OF NONLINEAR CIRCUITS 291


conditioned matrix at the expense of introducing fill-in terms. PIVREL is the other
option parameter that a user can modify if SPICE aborts because of singular matrix
problems.
Once an optimal order has been found, it is used throughout the analysis unless at
some point a diagonal element is less than _PIVTOL._ In this case _pivoting_ _on the fly_ is
performed for the remainder of the matrix.
In summary, two option parameters control the linear equation solution in SPICE,
PIVREL and PIVTOL. The user is not advised to modify these parameters unless SPICE
cannot find a solution because of a singular matrix problem. In order to modify one or
both linear equation option parameters, one adds the following line to the SPICE input
file:


•OPTIONS _PIVTOL=valuel_ _PIVREL=value2_


_PlVTOL_ should be reset to a smaller value than the maximum entry listed in the SPICE
message as long as the value is nonzero. If the largest entry is zero, one should carefully
check the circuit first, try increasing _PIVREL,_ or skip the DC solution and run a transient
analysis with the Ule flag on. The time-domain admittance matrix adds the contributions
of the charge storage elements, possibly leading to a well-conditioned matrix.


9.3 DC SOLUTION OF NONLINEAR CIRCUITS


In Chap. 3 semiconductor devices were shown to be described by nonlinear I-V characteristics that are exponential or quadratic functions. Controlled sources can also be
described by nonlinear BCEs that are limited to polynomials in SPICE2 but can be any
arbitrary function in SPICE3 and other commercial versions. The modified nodal equations for a circuit with transistors are a set of nonlinear simultaneous equations. The
iterative loop marked in Figure 9.1 for the DC solution of nonlinear equations is implemented in SPICE using the Newton-Raphson algorithm. This algorithm is described in
Sec. 9.3.1.
The iterative solution process continues until the values of the unknown voltages
and currents _converge,_ or in other words, until the solutions of two consecutive iterations
are the same. The criteria for convergence and the options available to the user to control
convergence are presented in Sec. 9.3.2.


9.3.1 Newton-Raphson Iteration


The Newton-Raphson algorithm for the solution of the equations of nonlinear circuits
is introduced with the simple circuit consisting of one diode, one conductance, G, and
one current source, _lA,_ shown in Figure _9.7a._ The graphical representation ofthe BCEs
for the two elements,



_lD_ = _Is(e_ _[v]_ _/_ _[Vth]_ _-_ 1)

_IG_ = _GV_



_(9.23a)_


_(9.23b)_


**292** 9 SPICEALGORITHMS AND OPTIONS


+


~ ~
Figure 9.7 Diode circuit: _(a)_ circuit diagram; _(b)_ graphical solution.



_v_



is shown in Figure 9.7 _b;_ the solution _V_ D is located at the intersection of the two functions
_I_ _D_ and _I_ _G,_ which must satisfy Kirchhoff's current law.


(9.24)


Nonlinear equations of this type are generally solved through an iterative approach,
such as Newton's method, also known as the tangent method (Ortega and Rheinholdt
1970). The current _ID_ in Eq. _9.23a_ can be approximated by a Taylor series expansion
around a trial solution, or operating point, _VDo:_
_ID_ = _IDo_ + _dV_ ~I _(VD -_ _VDO)_ = _IDo_ + _GDO(VD -_ _VDO)_ = _IDNo_ + _GDOVD_ ' _(9.25)_
D _Voo_


where only the first-order term is considered. Equation 9.25 represents the linearized
BCE of the diode around a trial operating point, _VDO._ The diode can therefore be represented by a _companion_ _model,_ a Norton equivalent with current _IDNo_ and conductance
Goo. The new circuit and the graphical representation of the linearized BCE of the diode
are shown in Figure 9.8. After Eq. 9.25 is substituted into Eq. 9.24, the nodal equation
for this circuit becomes


(G + _GDo)V_ = _IA_ _-_ _IDNo_ (9.26)


The solution of the above equation is _VDl,_ which becomes the new trial operating point
for the diode. Equation 9.26 is solved repeatedly, or iteratively, with new values for GD
and _IDN_ at each iteration _(i_ + 1), which are based on the voltage at the previous iteration


```
r---------..,

```


I
I
I
I

_I_ _`[DN]`_ I



DC SOLUTION OF NONLINEAR CIRCUITS **293**


_v_



I
I
I
I
L -.I



~ ~
**Figure9.8** Linearized companion model of the diode circuit: _(a)_ circuit diagram;
_(b)_ graphical solution.


_(i)._ The iterative process is described by the nodal equation


(9.27)


which represents for this simple case the Newton iteration. The graphical representatiqn of the iterative process for this circuit is given in Figure 9.9. Intersection of the
linearized diode'conductance with the load line G define the values _V_ _Di_ at successive
iterations. This process converges to the solution, _V._
The general Newton iteration applied to a nonlinear function _g(x)_ of a single variable is


(9.28)


where for tpe diode equation


_g(x)_ = _ID(V)_ = _Is(ev/Vth_ _-_ 1)

and at the solution _X,_ Ig+ [1] ) = _Ig)._

The generalized linearization approach for a set of,nonlinear equations g(x) = 0
consists in computing the partial derivatives with respect to the controlling voltages,
according to Eq.9.25. These values form the conductance contribution of the nonlinear
BeEs to the MNA of the circuit, called the Jacobian, J. For an arbitrary circuit the set
of all nonlinear equations is replaced at each iteration by the following set of linear
equations:


(9.29)


**294** 9 SPICEALGORITHMS AND OPTIONS


Figure 9.9 Newton iteration for the diode circuit.



_v_



where J(x(i») is the Jacobian computed with xU), the solution at the previous iteration.
The conductance matrix A and RHS b for a nonlinear circuit have the following matrix
representation:



A = J(x(i») + G
b = J(x(i») . x(i) - g(x(i») + C



(9.30)

(9.31)



Equation 9.31 includes the contributions of the linear elements and independent current .
sources in the circuit, G and C, respectively. At each iteration the circuit is described
as a linear system, Eqs. 9.6, 9.30, and 9.31, which is solved using the LU factorization
described in Sec. 9.2.1.
An important question is whether the above equations converge to a solution and
how many iterations it takes. The nonlinear I-V characteristics of semiconductor devices are exponential or quadratic functions. As exemplified by the diode characteristic
in Figure 9.8, the equivalent conductance can vary from 0 in the reverse region to infinity in the forward bias region. With the limited range of floating-point numbers available
on a computer and the unboundedness of solutions provided by the Newton algorithm
according to Eq. 9.28, the iterative scheme can fail to converge.
An algorithm that controls the changes in the state variables of the nonlinear elements from iteration to iteration is very important if the simulated circuit is to converge
to the correct solution. This algorithm is known as a _limiting algorithm_ and determines


DC SOLUTION OF NONLINEAR CIRCUITS **295**


the convergence features of the simulator. A limiting algorithm selectively accepts the
solution unchanged or, when large changes in the value of the nonlinear function would
occur, limits it by correcting the new value of the Newton iteration (Calahan 1972) from
Eq. 9.28 to the following:


(9.32)


The parameter _ex(O_ < ex ::s 1) indicates that only a fraction of the change is accepted
at each iteration. Equation 9.32 defines the Newton-Raphson iterative algorithm. The
choice of ex is implemented through the limiting algorithm, which is tailored to the different nonlinear characteristics of each semiconductor device. This parameter assumes
a different value at each iteration and for each device.
A practical implementation of the above modified Newton-Raphson iteration, Eq.
9.32, is shown in Figure 9.10. The scheme proposed by Colon is successfully used in
SPICE and its derivatives to limit the new junction voltage on diodes and BITs. At
each iteration the new solution of the junction voltage, _VI,_ if larger than the previous
value, _Va,_ is used to derive a new current, _I;,_ based on the last linearization of the diode
characteristic. The voltage corresponding to _I;_ on the nonlinear diode characteristic is
_V;,_ which is smaller than the original solution, _VI; V;_ becomes the new trial operating
point for the diode in the current iteration. If _VI_ is smaller than _Va,_ it is accepted directly


_v_


**Figure 9.10** Newton-Raphson iteration with current
limiting.


**296** 9 SPICE ALGORITHMS AND OPTIONS


as the new trial operating point because there is no danger of a runaway solution. The
danger in the absence of any limiting is that a trial solution can generate very large
values of the exponential function, which cannot be corrected in subsequent iterations,
and the process fails to converge.
The Newton-Raphson algorithm has quadratic convergence properties if the initial
guess, Yo in Figure 9.10, is close to the solution. Therefore, it is important in a circuit
simulator to provide an initial guess as a set either of node voltages or of terminal voltages for the nonlinear semiconductor devices. Circuit simulators start out usually with
all unknowns set to zero. SPICE2 initializes the semiconductor devices in a starting operating point such that nonzero conductances can be loaded into the MNA circuit matrix
at the first iteration. An additional protection built into SPICE is a parallel minimum
conductance, _GMIN,_ with a default value of 10- [12] mho, connected in parallel to every
pn junction, such as BE and BC for BITs and BD and BS for MOSFETs, to prevent
zero-valued conductances from being loaded into the circuit admittance matrix when
these junctions are reverse biased.


**9.3.2** **Convergence and SPICEOptions**


This section addresses the issues of how and when convergence is achieved. Equation
9.32 defines the Newton-Raphson iteration; the iterative process is finished when the
following two conditions are met:


**1.** All the voltages and currents of the unknown vector are within a prescribed
tolerance for two consecutive iterations.
**2.** The values of the nonlinear functions and those of the linear approximations
are within a prescribed tolerance.


Next, the tolerances used in SPICE to establish convergence are introduced. Each
tolerance, for voltage or current variables, is formed from a relati ve term and an absolute
term. The voltage tolerance for node _n, EVn,_ is defined as


(9.33)


The values of node voltages at two consecutive iterations have to satisfy the following
inequality for convergence:


! [y(i+1)] _n_                                                       - y(i)l _n_ :=; E _Vn_ (9.34)


**RELTOL** and **VNTOL** are SPICE option parameters representing the relative and the
absolute voltage tolerance, respectively. The default values are set to


_RELTOL_ = 10- [3]

_YNTOL_ = 1 _J.L_ V


DC SOLUTION OF NONLINEAR CIRCUITS 297


The absolute tolerance defines the minimum value for which a given variable is still
accurate; with the SPICE defaults, voltages are accurate to 1 part in 1000 down to 1 /-LV
of resolution. This means that a node with 100 V is accurate to 100 mV and a voltage
of 10 /-LV is accurate to only 1 /-Lv.
Convergence is based not only on the circuit variables but also on the values of
the nonlinear functions that define the BCEs of the nonlinear elements. In the case of
semiconductor devices, the nonlinear functions are the currents, for example, _ID_ for a
diode, _Ie_ and _IB_ for a _BIT,_ and _IDs_ for all FETs. In the following derivation the nonlinear
function will be referred to for simplicity as a current.
SPICE defines the difference between the nonlinear expression, _ID,_ evaluated
for the last junction voltage solution _vji)_ and the linear approximation _i_ _D,_ using the
present voltage solution, _VY+I),_ as the test for convergence:


A (i+1)
_ID_ = _GDV_ _J_ _-_ _IDN_



_ID_ = _Is (evji)/vth_ _-_ 1)


The tolerance is defined as


El = _RELTOL_ _._ max _(iD, ID)_ + _ABSTOL_


and the iteration process converges when


_liD - IDI_ :5 _Ej_

_IVJ+_ _[1]_ _)_ _- VJ)I_ :5 _EVJ_



(9.35)


(9.36)


(9.37)


(9.38)



ABSTOL is the absolute current tolerance and defaults to 10- [12] A in SPICE2 and
SPICE3. This default is very accurate for the base current of _BITs_ but may be too
restrictive for other devices, such as FETs, whose operation is controlled by the gate
voltage and for which _IDs_ is in most applications 1 _/-LA_ and higher.
There is a limit to the number of iterations computed by SPICE. This limit is set by
the option parameter **ITL1,** which defaults to 100. If the inequalities ofEqs. 9.34, 9.37,
and 9.38 are not satisfied in _ITLl_ iterations, SPICE2 prints the message - ERROR*: NO
CONVERGENCE IN DC ANALYSIS and the last node voltages.
When SPICE computes DC transfer curves, the number of allowed iterations is
_ITLl_ only for the first value of the sweeping variable and then is reduced to _ITL2,_
which defaults to 50. The advantage of subsequent analyses is that the unknown vector
is initialized with the values from the last point.
Convergence failure can also occur during a transient analysis, which consists of
quasi-static iterative solutions at a discrete set of time points. For each time point only
**ITL4** iterations are allowed before a failure of convergence is decreed. _ITIA_ defaults
to 10. In transient analysis failure to converge at a time does not result in the abortion
of thf' :m::llv~i~hnt r::ln~f'~::lrf'ihwtion of thf' timf' ~tf'n ::l~f'xnl::linf'n in Sf'r CJ4


**298** 9 SPICE ALGORITHMS AND OPTIONS


When SPICE fails to find a DC solution, an additional option can be used to achieve
convergence, called _source ramping._ This method consists in finding the DC solution
by ramping all independent voltage and current sources from zero to the actual values.
This is equivalent to an **.OP** analysis using a • DC transfer curve approach. Source
ramping can be viewed as a variation of the general modified Newton-Raphson solution
algorithm. SPICE2 does not automatically use source ramping if it fails to converge.
Option parameter **ITL6** must be set to the number of iterations to be performed for
each stepped value of the source, similar to **ITL2** for DC transfer curves. SPICE3 and
PSpice perform source ramping automatically when the regular iterative process fails to
converge. A more detailed presentation of convergence problems along with examples
and solutions can be found in Chap. 10.
All _ITLx_ options can be reset by the user, although this should be rarely necessary. A detailed presentation on the situations requiring the change of these options is
provided in the following chapter.
During the solution process the linear equivalent of each nonlinear element must
be evaluated. This is a very time-consuming process and may not always be necessary. **In** time-domain analysis, during the iterations performed at anyone time point
each nonlinear element is checked for a change in the terminal voltages and the output
current from the last time point. If the controlling variables and resulting function of
a device have not changed, a new linearized model is not computed for this device; it
is _bypassed._ **In** other words, the linearized conductances obtained at the previous time
point are used again in the circuit matrix.
The bypass operation results for a majority of circuits in analysis time savings without affecting the end result. There are, however, cases when bypass can cause nonconvergence at a later time point. The check for bypassing a device is based on Eqs. 9.37
and 9.38. This check can limit the devices being bypassed by reducing the tolerances;
however, this reduction can negatively affect the convergence test for the overall circuit.


**9.4** **TIME-DOMAIN SOLUTION**


The time-domain solution is the most complex analysis in a circuit simulator, because
it involves all the algorithms presented so far in this chapter, as shown graphically in
the flowchart of Figure 9.1. As described in the introductory overview of algorithms
(Sec. 9.1), transient analysis is divided into a sequence of quasi-static solutions.
This section outlines the numerical techniques used in SPICE to transform a set
of differential equations, such as the ones representing the BCEs of capacitors and inductors, into a set of algebraic equations. The presentation of the numerical methods is
simplified for the purpose of providing the SPICE user with insight into the workings
of the program; a rigorous description of the integration algorithm can be found in the
book by Chua and Lin (1975) and L. Nagel's Ph.D. thesis (1975). The specific implementation in SPICE is described here; furthermore, the accuracy of these algorithms is
analyzed along with the options available to the user regarding numerical methods and
error bounds.


TIME-DOMAIN SOLUTION **299**


**9.4.1** **Numerical Integration**


The different numerical integration algorithms and their properties are best introduced
with an example.       

_EXAMPLE_ 9.1


Consider the series RC circuit shown in Figure _9.11a;_ at _t_ = 0 a voltage step of magnitude _Vi_ is applied at the input. Find the voltage, _VR(t),_ across the resistor and the voltage,
_vcCt),_ across the capacitor over time.


_Vi_


_(a)_


'j


0.5 1.0 1.5


Time, 1.15


_(b)_

**Figure 9.11** RC circuit: _(a)_ circuit diagram; _(b)_ plots of solutions _VR(t)_ and _vc(t)._


**300** 9 SPICEALGORITHMS AND OPTIONS


_**Solution**_
From the BCEs of the resistor and capacitor the following equation is obtained:


KVL applied to the circuit allows the following substitution of _Vc:_


_vcCt)_ = _Vi -_ _VR(t)_


yielding the following differential equations for _VR(t)_ and _vcCt):_


The solutions _VR(t)_ and _vcCt)_ are


_VR(t)_ = _Vie-t/T_


_T_
_vcCt)_ = _Vi(l -_ _e-_ _[t]_ _/_ _),_


and are presented in Figure _9.11b._



(9.39)


(9.40)


(9.41)


(9.42)



**In** SPICE the solution of the above equation in the interval 0 to _TSTOP_ (see also Sec.
6.2) is performed at a number of discrete time points, where the differential equation is
replaced by an algebraic equation. For simplicity, let _x_ be the time function to be solved
for and _X_ _n_ the values at the discrete time points _tn:_


The solution at _tn_ _+!, X_ _n_ _+!,_ can be expressed by a Taylor series expansion around _X_ _n:_


_X_ _n+!_ = _X_ _n_ + _hX_ _n_ (9.43)


where _h_ is the time step, assumed equal for all time points for simplicity. This is identical
to the finite-difference approximation of the derivative of _x_ and represents the _forward-_
_Euler_ (FE) integration formula. Substitution of Eqs. 9.41 into 9.43 yields the following
recursive solution for _Vc_ at _tn+!:_


(9.44)


TIME-DOMAIN SOLUTION **301**


This is represented graphically in Figure _9.12a._ A rather sizeable error can be noticed
for _VC(tn+l)_ computed with Eq. 9.44.
A different solution is obtained for Vc if in Eq. 9.43 _x_ _n_ _+_ 1 is expressed in terms of
the derivative at _t_ _n_ _+_ 1> _X_ _n_ _+_ 1,


_Xn+l_ = _Xn_ + _hXn+l_ (9.45)


This represents the _backward-Euler_ (BE) integration formula. Because Eq. 9.45 must
be solved simultaneously for _x_ as well as for its derivative, this formula is known as
an _implicit method,_ whereas the FE is an explicit method. The graphical interpretation
of this solution is shown in Figure _9.12b._ It can be seen that _Vn+l_ as given by the BE
formula is less sensitive to the size ofthe time step _h_ than that given by the FE formula.
An important measure of the accuracy of a numerical integration method is the
_local truncation error, LTE,_ evaluated at each time point. For the FE and BE methods
_LTE_ can be approximated by the first discarded term in the Taylor expansion:


_h_ _[2]_

_Xn+l_ = _Xn_ + _hXn_ + _TXn_


_LTE_ = _Ih; xnl_ (9.46)


Algorithms for automatic time-step control such as the one used in SPICE are based on
checking whether the LTE of each time-dependent BCE is within prescribed bounds.
The actual algorithm is detailed in the following section.
The two methods introduced so far are known as first-order methods, because
higher-order terms are neglected in the series. Based on the above definition of _LTE,_
it can be thought that using higher-order terms of the series in the solution of _xn_ _+_ 1 can
lead to smaller _LTE._ The trapezoidal integration is a second-order method that can be
derived based on the observation that a more accurate solution _VC(tn+_ 1) can be obtained
if in Eqs. 9.43 and 9.45 the average of the slopes at _tn_ and _tn_ _+_ 1 are used as compared to
either one or the other:


(9.47)


The higher accuracy ofthis method is obvious from the graphical solution of Vc _(tn_ + 1)
shown in Figure 9.13.
The LTE of the trapezoidal integration formula can be derived by first substituting

_Xn+l_ in Eq. 9.47 with a Taylor expansion:


(9.48)


**302** 9 SPICE ALGORITHMS AND OPTIONS



Figure 9.12
BE solution.



_(a)_


_(b)_


Solutions of _vdt)_ between _tn_ and _tn_ _+_ 1: _(a)_ FE solution; _(b)_



**Figure 9.13** Trapezoidal solution of _vdt)_ between _tn_ and _tn+l,_


TIME-DOMAIN SOLUTION **303**


and then subtracting the trapezoidal solution, Eq. 9.47, from the exact solution given
by the first three terms of the Taylor series:


(9.49)


The resulting LTE of the trapezoidal integration method for _xn_ _+_ 1 is



_3_
_LTE_ = _Ih_ _..._ _,_
12 _x_ _[n]_



(9.50)



The LTE for _xn_ _+_ 1 is obtained by first substituting _x_ _n_ _+_ 1 in Eq. 9.47 byEq. 9.49 and then
subtracting the resulting equation in _x_ _n_ _+_ 1 from Eq. 9.48:


(9.51)


_EXAMPLE_ 9.2


Apply the trapezoidal integration method to the BCE of a capacitor. Use the result to
develop a companion model of the capacitor to be used in nodal equations.


_**Solution**_
The BCE of a capacitor, Eqs. 2.4 and 2.5, can be rewritten for a nodal interpretation:


_idt_ = _Cdvc_ (9.52)
_L_ r


The trapezoidal integration formula, Eq. 9.47, is applied to the above equation and
results in



_._ _._ _2C(_ _)_
_In+l_ = _-In_ + _h_ _Vn+l_ _-: Vn_


Equation 9.53 can be rewritten as a nodal equation at _tn_ _+_ 1:


or



(9.53)


(9.54)


**304** 9 SPICEALGORITHMS AND OPTIONS


+


G = 2C
_'q_ ~~_h_~~


**Figure 9.14** Companion model for a capacitor.


The companion model of the capacitor for nodal analysis is shown in Figure 9.14. It
is formed of the parallel combination of the equivalent conductance _G_ _eq_ and the equivalent current source _I_ _eq._ **In** SPICE Eq. 9.54 is updated at each time point and the contributions are loaded into the circuit matrix and RHS vector. The companion model for
an inductor can be derived similarly.


An important property of an integration method is its _stability_ or convergence feature. Whereas the LTE is a local measure of accuracy at each time point, stability is a
global measure of how the solution computed by a given method approaches the exact
solution as time proceeds to infinity. Stability is also a function of the specific circuit.
A quantitative analysis of the stability of the integration methods introduced so far can
be performed for the RC circuit in Figure 9.11. The exact solution for _VR(t),_ Eqs. 9.42,
can be compared with the FE, BE, and TR solutions computed after _n_ time steps:


(FE) _Vi(l - h/rt_ (9.55)

_Vi_
(BE) (9.56)
(1 + _h/r)n_

(l - _h/2r)n_
(TR) _V-_ (9.57)
I (l + _h/2r)n_


The FE solution can be seen to lead to the wrong solution if the step-size, _h,_ is greater
than _2r._ The BE solution, by contrast, decreases to zero as does the exact solution _VR(t)_
in Eqs. 9.42 as time increases. An interesting result is offered by the TR method, which
converges toward zero but does so in an oscillatory manner if _h_       - _2r._ This behavior of
the TR method can be observed in SPICE especially when the solution goes through
discontinuities.
Electronic circuits have time constants that can differ by several orders of magnitude; the equations representing these circuits constitute _stiff systems._ The integration
methods used to solve such systems must be _stiffly stable;_ in other words, these methods


TIME-DOMAIN SOLUTION 305


must provide the correct solution without constraining the time step to the smallest time
constant in the circuit. The implicit methods introduced so far, BE and TR, are stiffly
stable, but explicit methods, such as the FE method, are not. The TR and BE integration
methods are the default in the majority of SPICE versions.
Additional integration formulas have been developed that fall in the general category of polynomial integration methods defined by


_n_ _n_

_Xn+l_ = _aiXn-i_ + _bixn-i_ (9.58)
2: 2:
_i=O_ _i=-1_


If b-1 is zero, the method is explicit, and if _b-_ _1_ is nonzero, the method is implicit.
The algorithm'is a multistep,algorithm if _i_ - 1, that is, if more than one time point
from the past is needed to compute _X_ _n_ _+_ 1. The _Gear integration_ (Gear 1967) formulas
of order 2 to 6 have proven to have good stability properties. The Gear formulas of
varying order for _x_ _n_ _+_ 1 are listed in Appendix D. The Gear integration formulas'order 2
to 6 are implemented in SPICE2, SPICE3, and most commercial SPICE versions as an
alternative to the default TR method. PSpice uses only the Gear algorithms.
The time~domain response of.a circuit can differ depending on the integration
method used. Although in the vast majority of cases both the TR and the Gear methods lead to the same solution, the two have different characteristics. The TR method
converges to a solution in an oscillatory manner (Eq. 9.57) when the time step is larger
than a certain limit. The Gear formula of order 2 has an opposite behavior, which leads
to a damped response. This difference between the two methods is demonstrated by the
following example.


_**EXAMPLE**_ _9.3_


Find the time response oftl1eLC circuit shown in Figure. 9.15 assuming that at _t_ = 0
the switch is opened. Use both the TRAP and the GEAR options, the latter with a _MAX-_
_ORD_ of 2, if running,SPICE2 or SPICE3, and compare the results.
.,,


1~A t

1~1

Figure 9.15 LC circuit.


**306** 9 SPICEALGORITHMS AND OPTIONS


LC CIRCUIT

      L1 101M IC=-lM

C1 1 0 1N
** . OPTION METHOD=GEAR MAXORD=2

      .TRAN 1U 400U 0 UIC

.PWT TRAN V(l)


        - END


The SPICE input is listed above. Note that the current source must not appear in
the circuit description, which is valid for _t_ 2': 0; its effect, however, must be taken into
account by setting the appropriate initial condition for the inductor current. In order to
start the analysis from the initial condition at the time the switch is opened, the **Ule**
keyword must be specified in the • **TRAN** statement.
The result of trapezoidal integration is free oscillations with an amplitude of 1 V
at the resonant frequency of 10 [6] radls, or 159 kHz, as seen in the upper trace of Figure 9.16.
The inclusion of the • **OPTIONS** statement by removal of the asterisk at the beginning of the line leads to the solutions computation by the Gear formula. The result is
shown in the lower trace of Figure 9.16 to be a decaying oscillation, which is wrong.
Recent versions of PSpice produce the decaying waveform, probably because the Gear
2 method is used as default.


Trapezoidal
```
         1 V

          0

        -1V
```

   -   ```
         1 V

          0

        -1V

                 50 100 150 200 250 300 350

```

Time,lls
**Figure 9.16** LC circuit response computed with trapezoidal and Gear 2 algorithms.


TIME-DOMAIN SOLUTION **307**


The stability of integration methods is presentedinrriore detail in the works by
McCalla (1988) and by Nagel (1975). Several conclusions can be drawn based on the
first-order analysis presented in this section and the more thorough analysis found in
the .references.
First, the LTE of a numerical method diminishes for higher, order methods; by contrast, the stability deteriorates as the order of the method increases.' Second, the equations of electronic circuits must be solved by stiffly stable integration methods for which
the t~mestep is determined by LTE and not by stability constraints.


**9.4.2** **Integration Algorithms** **iii SPICE,** Accuracy, and **Options**


This section describes the implementation in SPICE of the integration algorithms introduced in the previous section and the options available to the user to improve the
accuracy of a solution.
As mentioned above, most SPICE programs support two integration algorithms,
second-order trapezoidal and Gear order 2 to 6. The default method is trapezoidal, but
a user can select the Gear algorithm with the optiOhsMETHODand MAXORD.The choices
for **METHOD** **are** **TRAP** or GEAR,and for **MAXORD** a number between 2 and 6 is required.
SPICE implements the Gear algorithm as a variable-order, multistep method. **MAXORD**
limits the order of the integration formula used for the variable-order Gear method and
is therefore relevant only when METHOD=GEAR.


f,


_EXAMPLE_ 9.4


Change the SPICE2 default integration method to Gear and limit the order of the integration formula'to 3. '


_**Solution**_ _**.'**_
This can,be achieved by adding the following **.OPTIONS** line to {he SPICE circuit
description:


.OPTIONS METHOD=GEAR MAXORD=3


The variable-order algorithm in SPICE selects at each time point the order that allows
for the maximum time step. A higher-order method has a smaller LTE, as shown in the
previous section, enabling the variable time step algorithm in SPICE to select a larger
time step. However, caution must be exercjsed with higher orders because inaccuracy
is introduced in the computation of the LTE and of the resulting time step.


**308** 9 SPICE ALGORITHMS AND OPTIONS


The truncation-error-based time-step control algorithm is described next for trapezoidal integration. This algorithm is common to most SPICE programs. An upper bound
is calculated for the truncation error at each time point based on the computation of
charges or currents of capacitors and fluxes or voltages of inductors. This error is similar to the one defined for nonlinear equations (Eqs. 9.33 and 9.36) and consists of a
relative and an absolute error:


(9.59)


_X_ _n_ _+_ 1 in the above equation represents the current of capacitors or the voltage across
inductors; SPICE defines also a charge or flux error: . .


(9.60) .


the LTE at each time point is taken as the maximum of the two errors:


(9.61)


A new SPICE option, **CHGTOL,** is introduced for the absolute charge or flux error, _E_ _qa._
The exact SPICE implementation of the truncation errors is



Ex = _RELTOL._ max(lxn+ll, _Ixnl)_ + _ABSTOL_


Ex = _RELTOL._ max(lxn+ll, Ixnl, _CH.GTOL)/hn_



(9.62)


(9.63)



The default value for _CHGTOL_ is 10- [14] C.
Based on the upper bound _E_ for the LTE at each time point, the next time step,
_hn_ _+1,_ is given by the following inequality:



_6E_

_3x_
_n_ I
~~I~~ _[d]_ ~~_dt_~~ ~~_[3]_~~



(9.64)



which results from the definition of the LTE of the trapezoidal method for _Xn+l,_ Eq.
9.51.
It is important to get an accurate estimate of the third derivative of the charge,
_d_ _[3]_ _x/ dt_ _[3]_ _,_ in the above inequality. The high-order derivatives are approximated in SPICE


TIME-DOMAIN SOLUTION **309**


by divided differences using the following definition:


(9.65)


which sets the relation between the _kth_ derivative, _dkx/ dt_ _[k]_ _,_ and the divided difference
of order _k, DDk._ The recursive formula for divided differences is



_DDk_ = _DDk-l(tn+[)_ _- DDk-l(tn)_

_k_
_L_ _hn_ _+l-i_
i=1


_DD1_ is the numerical approximation of the derivative of _x_ between _t_ _n_ and _t_ _n_ _+_ I:



(9.66)



With these formulas for divided differences, the time step computation in SPICE, Eg.
9.64, becomes


(9.67)


A value for the maximum time step given by Eg. 9.67 is computed for every linear
or nonlinear charge- or flux-defined element in the circuit. Comparisons between the
exact LTE for the circuit in Figure 9.11, Eg. 9.50, and the one approximated by divided
differences have shown that the divided difference overestimates the LTE several times
(Nagel 1975). This observation has led to the conclusion that a larger time step can be
used than the one defined by Eg. 9.67. An option parameter has been introduced in
SPICE, **TRTOL,** which scales down the divided difference and therefore the LTE. With
the new factor the predicted time step becomes


_TRTOL.E_

(9.68)
max _12,€a_ _(_ _[DD]_ _[3]_ _)_


The default value of 7 for _TRTOL_ has proven to provide a good compromise between
accuracy and speed for a large number of circuits. .
The automatic time-step control algorithm in SPICE selects _hn_ _+_ 1 based on the minimum value resulted from evaluating Eg; 9.68 for all capaciWrs and inductors in the
circuit. The SPICE time-selection algorithm is outlined below.


**310** 9 SPICEALGORITHMS AND OPTIONS


_tn+!_ = _tn_ + _hn_
solve at _tn_ _+_ 1
if _iter J1um_ < _ITIA_
compute _hn_ _+l_ = _f(_ _LTE)_
if _(hn+l_ < 0.9, _hn)_ then
reject _tn+l_
_hn_ = _hn+!_
recompute at new _tn+!_
else
accept _tn+l_
_hn_ _+l_ = min(h n+I,2. _hn, TMAX)_
proceed with _tn+2_
else
reject _tn+l_
_hn_ = _hn/8_
reduce integration order to I (BE)
if _(hn_                 - _h min)_ then
recompute at new _tn+!_
else
TIME STEP TOO SMALL;abort


Assume that the solution at _tn_ has been accepted and _hn_ has been selected as the
new time step. After removing the time dependency at _tn_ _+_ 1 using transformations of
the type given by Eq. 9.53, the set of nonlinear equations is solved as described in Sec.
9.3.
First, the program checks whether the nonlinear solution has converged in less than
_ITIA_ iterations, where **ITL4** is an option parameter defaulting to 10. If a solution could
not be obtained in _ITIA_ iterations, a new value is defined for _hn_ that is l of the previous
value. If this value for the time step is larger than the minimum acceptable time step,
_hmin,_ which is approximately eight orders of magnitude smaller than the print step,
_TSTEP_ (see Chap. 6), a new _tn+!_ is defined,


_`h`_ _n_
new _tn_ _+_ 1 = _tn_ + 8


and the solution is repeated. The solution at the newly defined _tn_ _+_ 1 is performed with
the first-order BE method. The method is changed back to the second-order TR only if
the new _tn+_ 1 is accepted. If the new _hn_ is not larger than _hmin,_ SPICE aborts the analysis and issues the message *ERROR*: INTERNAL TIMESTEP TOO SMALL IN
TRANSIENT ANALYSIS followed by the value of _t_ _n_ and _hn._
If the solution at _tn+l_ is obtained in less than _ITL4_ iterations, _hn+l_ is computed
based on the prescribed LTE, Eg. 9.51. The value of _h_ _n_ _+l_ is accepted if it is at least
_0.9hn_ which implies that the LTE is within bounds; if larger than _hn, hn+l_ is allowed
only to double at each time point. Also, the time step can only increase up to the lesser


TIME-DOMAIN SOLUTION **311**


of2. _TSTEP_ or _TMAX._ If _hn_ _+1_ evaluated according to Eq. 9.51 is less than _0.9hn,_ the
solution at _tn_ _+_ 1 is rejected and the smaller value obtained for the time step is assigned
to _hn,_ which defines in tum the new _tn+l._
There are a few additional details in the integration implementation that a knowledgeable user should be aware of.
First, there are certain time points, called _breakpoints,_ that are treated differently.
The time-step control algorithm is based on an estimate of the LTE, which in tum is
a function of the divided difference approximation of the derivative of a voltage or
current waveform. The approximation of the truncation error is therefore based on an
often untrue assumption that _x(t)_ is continuously differentiable to order _k_ in the time
interval of interest. Large inaccuracies are avoided by introducing the concept of a
_breakpoint,_ which is a time point where an abrupt change in the waveform is anticipated based on the shape of independent source signals. At a breakpoint a solution
of the circuit differential equations is enforced and a first-order method, the backward
Euler method, is used to solve for the time point immediately following the breakpoint.
The method applied at the first time point following a breakpoint is known as a _start-_
_up method._ The LTE of the first-order method is used at the new time point to minimize the error of the approximation. Breakpoints are important for an accurate solution because they prevent the evaluation of the LTE based on time points preceding the
discontinuity.
A second accuracy-enhancing technique is the prediction of the circuit-variable
values for a new time point. In the first iteration of a new time point SPICE employs a
linear prediction step for the voltages and charges of nonlinear branches.
A third implementation detail is the _bypass_ option. At every new time point after
the first iteration the nonlinear branch voltages, such as _VBE_ and _VBe_ of a BIT, and the
resulting nonlinear function, such as _Ie,_ are compared to the corresponding values at
the previous time point. If they have not changed more than the tolerance errors EV and

Ej (Eqs. 9.37 and 9.38), the computation of the linear equivalent is bypassed and the
conductance values from the last time point are used. Bypassing the reevaluation of
certain devices can result in 20% savings in analysis time, but it also can cause convergence problems for slowly moving variables that are within the prescribed tolerances
compared to the last time point but may differ more than the error tolerance if compared
to _k_ time points previously.
In SPICE2 and PSpice the only way to reduce bypassing is to tighten the relative
error, RELTOL. This must be done carefully since it can have the adverse effect of
nonconvergence depending on the nonlinear equations. SPICE3 provides an option at
compile time that prohibits bypass.
In SPICE2 and other commercial SPICE programs there is an alternate time-step
controlling mechanism, based on the Newton-Raphson iteration count used at each time
point. The time-step selection algorithm is defined by the **LVLTIM** option. The default
value is 2, which represents the LTE-based algorithm; if _LVLTIM_ = 1, the iterationcount time-step algorithm is used, which doubles the time step for any time point where
a solution is obtained in less than _ITL3_ iterations and reduces the time step by 8 when
more than _ITL4_ iterations are required. The iteration time-step control proves more


312 9 SPICEALGORITHMS AND OPTIONS


conservative but more foolproof for cases when no charge storage parameters are specified in the model definition of a nonlinear device or when the default error bounds are
not suitable. This time-step control algorithm is not available in SPICE3 or PSpice.
So far the time-step control mechanism has been presented only for the TR method.
As mentioned previously, the Gear algorithms order 2 to 6 are also implemented in
SPICE. The time-step is also controlled by the LTE in the same manner as described
above. An additional feature for the Gear method is that the order of the method can
also be modified dynamically. The order leading to the largest time step within the prescribed LTE is chosen. The highest order of the Gear method to be used is limited by
_MAXORD_ and the number of previous time points available since the last breakpoint.
The time step following a time point where the method of order _k_ has been used is evaluated for orders _k -_ 1, _k,_ and _k_ + 1. If the value of _h_ _n_ _+_ 1 for higher or lower order method
is 1.05 times larger than the value obtained for the current order, an order change is
performed. Nagel (1975) has found that for a set of benchmarks using the default tolerances, the Gear algorithm used order 2 most of the time. Only for tolerances reduced
by 2 to 3 orders of magnitude are the higher-order Gear algorithms being exercised.
The problem with the fifth- and sixth-order Gear algorithms is that the divided difference introduces a sizable error. In general it has been found that most problems where
Gear is beneficial, such as where there is numerical ringing or convergence problems, a
_MAXORD_ of 2 or 3 is sufficient. Although use of the Gear method can result in a reduction of computed time points and iterations, the savings in execution time over the TR
method is small, if there is any, because of the overhead of computing the coefficients
of the method at each time step (Nagel 1975).


9.5 SUMMARY OF OPTIONS


The various options available to a user for controlling solution algorithms and tolerances
have been introduced throughout this chapter. Although options differ among SPICE
versions, the majority of the options introduced in this text can be found in most versions. This section summarizes the •OPTIONS parameters by function. This summary
covers most common SPICE options; for a complete list of options available in a specific
SPICE version the reader is advised to consult the corresponding user's guide.


9.5.1 Analysis Summary


Before reviewing the analysis options it is instructive to introduce a SPICE option that
provides insight into the analysis: the accounting option, ACCT. A sample output of the
information printed by the ACCT request in SPICE2 is shown in Figure 9.17; the information is for the slew-rate transient analysis of the complete _/LA_ 741 circuit, whose
SPICE input is listed in Figure 7.28 and whose schematic is shown in Figure 7.29.
The list starts with circuit statistics; NUNODS is the number of nodes defined at the top


**SUMMARY OF OPTIONS** **313**

```
******* 03/23/92 ******** SPICE 2G.6 3/15/83 ******** 17:55:34 *****

UA741 FULL-MODEL SLEW RATE

```

`****` `JOB STATISTICS SUMMARY` `TEMPERATURE` = `27.000 DEG C`

```
***********************************************************************

NUNODS NCNODS NUMNOD NUMEL DIODES BJTS JFETS MFETS
   6 27 79 42 0 26 0 0

NUMTEM ICVFLG JTRFLG JACFLG INOISE IDIST NOGO
   1 0 201 0 0 0 0

NSTOP NTTBR NTTAR IFILL IOPS PERSPA
  82. 370. 472. 102. 1059. 92.980

NUMTTP NUMRTP NUMNIT MAXMEM MEMUSE COPYKNT
  284. 56. 1231. 400000 15484 41543.

    READIN 0.60
    SETUP 0.15
```

`TRCURV` `0.00` O.
```
    DCAN 3.68 84.
    DCDCMP 9.783 3.
    DCSOL 4.283
```

`ACAN` `0.00` O.
```
    TRANAN 51.53 1231.
    OUTPUT 0.45
    LOAD 35.067
```

`CODGEN` `0.000` O.
```
    CODEXC 0.000
    MACINS 0.000
    OVERHEAD 0.02
    TOTAL JOB TIME 56.43

```

**Figure 9.17** **SPICE statistics for the JLA741slew-rate analysis in Sec. 7.5.**


**level of the circuit,** NCNODS **is the number of the actual circuit nodes resulting after**
**expansion of subcircuits, and** NUMNOD **is the number of nodes after adding the internal**
**nodes generated because of the parasitic series resistances of semiconductor devices.**
**These numbers are followed by** NUMEL, **the total number of elements, which is broken**
**down into the different types of semiconductor devices. These numbers can be verified**
**from the data in Chap. 7.**
**The second set of data summarizes the analyses requested.** NUMTEM **is the number**
**of temperatures,** I CVFLG **is the requested points in a DC transfer curve,** JTRFLG **is**


**314** 9 SPICEALGORITHMS AND OPTIONS


the number of transient print/plot points, JACFLG is the number of frequency points
in the AC analysis, and INOISE and IDIST indicate whether a small-signal noise
or distortion analysis has been performed. Last in the analysis category is the variable
NOGO, which is 0, or FALSE, if the analysis has finished, and I, or TRUE, if the analysis
has been aborted because of an error.
The third set of data contains the linear system matrix statistics. NSTOP is the number of MNA equations, NTTBR is the total number of nonzero terms before reordering,
NTTAR is the total number of nonzero terms after reordering, IFILL is the number of
fill-ins created during the LU decomposition process and is equal to NTTAR-NTTBR,
lOPS is the number of floating-point multiplications and divisions required for each
solution of the linear system, and PERS PA is the sparsity of the MNA matrix expressed
as a percentage.
The fourth set summarizes information about the transient solution and memory
use. NUMTTP is the number of time points at which the circuit has been solved, NUMRTP
is the number of rejected time points, where the time step _hn_ _+_ 1 had to be rejected and
the analysis restarted at _tn,_ and NUMNIT is the total number of iterations performed
for the transient analysis. MAXMEMis the amount of memory available, MEMUSE is the
memory used by the present circuit, and CPYKNT is the number of memory transfers.
The last part of the summary lists the times in seconds for the different analyses and
solutions and the number of iterations. None of the above information has any bearing
on the actual solution, but it may be of interest to users who want to relate the knowledge
about algorithms acquired in this chapter to a specific circuit as well as to learn about
the ease or difficulty of convergence and time-domain solution. Note that the outputs
produced by different SPICE versions for this option vary but relate some of the same
statistics.


**9.5.2** **Linear Equation Options**


The following options are related to the linear equation solution:


_GMIN=value_ defines the minimum conductance connected in parallel to a pn junction; the default is 10- [12] mho.

_PIVTOL=value_ (SPICE2 and SPICE3) sets the smallest MNA matrix entry that can
be accepted as a pivot. If no entry is larger than _value_ at any LU decomposition
step, the circuit matrix is declared singular. The default is 10- [13] .

_PIVREL=value_ (SPICE2 and SPICE3) represents the ratio between the smallest
acceptable pivot and the maximum entry in the respective column; a larger value
for this option can lead to a better-conditioned matrix at the expense of more fillins. The default is 10- [3] .


These options should not be modified unless convergence failure is caused by singular matrix problems. Only increasing GMIN can lead in some cases to better convergence.


SUMMARY OF OPTIONS **315**


**9.5.3** **Nonlinear SolutionOptions**


The options that control the Newton-Raphson solution can be grouped as convergence
tolerances and iteration count limits.
The convergence tolerances are the following:


_RELTOL=value_ defines the relative error tolerance within which voltages and device currents are required to converge as set forth by Eqs. 9.33 and 9.36. The
default is 10- [3] . This option can have direct impact on convergence, time-step
control, and bypass.

_ABSTOL=value_ represents the absolute current tolerance as defined by Eq. 9.36.
The smallest current that can be monitored is equal to _value,_ which defaults to
10- [12] A.


_VNTOL=value_ is the absolute voltage tolerance defined by Eq. 9.33. It represents
the smallest observable voltage and defaults to 10- [6] V.


A few options control the number of iterations allowed in the nonlinear equation
solution. These options are the following:


_lTL1=value_ sets the maximum number of iterations used for the DC solution; this
is also the number of iterations used for a first solution in the time-domain when
**UlC** is present on the . **TRAN** line. The default is 100. A higher _value_ may lead
to a solution.

_lTL2=value_ sets the number of iterations allowed for any new source value in a

**. DC** transfer curve analysis. The default is 50. In PSpice _value_ is also used as
the maximum number of iterations at each source value during source ramping.
_lTL3=value_ is meaningful only in SPICE2, in connection with the LVLTIM=l
option where it defines the lower iteration limit at a time point; the time step is
doubled when the circuit converges in fewer iterations.
_lTL4=value_ sets an upper limit to the number of iterations performed at a time
point before it is rejected and the time step reduced by 8; the default is 10.
_lTL5=value_ is the total number of iterations allowed in a transient analysis; it defaults to 5000. This option is a protection against very long simulations and can
be turned off by setting _value_ to zero.

_lTL6=value_ (SPICE2 and SPICE3) represents both a flag for source ramping in
a DC solution and the maximum number of iterations allowed for each stepped
value of the supplies.


**9.5.4** **Numerical Integration**


The options for the time-domain solution can set integration methods as well as tolerances specific to this analysis.


**316** 9 SPICE ALGORITHMS AND OPTIONS


A user can select from two integration methods, several integration formula orders,
and two time-step control mechanisms as follows:


**METHOD=TRAP** /GEAR (SPICE2 and SPICE3) selects the numerical integration
formula; the default is the second-order trapezoidal method, **TRAP,** as defined
by Eq. 9.47.


_MAXORD=value_ (SPICE2 and SPICE3) sets the maximum order of the Gear method
when selected by the **METHOD** option; the default is 2. SPICE implements a
variable-order Gear integration formula contained in Appendix D.


_LVLTIM=value_ (SPICE2) selects whether the time-step is controlled by the local
truncation error, LTE, of the method _(value_ = 2) or by the iteration count needed
at each time point for convergence _(value_ = 1). The default value is 2.


The tolerances that can be modified in the transient analysis are the following:


_TRTOL=value_ is a scale factor for LTE as defined in Eq. 9.67; it defaults to 7.

_CHGTOL=value_ is the absolute charge tolerance at any time point according to Eq.
9.62; it defaults to 10- [14] e.


**9.5.5** **Miscellaneous Options**


A number of options in SPICE control the analysis environment, the analysis time,
global device properties, and which information is output.
The following option modifies the analysis environment:


_TNOM=value_ sets the reference temperature at which all device parameters are assumed to be measured; the default is 27°e. Note that this option effects the analysis results at temperatures specified in the . **TEMP** statement; see Sec. 4.1.3. **In**
SPICE3 the analysis temperature is also an option, _TEMP=value,_ rather than a
command line as in SPICE2 and PSpice.


The information and its format saved by SPICE in the output file is controlled by
the following options:


**LIST** generates a comprehensive summary of all elements in the circuit with connectivity and values; the default is **NOLIST.**


**NOMOD** suppresses the listing of device model parameters; by default the model
parameters are printed.


**NOPAGE** suppresses new pages for different analyses and header printing.


**NODE** requests the output of a node table, which lists the elements connected at
every node; the default is **NONODE.**


**OPTS** causes a complete list of all options parameter settings.


REFERENCES 317


_NUMDGT=value_ selects the number of digits to be printed after the decimal point
for results; _value_ is an integer number between 0 and 8 and defaults to 4. Note
that this option does not affect the computation of the results but only how many
digits are printed. More than 4 digits may be meaningless unless RELTOL is
reduced.

LIMPTS=value sets the number of points to be saved for a . PRINT or a . PLOT.
_value_ must be larger than the number of data points resulting from the analysis;
it defaults to 201.


Global geometric dimensions can be defined for MOSFETs as option parameters:


_DEFW=value_ sets the global, or default, device channel width, _W;_ the SPICE builtin default is 1 meter. The channel width, W, on the device line (see Chap. 3)
overrides the _DEFW_ value.

_DEFL=value_ sets the global, or default, device channel length, _L;_ the SPICE builtin default is 1 meter. The channel length, L, on the device line (see Chap. 3)
overrides the _DEFL_ value.

_DEFAD=value_ sets the global, or default, drain area, _AD;_ the SPICE built-in default
is 1m [2]    - The drain area, AD, on the device line (see Chap. 3) overrides the _DEFAD_
value.

_DEFAS=value_ sets the global, or default, source area, _AS;_ the SPICE built-in default
is 1 m [2] . The source area, AS, on the device line (see Chap. 3) overrides the
_DEFAS_ value.


PSpice and specific implementations of SPICE2 allow the user to limit the analysis
time through the following options parameter:


_CPTIME=value_ sets the maximum CPU time for the analysis.


There is an additional command belonging in the options category that controls the
line length in the SPICE2 output file:


•WIDTH _OUT=value_


where _value_ equals the number of characters per line. By default the SPICE2 output
line is 120 characters long.


**REFERENCES**


Boyle, G. R. 1978. Personal communication.
Calahan, D. A. 1972. _Computer-Aided Network Design._ New York: McGraw-Hill.
Chua, L. 0., and P. M Lin. 1975. _Computer-Aided Analysis of Electronic Circuits: Algorithms_
_and Computational Techniques._ Englewood Cliffs, NJ: Prentice Hall.
Cohen, E. 1981. Performance limits of integrated circuit simulation on a dedicated minicomputer
system. Univ. of California, Berkeley, ERL Memo UCBIERL M81/29 (May).


**318** 9 SPICEALGORITHMS AND OPTIONS


Dorf, R. C. 1989. _Introduction to Electric Circuits._ New York: John Wiley & Sons.
Forsythe, G. E., and C. B. Moler. 1967. _Computer Solution of Linear Algebraic Systems._ Englewood Cliffs, NJ: Prentice Hall.
Freret, J. P. 1976. _Minicomputer Calculation of the_ DC _Operating Point of Bipolar Circuits._
Technical Report No. 5015-1, Stanford Electronics Labs., Stanford Univ., Stanford, CA.
(May).
Gear, C. W. 1967. Numerical integration of stiff ordinary equations. Report 221, Dept. of Computer Science, Univ. of Illinois, Urbana.
Hachtel, G., and A. L. Sangiovanni- Vincentelli. 1981. A survey of third-generation simulation
techniques. _IEEE Proceedings_ 69 (October).
Hajj, I. N., P. Yang, and T. N. Trick. 1981. Avoiding zero pivots in the modified nodal approach.
_IEEE Transactions on Circuits and Systems_ CAS-28 (April): 271-278.
Ho, C. w., A. E. Ruehli, and P. A. Brennan. 1975. The modified nodal approach to network
analysis. _IEEE Transactions on Circuits and Systems_ CAS-22 (June): 504-509.
McCalla, W. J. 1988. _Fundamentals of Computer-Aided Circuit Simulation._ Boston: Kluwer
Academic.
McCalla, W. J., and D. O. Pederson. 1971. Elements of computer-aided circuit analysis. _IEEE_
_Transactions on Circuit Theory_ CT-18 (January).
Nagel, L. W. 1975. SPICE2: A computer program to simulate semiconductor circuits. Univ. of
California, Berkeley, ERL Memo ERL M520 (May).
Nagel, L. W., and R. Rohrer. 1971. Computer analysis of nonlinear circuits, excluding radiation
(CANCER). _IEEE Journal of Solid-State Circuits_ SC-6 (August): 166-182.
Nilsson, J. W. 1990. _Electric Circuits._ 3d ed. Reading, MA: Addison-Wesley.
Ortega, J. M., and W.R. Rheinholdt. 1970. _Iterative Solution of Non-Linear Equations in Several_
_Variables._ New York: Academic Press.
Paul, C. R. 1989. _Analysis of Linear Circuits._ New York: McGraw-Hill.
Vladimirescu, A. 1978."Sparse Matrix Solution with Pivoting in SPICE2," EECS 290H project,
Univ. of California, Berkeley.


_**Ten**_


_**CONVERGENCE ADVICE**_


**10.1** **INTRODUCTION**


Generally, SPICE finds a solution to most circuit problems. However, because of the
nonlinearity of the circuit equations and a few imperfections in the analytical device
models a solution is not always guaranteed when the circuit and its specification are
otherwise correct.
**In** the majority of the cases when a solution failure occurs it is due to a circuit
problem, either its specification or its inoperability. A convergence problem can be
categorized as either failure to compute a DC operating point or abortion of the transient
analysis because of the reduction of the time step below a certain limit without finding
a solution. The two most common messages that SPICE2 prints when it fails to find a
solution are


*ERROR*: NO CONVERGENCE IN OC ANALYSIS


and


*ERROR*: INTERNAL TIME STEP TOO SMALL IN TRANSIENT ANALYSIS


This chapter describes the most common causes of convergence failure and the appropriate remedies.
From the perspective of the previous chapter, failure to find a solution can occur
at the level of the linear equation, the Newton-Raphson iteration, or the numerical
integration. Rather than present the convergence issues based on the algorithm causing


**319**


**320** 10 CONVERGENCE ADVICE


the problem, it has been deemed beneficial to describe the causes for failure from a
user's perspective. Section 10.2 contains the most common remedies for SPICE solution failure.
Specific procedures can be followed when SPICE fails to find a DC solution of the
circuit. The prescribed remedies include redefinition of analysis options, use of built-in
convergence-enhancing algorithms, and DC operating point solution with a different
analysis. These approaches are presented and exemplified in Sec. 10.3.
Time-domain analysis can provide an inaccurate solution or fail because of a number of reasons related either to the integration method and associated time-step control
or the iterative solution of nonlinear equations. Section 10.4 describes some of the problems and several approaches that can lead to a solution in these cases.
Knowledge of the specifics of different types of electronic circuits can assist the
user in finding an accurate solution by specifying appropriate analysis modes, options,
tolerances, and suitable model parameters. Thus, oscillators require certain initializations not necessary for amplifiers, and bipolar circuits may need different convergence
tolerances than do MOS circuits. An overview of circuit-specific analyses and issues is
provided in Sec. 10.5.
All convergence issues described in this chapter are illustrated by small circuits
that can be easily understood by a new user. Although convergence failure is more
common for large circuits, the problems and their remedies are the same as for the
smaller circuits described in this chapter.
Note that the convergence problems described are specific to the simulators mentioned in the text. Because of differences between SPICE simulators, the problems presented below can be duplicated only in the specified simulator. Sometimes the same
simulator can succeed or fail to converge depending on the platform; different computers may use different floating-point representations and different mathematical libraries
of elementary functions. The results presented in this chapter are obtained from SPICE2
and SPICE3 running on SUN workstations and PSpice running on 386/486 PCs.


**10.2** **COMMON** **CAUSESOF SOLUTION FAILURE**


**10.2.1** **Circuit Description**


The first thing a user should do after a convergence error occurs is to check the circuit
description carefully; the SPICE input should be compared to the schematic for correct
connectivity. Additional SPICE information can be helpful for this verification. A list
of every node and the elements connected to it can be obtained by adding the **NODE**
option to the input description:


•OPTIONS NODE


The user should specifically look for and identify nodes that are floating or undefined
in DC.


COMMON CAUSES OF SOLUTION FAILURE **321**


SPICE checks every circuit for topological and component value correctness. Common error messages related to circuit topology are

```
  *ERROR*: LESS THAN 2 CONNECTIONS AT NODEnumber
  *ERROR*: NO DC PATH TO GROUND FROM NODEnu~ber
  *ERROR*: INDUCTOR/VOLTAGE SOURCE LOOP FOUND, CONTAINING
   Vname

```

The first message identifies any node that has only one terminal of one element connected to it. The second message points to the nodes that are floating in DC and cannot
be solved. Most often such nodes are connected to ground through capacitors, which
are open circuits in DC. The third error message records a violation of Kirchhoff's voltage law. As described in the previous chapter, inductors are equivalent to zero-valued
voltage sources in DC analysis and therefore cannot form a mesh or loop with voltage
sources or other inductors.
Although SPICE identifies and reports most topology errors, some evade the
scrutiny. One such example is the gate terminals of MOSFETs which need to be connected properly for DC biasing. The gate terminal of a MOSFET, unlike the base of a
BJT, has no DC connection to the other terminals of the device (Grove 1967), drain,
source, or bulk, and therefore must be properly biased outside the device. The following
example illustrates an analysis failure due to the improper connection of a MOSFET
which goes undetected by SPICE.


_**EXAMPLE 10.1**_


Find the time response of the circuit shown in Figure 10.1 to the input signals _VA_ and
_VB;_ defined in the SPICE deck listed in Figure 10.2.


C 1
_r&_
_-=-V1_


**Figure 10.1** Floating-gate MOS
circuit.


**322** **10** **CONVERGENCE ADVICE**

```
       *******01/16/92 ******** SPICE 2G.6 3/15/83********11:48:25*****

       FLOATING GATE OF MOSFET ERROR

```

******** `INPUT` `LISTING` `TEMPERATURE` `=` `27.000` `DEG` `C`

```
       ***********************************************************************
```

        ```
       M1 2 1 0 0 NMOS L=100U W=100U
       C1 4 1 lOP IC=O
       VA 4 3 PULSE 0 5 70U 2N 2N lOU 100U
       VB 3 0 PULSE 0 5 lOU 20U 20U lOU 100U
       V1 2 0 6
```

       ```
       .MODEL NMOS NMOS VTO=1.3
```

       ```
       .TRAN 1U 100U 0
       .PRINT TRAN I(V1) I (VA) I(VB)
       .OPTIONS NODE
       .WIDTH OUT=80
       .END
       *******01/16/92 ******** SPICE 2G.6 3/15/83********11:48:25*****

       FLOATING GATE OF MOSFET ERROR

```

******** `ELEMENT` `NODE` `TABLE` `TEMPERATURE` `=` `27.000` `DEG` `C`

```
       ***********************************************************************

```



     - VB
```
    1 C1
    2 V1
    3 VA
```

4 C1
```
*******01/16/92

```

```
   V1 M1
   M1
   M1
```

VB
```
   VA
******** SPICE 2G.6

```

```
M1

 3/15/83 ********11:48:25*****

```

```
FLOATING GATE OF MOSFET ERROR

**** MOSFET MODEL PARAMETERS TEMPERATURE = 27.000 DEG C

***********************************************************************

```

```
TYPE
LEVEL
VTO
KP

```

```
  NMOS
 NMOS
  1.000
  1.300
2.00D-05

```

```
*ERROR*: MAXIMUM ENTRY IN THIS COLUMN AT STEP 2(0.000000D+00)IS LESS THAN PIVTOL
*ERROR*: NO CONVERGENCE IN DC ANALYSIS
LAST NODE VOLTAGES:

```

```
NODE

```

( 1)


```
VOLTAGE NODE

 0.0000 (2)

```

```
VOLTAGE NODE

 0.0000 (3)

```

```
VOLTAGE

 0.0000

```

```
NODE

```

( 5)


```
VOLTAGE

 0.0000

```

```
      ***** JOB ABORTED

```

**Figure 10.2** **SPICE2 input and output with node table for circuit in Figure 10.1.**


COMMON CAUSES OF SOLUTION FAILURE 323


_Solution_
The SPICE2 output, including the input circuit, is shown in Figure 10.2. The initial
transient solution, that is, the DC analysis, fails with


`*ERROR*:` `NO` `CONVERGENCE` `IN` IX: `ANALYSIS`


A closer look at the output file reveals that the circuit matrix is singular within the
SPICE tolerances; the following singular matrix message is printed by SPICE2:

```
*ERROR*: MAXIMUM ENTRY IN THIS COLUMN AT STEP 2 (D.DDDED) IS LESS THAN
   PIVI'OL

```

The submatrix at the second elimination step is singular because the circuit is open
at node 1; the capacitor, which connects the signals _VA_ and _VB_ during the transient
response, leaves the gate terminal floating in DC. This problem goes undetected by the
SPICE topology checker, and it is up to the user to understand the problem.
If the singular matrix problem occurs but the value of the maximum element at a
certain elimination step is nonzero, the actual value is listed in parentheses in the error
message; _PIVTOL_ can then be lowered to a value less than the maximum entry and the
analysis rerun, as described in Example 10.2. The node table for this circuit, which is
printed by SPICE when the NODE option is set (see Figure 10.2), shows that only C]
and _M]_ are connected at node 1. Unfortunately, the information about which terminal
of _M]_ is connected at a given node is not provided.
There are several remedies once the cause of this type of failure is understood. If
only the time-domain response is of interest, the DC solution should be bypassed by
specifying the UIC keyword in the. THAN statement. Alternatively, if a DC solution is
needed, proper biasing should be provided to the gate. It is left as an exercise for the
reader to experiment with the suggested workarounds to find whether they result in the
completion of the analysis.


Another element that can cause singular matrix problems is a current source that
voluntarily or involuntarily is set to zero. The current source in this case is an open
circuit. It can be used to defeat the topology checker, as described in Examples 4.6 and
5.3, but care must be exercised.


_**EXAMPLE 10.2**_


The setup in Figure 10.3 can be used to measure the collector cutoff current, _ICBO,_ a
common data sheet parameter, by setting the emitter current supplied by the current


**324** 10 CONVERGENCE ADVICE


+


**Figure 10.3** Cut-off current measurement circuit.


source _Ie_ to zero and measuring _Ie_ of the transistor. This is equivalent to leaving the
emitter of QI open, which is not permitted in SPICE.


_**Solution**_
The input is listed in Figure lOA' together with the SPICE analysis results for _Ie_ = O.
The same message of a singular matrix is printed as in Example 10.1 but the maximum
entry is a finite number, 5.77 X 10- [14] . This problem can be overcome by lowering the
value of _PIVTOL;_ see also Sec. 9.2.
The cause for this error is that the circuit equations that SPICE solves constitute
an underdetermined system and the emitter voltage, _VE_ = _VI,_ can be set to any value.
Although PSpice finds a solution without flagging a singular matrix, the problem remains that random numbers are generated during the solution process for _VE'_ Note that
for _Ie_ =? 0 SPICE might not find a solution because of the erroneous circuit setup: QI
cannot conduct the driving current.
**In** the case of correctly defined circuits, lowering _PIVTOL_ below the value of the
maximum entry can cure the problem when a singular matrix is encountered. The following       - **OPTIONS** line added to the circuit description in Figure lOA,

```
      .OPTIONS PIVTOL=lE-14

```

causes SPICE2 to finish the analysis. Lowering of _PIVTOL_ allows SPICE to accept
smaller values as pivots in the linear equation solution. The default is _PIVT_ 0 _L_ = 10- [13]       

**COMMON** **CAUSES OF SOLUTION** **FAILURE** **325**

```
*******01/16/92 ******** SPICE 2G.6 3/15/83********11:41:02*****

COLLECTOR CUT-OFF CURRENT MEASUREMENT CIRCUIT

**** INPUT LISTING TEMPERATURE = 27.000 DEG C

***********************************************************************
```

```
Q1 3 0 1 M2N2501 AREA=l
.MODEL M2N2501 NPN
+ BF=166. 9 NR=1. 038 MJE=O. 3 VAF=49. 25
+ VAR=10 CJE=5.9P RE=741.8M VJC=800M NC=1.526
+ VJE=757.1M NE=1.38 IKR=2.294 NF=1 BR=744.4M CJC=3.5P RC=696.7M
+ TF=610 52P VTF=1.188K TR=29. 31N XTF=100 ITF=317. 8M PTF=O
+ CJS=O MJS=O VJS=750M XCJC=l XTB=l. 5 IS=6. 534F
+ IRB=100U RB=O RBM=O XTI=3 ISC=100P EG=l.ll ISE=23.42F
+ IKF=113.8M MJC=0.2 AF=1 KF=O FC=0.5
```

V+ 2 0 15
```
VC 2 3 0.0
IE 0 1 0
```

```
*.OPTION PIVTOL=1.0E-14
```

```
.OPT ACCT
.WIDTH OUT=80
.OP
```

. END

```
PIVOT CHANGE ON FLY: N= 7 NXTI= 7 NXTJ= 7 ITERNO= 23 TIME= O.OOOOOD+OO
*ERROR*: MAXIMUM ENTRY IN THIS COLUMN AT STEP 8 (5.773160D-14) IS LESS THAN PIVTOL
*ERROR*: NO CONVERGENCE IN DC ANALYSIS
LAST NODE VOLTAGES:

NODE VOLTAGE NODE VOLTAGE NODE VOLTAGE

```

( 1) `0.1474` `(2)` `15.0000` `(3)` `15.0000`

```
      ***** JOB ABORTED

```

**Figure 10.4** **SPICE2 inputandoutputfor circuit in Figure** **10.3.**


**The conclusion** **of this example is that a singular matrix message** **can be caused**
**by an error in the circuit specification** **and that if the circuit is correct and no floating**
**nodes are found, lowering** _**PIVTOL**_ **below the smallest matrix entry indicated in the**
**error message enables SPICE to compute the solution.**


**326** 10 CONVERGENCE ADVICE


_GMIN_


B


_GMIN_



c



D


```
G-----1

```


_GMIN_


_GMIN_



B



E S
**Figure 10.5** _GMIN_ conductance across pnjunctions for BJT and MOSFET.


A high-impedance node can result in the same failure mode as above, because
numerically it can become an open circuit, similar to the gate node of transistor _M1_ in
Example 10.1. As protection against this problem the internal SPICE models of the pn
junctions in diodes, BJTs, MOSFETs, and JFETs have a very small conductance, **GMIN,**
connected in parallel, which can be set as an option. _GMIN_ prevents the occurrence of
floating nodes in a transistor circuit. The schematics for the BJT and the MOSFET
including _GMIN_ are shown in Figure 105 Large resistances, smaller than _l/GMIN,_
can be added to high-impedance nodes if they do not disturb the operation; an alternate
way is to use the • **NODESET** command to initialize the voltages at these nodes.


**10.2.2** **Component Values**


In the case of an analysis failure or erroneous results, after the topology has been verified, the component values and model parameters should be double-checked. The **LIST**
option can be introduced in the SPICE input to obtain a comprehensive summary of all
elements and their values. The semiconductor model parameters are printed by default
in the output file obtained from SPICE2 and PSpice. Ideal elements and unrealistic
component values and semiconductor device model parameters can lead to voltages
and currents that combined with transcendental equations generate numbers outside
the computer range. The simple example presented below leads to a solution failure or
erroneous result depending on which SPICE version is used.


_**EXAMPLE 10.3**_


Use SPICE to find the operating point and the time-domain response of the half-wave
diode rectifier shown in Figure 10.6.


COMMON CAUSES OF SOLUTION FAILURE 327


CD

_`D`_ _1_


+
V 1N 20V _ID ~_ _VD_


            -             Figure 10.6 Half-wave
dioderectifiercircuit.


_Solution_
An uninformed user may try to simulate this circuit with the default diode model parameters, that is, with an ideal diode according to the SPICE input listed in Figure 10.7.
The simulation fails because the absence of current limiting leads to numerical range
error in computing the value of


(10.1)


This number is greater than the largest value, 10 [308], that can be represented in double
precision. For smaller values of the voltage source _VIN_ SPICE may find a solution as
long as _ID_ is in the range of floating-point numbers. Some versions of SPICE, such as
older PSpice releases, limit the value of the exponent to 80 in the internal computation
which combined with automatic source ramping leads to a solution; this solution is
wrong, however, because the current is limited at


The error in this example is due to the lack of a parasitic resistance in the diode
model. In the absence of an external resistor the role of the diode parasitic series resistance is to provide current limiting in the half-wave rectifier circuit. In reality the


DIODE CIRCUIT WITHOUT CURRENT LIMITING

VIN 1 0 20

Dl 1 0 DMOD

.MODEL DMOD D
```
.OP
```

.WIDTH OUI'=80


 - END


Figure 10.7 SPICE descriptionof half-wavediode rectifier.


328 10 CONVERGENCE ADVICE


pn junction of the diode would melt if no proper current-limiting resistor is added in
the circuit. This error can also occur for JFETs and MOSFETs when improperly biased
because of the presence of an ideal pn junction between gate and drain or source or
between bulk and drain or source, respectively.


Other model parameters that can cause numerical problems for bipolar devices are
the emission coefficients, such as N for a diode, NF and NR for a BJT (see Chapter 3), as
well as Fe, which approximates the junction capacitance, _C],_ for a forward-biasedjunction. The value of C] increases toward infinity as the junction voltage _VD_ approaches
the built-in voltage VJ according to Eg. 3.3. In SPICE the characteristic described by
Eg. 3.3 is replaced for pn junctions in all semiconductor models with the tangent to the
curve at a junction voltage determined by _FC_ and the built-in voltage, _Vi:_


_V_ _x_ = _FC. Vi_ where 0:5 _FC_ < 1. (10.2)


The approximation is shown graphically in Figure 10.8. The default for _FC_ is 0.5; that
is, Eg. 3.3 is replaced by the tangent to the curve it describes when the junction voltage
reaches half the value of the built-in voltage.
For an accurate solution it is important to observe certain limits on the element
values. The maximum conductance cannot be more than 14 to 15 orders of magnitude
larger than the smallest conductance in order to satisfy the constraint set by the limited
accuracy of number representation in a computer (see Sec. 9.2.2). It was shown above
that the smallest conductance used by SPICE is _GM IN_ = 10- [12] . This constraint limits
the smallest resistance to 1 mD.. Power electronics is the one area where resistances


Simple theory,
Eq.3.3


SPICE


                              - _Fe._ _VJ_ _VJ_


Figure 10.8 Junction capacitance approximation in forward
bias.


COMMON CAUSES OF SOLUTION FAILURE **329**


smaller than 1 n need to be modeled, but the lower limit defined above should still be
observed.
The use of ideal switches also leads to extreme values for the ON and OFF resistances. As explained in Sec. 2.3.3, it is not necessary to set these two parameters, _RON_
and _ROFF,_ more than six orders of magnitude apart as long as they are virtual shorts
and open circuits by comparison with the other conductances in the circuit. The OFF
resistance need not be as large as _lIGMIN_
The same rules on the ratio between the largest and smallest values of a component must be observed also for capacitors and inductors. The value of "theequivalent
conductance for these elements is also a function of the integration time step, as explained in Sec. 9.4. For practical circuits the largest capacitances should not surpass
. 1 _JLF;_ the smallest values are dictated by semiconductor models and are of the order of
femtofarads (l0-15 F). .
Convergence is related not only to specific values of model parameters but also
to the complexity of the models. The presence of a parameter causes the inclusion of
a specific physical effect in the behavior of a semiconductor device, whereas the absence of the parameter eliminates modeling of the corresponding effect. For example,
the presence of _VAF_ in a _BIT_ model results in a finite output conductance of the transistor; similarly, a nonzero value for _LAMBDA_ in a FET model introduces a finite output
conductance in the saturation region. MOSFETs can be described by more complex and
accurate models than the Schichman-Hodges model presented in Chap. 3; these models
are accessed by the **LEVEL** parameter, which can go to 3 in SPICE2 (Vladimirescu and
Liu 1981), to 6 in SPICE3 (Sheu, Scharfetter, and Ko 1985), and to 4 in PSpice. The
higher-level models include such second-order effects as subthreshold current, velocitylimited saturation, and small-size effects.
As mentioned earlier, the equations implemented in various versions of SPICE are
not perfect. For a specific combination of arguments the function describing the conductances can become discontinuous. The simpler the model, the lower the chance for
such an occurrence. Therefore, when a very complex model is used for a device and
the simulation of the circuit fails, a selective omission of second-order effects, such
as base-resistance modulation, parameters **RBM** and **IRB,** in a _BIT_ (Appendix A) or
small-size effects in a MOSFET, can help convergence. This approach is exemplified
by the BiCMOS voltage reference circuit in the following section. Once a first solution is obtained, convergence with "theinitial, more complex model can be achieved by
initializing key nodes of the circuit.
Convergence problems also occur when the most elementary or ideal models are
used, as demonstrated by Example 10.3. In this situation the user is advised to add those
parameters that increase accuracy to the simulation, such as finite output conductance
and charge storage. Also, subthreshold conduction in a MOSFET can help convergence,
as described in Sec. 10.5.2.
Once all the above guidelines on circuit correctness and component values limits
have been observed and SPICE still does not converge, it is necessary to use initialization of critical nodes and adjust some options parameters. These two issues are exemplified in the following two sections, on convergence improvement in DC and transient
analysis.


**330** 10 CONVERGENCE ADVICE


**10.3** **DC CONVERGENCE**


This section describes several approaches that can be followed when a circuit that has
passed the scrutiny of the previous section fails to converge in DC analysis. Note that
various SPICE versions handle nonconvergence in different ways. Thus, among the
three versions used in this text, PSpice and the latest versions of SPICE3 automatically
run a built-in convergence-enhancing algorithm after failing to find a solution in the
first _ITLl_ iterations; SPICE2, however, aborts the run if no convergence is reached in
_ITLI_ iterations, and the user must specifically request the source-ramping convergence
algorithm by specifying the **ITL6** option.
The first step to be taken after a convergence failure is to rerun the circuit for more
than the default _ITLl_ iterations. _ITLl_ defaults to 100 in SPICE2 and SPICE3 and to
40 in PSpice. It is questionable whether it makes sense to use a higher _ITLl_ in PSpice,
which automatically ramps the supplies after _ITLl_ iterations and may find a solution
faster through this approach. It definitely makes sense in SPICE2, especially for large
circuits, which may need more than 100 iterations to converge.


_**EXAMPLE 10.4**_


Compute the operating point of the CMOS operational amplifier shown in Figure 10.9
using SPICE2. This circuit is extracted from the collection of circuits with convergence
problems in SPICE prepared by the Micro-electronics Center of North Carolina. The
following **LEVEL=2** model parameters should be used for the two types of MOS transistors:

```
        NMOS: VTO=O.71 GAMMA=0.29 TOX=225E-IO NSUB=3.5E16 U0=411 LAMBDA=0.02
           CGS0=2.89E-IO CGDO=2.89E-IO CJ=3.74E-4 MJ=0.4
        PMOS: VTO=-0.76 GAMMA=0.6 TOX=225E-IO NSUB=1.6E16 UO=139 LAMBDA=O.02
           XJ=O.2E-6 CGS0=3.35E-IO CGDO=3.35E-IO CJ=4.75E-4 MJ=O.4

```

_**Solution**_
The circuit is a conventional three-stage CMOS operational amplifier (Gray and Meyer
1985) in a closed-loop unity-gain feedback configuration.The function of the various
transistors is documented in the input file, listed in Figure 10.10. The analysis of this
circuit produces a DC convergence error in SPICE2. The iteration count is increased
by adding the line

```
      .OPTION ITL1=300

```

to the input file; the DC operating point is found by SPICE2 in 108 iterations, and the
results are as listed in Figure 10.11. This circuit does not converge in PSpice or SPICE3,
which use automatic ramping algorithms.


5V
G)



100n


_R_ _`F`_



~~
..•



**Figure 10.9** CMOS opamp circuit diagram.


**332** **10** **CONVERGENCE** _**ADVICE**_

```
    CMOS OPAMP
```

** `This opamp is a conventional 3-stage, internally compensated, CMOS opamp`

     - `from the MCNC SPICE test circuits; The simulation file is set up for closed`

     - `loop (unity-gain feedback) analysis of transient and ac performance.`
** `SUPPLY VOLTAGES`

     ```
    VDD 1 0 DC 5
    VAP 34 99 PULSE ( 0.0 0.5 0 lE-9 lE-9 50E-9 100E-9 )
    VIN 99 0 DC 2.5
```

     *, `ANALOG INPUT`

     
     
     - `BIAS CIRCUIT`

     ```
    M65 0 0 7 1 PCH W=4.5U L=40U
    M64 7 7 1 1 PCH W=71U L=10U
    M63 5 7 1 1 PCH W=69U L=10U.
    M62 5 5 9 0 NCH W=35U L=10U
    M61 9 9 0 0 NCH W=12U L=10U

```


** `DIFFERENTIAL AMPLIFIER STAGE`

```
MI0 36 33
M20 3 34
```

`M30 36 36` - `0 NCH W=6U`
`M40` `3 36` - `0 NCH W=6U`
```
M50 32 7
```



```
32 1 PCH W=11U L=2U AD=24P AS=24P
32 1 PCH W=11U L=2U AD=24P AS=24P
```

 - `0 NCH W=6U` `L=3U AD=136P AS=136P`

 - `0 NCH W=6U` `L=3U AD=136P AS=136P`
```
 1 1 PCH W=14U L=2U AD=24P AS=24P

```



- `FOLDED CASCODE STAGE WITH COMPENSATION`

```
M2 6 7 1 1 PCH W=80U L=2U AD=24P AS=24P
M3 6 5 4 0 NCH W=24U L=2U AD=136P AS=136P
M4 4 3 0 0 NCH W=46U L=2U AD=136P AS=136P
M80 11 5 3 0 NCH W=4U L=3U
CC 6 11 .22PF
```


 - `COMMON DRAIN OUTPUT STAGE`

 ```
M7 1 6 12 12 NCH W=100U L=2U AD=136P AS=136P
M8 12 9 0 0 NCH W=63U L=2U AD=136P AS=136P

```


**Figure 10.10** **SPICE input for CMOS opamp.**


```
* LOAD
CL 12 0 10PF
```

```
* FEEDBACK CONNECTION
RF 12 33 100
```

```
* MOSFET PROCESS MODELS
```

```
.MODEL NCR NMOS LEVEL=2 CGS0=2.89E-10 VTO=O.71 GAMMA=0.29
```
+ `CGDO=2.89E-10 CJ=3.74E-4 MJ=0.4 TOX=225E-10 NSUB=3.5E16`
+ `U0=411 LAMBDA=O. 02`

```
.MODEL PCR PMOS LEVEL=2 VTO=-0.76 GAMMA=0.6 CGS0=3.35E-10
+ CGDO=3.35E-10 CJ=4.75E-4 MJ=0.4 TOX=225E-10 NSUB=1.6E16
```

+ `XJ=0.2E-6 UO=139 LAMBDA=O.02`

```
* ANALYSES
```

```
.OP
.OPTIONS ACCT ITL1=300
.END

```

**Figure 10.10** _(continued)_


```
*******01/21/92 ******** SPICE 2G.6

CMOS OPAMP

```

```
3/15/83********15:44:54*****

```

```
**** SMALL SIGNAL BIAS SOLUTION TEMPERATURE = 27.000 DEG C

***********************************************************************

NODE VOLTAGE NODE VOLTAGE NODE VOLTAGE NODE VOLTAGE

( 1) 5.0000 3) 1.0208 4) 1.1081 5) 2.3756
( 6) 3.6144 7) 3.8663 9) 1.2190 11) 1.0208
(12) 2.5000 32) 3.7841 33) 2.5000 34) 2.5000
(36) 1.0207 99) 2.5000

  VOLTAGE SOURCE CURRENTS

  NAME CURRENT

  VDD -3.250D-04
  VAP O.OOODtOO
  VIN O.OOODtOO

  TOTAL POWER DISSIPATION 1.620-03 WATrS

```

**Figure 10.11** **CMOS opamp DC solution.**
**333**


~--

```
*******01/21/92 ******** SPICE 2G.6 3/15/83********15:44:54*****

CMOS OPAMP

```

`****` `OPERATING POINT INFORMATION` `TEMPERATURE` = `27.000 DEG C`

```
***********************************************************************

**** MOSFETS

       M65 M64 M63 M62 M61 M10 M20
MODEL PCH PCH PCH NCH NCH PCH PCH
ID -8.62E-06 -8.63E-06 -8.72E-06 8.72E-06 8.72E-06 -5.37E-06 -5.37E-06
VGS -3.866 -1.134 -1.134 1.157 1.219 -1.284 -1.284
VDS -3.866 -1.134 -2.624 1.157 1.219 -2.763 -2.763
VBS 1.134 0.000 0.000 -1.219 0.000 1.216 1.216
VTH -1.062 -0.750 -0.748 0.865 0.710 -0.965 -0.965
VDSAT -2.389 -0.292 -0.293 0.265 0.444 -0.271 -0.271
GM 6.21E-06 4.52E-05 4.55E-05 5.99E-05 3.44E-05 3.37E-05 3.37E-05
GDS 1.89E-07 2.36E-07 2.24E-07 1.79E-07 1.79E-07 2.92E-07 2.92E-07
GMB 1.08E-06 1.42E-05 1.42E-05 5.98E-06 5.07E-06 5.49E-06 5.49E-06
CBD O.OOE+OO O.OOE+OO O.OOE+OO O.OOE+OO O.OOE+OO 5.58E-15 5.58E-15
CBS O.OOE+OO O.OOE+OO O.OOE+OO O.OOE+OO O.OOE+OO 7.88E-15 7.88E-15
CGSOVL 1.51E-15 2.38E-14 2.31E-14 1.01E-14 3.47E-15 3.68E-15 3.68E-15
CGOOVL 1.51E-15 2.38E-14 2.31E-14 1.01E-14 3.47E-15 3.68E-15 3.68E-15
CGBOVL O.OOE+OO O.OOE+OO O.OOE+OO O.OOE+OO O.OOE+OO O.OOE+OO O.OOE+OO
CGS 1.84E-13 7.26E-13 7.06E-13 3.58E-13 1.23E-13 2.25E-14 2.25E-14
CGD O.OOE+OO O.OOE+OO O.OOE+OO O.OOE+OO O.OOE+OO O.OOE+OO O.OOE+OO
```

`CGB` `O.OOE+OO` `O.OOE+OO` `O.OOE+OO` `O.OOE+OO` `O.OOE+OO O.OOE+OO` - `.OOE+OO`


```
       M30 M40 M50 M2 M3 M4 M80
MODEL NCH NCH PCH PCH NCH NCH NCH
ID 5.37E-06 5.37E-06 -1.07E-05 -6.19E-05 6.19E-05 6.19E-05 -1.25E-12
VGS 1.021 1.021 -1.134 -1.134 1.267 1.021 1.355
VDS 1.021 1.021 -1.216 -1.386 2.506 1.108 0.000
VBS 0.000 0.000 0.000 0.000 -1.108 0.000 -1.021
VTH 0.710 0.710 -0.707 -0.706 0.854 0.710 0.844
VDSAT 0.269 0.269 -0.331 -0.332 0.376 0.269 0.463
GM 3.47E-05 3.47E-05 5.07E-05 2.92E-04 2.99E-04 4.00E-04 3.23E-12
GDS 1.10E-07 1.10E-07 5.48E-07 3.05E-06 1.30E-06 1.27E-06 4.29E-05
GMB 5.33E-06 5.33E-06 1.36E-05 7.80E-05 3.03E-05 6.14E-05 3.51E-13
CBD 3.66E-14 3.66E-14 7.88E-15 7.63E-15 2.57E-14 3.59E-14 O.OOE+OO
CBS 5.09E-14 5.09E-14 1.14E-14 1.14E-14 3.59E-14 5.09E-14 O.OOE+OO
CGSOVL 1.73E-15 1.73E-15 4.69E-15 2.68E-14 6.94E-15 1.33E-14 1.16E-15
CGOOVL 1.73E:"15 1.73E-15 4.69E-15 2.68E-14 6.94E-15 1.33E-14 1.16E-15
CGOOVL O.OOE+OO O.OOE+OO O.OOE+OO O.OOE+OO O.OOE+OO O.OOE+OO O.OOE+OO
CGS 1.84E-14 1.84E-14 2.86E-14 1.64E-13 4.91E-14 9.41E-14 5.15E-15
CGD O.OOE+OO O.OOE+OO O.OOE+OO O.OOE+OO O.OOE+OO O.OOE+OO 1.16E-14
CGB O.OOE+OO O.OOE+OO O.OOE+OO O.OOE+OO O.OOE+OO O.OOE+OO O.OOE+OO

```


**Figure 10.11** _**(continued)**_
**334**


DC CONVERGENCE **335**


```
 M8
NCH
2.35E-04
  1.219
  2.500
  0.000
  0.710
  0.444
9.28E-04
4.95E-06
1.37E-04
2 ..89E-14
5.09E-14
1.82E-14
1.82E-14
O.OOE+OO
1.29E-13
O.OOE+OO
O.OOE+OO

```

```
MODEL
ID
VGS
VDS
VBS
```

VTH
```
VDSAT
GM
GDS
```

8MB
```
CBD
CBS
CGSOVL
CGDOvL
CGBOvL
CGS
CGD
CGB

```

```
 M7
NCH
2.35E-04
  1.114
  2.500
  0.000
  0.710
  0.352
1.17E-03
4.95E-06
1.76E-04
2.89E-14
5.09E-14
2.89E-14
2.89E-14
O.OOE+OO
2.05E-13
O.OOE+OO
O.OOE+OO

```


**Figure 10.11 .** _(continued)_


The next step in overcoming a convergence error is to relax the two,key tolerances
_ABSTOl,-,_ the absolute'curr~nttolerance, which defaults to I pA, and _RELTOL,_ the
relative convergence tolerance, which defaults to 10- [3] . Especially for MOS circuits
the default _ABSTOL_ can be too small.
When the above options do not lead to a solution, the source-ramping mechanism
must be invoked in SPICE2, or some of the iteration options must be changed in PSpice
and SPICE3. If the ramping methods fail, it is recommended to use initialization either
by setting the values of key nodes with **.NODESET and. Ie** (see Sec. 4.6 and Sec. 6.3)
or by identifying cutoff devices with the **OFF** keyword (see Chap. 3).
Next an operational amplifier that fails DC convergence will be considered, and
the steps that lead to a solution will be outlined.


_**EXAMPLE 10.5**_


Find the DC bias point of the,uA74l operational amplifier with an external emitterfollower circuit shown in Figure 10.12 using SPICE2. The external output stage is
formed of two emitter-follower stages built for higher current capability with discrete
transistors 2N2222 for _Q21_ and 2N3055 for _Q22._ The opamp is connected in a unityfeedback loop. The SPICE input file is listed in Figure 10.13.


_**Solution**_
The simulation of this circuit results in a convergence failure. Neither a higher number of iterations, _ITLl,_ nor looser tolerances help the solution of this circuit. The next


w
W
Q'I



_VT_



Qg
NPNL


_R,_ _R2_ R `lO`
SOkn 1kn son


**Figure 10.12** _p,A741_ opamp with high-current output stage.



V s
1SV


V s
-1SV



_R,S_
soon


```
 UA 741 W / POWER OUTPUT STAGE
```

 
 - `THIS` `CKT` `FAILS` `OC` `CONVERGENCE`

 ```
 Ql 18 5 24 NPNL AREA=l
 Q2 18 19 25 NPNL AREA=1
 Q3 23 3 25 PNPL AREA=4
 Q4 4 3 24 PNPL AREA=4
 Q5 3 18 9 PNPL AREA=5
 Q6 18 18 9 PNPL AREA=5
 Q7 23 21 22 NPNL AREA=l
 Q8 4 21 20 NPNL AREA=l
 Q9 9 23 21 NPNL AREA=0.5
 Q10 17 17 29 NPN AREA=2
Q11 3 17 16 NPNL AREA=2
Q12 29 6 8 PNP AREA=120
Q13 11 13 9 PNP AREA=30
Q14 13 13 9 PNP AREA=12
Q15 9 11 7 NPN AREA=60
Q16 11 7 1 NPN AREA=3 OFF
```

 - `Q16` `11 7 1 NPN` `AREA=3`
```
Q17 11 12 6 NPN AREA=7
Q18 6 15 14 NPN AREA=7
Q19 6 4 15 NPNL AREA=5
Q20 4 14 29 NPN AREA=4 OFF
```

 - `Q20` `4 14 29 NPN` `AREA=4`
```
Q21 9 1 2 2N2222 AREA=l
Q22 10 2 5 2N3055 AREA=1
```

 ```
Rl 29 21 50K
R2 29 20 lK
R3 29 22 1K
R4 17 13 30K
R5 29 16 5K
```

R6 12 11 4. 5K
```
R7 6 12 7.5K
R8 1 7 25
R9 8 1 50
RIO 29 14 50
R11 29 15 50K
R15 0 2 500
R16 0 5 300M
R17 30 0 3K
R18 9 30 12K

```

**Figure 10.13** **SPICE input file for circuit of Figure** **10.12.**



**DC CONVERGENCE** **337**


_**(continued**_ _**on next page)**_


 ```
C1 11 4 30P
```

 ```
VY 19 30
VT 9 10 0.0
V6 29 0 -15
V5 9 0 15
```

 ```
 .MODEL 2N3055 NPN IS=10.3P BF=120 NF=1.02167 VAF=50 IKF=3 ISE=
+ 500P NE=2 BR=8.1 NR=1.02167 VAR=500 IKR=l ISC=O NC=2 RB=1.8
+ IRB=80M RBM=100M RE=5M RC=50M CJE=711P VJE=530M MJE=530M
+ TF=20N XTF=5 VTF=10 ITF=10 PTF=O CJC=650P VJC=580M MJC=400M
```

`+ XCJC=O. 5 TR=400N CJS=O VJS=O. 7 MJS=O. 5` **XTB=2.1** `EG=l.11 XTI=3`
```
+ KF=O AF=1 FC=0.5
 .MODEL 2N2222 NPN IS=166.78F BF=150 NF=1.074 VAF=78 IKF=500M
+ ISE=3.92P NE=1.776 BR=2.394 NR=1.074 VAR=500 IKR=O
+ ISC=O NC=l RB=676M IRB=O RBM=676M RE=100M RC=654M
+ CJE=22.25P VJE=1.333 MJE=0.522 TF=454.4P
+ XTF=13.24 VTF=4.83 ITF=216.3M PTF=O CJC=8.37P VJC=1.333
+ MJC=O. 518 XCJC=O. 5 TR=117. 5N CJS=O VJS=O. 7 MJS=O. 5
+ XTB=2.34 EG=1.11 XTI=3 KF=O AF=1 FC=0.5
 .MODEL NPNL NPN IS=4.479F BF=260 NF=1.07 VAF=260 IKF=lM
+ ISE=3.471P NE=3.66 BR=l NR=1.07 VAR=500 IKR=O ISC=O NC=l RB=36
+ IRB=O RBM=36 RE=500M RC=l CJE=910F VJE=661M
+ MJE=294M TF=112P XTF=120 VTF=O ITF=O PTF=O
+ CJC=835F VJC=l MJC=280M XCJC=0.5 TR=lN
+ CJS=O VJS=700M MJS=0.5 XTB=2.3 EG=l.11 XTI=3 KF=O AF=1 FC=0.5
 .MODEL PNPL PNP IS=218.88F BF=150 NF=1.221 VAF=150 IKF=
+ 1.50M ISE=23.64F NE=2.155 BR=4.68 NR=1.221 VAR=500 IKR=O
+ ISC=O NC=l RB=12 IRB=O RBM=12 RE=100M RC=1.5 CJE=6.25P
+ VJE=916M MJE=389. 8M TF=361. 72P XTF=21 VTF=4. 7 ITF=
+ 260M PTF=O CJC=6. 6P VJC=l. 67 MJC=406. 5M XCJC=O. 5 TR=19. 92N
+ CJS=O VJS=700M MJS=O. 5 XTB=1.7 EG=l.11 XTI=3 KF=O AF=1 FC=O. 5
 .MODEL NPN NPN IS=4.479F BF=260 NF=1.07 VAF=260 IKF=100M
+ ISE=347.1P NE=3.66 BR=l NR=1.07 VAR=500 IKR=O ISC=O NC=l RB=36
+ IRB=O RBM=36 RE=500M RC=l CJE=910F VJE=661M
+ MJE=294M TF=112P XTF=120M VTF=O ITF=O PTF=O
+ CJC=835F VJC=l MJC=280M XCJC=O.5 TR=lN
+ CJS=O VJS=700M MJS=0.5 XTB=2.3 EG=1.11 XTI=3 KF=O AF=1 FC=O.5
 .MODEL PNP PNP IS=218.88F BF=150 NF=1.221 VAF=150 IKF=
 + 150M ISE=2.364P NE=2.155 BR=4.68 NR=1.221 VAR=500 IKR=O
 + ISC=O NC=l RB=12 IRB=O RBM=12 RE=100M RC=1.5 CJE=6.25P
 + VJE=916M MJE=389. 8M TF=361. 72P XTF=21 VTF=4. 7 ITF=
.+ 260M PTF=O CJC=6.6P VJC=1.67 MJC=406.5M XCJC=O.5 TR=19.92N
 +CJS=O VJS=700M MJS=O. 5 XTB=l. 7 EG=l.l1 XTI=3 KF=O AF=1 FC=O. 5
```

 ```
 .OP
 *.OPT ITL6=40 ACCT
 .WIDI'H OUT=80
 .END

```

**Figure 10.13** _**(continued)**_



**338**


DC CONVERGENCE **339**


step is to use the built-in source-ramping algorithm. This convergence method is exercised by adding the following line to the above circuit file:

```
.OPI'IONSITL6=40

```

The simulation results using this approach are shown in Figure 10.14. As can be verified, the results are correct because of the correct biasing ofthe output, which is node 5
and the emitter of _Q22,_ at 3 V, close to the value of node 19, the positive input of the
opamp. A quick inspection of the operating point of the devices shows that the current
through the external transistor _Q22_ is higher than the current in the class AB output
stage of the opamp, Q12 and _Q15'_ The source ramping that is invoked automatically in
PSpice fails to find a solution for this circuit; in such a situation it is suggested that the
user change _ITL2,_ which is the number of iterations taken at each source value. For
source ramping the function of IT.L2 in PSpice is similar to that of **!TL6** in SPICE2.
Another way of finding the bias point of this circuit is by understanding the role
of each transistor. As a result of this inspection one can see that transistors _Q20_ and

_Q16_ have the role oflimiting the current through the gain stage _Q18 - Q19_ and the output


```
*******01/21/92 ******** SPICE 2G.6

UA741 W/ POWER OUTPUT STAGE
**** SMALL SIGNAL BIAS SOLUTION

```

```
3/15/83********11:58:49*****

 TEMPERATURE = 27.000 DEG C

```

```
***********************************************************************

NODE VOLTAGE NODE VOLTAGE NODE VOLTAGE NODE VOLTAGE

```

`1)` `4.7906` `2)` `3.9773` `3)` `1.8958` ( `4) -13.6087`
`5)` `3.0004` `6)` `4.3167` `7)` `4.8498` ( `8)` `4.7862`
`9)` `15.0000` `10)` `15.0000` `11)` `5.4823` ( `12)` `5.0097`
`13)` `14.3784` `14)` `-14.8792` `15)` `-14.1871` ( `16) -14.8930`
`17) -14.2969` `18)` `14.4726` `19)` `2.9999` ( `20) -14.9902`
`21) -14.3947` `22)` `-14.9902` `23)` `-13.7767` ( `24)` `2.4057`
```
 25) 2.4054 29) -15.0000 30) 2.9999

  VOLTAGE SOURCE CURRENTS

  NAME CURRENT

  VY -3.859D-08
  VT 9.753DtOO
  V6 3.526D-03
  V5 -1.00IDtOl

```

```
  TOTAL POWER DISSIPATION 1.50Dt02 WA'ITS

```

**Figure 10.14** SPICE DC solution for the circuit of Figure 10.12.



_(continued on next page)_


_._


**340** **10** **CONVERGENCE** **ADVICE**

```
     *******01/21/92 ******** SPICE 2G.6 3/15/83********11:58:49*****

    UA741 W/ POWER OUTPUT STAGE
```

`****` `OPERATING` `POINT` `INFORMATION` `TEMPERATURE` = `27.000` `DEG` `C`

```
     ***********************************************************************

    **** BIPOLAR JUNCTION TRANSISTORS

            Q1 Q2 Q3 Q4 Q5 Q6 Q7
    MODEL NPNL NPNL PNPL PNPL PNPL PNPL NPNL
    IB 3.89E-08 3.86E-08 -6.05E-08 -6.10E-08 -1.32E-07 -1.32E-07 3.99E-08
    IC 9.94E-06 9.87E-06 -9.85E-06 -9.92E-06 -2.12E-05 -1.95E-05 9.81E-06
    VBE 0.595 0.594 -0.510 -0.510 -0.527 -0.527 0.595
    VBC -11.472 -11.473 15.672 15.504 12.577 0.000 -0.618
    VCE 12.067 12.067 -16.182 -16.014 -13.104 -0.527 1.213
    BETADC 255.873 255.829 162.865 162.706 160.137 147.733 245.722
    GM 3.56E-04 3.53E-04 3.11E-04 3.14E-04 6.69E-04 6.17E-04 3.51E-04
    RPI 7.37E+05 7.42E+05 5.26E+05 5.21E+05 2.40E+05 2.40E+05 7. 17E+05
    RX 3.60E+01 3.60E+01 3.00E+00 3.00E+00 2.40E+00 2.40E+00 3.60E+01
    RO 2.73E+07 2.75E+07 1. 68E+07 1.67E+07 7. 66E+06 7.66E+06 2.65E+07
    CPI 6.20E-12 6.17E-12 3.43E-ll 3.43E-ll 4.36E-ll 4.36E-ll 6.13E-12
    CMU 2.06E-13 2.06E-13 5.10E-12 5.12E-12 6.90E-12 1. 65E-ll 3.65E-13
    CBX 2.06E-13 2.06E-13 5.10E-12 5.12E-12 6.90E-12 1.65E-ll 3.65E-13
    CCS O.OOE+OO O.OOE+OO O.OOE+OO O.OOE+OO O.OOE+OO O.OOE+OO O.OOE+OO
    BETAAC 262.203 262.219 163.611 163.445 160.476 148.047 251.646
    FT 8. 56E+06 8.55E+06 1.11E+06 1. 12E+06 1.85E+06 1.28E+06 8. 14E+06

            Q8 Q9 Q10 Qll Q12 Q13 Q14
    MODEL NPNL NPNL NPN NPNL PNP PNP PNP
    IE 3.99E-08 4.42E-08 4.85E-06 8.18E-08 -1.80E-06 -2.04E-05 -8.18E-06
    IC 9.81E-06 1.21E-05 9.52E-04 2.13E-05 -8.50E-05 -2.46E-03 -9.28E-04
    VBE 0.595 0.618 0.703 0.596 -0.470 -0.622 -0.622
    VBC -0.786 -28.777 0.000 -16.193 19.317 8.896 0.000
    VCE 1.381 29.395 0.703 16.789 -19.786 -9.518 -0.622
    BETADC 245.881 274.882 196.394 260.623 47.341 120.222 113.489
    GM 3.51E-04 4.29E-04 3.42E-02 7.62E-04 2.69E-03 7.78E-02 2.94E-02
    RPI 7.17E+05 6.38E+05 6.88E+03 3.50E+05 2.56E+04 1.73E+03 4.31E+03
    RX 3.60E+01 7.20E+01 1. 80E+01 1.80E+01 1.00E-01 4.00E-01 1. OOE+OO
    RO 2.65E+07 2.38E+07 2.73E+05 1.29E+07 1. 99E+06 6.46E+04 1. 61E+05
    CPI 6.14E-12 6.52E-12 7.26E-12 1.31E-ll 9.93E-10 3.08E-10 1.23E-10
    CMU 3.55E-13 8.07E-14 8.35E-13 3.77E-13 1.42E-10 4.68E-ll 3.96E-ll
    CBX 3.55E-13 8.07E-14 8.35E-13 3.77E-13 1.42E-10 4.68E-ll 3.96E-ll
    CCS O.OOE+OO O.OOE+OO O.OOE+OO O.OOE+OO O.OOE+OO O.OOE+OO O.OOE+OO
    BETAAC 251.809 274.104 235.400 266.642 68.796 134.210 126.691
    FT 8.16E+06 1.02E+07 6.10E+08 8.76E+06 3.36E+05 3.08E+07 2.32E+07

```

**Figure 10.14** _**(continued)**_


DC CONVERGENCE **341**


```
  Q17
  NPN
1.26E-05
2.33E-03
  0.693
 -0.473
  1.166
 184.109
8.37E-02
2.76E+03
5. 14E+00
1. 12E+05
2.08E-11
2.62E-12
2.62E-12
O.OOE+OO
 230.797
5.11E+08

```

```
  Q18
  NPN
1.23E-05
2.40E-03
  0.692
 -18.504
 19.196
 195.513
8.65E-02
2. 84E+03
5.14E+00
1.16E+05
2.12E-11
1.27E-12
1.27E-12
O.OOE+OO
 246.215
5.81E+08

```

```
  Q19
  NPNL
1.11E-07
2.84E-05
  0.578
 -17.925
 18.504
 256.745
1.02E-03
2.63E+05
7.20E+00
9.76E+06
2.07E-11
9.16E-13
9.16E-13
O.OOE+OO
 268.691
7.23E+06

```

```
  Q20
  NPN
3.58E-09
4.10E-12
  0.121
 -1.271
  1. 391
  0.001
5. 11E-11
1.90E+07
9.00E+00
9.71E+11
3.86E-12
1.33E-12
1.33E-12
O.OOE+OO
  0.001
1.25E+00

```

```
  Q21
 2N2222
2.28E-03
2.54E-01
  0.813
 -10.209
 11.023
 111.186
6.96E+00
1.24E+01
6.76E-01
3.47E+02
1. 05E-08
1.38E-12
1.38E-12
O.OOE+OO
 86.406
1. 05E+08

```

```
MODEL
IB
IC
VEE
```

VBC
```
VCE
BETADC
GM
RPI
```

RX
```
RO
CPI
CMU
CBX
CCS
BETMC
FT

MODEL
IB
IC
VEE
VEC
VCE
BETADC
```

GM
```
RPI
```

RX
```
RO
CPI
CMU
CBX
CCS
BETMC
```

FT


```
  Q15
  NPN
2.53E-05
2.34E-03
  0.633
  -9.518
  10.150
  92.615
8.46E-02
2.04E+03
6.00E-01
1. 15E+05
9.55E-11
1.30E-11
1. 30E-11
O.OOE+OO
 172.648
1. 11E+08

  Q22
 2N3055
2.48E-01
9.75E+00
  0.977
 -11.023
 12.000
 39.344
2.13E+02
1.07E-01
6.81E-01
6.22E+00
1.49E-05
9.91E-11
9.97E-11
O.OOE+OO
 22.797
2.28E+06

```

```
  Q16
  NPN
9.04E-10
1.45E-12
  0.059
 -0.633
  0.692
  0.002
4.11E-12
4. 86E+07
1.20E+01
9.74E+11
2.81E-12
1.09E-12
1.09E-12
O.OOE+OO
  0.000
1. 31E-01

```


**Figure 10.14** _(continued)_


transistor Q15, respectively. **In** normal operation these two transistors should be turned
off. Adding the keyword **OFF** at the end of the lines corresponding to these transistors
and commenting out the line defining _ITL6_ result in the quick convergence of the circuit,
in only 11 iterations in SPICE2. PSpice and SPICE3 also converge easily to a solution.


The above example has illustrated how both source ramping and the **OFF** initialization of transistors can lead to a solution. Another circuit that demonstrates the need


**342** 10 CONVERGENCE ADVICE


of initialization is the bistable circuit in Figure 10.15, implemented with two _J.LA741_
opamps as the gain stages.


_**EXAMPLE 10.6**_


Find a DC solution to the bistable circuit shown in Fig. 10.15 prior to computing the
response to a sawtooth input voltage _VA._


_**Solution**_
The input description of the circuit is listed in Figure 10.16. The macro-model
UA741MAC, given in Sec. 7.5.1 (Figure 7.28), is used for the _J.LA741._ The subcircuit definition of UA741MAC has to be copied from Figure 7.28 into the deck of
Figure 10.16. All the approaches mentioned above, including source ramping, may
fail to lead to a solution for this circuit depending on the model used for the opamp.
This circuit, containing high-gain stages and high-impedance nodes, is one that requires


_+V_ _cc_ _=15V_
CD


_`D,`_ _R_ _`7`_ 15kQ


_`D`_ _2_
@


_+v_ _cc_
0 _R,_ @ CD R s 10kQ _`D`_ _4_

_R2_


100 kQ
@ @
0

       - `D` a

 - _R4_ 10kQ
R a


10kQ
0

_ems_
I
_Rs_ 15 kQ


0
_-V_ _EE_ _=-15_ V

**Figure 10.15** Bistable circuit with /LA 741 opamps.


`BI-STABLE` `CIRCUIT` _WI_ `UA741 OPAMPS`

 ```
*VA 3 0 -15
VA 3 0 DC,-15 PWL 0 -151M 152M -15 2.5M 0
VCC 1 0 15
VEE 2 0 -15
```

```
D1 15 13 M1M1N914 AREA=l
D2 13 15 M1M1N914 AREA=l
D3 9 16 M1M1N914 AREA=l
D4 16 11 M1M1N914 AREA=l
```

```
.MODEL M1M1N914 D IS=lN RS=500M N=1.55 TT=5N CJO=l.S5P
+ VJ=650M M=lS0M EG=1.11 XTI=3 KF=O AF=1 FC=O.5 BV=120 IBV=l '
```

```
R7 1 11 15K
R6 11 4 10K
R5 9 2 15K
R4 4 9 10K
R2 S 13 lOOK
R1 15 3 10K
```

```
*'FEEDBACK RESISTOR
```

```
R3 4 15 10K
```

```
CNS S 0 1P
CN15 15 0 1P
```

```
XOPA1 0 15 13 1 2 UA741MAC
XOPA2 0 S 4 1 2 UA741MAC
```

```
.SUBCKT UA741MAC 3 2 6 7 4
* NODES: INt IN- OUT VCC VEE
```

```
* INSERT UA741 MACRO-MODEL DEFINITION FROM FIG. 7~2S
```

```
.ENDS
```

```
.OP
.TRAN .OlM 2M 0
.PLOT TRAN V(3) V(15) V(13) V(S) V(4)
```

```
* INITIALIZATION FOR VIN=-15
```

```
.NODESET V(4)=-15 'V(13)=.6 V(l5)=O V(S)=.6
*.OPTIONS ITL1=300 ABSTOL=lU
.OPTIONS ACCT
.WIDTH OUT=SO
.END

```

**Figure 10.16** SPICE input for bistable circuit with JLA741 opamps.
**343**


**344** 10 CONVERGENCE ADVICE


the initialization mentioned in the previous section. The high-impedance opamp input,
nodes 8 and 15, as well as the opamp output, nodes 4 and 13, must be initialized.
As described in Example 4.8, for an NMOS flip-flop SPICE finds the metastable
state as solution. This state corresponds to all inputs and outputs of the opamps being at

      - V. The output of XOPAl, node 13, is limited by the two diodes D 1 and Dz to between
-0.6V and 0.6 V, with the input at a very low value. Therefore, one of the states of this
circuit can be specified with the following       - **NODESET** statement:

```
       .NODESET V(15)=O V(13)=O.6 V(8)=O.6 V(4)=-15

```

With this line added to the circuit description of Figure 10.16 the following refineo
solution is obtained:
v ( 15) = 0.0003

V (13 ) = 0.5964

V(B) = 0.5452

V(4) = -12.6983


Note that a DC solution is a prerequisite for a transient analysis unless the **UIC** keyword
is used on the • **TRAN** line; in this case an • **IC** line should be used to define the initial
state of the circuit in order to avoid a convergence failure at the first time point.
The waveform at node 4 together with the triangular input voltage is shown in Figure 10.17.


oj
~
_g_


0.5 1.0 1.5 2.0


Time. ms
**Figure 10.17** Transient response of V (4) to triangular input V (3 ) .


DC CONVERGENCE **345**


Circuits with high-impedance nodes are often difficult convergence cases for circuit simulators. For such circuits a combination of ramping methods, initialization and
variations in model parameters and complexity can help convergence. High-impedance
nodes are common in CMOS and BiCMOS circuits using cascode configurations. A
good example for a difficult convergence case is the BiCMOS reference circuit shown
in Figure 10.18.


NPN NPN


9kO


       

@
_-Vss_
Fi~ure **10.18** BiCMOS bias reference circuit.


**346** 10 CONVERGENCE ADVICE


_**EXAMPLE 10.7**_


Find the currents in the two branches of the thermal-voltage-referenced current source
in Figure 10.18.


_Solution_
The areas of the MOS transistors in the left branch are five times the areas of the MOSFETs in the right branch of the circuit; therefore we expect the current in the left branch
to be approximately five times the current in the right branch, which can be estimated
from the _VBE_ difference of the two identical BJTs (Gray and Meyer 1985):


_1=_ Rln5 _Vth_ = 4.6 _/LA_ (10.3)


Because of the cascode current-source configuration the drain connections between
transistors _M_ _3_ and _Ms_ and between _M4_ and _M6_ are high-impedance nodes, which make
convergence to the DC solution difficult. The transistors with the larger area are modeled as they are implemented on the layout, namely, as five transistors connected in
parallel. For the input specification of this circuit shown in Figure 10.19, PSpice finds
a solution after source ramping, and SPICE2 requires _ITL6_ to be set to 40 for convergence.
Note that a model of higher accuracy is used for the MOSFETs than the one
described in Chap. 3. The LEVEL=2 model includes such second-order effects as
subthreshold conduction, set by parameter NFS; saturation due to carrier velocity limitation, represented by parameters VMAXand NEFF; and mobility modulation by the gate
voltage, represented by parameters UCRIT and UEXP. The complete model equations
for LEVEL=2 can be found in Appendix A or in the text by Antognetti and Massobrio
(1988). For more details on the semiconductor device physics see the works by Muller
and Kamins (1977) and by Sze (1981).
Two approaches are suggested for solving this convergence problem. First, set the
ITL6 option in SPICE2 to invoke the source-ramping method. The solution to the
SPICE input of Figure 10.19 is the DC operating point shown in Figure 10.20. The
currents in the right and left branches are 4.66 _/LA_ and 23.3 _/LA,_ respectively, consistent with our estimates.
The second approach recommended in convergence cases of circuits using complex
models is to eliminate some of the second-order effects. A first approximation is to
neglect for all MOSFETs the small-size effects, such as narrow-width modulation of
the threshold voltage, represented by parameter DELTA, and velocity-limited saturation,
represented by parameters VMAXand NEFF. This is achieved by deleting the DELTA
parameter from the •MODEL statement. A rerun of the circuit results in the desired
solution in SPICE2 in 96 iterations without the need of ramping. Deletion ofVMAX and
NEFF as well leads to a SPICE2 solution in only 25 iterations.


```
 BIOMOS BIAS REFERENCE
```

 ```
 Q1 10 10 3 NPNMOD 400
 Q2 10 10 1 NPNMOD 400
 R1 1 2 9K
M1A 8 12 11 11 N
M1B 8 12 11 11 N
M1C 8 12 11 11 N
M1D 8 12 11 11 N
M1E 8 12 11 11 N
M2 12 12 11 11 N
M3A 6 13 8 11 N
M3B 6 13 8 11 N
M3C 6 13 8 11 N
M3D 6 13 8 11 N
M3E 6 13 8 11 N
M4 13 13 12 11 N
M5A 6 6 4 10 P W=60U
M5B 6 6 4 10 P W=60U
M5C 6 6 4 10 P W=60U
M5D 6 6 4 10 P W=60U
M5E 6 6 4 10 P W=60U
M6 13 6 5 10 P W=60U
M7A 4 4 3 10 P W=60U
M7B 4 4 3 10 P W=60U
M7C 4 4 3 10 P W=60U
M7D 4 4 3 10 P W=60U
M7E 4 4 3 10 P W=60U
M8 5 4 2 10 P W=60U
```

 ```
VDD 10 0 5
VSS 11 0 -5
```

 ```
.MODEL NPNMOD NPN
```

+ `IS=2E-17` `BR=.4` `BF=100` `ISE=6E-17` `ISC=26E-17` `IKF=3E-3` `IKR=lE-3`
```
+ VAF=100 VAR=30 RC=100K RB=200K RE=lK
.MODEL N NMOS LEVEL=2
```

+ `VTO=O.8` `TOX=500E-10` `NSUB=1.3E16`
```
+ XJ=0.5E-6 LD=.5E-6 U0=640 UCRIT=6E4 UEXP=O.l
```

+ `VMAX=5E4` `NEFF=4` `DELTA=4` `NFS=4E11`
```
.MODEL P PMOS LEVEL=2
```

+ `VTO=-0.8` `TOX=500E-10` `NSUB=2E15`
+ `XJ=0.5E-6` `LD=.5E-6` `U0=220` `UCRIT=5.8E4` `UEXP=0.18`
+ `VMAX=3E4` `NEFF=3.5` `DELTA=2.5` `NFS=3E11`

```
.OPTION ACCT DEFL=10U DEFW=20U
*.OPTION ABSTOL=lN
.WIDTH OUT=80
.OP
.END

```

**Figure 10.19** **SPICE description of BiCMOS bias reference circuit.**
**347**


**348** **10** **CONVERGENCE ADVICE**

```
    *******02/11/92 ******** SPICE 2G.6

    BICMOS BIAS REFERENCE

```

```
3/15/83********15:57:31*****

```


******** `SMALL` `SIGNAL` `BIAS` `SOLUTION` `TEMPERATURE` = `27.000` `DEG` `C`

```
***********************************************************************

```

```
VOLTAGE

 3.2322
 5.0000

```

```
VOLTAGE

 4.4360
-3.8354
-2.6967

```

```
NODE

```

4 )
```
 10)

```

```
VOLTAGE

 4.4359
 1.8759
-3.8484

```

```
NODE

```

3 )
```
 8)
 13)

```

```
NODE

```

1)
5 )
```
 11)

```

```
VOLTAGE

 4.4778
 3.2169
-5.0000

```

```
NODE

```

2 )
```
 6)
 12)

```

```
VOLTAGE SOURCE CURRENTS

```

```
NAME

VDD
VSS

```

```
 CURRENT

-2.798D-05
 2.798D-05

```

```
   TOTAL POWER DISSIPATION 2.80D-04
*******02/11/92 ******** SPICE 2G.6

BICMOS BIAS REFERENCE

```

```
WATTS
3/15/83********15:57:31*****

```


******** `OPERATING` `POINT` `INFORMATION` `TEMPERATURE` = `27.000` `DEG` `C`

```
***********************************************************************

**** BIPOLAR JUNCTION TRANSISTORS

```

```
 Q2
NPNMOD
6.36E-08
4.60E-06
  0.522
  0.000
  0.522
 72.318
1.78E-04
4.46E+05
5.00E+02
2.14E+07

```

```
MODEL
IB
IC
VBE
VBC
VCE
BETADC
GM
RPI
RX
RO

```

```
 Q1
NPNMOD
2.84E-07
2.30E-05
  0.564
  0.000
  0.564
 81.116
8.90E-04
9.67E+04
5.00E+02
4.26E+06

```

```
**** MOSFETS

        M1A M1B M1C M1D M1E M2 M3A
MODEL N N N N N N N
ID 4.66E-06 4.66E-06 4.66E-06 4.66E-06 4.66E-06 4.66E-06 4.66E-06
VGS 1.152 1.152 1.152 1.152 1.152 1.152 1.139
VDS 1.165 1.165 1.165 1.165 1.165 1.152 5.711
VBS 0.000 0.000 0.000 0.000 0.000 0.000 0.000
VTH 0.841 0.841 0.841 0.841 0.841 0.841 0.833
VDSAT 0.248 0.248 0.248 0.248 0.248 0.248 0.246
GM 2.51E-05 2.51E-05 2.51E-05 2.51E-05 2.51E-05 2.51E-05 2.54E-05
GDS 1. 01E-07 1.01E-07 1.01E-07 1.01E-07 1. 01E-07 1.01E-07 5.60E-08
GMB 1.25E-05 1.25E-05 1.25E-05 1.25E-05 1.25E-05 1.25E-05 1.26E-05

```

**Figure 10.20** **DC operating point of BiCMOS** **reference circuit.**


**DC CONVERGENCE** **349**

```
        M3B M3C M3D M3E M4 M5A M5B
```

`MODEL` N N N N N P, P
```
ID 4.66E-06 4.66E-06 4.66E-06 4.66E-06 4.66E-06 -4.66E-06 -4.66E-06
VGS 1.139 1.139 1.139 1.139 1.152 -1. 356 -1.356
```

`VDS` ., ., `5.711` `5.711` `5.711` `5.711` `1.152` `-1.356` `-1.356`
```
VBS 0.000 0.000 0.000 0.000 0.000 1.768 1.768
VTH 0.833 0.833 0.833 0':833 0.841 -1.097 -1.097
VDSAT 0.246 0.246 0.246 0.246 0.248 -0.i75 -0.275
GM 2.54E-05 2.54E-05 2.54E-05 2.54E-05 2.51E-05 3.04E-05 3.04E-05
GDS 5.60E-08 5.60E-08 5.60E-.08 5.60E-08 1. 01E-07 1. 31E-07 1.31E-07
GMB 1.26E-05 1.26E-05 1.26E-'05 1.26£-05 1.25E-05 3.29£-06 3.29E-06

        M5C M5D M5E M6 M7A M7B M7C
```

`MODEL` P ., p.,,P P P P P
```
ID -4.66E-06 -4.66E,-06 -4.66E-06 -4.66E-06 -4.66E-06 -4.66E-06 -4.66E-06
VGS -1:356 - .':1';356 -1 :356 -1.341 -1.204 -1.204 -1.204
VDS -1.356 ~1..356 -1.356 -5.914 -1.204 -1.204 -1.204
VBS 1.768 1.768 1.768 1.783 0.564 0.564 0.564
VTH -1. 097 -1. 097 -1.097 -1.091 -0.939 -0.939 -0.939
VDSAT,..0.275 -0.275 -0.275 -0.267 -0.270 -0.270 -0.270
GM 3.04E-05 3.04E-05 3.04E-05 3.14E-05,,2.98E-05 2.98E-05 2.98E-05
GDS 1.31E-07 1.31E-07 1.31E-07 1. 00E-07 1.29E-07 1.29E-07 1.29E-07
GMB 3.29E'-06 3,29E-06 3.29E-06 3.37E~06 4.58E-06 4.58E-06 4.58E-06

        M7D M7E M8
```

`MODEL` P P P
```
ID -4.66E-06 -4.66E-06 -4.66E-06
VGS -1.204 -1.204 -1.204
VDS -1.204 -1.204 -1.219
VBS 0.564 0.564, 0.564
VTH -0.939 -0.939 -0.939
VDSAT -0.270 -0.270 -0.270
GM 2.98E-05 2.98E-05 2.98E-05
GDS 1.29E-07 1.29E-07 1.29E-07
GMB 4.58E-06 4.58E-06 4.58E-06

```

**Figure 10.20** _**(continlfed)**_


**This example shows that both source ramping and selective** **deletion of some**
**second-order effects can lead to convergence for CMOS and BiCMOS circuits. An-**
**other possible' approach is to increase the values of ABSTOL** **and RELTOL.** **Once a**
**solution is obtained, initialization of critical nodes can be used to obtain convergence of**
**the circuit using the complex models and default tolerances.**


**Another approach to'finding the DC bias point of a circuit is to ramp up the supplies**
**in a** transi~nt **analysis. This method is applied in the next example to obtain the hystere-**
**sis curve of a CMOS Schmitt trigger, which displays very abrupt switching at the two**
**thresholds. The advantage** of time-domain **analysis for solving circuits with positive**
**feedback and high loop gain resides in the presence of charge storage elements, which**
**do not allow instantaneous switching to take place.**


**350** 10 CONVERGENCE ADVICE


_**EXAMPLE 10.8**_


Compute the hysteresis characteristic of the CMOS Schmitt trigger (Jorgensen 1976)
shown in Figure 10.21. The n- and p-channel transistors have the following LEVEL=l
model parameters:

```
         NMOS: VTO=2 KP=20U RD=lOO CGSO=lP
         PMOS: VTO=-2 KP=lOU RD=lOO CGSO=lP

```

If a finite output conductance in saturation needs to be modeled, use _LAMBDA_
0.05 V-I for both transistors. All transistors have the same geometry, with _W_ = 10 _/Lm_
and _L_ = 10 _/Lm._ Compare the results from PSpice and SPICE2.


_**Solution**_
The most appropriate analysis for computing the transfer characteristic is • **DC,** the
DC sweep analysis, presented in Sec. 4.3. The output voltage, _Vo_ can be computed
while _Vi_ first increases from 0 to _Vee_ and then decreases from _Vee_ to O. The positive and negative thresholds of the hysteresis curve are set by the voltages at nodes 5


**Figure 10.21** CMOS Schmitt trigger circuit.


DC CONVERGENCE **351**


and 3, respectively. The transistors _M2_ and _M4_ form a comparator, while the p-channel
transistor pair _MI-M3_ and the n-channel transistor pair _Ms-M6_ are voltage dividers,
which define the two thresholds. When _Vi_ is 0, p-channel transistors _Ml_ and _M2_ are
turned on and n-channel transistors _M4_ and Ms are off, with _V_ _[o]_ at _Vee._ This value of
_V_ biases _M3_ off and _M6_ on. When _Vi_ == _VTOn,_ or 2 V, Ms turns on and the voltage at
node 5 is set to approximately _o_ ~ _Vee._ When _Vi_ == Vs + _VTOn, M4_ starts turning on,
triggering regenerative switching and resulting in _V_ _o_ going to 0 V and transistors _M2_
and _M6_ turning off. This point is the positive switching threshold, _Vst+_ of the Schmitt


trigger and is equal to


_Vee_ _(10A)_
_Vst+_ == 2 + _VTOn_


The same process takes place when _Vi_ is varied from _Vee_ to 0, except that the switching


point occurs at


_Vee_ (10.5)
_Vi_ == _Vst-_ == 2 - _\VTOP\_


CMOS SCHMITT TRIGGER

  -  - THIS CIRCUIT DIES IN . DC AROUND VT+ AND vr-;

  - PSPICE SOURCE RAMPING CANNar SAVE IT; ONLY A .TRAN CAN PROVIDE THE HYSTERESIS;


  - FOR IMPROVED CONVERGENCE LAMBDA  - 0, CAPS IN MODEL.


  M1 2 1 3 2 P
```
  M2 3 1 4 2 P
  M3 043 2 P
```

M4 4 1 5 0 N

M5 5 1 0 0 N
M6 2 4 5 0 N
.OPTION DEFL=10U DEFW=10U
.MODEL P PMOS VTO=-2 KP=10U RD=100


*+ LAMBDA=O. 05 CGsa=lP
.MODEL N NMOS VTO=2 KP=20U RD=100


*+ LAMBDA=0.05 CGsa=lP


VCC 2 0 12

VI100
*VI 1 0 6 PWL 0 0 lOON 12 200N 0


.DC VI 0 12 0.1

*.TRAN 1N 200N
.OPTION ABSTOL=100N


*.PROBE

•END

**Figure 10.22** SPICE input for CMOS Schmitt trigger.


**352** 10 CONVERGENCE ADVICE


The SPICE input circuit is listed in Figure 10.22. The analysis of this circuit fails
both in SPICE2 and PSpice. A basic rule when simulating stacked CMOS transistors
is to provide a finite output conductance in saturation for all transistors. In the basic
LEVEL=l model, finite output conductance is modeled when a value is specified for
**LAMBDA** in the • **MODEL** statement. Models of higher **LEVEL** compute a finite conductance internally from process parameters, and specifying **LAMBDA** is necessary only
when the internal value must be overridden.
After the addition of **LAMBDA,** SPICE2 completes the DC transfer characteristic.
PSpice however fails to converge when _Vi_ reaches the positive switching threshold,
_Vst+._ In general, any SPICE simulator can fail to converge in DC analysis when strong
regenerative feedback is present in the circuit.
The approach to curing this problem is to find a time-domain solution rather than a
DC solution, by sweeping _Vi_ over time from 0 V to _Vee_ and then back to 0 V. VI must
be changed in the input circuit to include the ramping in time, and the • **TRAN** line must
be added in Figure 10.22:

```
      VI 1 0 0 PWL 0 0 lOON 12 200N 0
      .TRAN 1N 200N

```

The solution is obtained over 200 ns, with _Vi_ rising to _Vee_ at 100 ns and falling back
to 0 at the end of the analysis interval, at 200 ns.
Every SPICE program can complete this analysis. The hysteresis of the Schmitt
trigger is shown in Figure 10.23: it is the plot of _V_ _o_ as a function of _Vi._ The two switching points agree between the two programs and analyses.
In order to demonstrate the importance of the charge storage in the circuit it is left
for the reader as an exercise to remove CGSO from both • **MODEL** definitions in Figure
10.22 and observe the result of the analysis.


12


10


8

        ~ `6` `6`


4


2


               -, I, I,I,I ' I, I,I I I I I I

                  - 2 4 6 8 10 12


_VI'_ V
Figure 10.23 Hysteresis curve of the Schmitt trigger.


TIME-DOMAIN CONVERGENCE 353


10.4 TIME-DOMAIN CONVERGENCE


This section addresses the convergence problems that can occur during a transient analysis and the ways to overcome these problems. As in the case of DC analysis, the three
SPICE versions used in this text differ slightly in the implementation of the integration
algorithms and the control a user can exert on the time-domain solution.
Through the METHOD option SPICE2 and SPICE3 offer the user the choice between trapezoidal and Gear variable-order integration, whereas PSpice does not offer
this choice. SPICE2 and SPICE3 use trapezoidal integration by default, and PSpice exclusively uses the Gear algorithm. In addition, SPICE2 differs from SPICE3 by offering
the user the choice of the time-step control method through the LVLTIM option. By default the time step is controlled by the truncation error in both programs, corresponding
to _LVLTIM_ = 2 in SPICE2. If _LVLTIM_ = 1, an iteration-count time-step control is
used in SPICE2, which doubles the time step at any time point when the program does
not need more than 3 iterations to converge, and cuts it by 8 when convergence is not
reached within _ITL4,_ equal to 10, iterations.
In the following examples both potential traps of time-domain solution, convergence failure and accuracy, are addressed. The most important causes for convergence
failure are incomplete semiconductor model descriptions and lack of charge storage elements. Ideal representations of semiconductor devices, that is, models described only
by the default parameters are often the cause of a transient analysis failure.
The following example illustrates a TIME STEP TOO SMALL (TSTS) failure due
to an incomplete model used to represent a diode in a full-wave rectifier circuit.


_EXAMPLE_ _10.9_


Use SPICE to compute the time-domain response of the circuit shown in Figure 10.24.
The model parameters of the diodes are _IS_ = 10- [14] A and _CiO_ = 10 pF. Then perform a second analysis including the breakdown voltage for the two diodes, _BV =_
100Y.


Figure 10.24 Diode rectifier circuit.


**354** 10 CONVERGENCE ADVICE

```
      CHOKE CKT - FULL WAVE CHOKE INPUT
      VIN1 1 0 SIN(O 100 50)
      VIN2 2 0 SIN(O -100 50)
      Dl 1 3 DIO
      D2 2 3 DIO
```

`R1` `3 0` _10K_
```
      L1 3 4 5.0
```

R2 4 0 _10K_
```
      C2 4 0 2UF IC=80
      .MODEL DIO D IS=1.0E-14 CJO=10PF
      .TRAN 0.2MS 200MS UIC
      .PLOT TRAN V(1) V(2) V(3) V(4)
      .OPT ACCT
      .WIDTH OUT=80
```

        - END


**Figure 10.25** SPICE input for diode rectifier.


_**Solution**_
In the circuit of Figure 10.24 the two diodes, _D_ _1_ and _D2,_ driven by the two sinusoidal
sources represent a full-wave rectifier, which is followed by an RLC low-pass filter.The
. SPICE input file for this circuit is listed in Figure 10.25, and the voltage waveforms
at nodes 3 and 4 are plotted in Figure 10.26. The output voltage on capacitor C2 is
initialized at 80 V, which is the peak value and is reached when the voltage at node 3
reaches its lowest point.


8

     

€

     0


~ 70V

     - 0


10 `20` 30 40 50 60


Time, ms
**Figure 10.26** Rectifier waveforms for no BV.


100V
~

 - -100


100V
g

- -100


50V
ff

0


50V
~

0



... .


TIME-DOMAIN CONVERGENCE **355**


10 `20` `30` `40` `50` `60` `70`



Time, ms
**Figure 10.27** Rectifier waveforms for _BV_ = 100.


**In** order to model the breakdown characteristic of the diode in the reverse region,
the value of parameter **BV** is added to the • **MODEL** line. Resimulation of the circuit
results in a TSTS error in PSpice and a numerical exception in SPICE2. Because of the
ideality of the diodes in the previous analysis only one is conducting at anyone time and
proper current limiting is provided by the load circuit. When a breakdown characteristic
is added to the diodes at 100 V, a current path exists from one signal source to the other
through the series combination of the two back-to-back diodes. _D2_ breaks down when
V ( 1) reaches 50 V and V ( 2) reaches - 50 V, and the two diodes could be destroyed
in reality. The solution to this problem is to add a parasitic series resistance, **RS,** to the
diode model, which limits the current when _Dr_ or _D2_ operate in the breakdown region.
Resimulation of the circuit with RS=l 00 added to **the. MODEL** line in Figure 10.25
results in the waveforms V (3) and V (4) shown in Figure 10.27. Note that because of
the diode reverse conduction the voltage at node 3 is clamped at 50 V. **In** reality a
careful sizing of the series resistors is necessary in order to limit the reverse current to
the maximum value prescribed in the data book and avoid destruction of the diode.
This example has illustrated a failure condition that can develop during the transient
analysis because of an ideal model and improper circuit design. The addition of series
resistance for limiting the current solved the problem.


Analysis failure can also occur because of insufficient charge storage in a circuit.
**In** the absence of charge storage elements a circuit tends to switch in zero time, which
does not happen in reality and cannot be handled by the existing solution algorithms.
This issue is presented in the following example.


**356** 10 CONVERGENCE ADVICE


_**EXAMPLE 10.10**_


Simulate the behavior of the NMOS relaxation oscillator shown in Figure 10.28 (Kelessaglou and Pederson 1989) using SPICE. The model parameters for the enhancement
and depletion transistors are


LEVELF=l V'IO=O. 7 KP=30U (enhancement transistor)

LEVELF=l V'IO=-O. 7 KP=30U LAMBDA=O. 01 (depletion transistor)


_**Solution**_
The input description for SPICE is listed in Figure 10.29. Note that the current source,
_h,_ is used only to kick-start the oscillations. Also note that the substrates of all transistors are connected at _VEE_ = -9 V. The transient response is requested to be displayed
only from 1400 J,Lsto 1800 J,LS.As pointed out in Sec. 6.2, SPICE computes the waveform starting from 0 but saves only the results after _t_ = 1.4 ms.
**In** SPICE2 the analysis fails at _t_ = 46.23 J,LS,when the time step is reduced below
a minimum value set by the program to be 10- [9] of the smaller of2 X _TSTEP_ or _TMAX._
The first observation is that the MOS transistors do not have any capacitances given
in the • **MODEL** statement. It is necessary to correct the ideality of the MOSFET models
by adding a gate-source capacitance, **CGSO,** to the two models, MODl and MOD2. After
CGSO=l P is included in **the.** **MODEL** statement, the transient analysis finishes successfully; the resulting waveforms are shown in Figure 10.30. The period and pulse width
can be verified by hand using the GDS values printed in the operating point information
for depletion devices _Ms_ and Mg.


**Figure 10.28** NMOS relaxation oscillator.


**TIME-DOMAIN** **CONVERGENCE** **357**

```
 MOS RELAXATION OSCILLATOR
 M1 2 1 0 6 MOD1 W=100U L=5U
 M2 4 5 0 6 MOD1 W=100U L=5U
 M3 3 2 2 6 MOD2 W=20U L=5U
 M4 3 4 4 6 MOD2 W=20U L=5U
 M5 3 1 1 6 MOD2 W=20U L=5U
 M6 1 0 0 6 MOD2 W=20U L=5U
 M7 3 5 5 6 MOD2 W=20U L=5U
 M8 5 0 0 6 MOD2 W=20U L=5U
 C1 2 5 lOOP
 C2 4 1 200P
VEE 6 0 -9
```

VDD 3 0 5
```
 11 5 0 PULSE lOU 0 0 0 0 1
 .MODEL MOm NMOS V'I'CPt-O.7 KP=30U
```

*+ `CGSO==lP`
```
 .MODEL MOD2 NMOS VTO=-O.7 KP=30U LAMBDA=O.Ol
```

*+ `CGSO==lP`
```
 .OP
 .TRAN 2U 1800U 1400U
 .PLOT TRAN V(5) V(l) V(4)
 .WIDI'H OUT=80
 .OPTION NOPAGE NOMOD LIMPTS=1001 ITL5=O
 .OPTION ACCT ABSTOL=lN
 .END

```

**Figure** **10.29** **SPICE input for NMOS relaxation oscillator.**


~

- `0`


5

~
```
> 0

```

**0.5** **1.0** **1.5**

**Time, ms**

**Figure** **10.30** **Waveforms** V (1), V (2), V (4), **and** V (5) **for the NMOS relaxation oscillator.**


**358** 10 CONVERGENCE ADVICE


The above examples have focused on the main causes for the failure of transient analysis
and on how to overcome them. Another important issue is the accuracy of the solution
computed by the transient analysis.
Several observations were made in the previous chapter on the stability of numerical integration algorithms. The trapezoidal method was seen to oscillate around the solution for values of the time step that are larger than a limit related to the time constant
of the circuit. This behavior can be noticed in the computed response of a circuit, especially when the circuit switches. This numerical oscillation can be avoided by selecting
the Gear algorithm or controlling the tolerances for a tighter control of the truncation
error, which results in a smaller time step.
The following example illustrates ringing around the solution.


_**EXAMPLE 10.11**_


Find the waveform of the current flowing through the diode D] in Figure 10.6 when a
voltage step from 5 V to -5 V is applied to the circuit. For the first analysis use the
default model for the diode with the following two additional parameters:

```
       RS=100 TT=40N

```

The parameter **TT** is a finite transit time of the carriers in the neutral region of the diode;
the effect of this parameter is that when a diode is switched off it takes a finite time to
eliminate the carriers from the neutral region, and during this time the diode conducts
in reverse direction.


_**Solution**_
```
      DIODE SWITCHING
```

       `D1` `1` a `DMOD`
```
      VIN 1 0 PULSE 5 -5 50N .1N .1N 50N lOON
       .MODEL DMOD D RS=lOO
```

+ `TI'=40N`
*+ `CJO=lOP`
```
       .'IRAN .5N lOON
       .PLOT TRAN I (VIN)
```

         - . `OPTION` `METHOD=GEAR` `MAXORD=2`
```
       .WIDTH OUT=80
```

        - END


The SPICE input description is listed above. The waveform of the diode current
resulting from the SPICE simulation is plotted in Figure 10.31. Current ringing around
the value of zero can be noticed following the storage time, during which the diode
conducts in reverse. This result can be explained only by the oscillatory nature of the
trapezoidal integration method.
Whenever the simulated response of circuits displays oscillations that are not anticipated by design, the integration method should be changed to the second-order Gear


TIME-DOMAIN CONVERGENCE **359**



BOmA
z
```
~ 0

  -40
```

BOmA
z
```
~ 0

  -40
```

BOmA
z
```
~ 0

  -40

```


TRAP


GEAR 2


CJO+ TRAP



Time, ns
**Figure 10.31** Diode current computed with trapezoidal and Gear 2 integration methods and _C]._


method by adding the following line to the SPICE input:


•OPTION METHOD=GEAR MAXORD=2


The second-order Gear method is characterized by numerical damping. After the. addition of the above line to the input, repeating the simulation yields the second waveform
shown in Figure 10.31, which exhibits the expected behavior.
The model of the diode used in this example is ideal except for the finite transit time,
**TT,** and series resistance, RS. The charge storage of the diode is incomplete without the
depletion region charge (see Sec. 3.2). If this charge is modeled by specifying a value
for the parameter **CJO** on the • **MODEL** line, a gradual decay of the current is expected
with a time constant equal to _CjRs._ A new simulation with **CJO** added and the default
trapezoidal integration yields the third current waveform shown in Figure 10.31. It can
be noticed that the current returns to zero with minimal numerical ringing.
This last observation leads to the conclusion that the more complete the model, the
more accurate and stable is the solution. A common cause for numerical oscillation is
sudden changes in a circuit variable or in the model equations. The latter can also be
caused by imperfections in the built-in analytical models in SPICE in addition to the
absence of certain model parameters.


Next, a few comments are necessary about the impact of transient analysis parameters _TSTEP_ and _TMAX_ on the accuracy of the result. In Sec. 6.4 the accuracy of the
Fourier coefficients calculation was shown to depend on the value of _TMAX,_ which
controls the number of points evaluated for a signal each period. Numerical ringing can


360 10 CONVERGENCE ADVICE


also be avoided by selecting smaller values for _TMAX_ or reducing the relative tolerance
RELTOL. In general, the more time points are computed, the more accurate the results.
Sometimes the maximum time step must be set by the user in order to obtain an accurate
solution.


_**EXAMPLE 10.12**_


Simulate the current flowing through the CMOS inverter shown in Figure 10.32. The
SPICE input description and model parameters are listed in Figure 10.33. The input
voltage is ramped from 0 V to 10 V over 10 _/LS._


_Solution_
Current flows through the inverter only for values of _VIN_ from 1 V to 9 V. The graphical
solution of the inverter current in Figure 10.34, computed with the default trapezoidal
method, incorrectly displays ringing of 10 _/LA_ after reaching the peak value.
The same current computed with the Gear 2 method is smooth and overlaps the
trapezoidal solution in Figure 10.34. An alternate way to obtain the correct solution is
to limit the maximum time step the program takes during the trapezoidal integration.
A value of 50 ns added to the • TRAN line in Figure 10.33 also leads to a smooth waveform.
Modeling the subthreshold current with parameter NFS added to the device specification has an effect on the result similar to that of the Gear integration, that is, a smooth
current waveform.


+


Figure 10.32 CMOS inverter circuit diagram.


**TIME-DOMAIN** **CONVERGENCE** **361**

```
CMOS INVERTER
```

 ```
M1 2 1 0 0 NMOS
+ L=10U W=20U AD=160P AS=160P PD=36U PS=36U
VM 21 2
M2 21 1 3 3 PMOS
+ L=10U W=40U AD=1600P AS=1600P PD=216U PS=216U
VIN 1 0 PWL 0 0 lOU 10
VDD 3 0 10
```

 ```
.MODEL NMOS NMOS
+ LEVEL=2 VTO=.9 GAMMA=.6 PB=.8 CGSO=.28E-9 CGDO=.28E-9 CGBO=.2SE-9
+ CJ=.3E-3 MJ=.49 CJSW=.66E-9 MJSW=.26 TOX=.SE-7 NSUB=.SE16 NSS=lE11
+ TPG=l XJ=.SE-6 LD=.38E-6 UO=610 UCRIT=S.4E+4 UEXP=.l
+ VMAX=1.2E+S NEFF=3 KF=1.0E-32 AF=1.0
+ NFS=lEll
```

```
.MODEL PMOS PMOS
+ LEVEL=2 VTO=-.8 GAMMA=.69 PB=.8 CGSO=.28E-9 CGDO=.28E-9 CGBO=.2SE-9
+ CJ=.4E-3 MJ=.46 CJSW=.6E-9 MJSW=.24 TOX=.SE-7 NSUB=.6SE+16 NSS=lE+11
+ TPG=-l XJ=.7U LD=.S2U UO=230 UCRIT=S.2E+4 UEXP=.18
+ VMAX=.4E+S NEFF=3 KF=.2E-32 AF=1.0
+ NFS=lEll
```

```
*.TRAN 200N lOU 0 SON
.TRAN 200N lOU
.PLOT TRAN I(VM)
.WIDTH OUT=80
.END

```

**Figure** **10.33** **SPICE description** **of CMOS inverter.**


'3. 300

~~


**100**


    

**Time,** ~s


**Figure** **10.34** **CMOS inverter current computed with trapezoidal and Gear 2 integration**
**methods.**


**362** 10 CONVERGENCE ADVICE


PSpice does not provide a choice in integration methods. The results of PSpice
simulations for the above circuits show a certain level of damping, which points to the
Gear method.


**10.5** **CIRCUIT-SPECIFIC CONVERGENCE**


**10.5.1** **Oscillators**


The analysis of oscillators can represent a challenge for the user of circuit simulation. As
described in Example 6.3, the number of periods for oscillations to build up is inversely
proportional to the quality factor of the resonant circuit, _Q._ Another possible difficulty
in simulating oscillators is related to the numerical integration methods. In the previous chapter and in the previous section it was shown that the Gear integration method
has a damping effect on oscillations. Therefore, trapezoidal integration, the default in
SPICE2 and SPICE3, but seemingly not in PSpice, should always be used when simulating oscillators. It may be necessary to set a value of _TMAX,_ the maximum allowed
integration step, in order to control the accuracy of the trapezoidal method.
An important aid for initiating oscillations in a simulator is either a single pulse at
the input of the amplifier block or the initialization of the charge storage elements close
to the steady-state values reached during oscillations.
The most representative example for the difficulty encountered in simulating oscillators is a crystal oscillator. Because of the high _Q,_ of the order of tens of thousands, it
would theoretically take a number of periods on the same order of magnitude to reach
steady state. It is impractical to simulate a circuit for so many cycles. The following
example provides insight into the analysis of a Pierce crystal oscillator.


_**EXAMPLE 10.13**_


Verify the behavior of the CMOS Pierce crystal oscillator shown in Figure 10.35 using
SPICE2 and PSpice. The circuit drawing includes the equivalent schematic of the crystal, _Co, Cx, Lx,_ and _Rs._ The crystal has a resonant frequency of 3.5795 MHz, common
in color television, and has the following equivalent circuit parameters:

_Cx_ = 2.47 fF _Lx_ = 0.8 H _Rs_ = 600 n Co = 7 pF


Use the following model parameters for the n- and p-channel MOSFETs:

```
         NMOS: VTO=l KP=20U LAMBDA=O. 02
         PMOS: VTO=-l KP=lOU LAMBDA=0.02

```

An attempt to run the circuit as is or using a start-up pulse does not produce the expected
oscillations.


_**Solution**_
A first approach for simulating this circuit is to replace the crystal with an equivalent
circuit with a reduced _Q_ that allows for a rapid buildup of oscillations. The crystal has


CIRCUIT-SPECIFIC CONVERGENCE **363**

##### Figure 10.35 r Pierce CMOS crystal

oscillator.


a series and a parallel resonant frequency, _Is_ and _I_ _p,_ respectively. At frequencies below
_Is_ the reactance of the crystal is capacitive, whereas above _Is_ the reactance is inductive
and _Lx, Cx,_ and Co can be substituted by an effective inductance, _Leff._ The oscillation
frequency, _wo,_ of the equivalent circuit is given by


_Wo_ _=_ (10.6)


This frequency, _wo,_ is very close to the crystal resonant frequency, _ws,_ leading to the
following value for _Leff:_


_L_ _1 = 0.18 **mH**
_eff -_ w}C l _C_ _z/_ (C l + _C_ _z)_ (10.7)


**364** 10 CONVERGENCE ADVICE


The new equivalent resonant circuit has Q = 7, which is considerably smaller than the
original value. The crystal equivalent circuit, _C_ _x, Lx,_ _Co,_ must be replaced by _Left._ The
SPICE input description is listed below; a • **SUBCKT** block represents the crystal.


`PIERCE` `XTAL` `OSCILLATOR` _WI_ `CMOS`
```
       .OPTION LIMPTS=10000 ITL5=0
```

      ```
      M1 2 3 0 0 NMOS W=40U L=10U
      M2 2 3 1 1 PMOS W=80U L=10U
      RL 2 5 10K
      C1 5 0 22P
      C2 3 7 22P
      VDD 1 0 5
```

      
       - `XTAL`
.*
```
      Xl 3 5 XTAL
       .SUBCKT XTAL 1 2
      LEFF 1 3 .18M
      RS 3 2 600
      RP 1 2 22MEG
       .ENDS XTAL
```

** `KICKING` `SOURCE`

       ```
      VKICK 70 PULSE 0 10M .1N .1N .1N 1 1
```

       ```
       .MODEL NMOS NMOS VTO=l KP=20U LAMBDA=O. 02
       .MODEL PMOS PMOS VTO=-l KP=10U LAMBDA=0.02
```

       ```
       .OP
       .TRAN 10N 50U 45U 10N
       .PLOT TRAN V(2) V(3)
       .END

```

Resimulation of the circuit results in the waveforms V(2) and V(3) shown in
Figure 10.36. The circuit sustains oscillations centered around 2.5 V with an amplitude
of 1.75 V at the output of the gain block, node 2, and 0.75 V across the crystal with a
period of 280 ns, corresponding to the resonant frequency, _woo_
Note that the SPICE circuit description includes a voltage source, VKICK, which
provides a 0.1 ns pulse for triggering the oscillations. The • **TRAN** line requests the
results to be saved only after 45 fJ-S, that is, after approximately 150 cycles, when the
steady state should have been reached. The same results are obtained with both SPICE2
and PSpice.
Once the correct operatiori of the circuit has been verified, the circuit can be
simulated with the real crystal. As shown in Sec. 6.3, it is necessary to initialize the
charge storage elements as close as possible to the steady-state values; the previous
results can help in this task. Assume that at _t_ = 0+ both V(3) and V(5) are at 2.5 V,


ai
E
g



CIRCUIT-SPECIFIC CONVERGENCE **365**


Time,lLS,
**Figure 10.36** Waveforms V (2) and V (3) for oscillator with reduced _Q._



which corresponds to the maximum current in the inductor _Lx._ The results of the simulation using the equivalent inductor, _L_ _ejf,_ instead of the crystal can be used for guidance.
Note that it is important to initialize the state of one of the crystal components, such as
_Lx,_ in order to achieve steady-state oscillations in the solution. Therefore, the initial current through _Lx_ and Co should approximate the value of the current amplitude through
the equivalent crystal, _L_ _ejf._ For a rigorous derivation of the oscillation amplitude consult
the text by Pederson and Mayaram (1990).


`PIERCE` `XTAL` `OSCILLATOR` _WI_ `CMOS`

 
 - `THIS` `CKT` `OSCILLATES` `ONLY` `PSPICE` `3.02` `(OLD) BECAUSE` `IT USES` `TRAP`
..

 ```
.OPTION LIMPT8=10000 ITL5=0
```

```
M1 2 3 0 0 NMOS w=40U L=10U,
M2 2 3 1 1 PMOS W=80U L=10U
RL 2 5 10K
C1 5 0 22P IC=2.5
C2 3 0 22P IC=2.5
```

VDD 1 0 5
** `XTAL`



**366** 10 CONVERGENCE ADVICE

```
      Xl 3 5 XTAL
       .SUBeKT XTAL 1 2
```

      - `LEFF` `3 6` `.18M`
```
      LX 1 3 0.8 IC=0.6M
      ex 3 4 2.47FF
      eo 1 2 7PF
      RS 4 2 600
      RP 1 2 220K
       .ENDS XTAL
```

       ```
       .MODEL NMOS NMOS VTO=l KP=20U LAMBDA=O. 02
       .MODEL PMOS PMOS VTO=-l KP=10U LAMBDA=0.02
```

      ```
      .OP
       .TRAN ION sou 45U ION Ule
       .PLOT TRAN V(2) V(3)
       .END

```

The new SPICE input is shown above; note that the initial pulse is omitted and the
keyword **UIC** is used in the • **TRAN** statement in order to start the analysis at steady
state. The results are shown in Figure 10.37 and are identical to the previous solution.
The estimated steady state is verified by the analysis performed in SPICE2 or
SPICE3, and the oscillations are sustained for the 200 cycles simulated. The result


    ai
~
_g_


Time, l!S
**Figure 10.37** Waveforms V (2) and V (3) for oscillator with crystal.


CIRCUIT-SPECIFIC CONVERGENCE **367**


of a PSpice analysis for this circuit shows the oscillations decaying, which could be
explained by the use 'of Gear integration.


t".


**10.5.2** **BJTversus MOSFET Specifics**


MOSFET circuits have more convergence problems than bipolar circuits because of
a number of differences between the two devices types. First, the physical structures
of the two devices are different. The gate terminal of a MOSFET is insulated; that is,
it is an open circuit in DC. The, self-conductance of the gate)s therefore zero in DC,
often leading to ill-conditioned circuit matrices, as demonstrated by Example 10.1, and
subsequently to the failure of SPICE to find a solution. By contrast,icontinuous current
flows in or out of the base terminal of a bipolar transistor, independently of region of
operation and analysis.,mode.
Second, the generality of analytical models used in SPICE to describe the two devices is not the same. Whereas, the Ebers-Moll or Gummel.Poon formulation for the
BJT transistor applies to all regions of operation, the MOSFETmodels combine different ~quations t~describe distinct regions of operations and various second-order -effects. The differel}r fo.n;nulations have different levels of continuity for the equivalent
conductance at the tran~i!ion points. Tbe continuity of the conductance,. which is the
first deriv'ative of the f-unttion, is Important for the convergence of the iterative process.
Third, the ilpplementation details in SPICE also affect convergence. There are differences in the operating points in which the program initializes the two types of devices
and in the way new operating points, are selected at each iteration. An important difference between BJTs and MOSFETs in the first iteration is that by default the former are
initialized conducting whereas, generally,.MOSFETs are initialized turned off; MOSFETs are initialized with _Vcs_ = _VTO,_ and the difficulty with MOSFETs is that the actual threshold _voltage"VTH;_ is usually increased by back-gate bias to a higher value than
the zero-bias threshold'voltage, _VTO._ Only MOSFET devices with subthreshold current, model parameterNFS, are initially in the conduction state. This second-order effect
is supported only by the higher-level models, summarized}n Appendix A and described
in more detail in the references (Antognetti and Massobrio 1988; Sheu, Scharfetter, and
Ko 1985; Vladimirescu and Liu 1981). This is one example where convergence can be
improved by changing model parameters.
The default initi~lization oLtransistors has a different impact on convergence depending on the operation of the circuit. A smaller number of iterations has been noticed
for analog (linear) bipolar circuits as compared to digital (logic) bipolar circuits because
BJTs are initialized 'as'cond~cting in SPICE. The explanation can be found in the mode
of operation of analog circuits, which have the majority of the transistors turned on, in
contrast with digital circuits, whicJ;1.have an important percentage of the 'devices turned
off. Example 10.4 demonstrated thatthe initialization of two protective devices as **OFF**
improves the convergence,arid leads to"a sol~ti(:m without source ramping. Experiments
in the SPICE code that initialized all MOSFETs in the conduction state have proven to


**368** 10 CONVERGENCE ADVICE


speed up the convergence of analog circuits. The user can access initialization through
the device initial conditions, **IC** = _VDSO, Vcso,_ _VBSO,_ which are activated only in transient
analysis in conjunction with the **UIC** option.
The importance of initialization and device specifics for the convergence of MOS
analog circuits, especially those with high-impedance nodes, often present in cascode
loads, can be exemplified by a CMOS differential amplifier (Senderowicz 1991).


_**EXAMPLE 10.14**_


Find the DC operating point of the circuit shown in Figure 10.38 using the LEVEL=2
parameters given in the SPICE description.


_**Solution**_
This circuit is a differential amplifier in a unity-feedback loop; the conversion from
double- to single-ended output is achieved by PMOS transistors _M6_ through _M9._ The
state of this circuit is set by connecting the appropriate bias transistors M ll through
M14 to the gates of the transistor _Ms,_ the differential pair transistor _M_ _2,_ and the load
transistor pairs _M3-M4,_ and _M6-M7'_
Based on the knowledge acquired in Chap. 9, one can see the difficulty associated
with solving the modified nodal equations when a number of nodes are of very low
conductance; nodes 3 and 4 have very high impedances because of the cascode connection, and additionally, all transistors are biased very close to the threshold voltage,
on one hand, and at the limit between saturation and linear region, on the other hand.
This approach to biasing is common in analog CMOS circuits.
The attempt to find the DC operating point of the circuit as it is represented by
the input description in Figure 10.39 fails in SPICE2 but succeeds in PSpice and
SPICE3 after source ramping. Addition of the option ITL6=40 to the SPICE2 input
does not help for this circuit. It is important to note that SPICE2, which provides more
feedback related to a solution failure, encounters problems in the matrix solution: the
messages PIVOT CHANGE ON THE FLY and *ERROR*: MAXIMUM ENTRY ... IS

LESS THAN PIVTOL can be found in the output file.
When ramping methods fail for this type of difficult circuit, running a transient
analysis while ramping the supplies from 0 to the DC value or leaving them unchanged
may lead to a solution. If the supplies are ramped for part of the time interval, the DC
value should be preserved for the rest of the time-domain analysis in order to allow
the circuit to settle. A time-domain analysis of an MOS circuit has the additional advantage of a well-conditioned matrix because charge storage elements provide finite
conductance at the gates of MOSFETs. Transient ramping of the CMOS differential
amplifier in Fig. 10.39 is performed when the • **THAN** and • **PRINT** lines are activated.
A DC solution is avoided by using the **UIC** keyword on the • **THAN** line. A transient
analysis also fails in SPICE2 for this circuit.
Several options can be modified for this circuit. Based on the observation of the
condition of the circuit matrix, a first approach is to tighten the pivot selection criterion


_~_ _)17_



_~_ _)16_



~ )Is



@













~ } /10



~



V oo
CD


CD

_Vss_



**Figure 10.38** **CMOS differential amplifier with** cascode **load.**



W
Q'I
I.C


**370**


```
CMOS DIFFERENTIAL AMPLIFIER
*
M1 11 5 9 2 N W=120U L=1.2U AD=2N AS=2N PD=12U PS=12U
M2 12 6 9 2 N W=120U L=1.2U AD=2N AS=2N PD=12U PS=12U
M3 3 8 11 2 N W=120U L=1.2U AD=2N AS=2N PD=12U PS=12U
M4 4 8 12 2 N W=120U L=1.2U AD=2N AS=2N PD=12U PS=12U
M5 9 7 2 2 N W=240U L=1.2U AD=2N AS=2N PD=12U PS=12U
M6 3 10 13 1 P w=120U L=1.2U AD=2N AS=2N PD=12U PS=12U
M7 4 10 14 1 P W=120U L=1.2U AD=2N AS=2N PD=12U PS=12U
M8 13 4 1 1 P W=120U L=1.2U AD=2N AS=2N PD=12U PS=12U
M9 14 4 1 1 P W=120U L=1.2U AD=2N AS=2N PD=12U PS=12U
*
* BIAS CIRCUIT
* VOLTAGES AT NODES 6, 7, 8 AND 10 ARE SUPPLIED BY
* M13, M14, M12 AND M11
*
M11 10 10 1 1 P W=120U L=4.8U AD=2N AS=2N PD=12U PS=12U
M12 8 8 2 2 N W=120U L=9.6U AD=2N AS=2N PD=12U PS=12U
M13 6 6 2 2 N W=120U L=4.8U AD=2N AS=2N PD=12U PS=12U
M14 7 7 2 2 N W=120U L=1.2U AD=2N AS=2N PD=12U PS=12U
110 10 2 200U
18 1 8 200U
16 1 6 200U
17 1 7 400U
```

```
VDD 1 0 5.0
*+ PULSE(O.O 5.0 0 100U ION 100U 200U)
VSS 2 0 0.0
```

```
VFF 3 5 2.0
*+ PULSE(O.O 2.0 0 100U ION 100U 200U)
```

```
.WIDTH OUT=80
.OP
.OPT ACCT
*.OPT PIVREL=lE-2
*.OPT ABSTOL=lU
*.OPT ITL6=40
*.OPT ITL4=100
*.TRAN IUS 200US UIC
*.PRINT TRAN V(2) V(3) V(4) V(5) V(6)
*.PRINT TRAN V(7) V(8) V(9) V(10) V(ll)
*.PRINT TRAN V(12) V(13) V(14)
```

 ```
* N_CHANNEL TRANSISTOR, SANITIZED MODELS
```

 ```
.MODEL N NMOS LEVEL=2
+ U0=600 VTO=700E-3 TPG=1.000 TOX=25.0E-9
+ NSUB=5.0E+16 UCRIT=2E+4 UEXP=O.l
+ XJ=lE-10 LD=100E-9 PB=0.8 JS=100.0E-6 RSH=100
+ NFS=200E+9 VMAX=60E+3 NEFF=2.5 DELTA=3
+ CJ=400E-6 MJ=300E-3 CJSW=2.00E-9'MJSW=1.0
+ CGS0=2.0E-10 CGDO=2.0E-10 CGB0=3.0E-10 FC=0.5
```

```
* P_CHANNEL TRANSISTOR
```

 ```
.MODEL P PMOS LEVEL=2
+ U0=200 VTO=-700E-3 TPG=-1.000 TOX=25.0E-9
+ NSUB=2.0E+16 UCRIT=2E+4 UEXP=O.l
+ XJ=lE-10 PB=0.8 JS=100.0E-6 RSH=200
+ NFS=100E+9 VMAX=20.00E+3 NEFF=.9 DELTA=l
+ CJ=400E-6 MJ=300E-3 CJSW=2.00E-9 MJSW=1.0
+ CGS0=2.0E-10 CGDO=2.0E-10 CGBO=3.0E-IO FC=0.5
```

 ```
.END

```

**Figure 10.39** **SPICE input for CMOS differential** **amplifier with cascode load.**


CIRCUIT-SPECIFIC CONVERGENCE **371**


by increasing the value of _PIVREL_ by including the following statement:

```
.OPTIONS PIVREL=lE-2

```

Second, because of the possible operation near threshold of some transistors, the absolute current tolerance, _ABSTOL,_ can be raised:

```
.OPTIONS ABS'IOL=1U

```

These two options contribute to a successful time-domain solution in SPICE2. The
voltages at the circuit nodes are listed for the last 10 time points in Figure 10.40; an
average value is chosen to initialize the node voltages with a • **NODESET** statement.

```
.NODESET
```

+ V(3) = 3.29
+ V(4) = 3.71
+ V(5) = 1.29
+ V(6) = 1.28
+ V(7) = 1.1
+ V(8) = 1.54
+ V(9) = 0.19
+ V(10) = 3.32
+ V(ll) = 0.39
+ V(12) = 0.39
+ V(13) = 4.63
+ V(14) = 4.64


When the node voltages are initialized, the DC operating point is obtained for this circuit
in only 8 iterations.
The solution and the operating point information are listed in Figure 10.41. One
can verify the bias point of the transistors in this circuit and understand that the convergence difficulty is caused by the proximity of the operating points to the limits of the
subthreshold conduction, linear and saturation regions. MOS analog circuits are biased
with _VGS_ close to _VTO_ for maximum gain and at the edge of saturation for maximum
output signal swing (Gray & Meyer 1985). VTH represents the bias- and geometryadjusted values of the zero-bias threshold voltages, VTO, specified in the • **MODEL** statement.
An alternate way to find a solution for this circuit and for amplifiers in general is to
cut the feedback loop and find a DC solution of the open-loop amplifier. Then, the node
voltages obtained from the open-loop circuit can be used in a • **NODESET** statement to
initialize the closed-loop amplifier. The open-loop solution for this circuit is nontrivial.


**372** `10` CONVERGENCE ADVICE

```
      *******03/07/93 ******** SPICE 2G.6 3/15/83********20:18:56*****

      CMOS DIFFERENTIAL AMPLIFIER

```

`****` `TRANSIENT` `ANALYSIS` `TEMPERATURE` = `27.000 DEG C`

```
      ***********************************************************************

         TIME V(3) V(4) V(5) V(6)
       1.910E-04 3.287E+00 3.709E+00 1.287E+00 1.283E+00
       1.920E-04 3.288E+00 3.711E+00 1.288E+00 1.284E+00
       1.930E-04 3.289E+00 3.712E+OO 1.289E+00 1.285E+00
       1.940E-04 3.288E+00 3.711E+00 1.288E+00 1.285E+00
       1.950E-04 3.287E+00 3.710E+00 1.287E+00 1.283E+00
       1.960E-04 3.286E+00 3.708E+00 1.286E+00 1.282E+00
       1.970E-04 3.285E+00 3.707E+00 1.285E+00 1.281E+00
       1.980E-04 3.286E+00 3.708E+00 1.286E+00 1.282E+00
       1.990E-04 3.288E+00 3.710E+00 1.288E+00 1.284E+00
       2.000E-04 3.290E+00 3.712E+00 1.290E+00 1.286E+00

         TIME V(7) V(8) V(9) V(lO)

       1.910E-04 1.102E+00 1.537E+00 1.883E-01 3.320E+00
       1.920E-04 1.102E+00 1.541E+00 1.893E-01 3.316E+00
       1.930E-04 1.102E+00 1.546E+00 1.903E-01 3.313E+00
       1.940E-04 1.102E+00 1.542E+00 1.896E-01 3.315E+00
       1.950E..,04 1.102E+00 1.538E+00 1.886E-01 3.319E+00
       1.960E-04 1.102E+00 1.533E+00 1.876E-01 3.323E+00
       1.970E-04 1.102E+00 1.529E+00 1.866E-01 3.327E+00
       1.980E-04 1.102E+00 1.534E+00 1.877E-01 3.323E+00
       1.990E-04 1.102E+00 1.540E+00 1.890E-01 3.317E+00
       2.000E-04 1.102E+00 1.546E+00 1.904E-01 3.312E+00

         TIME V(ll) V(12) V(13) V(14)

       1.910E-04 3.844E-01 3.874E-01 4.633E+00 4.642E+00
       1.920E-04 3.876E-01 3.906E-01 4.630E+00 4.639E+00
       1.930E-04 3.907E-01 3.939E-01 4.626E+00 4.635E+00
       1.940E-04 3.883E-01 3.914E-01 4.629E+00 4.638E+00
       1.950E-04 3.852E-01 3.882E-01 4.632E+00 4.642E+00
       1.960E-04 3.821E-01 3.850E-01 4.636E+00 4.645E+00
       1.970E-04 3.791E-01 3.817E-0l 4.639E+00 4.649E+00
       1.980E-04 3.824E-01 3.853E-01 4.635E+00 4.645E+00
       1.990E-04 3.867E-01 3.897E-01 4.631E+00 4.640E+00
       2.000E-04 3.909E-01 3.942E-01 4.626E+00 4.635E+00

```

**. Figure 10.40** Transient solution of CMOS differential amplifier.


CONVERGENCE OF LARGE CIRCUITS 373


**10.5.3** **CONVERGENCE OF LARGECIRCUITS**


The larger a circuit, the more complex is its behavior. A large circuit usually consists of
a number of individual functional blocks, or cells, which perform different functions,
some analog, linear or nonlinear, and some digital. The large number of transistors operate in very different conditions depending on the functions of the blocks. The difficulty
of finding a solution is directly related to the number of nonlinear elements. With no
prior knowledge of the expected function, SPICE requires considerable more iterations
than for a few transistors. For most common purposes a circuit with more than 100
semiconductor devices can be considered a large circuit.
It is a good practice to describe a large circuit hierarchically. The . **SUBCKT** definition capability of SPKE introduced in Chap. 7 should be used for this purpose. Before
the entire circuit is stimulated, the component functional blocks should be characterized individually. Key nodes can be expressed as interface nodes and initialized. This
is necessary since • **NODESET** and • **IC** cannot initialize nodes internal to a subcircuit.
Specifying the state of transistors that are **OFF** also helps.
Because of the size of the circuit, the 100 iterations of the default _ITLl_ are often
insufficient for finding a DC solution. _ITLl_ should be increased to 300 to 500 but not

```
    *******03/08/93 ******** SPICE 2G.6 3/15/83********21:30:55*****

    CMOS DIFFERENTIAL AMPLIFIER

    **** SMALL SIGNAL BIAS SOLUTION TEMPERATURE = 27.000 DEG C

    ***********************************************************************

    NODE VOLTAGE NODE VOLTAGE NODE VOLTAGE NODE VOLTAGE

     1) 5.0000 2) 0.0000 3) 3.2872 4) 3.7093
     5) 1.2872 6) 1.2831 7) 1.1019 8) 1.5372
     9) 0.1884 10) 3.3196 11) 0.3848 12) 0.3878
     13) 4.6327 14) 4.6421

      VOLTAGE SOURCE CURRENTS

      NAME CURRENT

      VDD -1.467D-03
      VSS 1.467D-03
      VFF O.OOODtOO

```

`TOTAL POWER DISSIPATION` `3.67D-03` `WATTS` _(continued on next page)_


**Figure 10.41** DC operating point computed after initialization.


```
*******03/08/93 ******** SPICE 2G.6 3/15/83********21:30:55*****

CMOS DIFFERENTIAL AMPLIFIER

```

`****` `OPERATING` `POINT INFORMATION` `TEMPERATURE` = `27.000 DEG C`

```
***********************************************************************

**** MOSFETS

```

```
M1 M2 M3 M4 M5 M6 M7

```

```
MODEL N N N N N P P

```


10 `2.35E-04` `2.32E-04` `2.35E-04` `2.32E-04` `4.67E-04 -2.35E-04 -2.32E-04`
```
VGS 1.099 1.095 1.152 1.149 1.102 -1.313 -1.322
VDS 0.196 0.199 2.902 3.322 0.188 -1.346 -0.933
VBS -0.188 -0.188 -0.385 -0.388 0.000 0.367 0.358
```

VTH `0.845` `0.845` `0.931` `0.932` `0.765` `-0.859` `-0.857`
```
VDSAT 0.172 0.170 0.156 0.154 0.202 -0.306 -0.314
GM 1.19E-03 1.23E-03 1.82E-03 1.82E-03 1.37E-03 9.70E-04 9.25E-04
GDS 7.69E-04 6.84E-04 9.14E-06 8.52E-06 4.02E-03 3.30E-05 4.06E-05
GMB 5.37E-04 5.53E-04 7.46E-04 7.48E-04 6.88E-04 2.47E-04 2.36E-04
CBD 7.32E-13 7.31E-13 4.96E-13 4.81E-13 7.82E-13 5.79E-13 6.13E-13
CBS 7.65E-13 7.65E-13 7.23E-13 7.22E-13 8.09E-13 7.22E-13 7.24E-13
CGSOVL 2.40E-14 2.40E-14 2.40E-14 2.40E-14 4.80E-14 2.40E-14 2.40E-14
CGDOVL 2.40E-14 2.40E-14 2.40E-14 2.40E-14 4.80E-14 2.40E-14 2.40E-14
CGBOVL 3.00E-16 3.00E-16 3.00E-16 3.00E-16 3.00E-16 3.60E-16 3.60E-16
CGS 1.10E-13 1.10E-13 1.11E-13 1.11E-13 2.01E-13 1.33E-13 1.33E-13
CGD 1.20E-14 9.21E-15 O.OOE+OO O.OOE+OO 1.13E-13 O.OOE+OO O.OOE+OO
CGB O.OOE+OO O.OOE+OO O.OOE+OO O.OOE+OO O.OOE+OO O.OOE+OO O.OOE+OO

```

```
M8 M9 Mll M12 M13 M14

```

```
MODEL P P P N N N

```


10 `-2.35E-04 -2.32E-04 -2.00E-04` `2.00E-04` `2.00E-04 4.00E-04`
```
VGS -1.291 -1.291 -1.680 1.537 1.283 1.102
VDS -0.367 -0.358 -1.680 1.537 1.283 1.102
VBS 0.000 0.000 0.000 0.000 0.000 0.000
```

VTH `-0.751` `-0.751` `-0.751` `0.757` `0.756` `0.762`
```
VDSAT -0.348 -0.348 -0.677 0.540 0.361 0.207
GM 5.26E-04 5.08E-04 4.08E-04 4.76E-04 6.89E-04 2.16E-03
GDS 5.98E-04 6.23E-04 6.03E-06 1.13E-06 2.46E-06 2.55E-05
GMB 1.64E-04 1.59E-04 1.13E-04 2.14E-04 3.23E-04 1.04E-03
CBD 7.40E-13 7.42E-13 5.80E-13 5.90E-13 6.11E-13 6.31E-13
CBS 8.09E-13 8.09E-13 8.11E-13 8.18E-13 8.18E-13 8.11E-13
CGSOVL 2.40E-14 2.40E-14 2.40E-14 2.40E-14 2.40E-14 2.40E-14
CGDOVL 2.40E-14 2.40E-14 2.40E-14 2.40E-14 2.40E-14 2.40E-14
CGBOVL 3.60E-16 3.60E-16 1.44E-15 2.82E-15 1.38E-15 3.00E-16
CGS 1.29E-13 1.29E-13 5.30E-13 1.04E-12 5.08E-13 1.11E-13
CGD 3.87E-14 4.20E-14 O.OOE+OO O.OOE+OO O.OOE+OO O.OOE+OO
CGB O.OOE+OO O.OOE+OO O.OOE+OO O.OOE+OO O.OOE+OO O.OOE+OO

```


**Figure 10.41** _(continued)_



**374**


SUMMARY 375


beyond; the probability for a circuit to converge beyond this. number is low. Source
ramping offers a better chance of success than increasing _ITLl_ above the limit of 500
.iterations.
Another approach that may help large circuits converge is,to relax the tolerances
RELTOL and ABSTOL. _RELTOL_ can be increased to 5 X 10- [3], and _ABSTOL_ c,anbe made
as high as six orders of magnitude below the highest current of a single device in the
circuit. Once a solution is available, it can be used for initialization and the tolerances
can be tightened back for more rigorous results.
If all the above attempts fail, a transient analysis with ure and all supplies ramped
up from zero should help. The time interval should be chosen so that elements with the
slowest time constants can settle to steady-st,!te values. '[he r:esults can then be used
either to find an 0p,?ratingpoint or to initialize another.transient analysis.


10.6 **SUMMARY**


Based on the information on the solution algorithms of the previous chapter, a number of
approaches and simulator option parameters for overcoming convergence failure have
been presented in this chapter.
The following is the sequence of actions to undertake when SPICE fails to find the
DC solution.


1. Carefully check the circuit connectivity and elem~nt values for possible specification errors and typographical errors; the NODE, LIST and MODEL options
provide useful information on connectivity, element values, and model parameters, respectively. Note that only tlie MODEL option is turned on by default in
most SPICE versions.

2. If the circuit specification is correct and SPICE does not converge, try first increasing the maximum number of iterations _ITLI_ to 300 to 500. PSpice and
SPICE3 automatically exercise the ramping methods if the main iterative process fails; SPICE2, however, needs to be directed to ~pply source ramping by
setting _ITL6_ to a value of 20 to 1OO;themaxiIhum number of iterations allowed
for anyone set of source values. If automatic convergence algorithms fail, the
number of iterations taken at each step should be increased; for example, increase _ITL2_ in PSpice from the default of 20to 40 or more.

3. Initialization of node voltages and cutoff semiconductor devices can be of help
in finding a solution. For large circuits it can be useful'to initialize all nodes
once a solution'is available and reduce the time for subsequent DC solutions.

4. The next step toward finding a solution is to add or delete certain physical
effects of the model. Examples in this chapter have demonstrated the importance of finite output conductance in saturation and subthreshold conduction
for MOS circuits. In other situations a simpler model can lead to better convergence; see Example 10.7.


376 10 CONVERGENCE ADVICE


5. Relaxation of the convergence tolerances, RELTOL and ABSTOL, can also lead
to a solution. _ABSTOL_ can easily be raised to 1 nA for MOSFETs. In general,
_ABSTOL_ should not be more than 9 orders of magnitude smaller than the largest
current of a nonlinear device.


6. The protective parallel junction conductance, _GMIN,_ can be increased 2 or 3
orders of magnitude.


7. A very reliable method for finding a DC solution is to run a transient analysis
with the UlC option. All supplies should be ramped from zero to the final value
for part of the interval and then held constant for the nodes to settle.


8. The solution of large-gain blocks connected in a feedback loop can be found by
opening the loop and then using the results to initialize the closed-loop circuit.


Convergence failure can occur not only in a DC analysis but also in the time-domain
solution. The following steps should be taken.


1. Check the circuit for charge storage, which insures a finite transition time from
state to state. Also check the circuit for an abnormally high range of values
for a single component type; the ratio of the largest to the smallest value of
a component type should preferably be within nine orders of magnitude. See
Sec. 9.2.2 for the underlying explanation.


2. Check model parameters that can produce unrealistic conductance values, such
as FC.

3. Increase the number of iterations, _ITIA,_ allowed at each time point to 40 or
higher from the default of 10.


4. Relax the tolerances ABSTOL and RELTOL.


5. Use a different integration method if available. METHOD=GEAR with
MAXORD=2orMAXORD=3 is recommended.


6. Reduce the maximum allowed time step, _TMAX._


7. Disable control of truncation error by setting _TRTOL_ to a large value, such as
10 [3] . The time step in this situation is controlled by the iteration count; SPICE2
grants the option of setting LVLTlM=l, which is equivalent to setting _TRTOL_
to a very large value.

8. Reduce, rather than relax, _RELTOL;_ a value of 10- [4] or smaller can force a
smaller time step and avoid the bypass of a seemingly inactive device (see
Sec. 9.3.2). Bypass is sometimes the culprit in a failed time-domain analysis.


If more than one SPICE simulator is available, it is useful to try to solve a difficult circuit with another version. Once a solution is available, it can be transferred
as a .NODESET initialization to the simulator of choice, which is usually linked to a
graphical postprocessing package for documentation purposes. Not many users have
this luxury, however.


SUMMARY **377**


**REFERENCES**


Antognetti, P., and G. Massobrio. 1988. _Semiconductor Device Modeling with SPICE._ New
York: McGraw-Hill.
Gray, P. R., and R. G. Meyer. 1985. _Analysis and Design of Analog Integrated Circuits._ New
York: John Wiley & Sons.
Grove, A. S. 1967. _Physics and Technology of Semiconductor Devices._ New York: John Wiley
& Sons.
Jorgensen, J. M. 1976. (October 5). CMOS Schmitt Trigger. _U.S. Patent 3,984,703._
Kelessoglou, T., and D. O. Pederson. 1989. NECTAR-A knowledge-based environment to enhance SPICE. _IEEE Journal of Solid-State Circuits._ SC-24 (April) 452-457.
Muller, R. S., and T. I. Kamins. 1977. _Device Electronics for Integrated Circuits._ New York:
John Wiley & Sons.
Pederson, D.O., and K. Mayaram. 1990. _Integrated Circuits for Communications._ Boston:
Kluwer Academic.
Senderowicz, D. 1991. Personal communication.
Sheu, B. J., D. L. Scharfetter, and P. K. Ko 1985. SPICE2 implementation of BSIM. Univ. of
California, Berkeley, ERL Memo UCB/ERL M85/42 (May).
Sze, S. M. 1981. _Physics of Semiconductor Devices._ New York: John Wiley & Sons.
Vladimirescu, A, and S. Liu. 1981. The simulation of MOS integrated circuits using SPICE2.
Univ. of California, Berkeley, ERL Memo UCB/ERL M8017 (March).


_**APPENDIX**_ _**A**_


_**SEMICONDUCTOR-DEVICE**_
_**MODELS**_


`A.1` **DIODE**


Table A.l Diode Model Parameters


Name Parameter Units Default Example Seale Factor

IS Saturation current A 1 x 10- [14] lE-16 _area_
N Emission coefficient 1 1.5
RS Ohmic resistance n 0 100 _l/area_
TT Transit time s 0 O.IN
CJO Zero-bias junction capacitance F 0 2P _area_
VJ Junction potential V 1 0.6
M Grading coefficient 0.5 0.33
EG Activation energy eV 1.11 1.11 Si
0.69 Sbd
0.67 Ge
XTI _Is_ temperature exponent 3 3 pn
2Sbd
BV Breakdown voltage V 00 40
IBV Current at breakdown voltage A 1 X 10- [3] lOU _area_
FC Coefficient for forward-biased 0.5
depletion capacitance
formula
KF Flicker noise coefficient 0
AF Flicker noise exponent 1


378


DIODE **379**



**A.l.l** **DC,** **Transient,** **and** **AC** **Models**


All SPICE2 and SPICE3 model parameters are listed in Table A.I.



_NkT_
for _VD_ 2: -5-_q_


_NkT_ (Al)
for _-BV_ < _VD -_ 5-_q_



_ID =_



_IS(eqVD/NkT -_ 1) + _VDGMIN_


_-IS_ + _VDGMIN_



_-IS(e-q(Bv+vD)/kT_ _-_ 1) - _IBV_ for _VD_ < _-BV_


_TT_ _[dID]_ + _CIO_ _~_ _V_ _FC_ _VI_
_dVD_ (1 - _VD/VIO)M_ lor _D_ < .

_CD =_

_{_

_TT dVDdID_ + (1 _ _FC)I+MCIO_ [1 _ _FC(1_ + _M_ + _)_ _MVD]VI_ _~_ lor _VD_ 2: _FC_ . _VI_

(A2)


**A.l.2** **Temperature** **Effects**


Model parameters _IS, VI, CIO,_ and _EG_ vary with temperature according to the following functions of temperature, _Is(T), <p](T),C](T)_ and _Eg(T):_


(A3)


(A 4)



_E (T)_ = _E_ (0) _ (7.02 X 10- [4] eV _/K)T_ _[2]_

g g (1108 K) + _T_


_C](T_ _2)_ = _C](Td {_ 1 + _M_ [400 X _1O-_ _[6]_ _(T_ _2_ _-_ _T_ _1)_ _-_ _<PAT~]ZT ~](Td_ _])_



_(A.5)_


(A 6)



Model parameters are assumed to be specified at the reference temperature, _T1,_ equal
to _TNOM,_ which defaults to 300 K. _TNOM_ can be modified with a • **OPTIONS** statement.


380 APPENDIX A SEMICONDUCTOR-DEVICE MODELS


A.l .3 Noise **Model**


The three noise contributions are due to the parasitic series resistance, _RS,_ and the shot
and flicker noise of the pn junction:



'2 _4kTt::.f_
_lRS_ _=_
_RS_



_(A.7)_
~ - 2 _I t::.f_ _KFl~Ft::.f_



_ld_ _-_ _qD_ _+-f-_



A.2 **BIPOLAR** **JUNCTION** **TRANSISTOR**


Table A.2 BJT Model Parameters


Name Parameter Units Default Example Scale Factor

IS Saturation current A 1 x 10- [16] lE-16 _area_
BF Forward current gain 100 80
NF Forward emission coefficient 1 2
VAF Forward Early voltage V 00 100
IKF {3F high-current roll-off comer A 00 0.1 _area_
ISE BE junction leakage current A 0 lE-13 _area_
NE BE junction leakage emission coefficient 1.5 2
BR Reverse current gain 1 3
NR Reverse emission coefficient 1 1.5
VAR Reverse Early voltage V 00 250
IKR (3R high-current roll-off comer A 00 0.1 _area_
ISC BC junction leakage current A 0 lE-13 _area_
NC BC junction leakage emission coefficient 1.5 2
RC Collector resistance n 0 200 _l/area_
RE Emitter resistance n 0 2 _I/area_
RB Zero-bias base resistance n 0 100 _l/area_
RBM Minimum base resistance at high current n _RB_ 10 _l/area_
IRB Current where base resistance falls
nalfway to its minimum value A 00 0.1 _area_
TF Forward transit time s 0 IN
XTF Coefficient for bias dependence of _TF_ 0
VTF Voltage for _TF_ dependence on _VBC_ V 00
ITF Current where _TF_ = _f(lc,_ _VBe)_ starts A 0 _area_
PTF Excess phase at _f_ = 1/ _(2nTF)_ degrees 0
TR Reverse transit time s 0 lOON
CJE BE zero-bias junction capacitance F 0 2P _area_
VJE BE built-in potential V 0.75 0.6
MJE BE grading coefficient 0.33 0.33
CJC BC zero-bias junction capacitance F 0 2P _area_
VJC BC built-in potential V 0.75 0.6
MJC BC grading coefficient 0.33 0.5


BIPOLAR JUNCTION TRANSISTOR 381


Table A.2 _(continued)_


Name Parameter Units Default Example Scale Factor

XCIC Fraction of _CJC_ connected at 0.5
internal base node _B'_
CIS CS zero-bias junction capacitance F 0 2P _area_
VIS CS built-in potential V 0.75 0.6
MIS CS grading coefficient 0 0.5
EG Activation energy eV 1.11 1.11 Si
XTI _Is_ temperature exponent 3
XTB _{3F_ and _{3R_ temperature exponent 0
FC Coefficient for forward-biased 0.5
depletion capacitance formula
KF Flicker noise coefficient 0
AF Flicker noise exponent 1


A.2.1 **DC Model**


_I_ _c_ _~~ (eqVBdNFkT _ eqVBclNRkT) _ ~~_ _(eqVBclNRkT -_ 1)

_- ISC(eqVBclNCkT_ _-_ 1) (A 8)


_IB_ = ~~ _(eqVBdNFkT -_ 1) + ~~ _(eqVBclNRkT -_ 1)

_+_ _ISE(eqVBdNEkT_ _-_ 1) + _ISC(eqVBclNCkT_ _-_ 1) (A9)


where _qb_ is defined by


_qb_ = ~' (1 + _Jl_ + _4q2)_



_ 1 _ _VBC __ _VBE_
_q, -_ _VAF_ _VAR_
( ) [-']

_q_ = _IS_ _(eqVBdNFkT __ 1) + _IS_ _(eqVBclNRkT -_ 1)
2 _IKF_ _IKR_



(A 10)



Older versions of SPICE use parameters C2 and C4, which correspond to the junction
leakage currents ISE and ISC:


_ISE_ = _C2._ _IS_

_ISC_ = _C4._ _IS_


**382** APPENDIX A SEMICONDUCTOR-DEVICE MODELS


The effective series base resistance, _RBB,_ is


_RBM_ + _RB - RBM_
_qb_
_R_ _BB,_ _=_

_{_ _RBM_ + _3(RB - RBM)_ tan _z -_ z

ztan [2] z



if _IRB_ is not specified

(All)
if _IRB_ is specified



where


**A.2.2** **Transient and AC Models**



-1 + _J1_ + 1. _44IB/_ _'TT_ _[2]_ _IRB_
_z_ = ----,---===--_24/_ _'TT_ _[2]_ _JIB/IRB_


_CBE_ = _CDE_ + _CJE_

_CBC_ = _CDC_ + _CJB,c_


_CCS_ = _CJS_



Diffusion capacitances are implemented as

_CDE_ = __J__ _[T/_ _[S]_ _(eQV8dNFkT -_ 1)]
_JVBE_ _qb_


C = _TR_ _qIS_ _eQV8c1NRkT_
_DC_ _NRkT_


where

_TF_ = _TF[l_ + _XTFeV8c11.44VTF (_ _Icc_ )2]
_Icc_ + _ITF_


and


Junction capacitances are defined by



(AI2)


(A13)


(A 14)


(AI5)


BIPOLAR JUNCTION TRANSISTOR **383**


The Be junction capacitance has two components, one connected to the external and
one to the internal base node:



_CIB,C_ = _XJC._ _CIC_

_CIBC_ = (l - _XJC)CIC_


At high frequencies a phase shift equal to


() = _wPTF._ _TF_


is applied to the phasor Ie:


This effect is also present in the time-domain expression of _ie(t)._


**A.2.3** **Temperature Effects**


The following quantities are adjusted for temperature variation:



(A 16)


(A 17)


(A.I8)


(A 19)


_(A._ 20)



The temperature dependence of _Eg, cPI,_ and _CI_ for the diode is implemented as determined by Eqs. _AA_ to _A.6._


**A.2.4** **Noise Model**


Noise is modeled as thermal noise for the parasitic series resistances and as shot and
flicker noise for _i_ C and _i_ _B:_


_i~_ = _4kTtlf_
(A2l)
_R_


384 APPENDIX A SEMICONDUCTOR-DEVICE MODELS


-:z - _lb_ _-_ 2 _I_ _q B_ 11/ + _KF._ _IY_ / _11/_ _(A._ 22)

_-:z_
_lc = 2q1cl1/_ _(A._ 23)


A.3 MOSFET


Table A.3 MOSFET Model Parameters


Name Parameter Units Default Example Scale Factor


LEYEL Model index I
YTO Threshold voltage Y 0 1.0
KP Transconductance parameter A/y [2] 2 X 10- [5] 1.0E-3
GAMMA Bulk threshold parameter y [l] / [2] 0 0.5
PHI Surface potential Y 0.6 0,7
LAMBDA Channel length modulation parameter y-I 0 1.0E-4
RD Drain ohmic resistance n 0 10
RS Source ohmic resistance n 0 10
RSH D and S diffusion sheet resistance n 0 10 _`NRD`_
```
                                    NRS
```

CBD Zero-bias BD junction capacitance F 0 5P
CBS Zero-bias BS junction capacitance F 0 IP
CJ Zero-bias bulk junction bottom _F/m_ _[2]_ 0 2.0E-4 _`AD`_
capacitance _`AS`_
MJ Bulk junction grading coefficient 0,5 0,5
CJSW Zero-bias bulk junction sidewall _F/m_ 0 1.0E-9 _`PD`_
capacitance _`PS`_
MJSW Bulk junction grading coefficient 0.33 0.25
PB Bulk junction potential Y I 0.6
IS Bulk junction saturation current A I x 10- [14] 1.0E-I6
JS Bulkjunction saturation current _Nm_ _[2]_ 0 I,OE-8 _`AD`_
per junction area _`AS`_
CGDO GD overlap capacitance per unit _F/m_ 0 4,OE-II _W_
channel width
CGSO GS overlap capacitance per unit _F/m_ 0 4,OE-II _W_
channel width
CGBO GB overlap capacitance per unit _F/m_ 0 2.0E-1O _L_
channel length
NSUB Substrate doping cm- [3] 0 4,OEI5
NSS Surface state density cm- [2] 0 1.0ElO
NFS Fast surface state density cm- [2] 0 1.0ElO
TOX Thin-oxide thickness m 00 O,lU
TPG Type of gate material
+ 1opposite to substrate
-1 same as substrate

         - Al gate
XJ Metallurgical junction depth m 0 O,5U
LD Lateral diffusion m 0 O,2U
.UO Surface mobility _cm_ _[2]_ _N._ s 600 700


**A.3.1** **DC Model**


The **LEVEL** parameter differentiates and sets the analytical models describing the behavior ofa MOSFET. There are 3 levels in SPICE2 and 6 in SPICE3. Only the equations
for LEVEL==2 and LEVEL==3 are listed; these two models together with the LEVEL==l
model, described in Chap. 3, are available in all SPICE versions.


LEVEL==2:


_1]V_ _[DS]_ _)_
_IDs_ == _f3_ _{ (_ _l:'CS - VBIN -_ -2- _VDS_



_-~YS_ _[(PHI_ + _VDS - VBS)3/2 - (PHI - VBS)3/2])_


where the transconductance and mobility factors are defined by

_w_
_f3_ == _IJ-sCox L_ _-_ _ilL_
_ejf_


_UEXP_
IJ- == _VO_ _VCRITEs;_ _."_

_[_ _Cox(Vcs_ _- VTH -_ _VTRA._ _VDS)_ _]_


The built-in voltage including small-size effects is


7TES'
_VBIN_ == _VFB_ + _PHI_ + _DELTA_ 4 _Cox~(PHI_ _- VBS)_



_(A._ 24)


_(A._ 25)


_(A._ 26)


_(A._ 27)


**386** APPENDIX A SEMICONDUCTOR-DEVICE MODELS


The adjusted and zero-bias threshold voltages are


_VTH_ = _VBlN_ + ')Is ( _JPHI_ _-_ _VBS -_ _JPHI)_

_VTO_ = _VFB_ + _PHI - GAMMA JPHI_


where


')Is = _GAMMA(l_ _-_ _as - aD)_


_IXl_ _Ws_ _)_
_as_ = 2£ _(J_ 1 + 2 _Xl -_ 1


_)_
_aD_ = 2£ _lXl(J_ 1 + 2 _Xl_ _W_ _[D]_ _-_ 1


_Ws_ = _Xd JPHI_ _-_ _VBS_


,
., _2ESi_
_q.NSUB_



_(A._ 28)


_(A.29)_


_(A.30)_



The geometric channel length, _**L,**_ is adjusted due to lateral diffusion, _LD,_ and channel
shortening in saturation:



_Left_ = _L - 2LD_


Ll _ { _LAMBDA_ _. VDS_ if _LAMBDA_ is specified
_L -_ _f(VDSAT)_ if _LAMBDA_ is not specified


The pinch-off saturation voltage is defined by


_-_ _(VGS -_ _VBIN)_
_V_ _DSAT_ _-_
_YJ_



(A.31)


_(A._ 32)


_(A._ 33)


_(A._ 34)


MOSFET **387**


The velocity-saturation-based model derives _VDSAT_ and _ilL_ from the following equations:



_IDSAT - VMAX._ _W._ _Qchan(L)_ = 0


_Qchan_ = _Cox [VGS -_ _VBIN -_ _'l7_ _VDSAT - Ys(PHI_ _-_ _VBS_ + _VDSAT)_ '/2 ]


L.l _AL -_                - X [ _d_ _(X_ _[d]_ _VMAX)2_ 2 + _(V_ _DS -_ _VDSAT)_ + -2-- _Xd_ _[VMAX]_ _]_
JJ-s JJ-s


Subthreshold conduction is modeled when **NFS** is present:


_IDS_ _=f3_ _{(VON -_ _VBIN -_ 'l7~DS _)VDS_



_(A._ 35)


_(A._ 36)


_(A._ 37)



-~YS _[(PHI_ + _VDS - VBS)3/2 - (PHI - VBS)3/2]) eq(VGS-VoN)/nkT_ _(A._ 38)


where


_nkT_
_VON_ = _VTH_ +_q_


_Cis_ _Cd_
_n=l+-+-_
_Cox_ _Cox_

_Cis_ = _q . NFS_ _(A.39)_

_Cd_ = _aQB_
_aVBS_

_d_ _J_ _ays_ _J_ _7TESi_ _)_
= _(_ -Ys _dV_ _PHI -_ _VBS -_ _av_ _PHI -_ _VBS_ + _DELTA -4C_ _Cox_
```
         ~ ~ mW

```

LEVEL=3:


1+ _FB_ _)_
_IDS_ = _f3_ _VGS - VTH -_ ( _-2-VDS_ _VDS_ _(A._ 40)


where


(A.41)


**388** APPENDIX A SEMICONDUCTOR-DEVICE MODELS


_va_
_JLs_ = 1 + _THETA(VGS_ _-_ _VTH)_

_JLs_
_JLejf_ = _JL_
1 + _VMAl._ _Lejf VDs_


The threshold voltage is defined by


where


8.15 X 10- [22]
_a_ = _ETA_ _3_
_CoxLejf_



_(A.42)_


_(A.43)_


_(A.44)_


_(A._ 45)



_Fs_ = 1 _ _Xl [LDLejf_ + _Xl_ _We_ 1 - _(_ 1 + _Wp/Xl Wp/Xl_ )2 _-_ _LD]Xl_ _(A.46)_


_F_ _N_ = _DELTA_ _'TTESi_ _(A._ 47)
_2CoxW_


_(A.48)_


_(A.49)_


_do_ = 0.0631353, _d]_ = 0.8013292, _d2_ = -0.01110777


The saturation model is based on velocity-limited carrier flow:



_VDSAT_ _=_


where



_VGS -_ _VTH_ + _VMAX._ _Lejf_ _(VGS -_ _VTH)2_ + _(VMAX._ _Lejf)2_
1 _+FB_ _JLs_ 1 _+FB_ _JLs_


_EPXd)2_ _EPXd]_
_**ilL**_ = _Xd_ _[_ _(_ -2- + _KAPPA(VDS_ _-_ _VDSAT) -_ -2

_IDSAT_
_Ep=_ _---_
_GDSATLejf_



_(A._ 50)


_(A.51)_


MOSFET **389**


For the BSIM and BSIM2 models, LEVEL=4 and LEVEL=5 in SPICE3, see the
University of California at Berkeley research reports (Jeng 1990; Sheu, Scharfetter,
and Ko 1985).


A.3.2 **Transient and AC Models**


The gate capacitances defined by the Meyer model, _CGS, CGD,_ and _CGB,_ shown graphically as a function of _V_ GS in Figure 3.17, are listed below for the three main regions of
operation of a MOSFET.
In the cutoff region, _V_ GS ::s; _V_ _TH,_ all three capacitances are constant:


_CGB_ = _Cox_ + _CGBO_ _. Leff_



_CGS_ = _CGSO._ _W_

_CGD_ = _CGDO._ _W_


In saturation, _VTH_ < _VGS_ ::s; _VTH_ + _VDs,_ the expressions are


_CGB_ = _CGBO'_ _Leff_
2
_CGS_ = _3CoX_ + _CGSO._ _W_


_CGD_ = _CGDO'_ _W_


In linear operation, _VGS_ - _VTH_ + _VDS,_


_CGB_ = _CGBO'_ _Leff_


_VGS -_ _VDS -_ _VON_
_C_ _[GS]_ = _Cox_ ( 1 - [ _2(VGS _ VON) _ VDS_ ] [2)] + _CGSO._ _W_


_VGS -_ _VON_
_CGD_ = _Cox_ 1 - + _CGDO'_ _W_
( [ _2(VGS _ VON) _ VDS_ ] [2)]


where


_Cox_ = _Cox W . Leff_
C = _€ox€O_
_ox_ _TOX_



_(A.52)_


(A53)


(A 54)



The charge conservation model derives asymmetrical capacitances according to the
following definitions:


_Qchan_ = _QD_ + _Qs_ = _-(QG_ + _QB)_ (A55)


**390** APPENDIX A SEMICONDUCTOR-DEVICE MODELS


QD = _XQC'_ _Qchan_


___ _aQx_ _aQy__
_Cxy -_ _-_ ¥- -                     - _Cyx_
_avy_ _avx_


**A.3.3** **Temperature Model**



(A56)


(A5?)



**In** addition to _Is, cf>],_ and C] which have the temperature dependence described for the
diode, the intrinsic concentration _ni_ and the mobility are adjusted for temperature:



___ _(T)1.5_ _[Q(1.16eV_ _£g)]_
_ni(T)_ _-_ _ni(300)_ 300 exp _2k_ 300 K - _T._


_ni(300)_ = 1.45 X 10 [10] m- [3]


300)1.5
_jL(T)_ = _jL(300)_ _T_ (


**A.3.4** **Noise Model**


The noise contributed by the drain-source current is


j2 = _8kTg_ _[m]_ _D.f_ + _KF._ _I~~ D.f_
_ds_ 3 _fC_ _L_ _[2]_
_ox_ _eff_


**REFERENCES**



(A58)


(A59)


_(A._ 60)



Jeng, M.-C. 1990. Design and modeling of deep-submicrometer MOSFETs. University of California, Berkeley, ERL Memo UCBIERL M90/90 (October).
,Sheu, B. J., D. L. Scharfetter, and P. K. Ko. 1985. SPICE2 implementation of BSIM 'model.
University of California, Berkeley, ERL Memo UCBIERL M85/42 (May).


_**APPENDIX**_ _**B**_


_**ERROR**_ _**MESSAGES**_


A large percentage of aborted simulation runs are due to erroneous input specifications.
This section enumerates all the SPICE2 error and warning messages related to input
specifications. Other SPICE programs flag the same problems as the ones listed below,
but the wording may differ.


**B.1** **GENERAL SYNTAX ERRORS**


***ERROR*:** **UNRECOGNIZABLE** **DATA** **CARD**
This message follows an input statement that starts with a number in the first field. This
error may arise when the continuation character, +, is omitted in the first column of a
continuation statement. This error is fatal.


***ERROR*:** **UNKNOWN DATA** **CARD:** _Name_
_Name,_ that is, the first field of the statement, does not start with any of the accepted key
characters in the first column. An example is the occurrence of two title statements in
the same circuit specification. This error is fatal.


***ERROR*:** **ELEMENT** **TYPE** **NOT** **YET** **IMPLEMENTED**
This error message should hardly ever occur, since it duplicates the previous message.
It is an added protection that ensures that additional element types are implemented
correctly at future times. This error is fatal.


***ERROR*:** **NEGATIVE** **NODE** **NUMBER** **FOUND**
This statement is printed immediately following an input statement that contains a negative node number. This error is fatal.


**391**


**392** APPENDIX B ERROR MESSAGES

```
     *ERROR*: NODE NUMBERS ARE MISSING
```

This error message is printed immediately following an input statement that does not
contain the correct number of nodes for a particular element type. This error message
would occur if, for example, only three nodes are specified for a MOSFET; even if all
bulk terminals are connected to ground, the fourth node must be defined for a MOSFET.
This error is fatal.

```
     *ERROR*: .END CARD MISSING

```

**`*ERROR*:`** **`ILLEGAL`** **`NUMBER--SCAN`** **`STOPPED`** **`AT`** `COLUMN` _number_
A number with an absolute value outside the interval from 10- [35] to 10 [35] has been.
specified.


**8.2** **MULTITERMINAL** **ELEMENT ERRORS**

```
     *ERROR*: MUTUAL INDUCTANCE REFERENCES ARE MISSING
```

A mutual inductance name must be followed by two inductor names starting with the
letter _L._ This error is fatal.

```
     WARNING: COEFFICIENT OF COUPLING RESET TO 1.0
```

A coupling coefficient in excess of 1 must have been specified in the above statement.
The analysis continues with a coupling coefficient of 1.


**`*ERROR*:`** **ZO** **`MUST`** **`BE SPECIFIED`**
A value must be specified for the characteristic impedance of a transmission line. This
error is fatal.

```
     *ERROR*: EITHER TD OR F MUST BE SPECIFIED
```

A value must be specified for either the delay time, _TD,_ or the frequency, _F,_ of a transmission line. This error is fatal.


**8.3** **SOURCE** **SPECIFICATION** **ERRORS**

```
     *ERROR*: VOLTAGE SOURCE NOT FOUND ON ABOVE LINE
```

A current-controlled source requires the name of the voltage source through which the
controlling current flows to be specified. The voltage source name must follow the node
numbers of the source. This error is fatal.


**`*ERROR*:`** **`UNKNOWN`** **`SOURCE`** **`FUNCTION:`** _source-function_
A transient source function is specified. Check the types and abbreviations for transient
source functions. This error is fatal.


ELEMENT, SEMICONDUCTOR-DEVICE, AND MODEL ERRORS **393**


***ERROR*:** **ELEMENT** _Name_ **PIECEWISE** **LINEAR** **SOURCE** **TABLE** **NOT**
**INCREASING** **IN** **TIME**
The time values of the _(ti, Vi)_ coordinates must be in increasing order.


**8.4** **ELEMENT, SEMICONDUCTOR-DEVICE,** **AND MODEL ERRORS**


***ERROR*:** **VALUE** **IS** **MISSING** **OR IS** **NONPOSITIVE**
This error message can follow an element definition statement that is expected to
contain a value. The following elements belong in this category: resistors, capacitors,
inductors, mutual inductors, and controlled sources. Each of these elements must be
accompanied by a positive value. This message may be encountered also following a
semiconductor device definition statement that contains negative geometry parameters,
such as _area,_ l¥, or _L._ This error is fatal.


***ERROR*:** **VALUE** **IS** **ZERO**
This message follows a zero-valued resistor. The solution of nodal circuit equations in
SPICE precludes the use of zero-valued resistors, which lead to infinite conductances.
For convergence reasons it is not advisable to use resistor values less than 1 mf!. This
error is fatal.


***ERROR*:** **UNKNOWN PARAMETER:** _Name_
A parameter name used in an element statement is not valid. Check element statement
for valid parameter names. This error is fatal.


***ERROR*:** **EXTRA NUMERICAL** **DATA ON MOSFET** **CARD**
A MOSFET can have up to eight device parameters. Up to eight values can follow the
model name, which are assigned in order to _L,_ l¥, _AD, AS, PD, PS, NRD,_ and _NRS._ The
number of values in the above line exceeds the maximum number of parameter values.
This error is fatal.


***ERROR*:** **MODEL NAME IS** **MISSING**
A model name is expected to follow the node specification on diode, BJT, JFET, and
MOSFET statements. This error is fatal.


***ERROR*:** **MODEL TYPE** **IS** **MISSING**
Every • **MODEL** statement must contain a model type. This error is fatal.


***ERROR*:** **UNKNOWN MODEL TYPE:** _model-type_
A model type was specified in the above statement that is not one of the eight types
recognized by SPICE2. This error is fatal.


***ERROR*:** **UNKNOWN MODEL PARAMETER:** _Name_
The above parameter name is not supported by the model. This error is fatal.


**394** APPENDIX B ERROR MESSAGES

```
     WARNING: MINIMUM BASE RESISTANCE (RBM) IS LESS THAN TOTAL
```

**`(RB)`** FOR **`MODEL`** _MODname_ **`RBM SET EQUAL`** **`TO RB`**


**`WARNING:`** **`THE VALUE`** **`OF LAMBDA`** **`FOR MOSFET`** **`MODEL,`** _MODname,_ **`IS`**
```
     UNUSUALLY LARGE AND MIGHT CAUSE NONCONVERGENCE

```

**`WARNING:`** **`IN DIODE`** **`MODEL`** _MODname_ **`IBV INCREASED`** **`TO`** _value_ **`TO`**
```
     RESOLVE INCOMPATIBILITY WITH SPECIFIED IS

     WARNING: UNABLE TO MATCH FORWARD AND REVERSE DIODE REGIONS,
```

**`BV`** **=** _value_ **`AND`** **`IBV`** **=** _value_


**8.5** **CIRCUIT TOPOLOGY ERRORS**

```
     *ERROR*: CIRCUIT HAS NO NODES
```

The circuit needs to contain at least one other node than ground.


**`*ERROR*:`** **`LESS`** **`THAN`** **`2 CONNECTIONS`** **`AT NODE`** _number_
At least two elements must be connected at any node.


**`*ERROR*:`** **`NO DC PATH`** **`TO GROUND`** **`FROM`** **`NODE`** _number_
From every node there must be a path to ground in order to find a DC solution.

```
     *ERROR*: INDUCTOR/VOLTAGE SOURCE LOOP FOUND, CONTAINING
```

_Vname_
Such a loop would contradict Kirchhoff's voltage law.


**`WARNING:`** **`ATTEMPT`** **`TO REFERENCE`** **`UNDEFINED`** **`NODE`** _number-NODE_
```
     RESET TO 0

```

**8.6** **SU8C1RCUIT DEFINITION** **ERRORS**


**`*ERROR*:`** **`SUBCIRCUIT`** **`DEFINITION`** **`DUPLICATES`** **`NODE`** _number_
Two terminals (nodes) on the subcircuit definition line have the same number.

```
     *ERROR*: NONPOSITlVE NODE NUMBER FOUND IN SUBCIRCUIT
     DEFINITION
```

All node numbers must be positive numbers.

```
     *ERROR*: SUBCIRCUIT NAME MISSING
```

A name starting with a character must follow the **`word. SUBCKT`** on a subcircuit definition line or the node numbers on an X element, subcircuit instantiation, line.


ANALYSIS ERRORS **395**


***ERROR*:** **SUBCIRCUIT** **NODES MISSING**
Node numbers are expected to follow the subcircuit name on a SPICE2 subcircuit definition line.


***ERROR*:** **UNKNOWNSUBCIRCUIT** **NAME:** _SUBname_
A • **SUBCKT** definition for _SUBname_ referenced by an X element cannot be found in
the circuit deck.


***ERROR*:** **.ENDS** **CARD MISSING**
The end of the circuit deck, • **END** line, has been encountered before all • **SUBCKT** lines
have been matched by • **ENDS** lines; every subcircuit definition must be completed with
an • **ENDS** line.


***ERROR*:** _Xname_ **HAS DIFFERENT NUMBER OF NODES THAN** _SUBname_
The number of nodes on an X line must match the number of nodes on the subcircuit
definition line it references.


***ERROR*:** **SUBCIRCUIT** _SUBname_ **IS** **DEFINED RECURSIVELY**
A subcircuit definition contains an X element that references the subcircuit being defined.


**WARNING: ABOVE LINE** **NOT ALLOWEDWITHIN SUBCIRCUIT- - IGNORED**


**WARNING: NO SUBCIRCUIT** **DEFINITION** **KNOWN--LINE** **IGNORED**


**8.7** **ANALYSIS** **ERRORS**


***ERROR*:** **MAXIMUMENTRY IN** **THIS** **COLUMNAT STEP** _number_ _value_ **IS**
**LESS** **THAN PIVTOL**
Circuit matrix is singular; see Sec. 10.2.1 for detailed examples.


***ERROR*:** **NO CONVERGENCEIN** **DC ANALYSIS.** **LAST NODE VOLTAGES:**
_list_
Failure to find a DC solution; see Chap. 10 for advice on overcoming convergence
problems.


***ERROR*:** **NO CONVERGENCEIN** **DC TRANSFER CURVES AT** _Name_ = _value_
**LAST NODE VOLTAGES:** _list_
Solution failure during a •DC analysis at a specific _value_ of the variable _Name;_ in
SPICE2 increase _ITL2_ and consult Example 10.8.


***ERROR*:** **INTERNAL TIMESTEP TOO SMALL IN** **TRANSIENT ANALYSIS**
The smallest acceptable time step has been reached after repetitively cutting the time
step without converging to a solution; see Chaps. 9 and 10 for more insight.


396 APPENDIX B ERROR MESSAGES


*ERROR*: TRANSIENT ANALYSIS ITERATIONS EXCEED LIMIT OF _number_
THIS LIMIT MAY BE OVERRIDDEN USING THE ITL5 PARAMETER ON THE
.OPTION CARD
The transient analysis is stopped after a preset number of iterations, equal to 5000 in
SPICE2, to give the user the opportunity tojudge the correctness of results and whether
analysis should be continued; set ITL5 = 0 to remove this limit. Many SPICE programs do not have this built-in limit, and when interactivity is available, such as in
SPICE3, the user can monitor the correctness of the solution.


*ERROR*: MEMORYREQUIREMENT EXCEEDS MACHINE CAPACITY MEMORY
NEEDS EXCEED _value],_ _value2_
The analysis of the circuit requires more internal memory than available.


*ERROR*: TEMPERATURE SWEEP SHOULD BE THE SECOND SWEEP
SOURCE, CHANGE THE ORDER AND RE- EXECUTE
In a •DC statement the temperature variable must always be the second variable if
another sweep variable is specified.


WARNING: UNDERFLOW _OCCURREDnumberTIME(S)_


WARNING: UNDERFLOW _numberTIME(S)_ IN AC ANALYSIS AT FREQ

_jreq_ HZ


WARNING: _UNDERFLOWnumberTIME(S)_ IN DISTORTION ANALYSIS AT

_FREQjreq_ HZ
A smaller number than can be represented on the computer was generated during a •DC
•TRAN, •AC, or •DISTO analysis. SPICE has trapped and minimized the effect of the
problem; note that in IEEE format, floating-point arithmetic computation may continue
after an underflow condition leading to the creation and proliferation of out-of-range or
NaNs (not-a-number), quantities.


WARNING: MORE THAN _number_ POINTS FOR _Name_ ANALYSIS, ANALYSIS
OMITTED. THIS LIMIT MAY BE OVERRIDDEN USING THE LIMPTS
PARAMETER ON THE .OPTION CARD
Some SPICE programs limit the number of print/plot points that can be output by
•DC, •TRAN, or .AC analysis. Use the LIMPTS options parameter to override this
limit.


WARNING: NO _Name_ OUTPUTS SPECIFIED ••• ANALYSIS OMITTED
In SPICE2 a •DC, .TRAN, or .AC analysis must be accompanied by a .PLOT or
•PRINT request.


WARNING: TOO FEW POINTS FOR PLOTTING
Toofew points have been computed or requested; the line-printer plot has been omitted.


ANALYSIS ERRORS 397


WARNING: MISSING PARAMETER(S) ••• ANALYSIS OMITTED
Incorrect •DC specification.


WARNING: UNKNOWNFREQUENCY FUNCTION: _Name ••• ANALYSIS_ OMITTED
Frequency variation is limited to LIN, OCT, or DEC; see Chap. 5.


WARNING: FREQUENCY PARAMETERS INCORRECT ••• ANALYSIS OMITTED


WARNING: START FREQ > STOP FREQ ••• ANALYSIS OMITTED


WARNING: TIME PARAMETERS INCORRECT ••• ANALYSIS OMITTED


WARNING: START TIME> STOP TIME ••• ANALYSIS OMITTED


WARNING: ILLEGAL OUTPUT VARIABLE ••• ANALYSIS OMITTED
Incorrect output variable specification in •TF analysis.


WARNING: VOLTAGE OUTPUT UNRECOGNIZABLE ••• ANALYSIS OMITTED
Incorrect noise analysis output specification.


WARNING: INVALID INPUT SOURCE ••• ANALYSIS OMITTED
Incorrect input noise source specification.


WARNING: DISTORTION LOAD RESISTOR MISSING ••• ANALYSIS OMITTED


WARNING: DISTORTION PARAMETERS INCORRECT ••• ANALYSIS
OMITTED


WARNING: FOURIER PARAMETERS INCORRECT ••• ANALYSIS OMITTED


WARNING: FOURIER ANALYSIS FUNDAMENTAL FREQUENCY IS INCOMPATIBLE WITH TRANSIENT ANALYSIS PRINT INTERVAL ••• FOURIER
ANALYSIS OMITTED
Transient analysis interval _(TSTOP_ _- TSTART)_ is less than the period of the fundamental specified on the •FOUR line.


WARNING: OUTPUT VARIABLE UNRECOGNIZABLE ••• ANALYSIS OMITTED
Incorrect sensitivity analysis output specification.


WARNING: UNKNOWNANALYSIS MODE: _Name ... LINE_ IGNORED
The analysis type on a plot or print statement must be one of DC, AC, TRAN, NOISE or
DISTO.


WARNING: UNRECOGNIZABLE OUTPUT VARIABLE ON ABOVE LINE
Incorrect output variable specification on a plot or print statement.


**398** APPENDIX B ERROR MESSAGES


**B.8** **MISCELLANEOUS** **ERRORS**


***ERROR*:** **CPU TIME** **LIMIT** **EXCEEDED ...** **ANALYSIS** **STOPPED**
Some SPICE programs allow the user to set a limit on how long an analysis can run.


**WARNING:** **NUMDGT MAY NOT EXCEED** _number;_ **MAXIMUM VALUE ASSUMED**


**WARNING:** **UNKNOWN OPTION:** _Name_ _•••_ **IGNORED**


**WARNING:** **ILLEGAL** **VALUE** **SPECIFIED** **FOR OPTION:** _Name_ _•••_ **IGNORED**


The following warnings are issued for an incorrect      - NODE SET or • **IC** line.


**WARNING:** **OUT-OF-PLACE** **NON-NUMERIC** **FIELD** _Name_ **SKIPPED**


**WARNING:** **INITIAL** **VALUE MISSING** **FOR NODE** _number_


**WARNING:** **ATTEMPT TO SPECIFY** **INITIAL** **CONDITION** **FOR GROUND**
**IGNORED**


_**APPENDIX**_ **C**


_**SPICE STATEMENTS**_


This appendix lists all the SPICE statements introduced in this text. Statements followed by [SPICE3] appear only in SPICE3.


**C.l** **ELEMENT STATEMENTS**


_Rname nodel node2 rvalue_ < _TC=tc1<tc2> >_

_Rname nodel node2 <rvalue><Mname><L=L><W=W>_ [SPICE3]
_Cname nodel node2 lvalue_ <IC=vco >

_Cname nodel node2_ **POLY** Co CI < _C2 ..._ _><IC=vco >_
_Cname nodel node2 <cvalue><Mname><L=L><W=W><IC=vco_ _>_

[SPICE3]

_Lname nodel node2 lvalue_ <IC=iLO>

_Lname nodel node2_ **POLY** _1_ _0_ II < _1_ _2 ..._ ><IC= _iLO>_
_Vname node1 node2 «DC>devalue><AC_ _<acJnag <ac..phase»>_
_+_ _<TRANjunction_ _<valuel <value2 ..._ »>
_Iname nodel node2_ «DC> _devalue><AC_ _<acJnag <ac..phase»>_
_+_ _<TRANjunction_ _<valuel <value2 ..._ »>


_TRANJunction_ can be one of the following:


PULSE(Vl _V2 <TD <TR <TF<PW<PER»»»_
_SIN(VO_ _VA <FREQ <TD <THETA»»_

**SFFM** _(VO VA <Fe <MDI <FS>_        - > )


**399**


**400** C SPICE STATEMENTS


_EXP(Vl_ _V2 <TDl_ _TAW_ _TD2 <TAU2»)_

**PWL** _(tI VI_ < _tz Vz_ < _t3V3 ..._        - > )

_Kname Lnamel_ _Lname2_ _k_

_Gname n+ n-_ _nc+ nc-_ _gvalue_

_Gname n+ n-_ <POLY _(ndim)_       - nc1 + _nc1-_ < _nc2+ nc2-_ _..._       - _Po_ < PI

+ < _pz ..._ » _<IC=Vncl+,ncl-.vllcZ+,ncZ-,'"_ _>_

_Ename n+ n-_ _nc+ nc-_ _evalue_

_Ename n+ n-_ <POLY _(ndim)_       - nc1 + _nc1-_ < _nc2+ nc2-_ _..._       - _Po_ < _PI_
+ < _pz ..._ » _<IC=Vncl+,llcl-, vncZ+,ncZ-,... >_

_Fname n_ + _n -_ _Vname fvalue_

_Fname n+ n-_ <POLY _(ndim)_       - _Vname1 <Vname2_ _..._       - _Po_ < _PI_ < _Pz ... »_
+ < _IC=i(Vname1_ _), i(Vname2)_ _... >_

_Hname n_ + _n -_ _Vname hvalue_

_Hname n+ n-_ <POLY _(ndim)_       - _Vnamel_ _<Vname2_ _..._       - _Po_ < PI < _pz ..._ »
_+_ _<IC=i(Vnamel),_ _i(Vname2)_ _... >_

_Bname nodel_ _node2_ <VII> _=expr_ [SPICE3]

_Sname n+ n-_ _nc+ nc-_ _Model_ <ON/OFF> [SPICE3]

_Wname n+ n-_ _Vname Model_ <ON/OFF> [SPICE3]

_Tnamenl_ _nz n3 n4 ZO=zO <TD=td> <F=freq <NL=nl_ » _<IC=VIlI,IlZ,_ _ii, VIl3,1l4,iz >_

_Dname n+ n-_ _MODname_ _<area><OFF><IC=VDO_ _>_

_Qname nc nb ne <ns>_ _MODname_ _<area>_ <OFF> < _IC=VBEO,VCEO>_

_Jname_ _nd ng ns MODname_ _<area><OFF>_ < _IC=VDSO,vcso >_

_Mname nd ng ns nb MODname_ _«L=>L>«W=>W><AD=AD><AS=AS>_
+ _<PD=PD> <PS=PS>_ < _NRD=NRD_      - _<NRS=NRS>_ <OFF>
_+_ _<IC=VDSO, vcso, VBSO>_

_Zname nd ng ns MODname_ _<area><OFF>_ < _IC=VDSO,vcso_        - [SPICE3]

_Xname xnodel_ _<xnode2_ _..._        - _SUBname_


**C.2** **GLOBAL** **STATEMENTS**


•MODEL _MODname_ _MODtype_ _<PARAM1=valuel_ _<PARAM2=value2_ _... »_


_MODtype_ can be one of the following:

D Diode model

**NPN** npn BJT model


CONTROL STATEMENTS **401**


PNP pnp BJT model

NJF n-channel JFET model

PJF p-channel JFET model

NMOS n-channel MOSFET model

PMOS p-channel MOSFET model

R Diffused resistor model [SPICE3]

C Diffused capacitor model [SPICE3]

URC Uniform-distributed RC model [SPICE3]

SW Voltage-controlled switch model [SPICE3]

CSW Current-controlled switch model [SPICE3]

NMF n-channel MESFET model [SPICE3]

PMF p-channel MESFET model [SPICE3]


•SUBCKT _SUBname node] <node2 ..._       
•TEMP _temp] <temp2 ..._       

C.3 **CONTROL STATEMENTS**

```
      .OP
```

         - DC _V/Iname] start] stop] step] <V/Iname2 start2 stop2 step2>_
.TF _OUT_varV/Iname_

        - SENS _OUT-var] <OUT_var2 ..._        
.AC DEC/OCTILIN _numptsfstartfstop_

.NOISE V( _n]<,n2»_ _V/Iname nums_

_.DISTORLname_ _<nums <f2/fl_ < _Pre!_ < S2 »»

•PZ _node_in]_ _node_in2 node_outl_ _node_out2_ <CUR/VOL><POL/ZERlPZ>

[SPICE3]

.TRAN _TSTEP TSTOP_ < _TSTART <TMAX»<UIC>_

_•FOURfreq OUT_var] <OUT_var2 ..._       
•PRINT/PLOT _Analysis-TYPE OUT_varl <OUT_var2 ... ><ploLlimits>_


_Analysis_TYPE_ can be one of the following:


DC,AC,TRAN,NOISE,DISTO

.NODESET _V(nodel)=value]_ _<V(node2)=value2_ _... >_

•IC _V(nodel)=valuel_ _<V(node2)=value2_ _... >_

•ENDS _<SUBname>_

•END


_**APPENDIX**_ **D**


_**GEAR INTEGRATION**_
_**FORMULAS**_



Gear 1:


Gear 2:


Gear 3:


Gear 4:


Gear 5:


Gear 6:



_._ _h_ _[2]_ _d_ _[2]_ _x_
_Xn+l =Xn_ + _hXn+l -_ 2 _dt2 (~)_


4 1 _2h ._ _2h_ _[3]_ _d_ _[3]_ _x_
_Xn+l_ = _3_ _[xn ]_ _- 3_ _[Xn]_ _-_ _1_ + _3_ _[Xn]_ _+_ _1_ _-_ 9 _dt_ _3_ _(~)_


18 9 2 _6h._ _3h_ _[4]_ _d_ _[4]_ _x_
_Xn+l_ = _TIxn_ _-_ _TIXn-l_ + _TI_ _[X]_ _n-2_ _-_ _TIXn+l_ _-_ 22 _dt4 (~)_


48 36 16 3 _12h._ _3h_ _[5]_ _d_ _[5]_ _x_
_Xn+l_ = _25_ _[xn ]_ _-_ _25_ _[xn]_ _-_ _[1]_ + _25_ _[xn]_ _-_ _[2]_ _-_ _25_ _[xn]_ _-_ _[3]_ + 25 _Xn+l -_ 125 _dt5_ _(~)_


300 300 200 75 12
_Xn+l_ = _137_ _[xn ]_ _-_ _137_ _[xn]_ _-_ _[1]_ + _137_ _[xn]_ _-_ _[2]_ _-_ _137_ _[xn]_ _-_ _[3]_ + _137_ _[xn]_ _-_ _[4]_


_60h ._ _lOh_ _[6]_ _d_ _[6]_ _x_
_+_ _137_ _[xn]_ _+_ _[1]_ _-_ 137 _dt_ _6 (~)_

360 450 400 225 72 10
_Xn+l_ = _147_ _[xn ]_ _-_ _147_ _[xn]_ _-_ _[1]_ + _147_ _[xn]_ _-_ _[2]_ _-_ _147_ _[xn]_ _-_ _[3]_ + _147_ _[xn]_ _-_ _[4]_ _-_ _147_ _[xn]_ _-_ _[5]_


_60h ._ _180h_ _[6]_ _d_ _[7]_ _X_
_+_ _147_ _[xn]_ _+_ _[1]_ _-_ 3087 _dt_ _7_ _(~)_



**402**


_**APPENDIX**_ _**E**_


_**SPICE INPUT**_ _**DECK**_


**This is an example SPICE input for a differential amplifier from the University of Cal-**
**ifornia, Berkeley, SPICE benchmarks. Most types of statements and analyses are used.**

```
DIFFPAIR CIRCUIT - SIMPLE DIFFERENTIAL AMPLIFIER
```

** `CIRCUIT` `DESCRIPTION`

 - `ELEMENT` `STATEMENTS`

 ```
Ql 4 2 6 QNL
Q2 5 3 6QNL
Q3 6 7 9 QNL
Q4 7 7 9QNL
RSI 1 2 lK
```

`RS2` `3` - `lK`
```
RCI 4 8 10K
RC2 5 8 10K
RBIAS 7 8 20K
```

`VCC` `8` - `12`
`VEE` `9` - `-12`
`VIN` `1` - `SIN(` - `0.1` `SMEG)` `AC` `1`
** `GLOBAL` `STATEMENTS`

```
.MODEL QNL NPN BF=80 RB=100 CCS=2P TF=0.3N TR=6N
```
+ `CJE=3P` `CJC=2P` `VAF=SO`
** `ANALYSIS` `REQUESTS`


**403**


**404** E SPICE INPUT DECK


       ```
       .OP
      .TF V(5) VIN
      .DC VIN -0.25 0.25 0.005
      .AC DEC 10 1 10GHZ
       .TRAN 5N SOON
```

       
       - `OUTPUT` `REQUESTS`

       .pwr DC V(5)
.pwr AC _\!M(5)_ VP(5)
.pwr `TRAN` `V(5,4)`

       
        - END