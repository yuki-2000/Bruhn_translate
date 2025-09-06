



**ANALYSIS AND DESIGN**


**OF**


**FLIGHT** **VEHICLE** **STRUCTURES**


TRI-STATE OFFSET COMPANY


![](images/73-Bruhn-analysis-and-design-of-flight-vehicles.pdf-1-full.png)
**ANALYSIS** **AND** **DESIGN**


**OF**


**FLIGHT** **VEHICLE** **STRUCTURES**


**By**


**E. F. Bruhn, B.** **S.,** **M.S., C.E.**


**Professor (Emeritus)** **of** **Aeronautics and Astronautics**


**Purdue University**


Assisted by the following persons and
the chapters and parts they contributed:


DR. R. J. H. BOLLARD, (Chapters A24, A25, A26)
_Head,_ _Department_ _of_ _Aeronautics_ _and_ _Astronautics_
University of Washington, Seattle, Washington


LLOYD E. HACKMAN, (Chapters C12)
_Consultant_ _on_ _Composite_ _Structures Engineering_


DR. GEORGE LIANIS, (Chapter A18)
_Professor_ _of_ _Aeronautics_ _and_ _Astronautics_
Purdue University


WILLIAM F. McCOMBS, (Chapter CIO-Part 2, Chapter CllPart 2, Chapter D3)


DR. A. F. SCHMITT, (Chapters A7, A8, A16, A17, A22)
Litton Systems, Inc.


CLARENCE R. SMITH, (Chapter C13)
_Engineering_ _Consultant_ _on_ _Fatigue_ _of_ _Metals_ _and_ _Structures_


DR.JOSEPHA. WOLF,JR., (ChapterA23)
_Senior Research Engineer_
General Motors Research Laboratories


Copyright 1973 by E. F. Bruhn


All rights reserved. including the right of
reproduction in whole or in part in any form.


Portions previously published
under the following titles
"Analysis and Design of Aircraft Structures"
by E. F. Bruhn
"Analysis and Design of Flight Vehicle Structures"
by E. F. Bruhn


Published and Distributed by
Tri-State Offset Company


Printed in U.S.A.


**PREFACE**


The 1965 edition of the book "Analysis and Design of Flight Vehicle Structures", contained
over 950 pages. As time passes it is normal to expect expanded or new material to be added to later
editions of a book. Thus it appeared desirable to add some 380 pages of additional material, which
meant that a new edition would contain over 1300 pages or too large for a single volume. A decision
was made to issue the new edition in two volumes. This two volume edition was practically ready
for binding, when a further final decision was made to remain with one volume edition and place the
380 pages of new material referred to above in 3 separate, rather small sized books, Information on
these 3 separate books is given on the 3 pages following the Table of Contents. The reader will note
that these 3 books deal with special subjects in the structural design field and are available.


This new 1973 one volume edition presents 2 major changes from the 1965 edition. Chapter
A23 has been completely revised and expanded by a new co-author, namely, Dr. Joseph A. Wolf,
formerly on the faculty of UCLA and now with the General Motors Research Laboratories. Dr. Wolf
had the cooperation of Dr. A. F. Schmitt, the author of the A23 Chapter in the 1965 edition. The
other major change is the replacement of Chapter C13 on the subject of fatigue in the 1965 edition
by a new chapter on fatigue. The Author of this new C 13 is C. R. Smith, a widely known
authority in the broad field of fatigue of materials and structures.


This author expresses his thanks to the several co-authors for checking over their material. Only

minor corrections have resulted from this check.


A considerable amount of material in various chapters by the author made use of reports, manuals, drawings and photographs supplied to the author by many aerospace companies, in particular,
Boeing of Seattle; Douglas Co.; General Dynamics, Fort Worth and San Diego Divisions; Martin
in Denver; North American Aviation, Columbus and Tulsa Divisions; and the Vought Division of
LTV Corp. The author is deeply grateful for this assistance and cooperation.


As a final note, if any reference in the Chapters of this book refers to Volume 2 it should
be discarded by the reader.


June 1973


![](images/73-Bruhn-analysis-and-design-of-flight-vehicles.pdf-5-full.png)

1


1


1


1


1


1


1


1


1


1


1


1


1


1


1


1


1


1


1


1


1


1


1


1


1


1


1


1


1


1


1


1


1


1


1


1


1


1


1


1


1


1


1


1


1


1


1


1


1


1


1


1


1


1


I


**T** **ABLE** **OF** **CONTENTS**


Chapter No.


A1 The Work of the Aerospace Structures Engineer.


**STATICALLY** **DETERMINATE** **STRUCTURES**


