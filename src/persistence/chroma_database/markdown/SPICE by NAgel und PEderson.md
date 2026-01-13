_**0**_
```
.MODEL Ml NPN BF-35 RB»100 RE-0.1 IS-1.5E-15 FNK-6.6E-16 FNA-1.0

External Models in SPICE
  The ability to define an arbitrary device which contains allowable
elements has been included in SPICE (versions IG and later). Hence

the gate shown in Figure 1 could be defined to be an element in
SPICE just as a bipolar device is a model in SPICE. The restrictions

are:
a. External models cannot be nested, that is, an external model

cannot contain an external model.

b. An external model cannot have more than 20 external nodes (the
gate on the following page has 5 external nodes and three internal

nodes)•

  To define an external model, a group of cards is required. The

first card is a .MODEL card which contains the word .MODEL, the name

of the model, the letter X, and the external nodes of the device.

The following cards are the set of element cards which define the

model card, and the last card is a .FINIS card, which contains simply

 the word .FINIS. The following group of cards defines the TTL gate

shown in Figure 1.

 •MODEL TTLGATE X 1 2 3 4 5 .
 Ql 6 8 1 Ml
 Q2 6 8 2 Ml
 Q3 6 8 3 Ml
 Q4 4 6 7 Ml
 Q5 4 7 0 Ml

                     -12b
```

_**'%**_


```
Rl 5 4 IK
R2 7 0 1.5K
R5 5 8 4K
.MODEL Ml NPN BF*80 RB=50 TF«0;1NS TR-10NS CJC-0.3PF CJE-0.5PF
.FINIS

   Once the model has been defdined, it can be referenced just as an

internal built-in model is referenced. The "device" name must begin

with the letter X. The device is specified by the name, the external

nodes, and the model name. For example, the logic circuit shown in

Figure 2 could be simulated by the following group of cards:

EXAMPLE LOGIC CIRCUIT
VCC 10 0 DC 5
VIN1 1 0 PULSE 0 5 IONS IONS IONS 100NS
VIN2 2 0 PULSE 0 5 200NS IONS IONS 100NS
XG1 1113 10 TTLGATE
XG2 1 1 2 4 10 TTLGATE
XG5 5 2 4 5 10 TTLGATE
.OUT V5 5 0 PLOT TRAN
•TRAN 5NS 500NS
•MODEL TTLGATE 112345
*Q1*6..&.1.M1
Q2 6 8 2 Ml
Q3 6 8 3 Ml
Q4 4 6 7 Ml
Q5 4 7 0 Ml
Rl 5 4 IK '
R2 7 0 1.5K
R3 5 8 4K
.MODEL Ml NPN BF«80 RB=50 TF^O.INS TR-10NS CJC-0.3PF CJE=0.5PF
•FINIS
 •END

                     -12c
```

```
DC Sensitivity Analysis in SPICE
 A dc sensitivity analysis capability was also included in SPICE
(versions IG and later) but never documented. This option is used to
obtain the dc, small-signal sensitivities of a given output variable
with respect to every circuit value. The general format for sensitivity

analysis is:

  .SENS ovar 1 ovar 2. ... ovar 10

Note that from one to ten outputs can be specified. Only one .SENS

card should be used in a deck. The syntax for the output variables
(ovar 1 ... ovar n) is identical to the syntax for output variables

in the .OUTPUT card.

Examples:

   SENS^VOUT .3 .2

   .SENS VI 1 0 V2 2 0 IX VCC

If a .SENS card is included in the SPICE data deck, the program will

compute the dc, small-signal sensitivities (derivatives) at each

specified output variable with respect to every circuit value

(including the dc parameters for BJT model and diode model). There

is no way of selecting specific sensitivities. In the first example,

the program will compute and print the derivative of the voltage

between node 3 and node 2 with respect to every circuit parameter.

                     -12d
```

_1_



_IK_


_Q5_
_R2._
_1-5K._ _[K]_


