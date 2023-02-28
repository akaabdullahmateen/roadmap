# Introduction

## Review of electronics

Current
: An electric current is a stream of charged particles, such as electrons or ions, moving through an electrical conductor or space. It is measured as the net rate of flow of electric charge through a surface or into a control volume. The moving particles are called charge carriers, which may be one of several types of particles, depending on the conductor. In electric circuits, the charge carriers are often electrons moving through a wire. In semiconductors, they can be electrons or holes. In an electrolyte, the charge carriers are ions, while in plasma, they are ions and electrons.

  The SI unit of electric current is Ampere, which is the flow of electric charge across a surface at the rate of 1 Coulomb per second (6.241 * 10<sup>18</sup> electrons per second). Electric current has both an amplitude and direction. It is measured at one point as the number of electrons traveling per second, using an ammeter. Since electrons are negatively charged, if the electrons are moving to the left, electric current is defined as moving to the right.

Voltage
: Voltage (also called electric potential difference) is the difference in electric potentials between two points. In a static electric circuit, it corresponds to the work needed per unit of charge to move a test charge between two points. Voltage is the electromotive force or potential to produce current.

  The voltage between points can be caused by the build-up of electric charge (such as capacitors), and from an electromotive force (such as electromagnetic induction in generators, inductors, and transformers). On a macroscopic scale, a potential difference can be caused by electrochemical processes (such as cells and batteries), the pressure-induced piezoelectric effect, and the thermoelectric effect.

  A voltmeter can be used to measure the voltage between two points in a system. Often a common reference potential (such as the ground of the system) is used as one of the points. A voltage can represent either a source of energy or the loss, dissipation, or storage of energy.

  In SI units, work per unit charge is expressed as Joules per Coulomb, where 1 Volt = 1 Joule (of work) per 1 Coulomb (of charge). In the International System of Units, the derived unit for voltage is named Volt.

Resistance
: The electrical resistance of an object is a measure of its opposition to the flow of electric current. Its reciprocal quantity is electrical conductance, measuring the ease with which an electric current passes. The SI unit of electrical resistance is the Ohm, while electrical conductance is measured in Siemens.

Conductors and Resistors
: Substances in which electricity can flow are called conductors. Conductors are made of high-conductivity materials (such as metals, in particular copper and aluminum). A wire is common type of conductor, which ideally has a resistance of 0 Ohms. A piece of conducting material of a particular resistance meant for use in a circuit is called a resistor. Resistors, on the other hand, are made of a wide variety of materials depending on factors such as the desired resistance, amount of energy that it needs to dissipate, precision, and cost.

Ohm's law
: Ohm's law states that the current through a conductor between two points is directly proportional to the voltage across the two points. Introducing the constant of proportionality, the resistance, the following mathematical equation describes the relationship:

$$
I = \frac{V}{R}
$$

$$
R = \frac{V}{I}
$$

$$
V = I R
$$

Power
: Electric power is the rate at which electrical energy is transferred by an electric circuit. The SI unit of power is the Watt, equal to 1 Joule per second. Electric power is the rate of doing work, represented by the letter $P$. The electric power has neither polarity nor direction. The electric power in Watts produced by an electric current $I$ consisting of a charge of $Q$ Coulombs every $t$ seconds passing through an electric potential difference of $V$ Volts is given as:

$$
\begin{aligned}
P &= \frac{W}{t} \\
  &= \frac{W}{Q}\frac{Q}{t} \\
  &= V I \\
  &= \frac{V^{2}}{R} \\
  &= I^{2} R
\end{aligned}
$$

Energy
: Electrical energy is the energy derived from electric potential energy or kinetic energy of the charged particles. The SI unit for electrical energy is the Joule. Similar to electric power, the electrical energy has neither polarity nor direction. It can be described mathematically as:

$$
\begin{aligned}
E &= P t \\
  &= V I t
\end{aligned}
$$

Kirchhoff's circuit laws
: Kirchhoff's circuit laws are two equalities that deal with the current and potential difference in the lumped element model of electric circuits.

  Kirchhoff's current law
  : This law (also called Kirchhoff's first law or Kirchhoff's junction rule) states that, for any node (junction) of an electric circuit, the sum of currents flowing into that node is equal to the sum of currents flowing out of that node, or equivalently:

    > The algebraic sum of currents in a network of conductors meeting at a point is zero.

    Recalling that current is a signed (positive or negative) quantity reflecting direction towards or away from a node, this principle can be succinctly stated as:

    $$
    \sum^{n}_{k=1}{I_{k}} = 0
    $$

  Kirchhoff's voltage law
  : This law (also called Kirchhoff's second law or Kirchhoff's loop rule), states the following:

    > The directed sum of the potential differences around any closed loop is zero.

    Similar to the Kirchhoff's current law, the voltage law can be stated as:

    $$
    \sum^{n}_{k=1}{V_{k}} = 0
    $$

Series resistance and parallel resistance ????

Voltage divider rule and current divider rule ????

## Binary information implemented with MOS transistors