(Loads, Reactions, Stresses, Shears, Bending Moments, Deflections)


A2 Equilibrium of Force Systems. Truss Structures. Externally Braced Wings. Landing Gear.
A3 Properties of Sections - Centroids, Moments of Inertia, etc.
A4 General Loads on Aircraft.

A5 Beams - Shear and Moments. Beam - Column Moments.

A6 Torsion  - Stresses and Deflections.

A7 Deflections of Structures. Castigliano's Theorem. Virtual Work. Matrix Methods.


**THEORY** **AND** **METHODS FOR SOLVING** **STATICALLY**

**INDETERMINATE** **STRUCTURES**


A8 Statically Indeterminate Structures. Theorem of Least Work. Virtual Work. Matrix Methods.
A9 Bending Moments in Frames and Rings by Elastic Center Method.
Al0 Column Analogy Method.
A 11 Continuous Structures  - Moment Distribution Method.

A 12 Slope Deflection Method.


**BEAM BENDING** **AND** **SHEAR STRESSES.**

**MEMBRANE STRESSES. COLUMN** **AND** **PLATE** **INSTABILITY.**


A 13 Bending Stresses.
A 14 Bending Shear Stresses - Solid and Open Sections - Shear Center.
A15 Shear Flow in Closed Thin-Walled Sections.

A 16 Membrane Stresses in Pressure Vessels.

A 17 Bendi ng of Plates.
A18 Theory of the Instability of Columns and Thin Sheets.


**INTRODUCTION TO PRACTICAL** **AIRCRAFT** **STRESS ANALYSIS**


A 19 Introduction to Wing Stress Analysis by Modified Beam Theory.
A20 Introduction to Fuselage Stress Analysis by Modified Beam Theory.
A21 Loads and Stresses on Ribs and Frames.

A22 Analysis of Special Wing Problems. Cutouts. Shear lag. Swept Wing.
A23 Analysis by the "Method of Displacements".


**THEORY** **OF ELASTICITY AND** **THERMOELASTICITY**


A24 The 3-Dimensional Equations of Thermoelasticity.
A25 The 2-Dimensional Equations of Elasticity and Thermoelasticity.
A26 Selected Problems in Elasticity and Thermoelasticity.


Chapter No.



**TABLE OF CONTENTS Continued**


**FLIGHT** **VEHICLE** **MATERIALS** **AND** **THEIR** **PROPERTIES**



B1 Basic Principles and Definitions.
B2 Mechanical and Physical Properties of Metallic Materials for Flight Vehicle Structures.


**STRENGTH OF STRUCTURAL ELEMENTS** **AND** **COMPOSITE STRUCTURES**


C1 Combined Stresses. Theory of Yield and Ultimate Failure.
C2 Strength of Columns with Stable Cross-Sections.
C3 Yield and Ultimate Strength in Bending.
C4 Strength and Design of Round, Streamline, Oval and Square Tubing in Tension, Compression, Bending,
Torsion and Combined Loadings.
C5 Buckling Strength of Flat Sheet in Compression, Shear, Bending and Under Combined Stress Systems.
C6 Local Buckling Stress for Composite Shapes.
C7 Crippling Strength of Composite Shapes and Sheet-Stiffener Panels in Compression. Column Strength.
C8 Buckling Strength of Monocoque Cylinders.
C9 Buckling Strength of Curved Sheet Panels and Spherical Plates. Ultimate Strength of

Stiffened Curved Sheet Structures.

C10 Design of Metal Beams. Web Shear Resistant (Non-Buckling) Type.
Part 1. Flat Sheet Web with Vertical Stiffeners. Part 2. Other Types of Non-Buckling Webs.
Cll Diagonal Semi-Tension Field Design.
Part 1. Beams with Flat Webs. Part 2. Curved Web Systems.
C12 Sandwich Construction and Design.
C13 Fatigue.


**CONNECTIONS** **AND** **DESIGN DETAILS**


Dl Fittings and Connections. Bolted and Riveted.
D2 Welded Connections.

D3 Some Important Details in Structural Design.


Appendix A Elementary Arithmetical Rules of Matrices.


SPECIAL BOOKS NOW AVAILABLE


As explained in the preface, instead of changing to a 2 volume edition in order to include 380
pages of new material, it was decided at the last minute so-to-speak, to remain with one volume and
issue this new material on three different subjects as separate books. A description of these 3 books
follows:


ENGINEERING COLUMN ANALYSIS

By

**WILLIAM** F. McCOMBS

Senior Structures Design Specialist


Vought Aeronautics Div. of LTV Corp., Dallas, Texas