_/*_


_*6*_
_©_
# _o_


_**<r**_


_-12e-_



_6)_



_©_ _©•_


_MIKd. r*_


_VtKl. f;_



_©_ _/_


_c* 7\_


_K*l_
_©_


_®_



_©_


```
• »

 <• .
```

```
SPICE 1Q, (1 Mar 74)
  The latest version of SPICE, SPICE 1Q, is now released. Versions
1M, IN, 10, and IP were all local versions, so 1Q is the replacement
version for SPICE IL. In contains the following modifications:
1. Overlay organization - The program structure has been
   modified slightly to readily accomodate an overlay
   structure. The program requires a 60000 octal region
   to execute on the CDC 6400 computer at the University
   of California, Berkeley.
2. Distortion analysis - A new analysis algorithm for
   computing the small-signal distortion performance
   of a linear circuit has been implemented. For further
   details on the theory of distortion analysis, see
   Trans. IEEE, Vol. CT-7, November 1973, pp. 709 - 717
   and pp. 742 - 746.
3. Revised .OUTPUT control card - To accomodate distortion
   analysis; and to add some flexibility to the AC analysis
   output, the .OUTPUT format has been modified.
4. Assembly language matrix routines - The matrix decomposition
   and solution routines have been recoded in COMPASS
 . _•., •asseably^languag.c. ...For .CDC users, ..this results in
 "a savings of 10% - 40%. For non-CDC users, the FORTRAN
   code has been included, as comments, in the assembly
   routines, and can be easily reinstated.

5. Addition of the .RUN card - The .RUN control card has been
   added to allow the printing of various execution
   statistics (matrix structure, number of iterations,
   and timing data for each phase of a simulation).
 6. FET convergence - The routines for JFET's and MOSFET's
   have been modified to improve the convergence of
   simulations involving JFET's and MOSFET's.

 7. Small-signal dc transfer curve errors - An error in the
   computation of the dc, small-signal input resistance,
   transfer function, and output resistance has been
    corrected.

 8. Gummel-Poon temperature dependence - An error that caused
    the saturation currents in the Gummel-Poon transistor
   model to be computed incorrectly (as a function of
    temperature) has been corrected.

                        -12f
```

```
   9 Voltage source polarity error - An error that caused the
    '* £iarit?tf voltage sources to sometimes be reversed has
        been corrected.

[ SPICE 1Q 1NP"T FORMAT CHANCES

      1. Distortion analysis
- SPICE will compute the distortion characteristics of
       the circuit in a small-signal mode as a part of the
       ac small-signal sinusoidal steady-state analysis
       if requested. The analysis is performed assuming
       that signals of two frequencies are imposed at the
       input; let the two frequencies be ^ and f2.
       The program then computes the following distortion
           measures:
       HD2 - The magnitude of the frequency component 2 fx
            assuming that f2 is not present.
```

_`HD3`_ _`- The magnitude of the frequency component 3`_ _**f1**_
_`assuming that`_ _**±2**_ _`is not present.`_
```
     ...:&B£2 •— ..The.oftagnitude.of .the..frequency component i^ + f2
       DIM2 - The magnitude of the frequency component fx - f2
       DIM3 - The magnitude of the frequency component 2fx - f2

        All of these distortion measures can be computed at each
       frequency point (value of fx) and printed or Plotted
        (either as REAL and IMAG, or as MAG, DB, and PHASE)
        just as any other output variable. In addition, at
        specified frequencies, the contribution of every nonlinear
        device to the total distortion can be printed.
```

_**\-**_ _`Distortion analysis is specified on the .AC card:`_
```
      •AC DEC 10 1 10KHZ DISTO RLOAD INTER REFPWR SKW2 SPW2

       any legal freq optional - defaults
        variation format supplied if not specified

           KHERE:
         RLOAD - The name of the output load resistor into
              which all distortion power products are
             to be computed (must be specified).

                            -12g
```

```
  INTER - The interval at which the summary P^out
       of the contributions of all nonlinear devices
       to the total distortion is to be printed.
       Zero implies no printout, 1 Implies every point,
      2 implies every other point, 3 implies every
       third point, and so on. Defaults to zero if
        not specified.
  REFPWR - The reference power level used in computing
       the distortion products. If not specified,
       a value of 1 mW (that is, dBm) is used.
   SKW2 - The ratio of f2 to fr If not specified,
       a value of 0.9 is used (i.e., f2 - 0.9 fx).
   SPW2 - The amplitude of f2. A value of 1.0 is used if
        not specified.
EXAMPLE: .AC DEC 10 1.0 100K DISTO RL 2 1.0E-3 0.95 0.75

2. Output options (.OUTPUT card)
  Some new options have-been added to the .OUTPUT card to
  accomodate distortion analysis and improve output for
   AC analysis:
..AqiUPUT.Vxxxxxx.Nl N2 .PRINT (options) .PLOT^(options)
     Ixxxxxx Vyyyyy "
     0N0ISE either print or plot or both can
     RINOISE be deleted
      HD2
      HD3
      SIM2
      DIM2
      SIM3
The output variable Vxxxxxx is a voltage output (Nl is the
 positive node, and N2 is the negative node), Ixxxxxx is a
 current output (Vyyyyyy is the voltage source the current is
 flowing in), 0N0ISE is the output noise computed in the
 noise analysis, RINOISE is the reflected input noise computed
 in the noise analysis, and HD2, HD3, SIM2, D1M2, and DIM3
 are the distortion measures mentioned in distortion analysis.

 The options available are:

    DC dc analysis output
    TR transient analysis output
   MAG ac analysis output, magnitude
   DB *c analysis output, magnitude (in dB)
    PHS ac analysis output, phase
    RE ac analysis output, real part
    IM ac analysis output, imaginary part

                        -12h
```

```
Some output examples:
To plot a transient response of node voltage 4

.OUTPUT V4 4 0 PLOT TR
To print and plot the dc transfer curve for node voltage 17
and the bode plot for node voltage 17
.OUTPUT V17 17 0PRINT DC^lAG DB PHS PLOT MAG DB PHS DC
To plot the output noise and equivalent input noise in both
volts and dB:

.OUTPUT ONOISE PLOT MAG DB
.OUTPUT RINOISE PLOT MAG DB
To plot the distortion measures HD2, HD3, DIM2, and DIM3:

.OUTPUT HD2 PLOT DB PHS
.OUTPUT HD3 PLOT DB PHS
.OUTPUT DIM2 PLOT DB PHS
 .OUTPUT DIM3 PLOT DB PHS

3. .RUN card - If a .RUN card is included in the input deck,
        -*~the -program will print matrix statistics,
         circuit statistics, and timing information.
   . . This data is not printed if the .RUN card is
            absent.

                        -12i
```

```
•. i

```

```
MUTUAL INDUCTORS

  SPICE 1Q also contains provision for specifying a
coupling between inductors in the circuit. A mutual
inductance is specified by the following card:

uxxxxxx Lyyyyyy Lzzzzzz value
The name must begin with a U. Lyyyyyy and Lzzzzzz are the
two coupled inductors, and 'value1 is the value of mutual
inductance between the inductors. The coefficient of

coupling/ k, is defined by:

            M
    k « _
       Li L2
```

_`where M is the mutual inductance/ and`_ _**l1**_ _`and L2 are the`_
```
values of inductance for the two coupled inductors.
This coeff.detent of ..coupling, must..always Jxe l*ss tnan
unity.in absolute value. A negative value of M inverts
the direction in which current flows. The following data
deck defines an ac analysis of the simple transformer cir

cuit shov/n below.

```

```
TEST OF MUTUAL INDUCTANCE
II 0 1 AC 1
KIN 1 0 IK
LI 1 0 1UH
L2 2 0 1UH
U12 LI L2 0.99UH
RLOAD 2 0 IK
•AC DEC 10 10 100KHZ
.OUTPUT VI 1 0 PLOT MAG PHS
.OUTPUT V2 2 0 PLOT MAG PHS
• END

```

```
11

 -12j
```


_**LZ,**_ _`ffft.L*AD`_


_**y**_
_I_


```
          TYPICAL BJT AND FET PARAMETERS
  For bipolar transistors, forward and inverse current gains, output
conductance or Early voltage, and emitter saturation current are measured
at . typical active region operating point. Collector series resistance
1. measured at' atypical saturated region operating point. Base series

```

```
resistance is calculated from mask dimensions and base sheet resistance.

```

```
The three depletion layer capacitances are calculated at aero bias from

```

```
mask dimensions and process specifications. Forward and inverse transit

```

```
times are calculated from these capacitances (under bias) and measured
values of forward and inverse current gain-bandwidth (fj). taken at a
typical operating point. These eleven parameters are adequate to char
acterize integrated circuit bipolar transistors in almost all analog and
digital applications. Representative values for a small IC transistor

                                              * * • •
 are given in Table I.
  Once these parameters are known for one transistor made by a given
 process, parameters for devices of differing mask geometry may be deter
 mined without further measurements. Current gains, Early voltage, and
 transit times are to first order independent of mask geometry for npn
.IC transistors. Emitter saturation current, junction capacitances, and
 series resistances are simple functions of mask dimensions and process
 specifications. The most troublesome parameters in this scaling process
 are the inverse current gain and inverse transit time; due to the trend
 toward non-saturating and Schottky clamped circuits, the significance of
 these parameters is decreasing. In such circuits, inverse parameters
 have virtually no influence on circuit performance.

                       -12k
```

```
  This approach to modeling bipolar IC components usually will
produce circuit simulation results accurate to within .05 Vin DC
levels and to within 102 in time and frequency domain characteristics.
Substantially more effort is needed to reduce errors by a factor of

two.
  A similar approach works well for MOS transistor model parameter
determination. Asample device made by the chosen process is evaluated.
 Threshold voltage, gain factor (k or Beta), body effect coefficient,
 and output conductance or Early voltage are measured. The five inter electrode capacitances are calculated from mask dimensions and process
 specifications. Source-body and drain-body capacitances are those of
 normal pn junctions. Gate area and oxide capacitance determine the
 total capacitance from gate to source, body, and drain. This capacitance
```

_**.may**_ _`be divided into two or three parts.`_ _`For static MOS circuits,`_
```
 dividing this capacitance into equal, constant gate-source and gate drain components is simple and adequate. For dynamic circuits (particularly
 the ratioless type), gate capacitance should be divided into three

 voltage-dependent parts. Representative parameters for a small p
 channel silicon-gate MOS transistor are shown in Table II.

   Parameters for other MOS transistors, differing in mask geometry
 from the sample device, are obtained by scaling. Gain factor and
 capacitances are simple functions of geometry; the other parameters

 are independent of geometry in first-order approximation.

                       -12£
```

```
           FORWARD BETA 10°
```

_`• INVERSE BETA`_ _`f -16`_ _**'**_
_**"**_ _`v`_ _`EMITTER SATURATION`_ _`CURRENT`_ _`2 x 10`_ _`A`_
```
           EARLY VOLTAGE 50 V .
      ' " COLLECTOR SERIE£ RESISTANCE 50 ft
V.' BASE SERIES RESISTANCE 50 ft
```

_`FORWARD TRANSIT TUB`_ _**'**_ _`0.3 nS`_
```
            INVERSE TRANSIT TIME . 10 nS
           EMITTER JUNCTION CAPACITANCE 0.5 pF
           COLLECTOR JUNCTION CAPACITANCE • 0.5 pF
           SUBSTRATE JUNCTION CAPACITANCE . 1.0 pF

                           TABLE I

           CHANNEL WIDTH TO LENGTH RATIO ' .1.0
```

_`THRESHOLDGAIN FACTOR VOLTAGE`_ _22_ _uA/V*V_
_`BODY EFFECT`_ _0.75 V1'*_
_`EARLY VOLTAGE`_ _50 V_
_`SOURCE-BODY CAPACITANCE`_ _0.05 pF_
_`DRAIN-BODY CAPACITANCE`_ _0.05 pF_
_`GATE-SOURCE CAPACITANCE`_ _0.01 pF_
_`GATE-DRAIN CAPACITANCE`_ _0.01 pF_
_`GATE-BODY CAPACITANCE`_ _-0_

```
                          TABLE II

                               -12m
```

_\\_ _w_


```
                 REFERENCES

```

_`W. J. McCalla and W. G. Howard. Jr.,`_ _**y»*-***^£f***_
```
Nonlinear DC Analysis of Bipolar Transistor Circuits, IEEE^K
Solid State Circuits, vol. SC-6, Feb. 1971, pp. 14-1*.

```

```
121 L Nagel and R. Rohrer, "Computer Analysis of Nonlinear Circuits,
11 kcludlng^adiation (CANCER)." TIM J. Solid State Circuits, vol.
   SC-6, Aug. 1971. pp. 166-182.
```

_`Ml`_ _**v**_ _`S Jenkins and S. P. Fan, 'TIME — A Nonlinear DC and Time`_
_`131`_ _`^in C^itTimuiation Program."`_ _**ITT,?,**_ _`J. Solid State Circuits,`_
```
   vol. SC-6, Aug. 1971, pp. 182-188.

```

```
[4) T. E. Idleman, F. S. Jenkins, W. J. McCalla. and D. 0. person,
1 "SLIC - A Simulator for Linear Integrated Circuits IEEE^
   Solid State Circuits, vol. SC-6, Aug. 1971, pp. 188-203..

```

```
l5] R. A. Rohrer. L. W. Nagel. R. Meyer, and L. Weber. "Computationally
   Efficient Electronic Circuit Noise Calculations," IEEE J. Solid
   State Circuits, vol. SC-6, Aug. 1971, pp. 204-213.

```

```
[6] H. Shichman and D. A. Hodges, '•Modeling and Simulation of In-lated   Gate Field-Effect Transistor Switching Circuits.'IEEE J. Solid
   State Circuits, vol. SC-3. Sept. 1968, pp. 285-289.

```

```
171 a D Berry. "An Optimal Ordering of Electronic Circuit Equations
```

_`11`_ _`for a`_ _**lllVae**_ _`Matrix Solution." tIpp. Tr»ns. Circuit Theory, vol.`_
```
    CT-18, Jan. 1971, pp. 40-50.
```

_`[8]`_ _`R. Meyer, L. Nagel. and S. I. Lui, "Computer Simulation of`_ _**&**_
```
   Noise Performance of Electronic Circuits," to appear, IEEE J. Solid
    State Circuits, Dec. 1973.
[9]"" P. E.Gray, et al., Physical Electronics and Circuit Models of
    Transistors, SEEC, Vol. II, Wiley, Chicago, 1964.
[10] J. J. Elbers and J. L. Moll, "Large Signal Behavior of Junction
   Transistors," Proc. IRE, vol. 42, Dec. 1954, pp. 1761-1772.
[11) J. M. Early, "Effects of Space-Charge Layer Widening in Junction
   Transistors," Proc. IRE, vol. 46, Nov. 1952, pp. 1141-1152.
[12) W. M. Webster, "On the Variation of Junction Transistor Current
    Cain Amplification Factor with Emitter Current," Proc. IRE,
    vol. 42, June 1954, pp. 914-920.

```

```
[13) C. T. Kirk, Jr., "A Theory of Transistor Cutoff Frequency (O at
   High Current Densities," IRE Trans. Electron Devices, vol, Et>-9,
    Mar. 1962, pp. 164-174.
1141 R. J. Whittler and D. A. Tremere, "Current Cain and Cutoff
   Frequency Falloff at High Currents," IEEE Trans. Electron Devices,
    vol. ED-16, Jan. 1969, pp. 39-57.
[15] C. T. Sah, R. N. Noyc'e, and W. Shockley, "Carrier Generation and
1 J Recombination in p-n Junctions and p-n Junction Characteristics,
    Proc. IRE, vol. 45, Sept. 1957, pp. 1228-1243.
[16) H. K. Gummel. "A Charge Control *eUtion for Bipolar Transistors."
I J »ell System Tech. J., vol. 49, Jan. 1970. pp. 115-120.
tl71 H K. Gummel and H. C. Poon, "An Integral Charge Control Model of
II Sipoiar^ansistors." lall System Tech. J.. vol. 49. May/June 1970.
    pp. 827-852.

```

```
[18]

[19)

```

```
R I. Dowell. "Automated Biasing of Integrated Circuits." Ph.D.
Thesis. University of California, Berkeley, March 1972.
I. B. Getreau, "Low-Voltage, Micropower Integrated Amplifiers,"
Ph.D. Thesis, University of California, Berkeley, March 1972.

```

```
'* t

```

```
[20] W. J. McCalla and D. 0. Pederaon, ^«*f• of ^u^f*£* i97l.
   Circuit Analysis," IEEE Trans. Circuit Theory, vol. CT-18, June x97l,
    pp. 14-26.
[211 C. W. Gear, "The Automatic Integration of Stiff Ordinary Differentia
11 Equations,1 Information Processing 68, A. J. H. Morrell, Ed.,
    Amsterdam, the Netherlands, 1969, pp. 187-193.
!7?1 * K Bravton F. G. Gustavson, and G. D. Hachtal, "The Use of
11 SariabSeKr Sarlabie-Step Backward Differentiation Methods for
   Nonlinear Electrical Networks," New Mexico 1971 International
    IEEE Conf. Systems. Networks, and Computers, Oaxtepec, Mexico,
    pp. 102-106.
[23] D. Frohman-Bentchskowsky and L. Vadasz, "S^^^S^^sS^
    Characterization of Digital MOS Integrated Circuits, IEEE J. Solid
    State Circuits, vol. Sfc-3, Sept. 1968, pp. 285-289.
[24] A. S. Grove, Physics and Technology of Semiconductor Devices, New
    York, Wiley, 1968.

```

_TABLE 1_


_**'-**_ _BJT MODEL PARAMETERS FOR SHUNT-SERIES FEEDBACK AMPLIFIER_

_**\[**_ _EBERS-MOLL_ _GUMMEL-POON_



_$-_ _75_ _***m**_
_F_ _i_ _*,_



_100_



_F_ _i_ _*,_ _1_

_*r_ _,/_ _**™**_ _^-14_
_I„R_ _1AU_ _**.**_ _0X10-14 X XU_ _*SXr_ _1«10_
_s_



_0_


_0_


_0_



_*c_ _0_
_O r_
_r_ _e_
_e_ _r_ _100_
_t._ _1 ns_ _C2_
_xRF_ _.ft°_ _*kt_



_F_ _.ft_ _t_ _3mA_



_2_



_c68_ _o_ _c4_ _0o_
_„jC°_ _1 nF_ _I_ _infinite_
_Cjco_ _1PF_ _*»_ _2_



♦e _e_ _i_

_*_ _"'_ _21_



_1 ns_
♦- _X_ _TF_



_c_ _0_
_VA_ _5050_ _TR_ _°_



_0_


_0_



_Ccs_
_Cjeo_ _0_

_lpF_

_Cjco_
_V_ _50_
_A_
_y__ _infinite_



_lpF_



_B_



_1_


_0.5_


_1_


_0.5_



_Te_


_m_
_e_

♦c


_m_
_c_



_-15-_


```
                   TABLE 2

       EXECUTION TIMES FOR SN7400 TTL INVERTER
       (27 NODES, 8 BJT1 S, 101 TIMEPOINTS)

         READIN °-A2 6ec

          SETUP °*08 sec
         DC ANALYSIS 0.52 sec
            (ITERATIONS) (22>
         TRANSIENT 7#26,!?!L
            (ITERATIONS) • C340)

                                0.92 sec
             OUTPUT

          TOTAL 9-20 8ec

TIME PER NEWTON ITERATION:

TIME PER NEWTON INTERATION PER BJT:

```

```
21.4 msec

 2.7 msec

```

```
 •• \

```

**\** `I` _**/**_
```
                            TABLE 3

                   EXECUTION TIMES FOR 741 OP AMP
               (49 NODES, 22 BJTS, 101 TIMEPOINTS)

```

```
             READIN

             SETUP

            DC ANALYSIS
              (ITERATIONS)

             TRANSIENT
              (ITERATIONS)

             OUTPUT

             TOTAL

TIME PER NEWTON ITERATION:

TIME PER NEWTON INTERATION PER BJT:

```

```
0.8 sec

 0.5 sec

 0.9 sec
  (12)

13.6 sec
  •(203)

 0.9 sec

16.7 sec

```

```
67 msec

 3 msec

```

_._ _1_
_r*_


_•*_ _^_


```
                                                      • CONTROL
             PROGRAM
               /

                           L

INIPUT DC; AND

```

```
SETUP ANALYSIS
       1

```

_Figure 1_


_-18-_


```
ERROR TRANSIENT OUTPUT

```

```
CHECKING ANALYSIS

        •

        SPA RSE SIAALL
        MATRIX SIGNAL

```

```
.
```

_1_


_C_


_o_



_*.._ _•_ _**/**_


_B_



_VftC_ _-_


_Figure 2_


_.10._



_Vce_


_Is_ _to_



_800_



_Figure 3_


_Figure 4_


_I*-1* *_


_~lt_
_10_
_*•*_ _**»_ _goo_


_Figure 5_


_«_ _:_



_2*_
_ll_ _•_




_o_

_o_



_**I**_ _**-f**_



_H_


_t_
_•4_ _e_


_•A_
_I_
_+_ _O_


_.>_ _**\**_


_VI_
_%_


_4_
_+_ _'ft_


_7_


_Figure 6_


_**#**_


_Figure 7_


_-24-_


_**o**_

_o_

_>_



_i_ _:_ _'._



_Figure 6_


_-25-_


_%_ _**%**_



_**9i**_
_I_



_**%**_


_H_


_.._ _•»_


_**1**_


_in_


_rr_


_ff_



_Figure 9_


_«9A-_


_D_

_e_



_rji_



_Qto_



_6_ _o_



_I*o_


_t*_

_+_ _v a©_


_Figure 10_


__M__



_+_


_vos_


_/_



_8*_


_**/**_ _iMM_