"Engineering Column Analysis" has been written to provide the engineer with practical
methods for analyzing nearly all types of columns and beam-columns, including those on elastic
supports and these loaded into the plastic range of the material. The book has been written in such
a manner that no prior study of elastic stability theory is necessary. The only prerequisite is an
understanding of elementary strength of materials as given in undergraduate engineering courses.


The numerous methods and techniques of analysis are presented for "hand solutions" by the
engineer, but these can, of course, be arranged for analysis by computer if desired. The broad scope
of the book is indicated by the following list of Part titles. References are also provided for further
reading on specific subjects. Much of the material has been used by the author in classes for practicing engineers in the aircraft industry. It is often surprising to one how easily many seemingly
complicated columns or beam-columns can be analyzed for engineering purposes.


Part Title


A A Survey of Various Column Problems.

B Stability and Critical Loads.

C Columns of Constant Section and Single Span.

D Columns of Variable Section and Single Span.

E Beam-Columns of Constant Section and Single Span.

F Multiple Beam-Columns of Constant Between Supports.

G Multispan Columns of Constant Section Between Supports.

H Analysis of Truss Structures for Stability and Strength.

I Elastic Weight Numerical for Calculations Beam Distortions.
J Columns of Varying Section and Single Span.

K Beam-Columns of Varying Section and Single Span.

L Multispan Columns and Beam-Columns of Varying Section.

M Beam-Columns on Elastic Supports.

N Columns on E"lastic Supports.

o Torsional Buckling of Free Columns (Struts).

P Torsional Buckling of Restrained Columns.

Q Special Topics.


DESIGN AND ANALYSIS OF FILAMENTARY COMPOSITE STRUCTURES


By


Lloyd E. Hackman


Consultant on composite structures engineering.


The Author has presented a basic review of a new structural technology. He has also presented
an insight into the development of the technology as well as the application of the technology in
practical structural elements.


The Author presents the application of the design and analysis methodology from the micromechanics of fiber matrix interaction to the use of composite lamination in various types of structural elements and methods of joining. The application analysis also includes the description of
failure modes, a statement of failure criteria, and test methods for the experimental evaluation of
composite materials.


The Author demonstrates the use of all analysis methodology and failure criteria with example
problems taken from ten years of experience in the design with composite materials in the aerospace
industry.


TABLE OF CONTENTS


C13.l Introduction

C13.Ll The Development of a Technology
C13.L2 The Material Concept
C13.L3 The Design Approach to Composite Structures
C14.L4 Nomenclature


C13.2 General Relations for Orthotropic Laminates

C13.2.l Elastic Relations
C13.2.2 Strength Relations of Fabric Laminates
C13-2-3 Properties of Various Constructions
C13.2.4 Elastic Properties of Oriented Laminates
C 13.2.5 Elastic Properties of Cross Laminates or Parallel Laminates
C13.2.6 Isotropic Laminates Made with Orthotropic Laminations


C13.3 Relationships of Unidirectional Laminate Materials

C13.3.l Elastic Relationships for laminae
C13.3.2 Strength Relationships for a lamina of a Rectangular Array
C13.3.3 Strength Relationships for a lamina of a Hexagonal Array
C13.3.4 Multi Laminate Properties and Stresses
C13.3.5 Compressive Strength of Unidirectional Laminates
C13.3.6 Effect of voids on Compression Strength



C13.4

C13.4.l

C13.4.2

C13.4.3



Laminate Failure Criterian

Failure modes and Test Methods

Nonlinear characteristics of Laminate and Failure Modes



C13.5 Stability of Filamentary Composite Structural Elements

C13.5.l Flat Rectangular Panels
C13.5.2 Honeycomb Sandwich


C13.6 Joining of Composite Materials

C13.6.l Bonded Lap Joints
C13.6.2 Mechanical Fastened Joints


**ANALYSIS** **AND DESIGN**


**OF**


**MISSILE STRUCTURES**


By


J. I. ORLANDO, _Branch_ _Chief_


_Missile_ _and_ _Space Division_


Douglas Aircraft Company


And

J. F. MEYERS, _Section_ _Chief_


_Missile_ _and_ _Space Division_


Douglas Aircraft Company


This section represents an elaboration for Prof. E. F. Bruhn's book, "Analysis and Design of
Flight Vehicle Structures." It has been designed to introduce the student and beginning engineer to
the general field of missile structures and to give a limited presentation of the preliminary load,
stress analysis, and structural design practices of typical boost missiles.


The first portion is both analytical and descriptive in nature and serves to acquaint the reader
with current practices in configuration, material usage, structural techniques, and design factors.
The main body, or Parts E1.7 and E1.8, takes a hypothetical multistage vehicle, derives the critical
flight load conditions, and indicates analysis for these loads. The analysis techniques derive directly
from the body of Professor Bruhn's book, "Analysis and Design of Flight Vehicle Structures"; hence
giving the reader examples of practical usage of that data for missile design.


TABLE OF CONTENTS



Part ELI


Part E1.2


Part E1.3


Part E1.4


Part E1.5


Part E1.6


Part E1. 7


Part E1.8


Part E1.9



HISTORY, TERMINOLOGY, WEIGHT DISTRIBUTION


PROPULSION SYSTEM FUNDAMENTALS


MISSILE AND SPACE VEHICLE SPECIFICATIONS


MISSILE AND SPACE VEHICLE TYPICAL STRUCTURES


MATERIALS FOR MISSILES


STRUCTURAL DESIGN FACTORS


MISSILE LOADS ANALYSIS


MISSILE STRESS ANALYSIS


CONCLUSIONS



APPENDIX: Reference Design Charts and Material Taken from
"Analysis and Design of Flight Vehicle Structures" by Bruhn.


![](images/73-Bruhn-analysis-and-design-of-flight-vehicles.pdf-11-full.png)

_Launch_ _Escape_
----""II
_System_

![](images/73-Bruhn-analysis-and-design-of-flight-vehicles.pdf-11-0.png)


SATURN V

LAUNCH VEHICLE



APOLLO

SPACECRAFT


1--- S _-I_ _VB Stage_


-- S _-II_ _Stage_


-- _S-IC_ _Stage_



Space exploration requires


a tremendous launch veh i

cle, as illustrated, by the


AppollojSaturn ve hi c Ie.


Note size of vehicle when


compared to size of a man.


Such large vehicles present


many challenging problems


to the structures engineer.


(Drawing - Courtesy of N.


American Aviation Co.)



![](images/73-Bruhn-analysis-and-design-of-flight-vehicles.pdf-11-1.png)

APOLLO/SATURN VEHICLE


![](images/73-Bruhn-analysis-and-design-of-flight-vehicles.pdf-12-full.png)

**1959 -** **60** **BEGINNING** **OF** **THE** **"JET"** **AGE** **OF** **AIR TRANSPORTATION** **- 550-650 MPH**

![](images/73-Bruhn-analysis-and-design-of-flight-vehicles.pdf-12-0.png)

![](images/73-Bruhn-analysis-and-design-of-flight-vehicles.pdf-12-1.png)


MARTIN "404" TRANSPORT CONYAIR "340" TRANSPORT BOEING "STATOCRUISER"

![](images/73-Bruhn-analysis-and-design-of-flight-vehicles.pdf-12-2.png)


1928 BOEING MODEL 80-A 1930 FORD TRI-MOTOR 1931 BOEING "MONOMAIL" 1933 LOCKHEED "ELECTRA"

![](images/73-Bruhn-analysis-and-design-of-flight-vehicles.pdf-12-3.png)


1903 FIRST FLIGHT BY 1912 GLEN. L. MARTIN 1918 STANDARD AIRCRAFT 1926 FOKKER TRANSPORT

WRIGHT BROTHERS IN HIS BIPLANE CORP BIPLANE


L....-_ **PHOTOGRAPHS** **ILLUSTRATING** **PROGRESS** **OF** **AIRCRAFT** **DESIGN** **FOR** **AIR** **TRANSPORTATION** **-** **40** **TO** **175** **MPH**


![](images/73-Bruhn-analysis-and-design-of-flight-vehicles.pdf-13-full.png)

![](images/73-Bruhn-analysis-and-design-of-flight-vehicles.pdf-13-0.png)



SIX AIR FORCE SUPERSONIC FIGHTERS

SHOWING VARIOUS WING SHAPES
(Picture from United Aircraft Publication "BEEHIVE" Spring 1958)



1959 N. AMERICAN

AVIATION

X-15 HYPERSONIC

RESEARCH AIRPLANE



(1964) N. AMERICAN
AVIATION

B-70. SPEED
2000 M. P.H. (PLUS)



![](images/73-Bruhn-analysis-and-design-of-flight-vehicles.pdf-13-1.png)

1930 MARTIN P3M-l NAVY



1933 VOUGHT-NAVY SU-4



1936 GRUMMAN-NAVY SF-l 1939 VOUGHT-SIKORSKY S02U



![](images/73-Bruhn-analysis-and-design-of-flight-vehicles.pdf-13-2.png)

![](images/73-Bruhn-analysis-and-design-of-flight-vehicles.pdf-13-3.png)