_•_ _V«.s_



_-Vt._



_Figure 11_


_(A_



_0_
_H_



_Figure 12_



_**\4**_


_o_


_o_



_Cm_



_**/**_



_Qft©_
_u_
_I»D_



_6_ _*•_



_+_ _V&o_ _-_ _w—_


_Vos ©I_



_-e_



_+_ _VW_ _-_


_Cos_ _[•W]_


_C&&_




_-_ _Vas_
_KH_


_z«s_
_0_
_Qas_



_6_


_Figure 13_


_-30-_


_*_ _._



_**%**_ _I_ _»_ _I_ _I_ _I_ _I_ _i_ _II_ _v«$_


_-5_
_-lo_


_**fy**_ _t_ _0*1_ _i>*^_


_Figure 14_


_**/**_



_APPENDIX_


```
                                     PAGE 11

PARAMETER DEFAULT TYPICAL

SAT CURRENT/I0EAL B-E SAT CURRENT 100 100
SAT CURRENT/IOEAL B-C SAT CURRENT 1 0.1
BASE OM*!C RESISTANCE ... 0 100
COLLECTOR OHMIC RESISTANCE 0 10
EMITTER OHMIC RESISTANCE 0 1
COLLECTOR-SUBSTRATE CAPACITANCE 0 2PF
FORWARO TRANSIT TIME 0 0.1NS
REVERSE TRANSIT TIME 0 IONS
ZERO BIAS B-E JUNCTION CAPACITANCE .0 2PF
ZERO BIAS B-C JUNCTION CAPACITANCE 0 IPF
SATURATION CURRENT l.OE-14 l.OE-14
FORWARO EARLY VOLTAGE INFINITE 50
REVERSE EARLY VOLTAGE INFINITE 50
NONIOEAL B-E SAT CURRENT/SAT CURRENT 0 1000
FORWARO RNEE CURRENT . ._ . INFINITE 10MA
B-E EMISSION COEFFICIENT 2*0 1.5
NONIOEAL B-C SAT CURRENT/SAT CURRENT 0 1.0
REVERSE RNEE CURRENT INFINITE 100NA
B-C EMISSION COEFFICIENT 2*0 1*5
B-E JUNCTION POTENTIAL 1.0 O.T
B-E GRADING COEFFICIENT 0.9 0.33 ...
B-C JUNCTION POTENTIAL 1-0 0.5
B-C GRAOING COEFFICIENT 0.5 0.33
```

_`ENERGY GAP`_ _`l.H`_ _`1-"`_ _**™**_ _`J«`_
```
                                  0.6T FOR GE

```

```
 1
 2
 3
 4
 9
 6
 T
 8
 9
10
II
12
13
14
19
16
IT
18
19
20
21
22
21
24

```

```
NAME

 BFN
 BRN
 RB
 RC
 RE
 CCS
 TF
 TR
 CJE
 CJC
 IS
 VA
 VB
 C2
 IK
 NE
 C4
 IRR
 NC
 PE
 NE
" PC "
 MC
 EG

```

```
V

```

```
 --~«_JFET N00ELS..I00TH N ANO P CHANNEL! ... ._.
    THE JFET NOOEL IS OERIVEO FRON THE FET NODEL OF SHICHMAN AND HODGES. THE
  OC CHARACTERISTICS ARE OEFINEO BY THE PARAMETERS VTO AND BETA. WHICH DETERMINE
  THE VARIATION OF ORAIN CURRENT WITH GATE VOLTAGE. LAMBDA. WHICH DETERMINES THE
```

_`OUTPUT CONDUCTANCE. AND IS. THE SATURATION CURRENT OF THE TWO GATE`_ _**mmmtkmttm**_ _`..`_
```
  JUNCTIONS. TWO OHMIC RESISTANCES. RO AND RS. ARE INCLUDEO. CHARGE STORAGE IS
" MODELEO BY NONLINEAR DEPLETION LAYER CAPACITANCES FOR BOTH GATE JUNCTIONS WHICH
  VARY AS THE -1/2 POWER OF JUNCTION VOLTAGE AND ARE OEFINEO BY THE PARANETERS
  COS, CGO. ANO PB.

```

```
NAME PARAMETER

 VTO THRESHOLD VOLTAGE
 BETA TRANSCONDUCTANCE PARAMETER
 LAMBDA CHANNEL LENGTH MODULATION PARAMETER
 RD DRAIN OHMIC RESISTANCE
 RS SOURCE OHMIC RESISTANCE
 CGS ZERO BIAS G-S JUNCTION CAPACITANCE
 CGO ZERO BIAS G-0 JUNCTION CAPACITANCE
 PB GATE JUNCTION POTENTIAL
 IS GATE JUNCTION SATURATION CURRENT

```

```
DEFAULT TYPICAL

```

```
 -2.0
1.0E-4
  0
   0
   0
   0
   0
   1
l.OE-14

```

```
 -2.0
l.OE-3
1.0E-4
  100
  100
 5PF
" IPF
  0.6
l.OE-14

```