1908 "WRIGHT" AIRPLANE 1918 CURTIS ':JENNY" 1921 BOEING-ARMY 1929 CURTIS P-6 "HAWK"
FIRST ARMY AIRPLANE ARMORED ATTACK AIRPLANE


SOME PRE-WORLD WAR II AIRCRAFT

I----PHOTOGRAPHS ILLUSTRATING TREMENDOUS PROGRESS OF MILITARY AVIATION-- .....



1908 "WRIGHT" AIRPLANE

FIRST ARMY AIRPLANE



1918 CURTIS ':JENNY"


![](images/73-Bruhn-analysis-and-design-of-flight-vehicles.pdf-14-full.png)

PIONEER. Interplanetary Probing
up to 90 million miles (1965)

###### -

PROJECT GEMINI. Two-man Spacecraft.
(1965)



LUNAR ORBITER. Will orbit the moon taking
pictures (1966)


MARINER. To obtain scientific information
on Mars and Venus (1964-65)


RANGER. Photographed the Lunar Surface.
(1964)



The Age for Spacecraft is just dawning. Regardless of the type of Spacecraft,
its creation will involve the work of the structural designer.


![](images/73-Bruhn-analysis-and-design-of-flight-vehicles.pdf-15-full.png)

![](images/73-Bruhn-analysis-and-design-of-flight-vehicles.pdf-15-0.png)























18


![](images/73-Bruhn-analysis-and-design-of-flight-vehicles.pdf-16-full.png)

IQl
en
c
.;:
Vl +


c
en
Z - ." Ql
0"
--0
a.. I0::: ::>
Ou
U ::>
Vll:
= ."
u-=E
0- I00 U
I .::
u.. 0

ti:-o
~ .~
0::: Q..
U >...

o:::+~ (G
+a.. ~
Ot;

0:::2
:1::::
I
0::: en
0.=
Z ~
~
o


![](images/73-Bruhn-analysis-and-design-of-flight-vehicles.pdf-17-full.png)

LIFTOFF _AT_ _THE_ _CAPE_ - _the_ huge Saturn V
in a 7 [1] /,-million-pound thrust toward the stars.


TRANSLUNAR _INJECTION_ - _S-IVB_ _stage_ pushes
_Apollo_ spacecraft out of earth's _gravity_ _pull._

4


~.j/ ..."",~ _....._ '\ ..... .
.. ~


LEM EXPOSED - two crewmen enter LEM
for an equipment checkout; _S-IVB_ is _left_ behind.


7


LUNAR EXPLORATION - during moon stay
fwo astronauts undertake scientific observations.


10


_HOMEWARD_ BOUND - LEM stays behind in
lunar orbit as three men _head_ _Apollo_ for _earth._


13


_LANDING_ - _CIM's_ three _main_ chutes de_ploy_ to bring _the_ _craft_ back down _safely_ to earth.


16



In the tremendous task of landing on and returning


man from the moon, the structures engineer is


faced with many new and challenging design


requirements.


Appollo II with Astronauts Armstrong, Aldrin and


Collins landed on the moon on July 20/ 1969.


(Photos - Courtesy of N. American Aviation Co.)



S-IC SEPARATION - first stage drops _away,_
and _the_ Saturn _S-II_ second stage is now ignited.


2


APOLLO - _S-IVB_ _SEPARATION_ - _the_ _adapter_
panels _are_ blown free; _Apollo_ craft separates.

5


LUNAR _ORBIT_ - Service Module engine
retro-fires to put _craft_ in _aO-mile_ _lunar_ orbit.


8


_MOON_ _BLAST-OFF_ - _the_ LEM employs its
expended descent stage (JS plotfonn for _jift-off._


11


_SIM_ _JETTISONED_ - prior to _entry_ into
_the_ earth's atmosphere, S/M _is_ detached and _left._


14



_S-IVB_ _IGNITES_ - _$-II_ _stage_ is jettisoned;
_S-IVB_ _hurls_ _Apollo_ spacecraft into _earth_ _orbit._


3


FREE _FLY-AROUND_ - _Apollo_ craft turns
around in space to _dock_ _with_ _the_ waiting LEM.

6


_THE_ _DESCENT-Apollo_ croft remains in
orbit while _two_ nstronouts guide LEM to _the_ moon.


9


LUNAR _RENDEZVOUS_ - the LEM ClstrOllauts
_line_ up ernft for critical dock'm(Jte m(Jneuver.


12


REENTRY - pilot now orients Command
_Module_ so base _heat_ _shield_ _takes_ friction heat.


15

