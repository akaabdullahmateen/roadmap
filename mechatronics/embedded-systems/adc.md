# ADC

An analog-to-digital convertor (ADC, A/D, or A-to-D) is a system that converts an analog signal, such as sound picked up by a microphone or light entering a digital camera, into a digital signal. Typically the digital output is a two's complement binary number that is proportional to the input, but there are other formats.

Due to the complexity and the need for precisely matched components, most ADCs are implemented as integrated circuits (IC). Typically these take the form of metal-oxide semiconductor (MOS) mixed-signal integrated circuit chips that integrate both analog and digital circuits.

A digital-to-analog convertor (DAC) performs the reverse function; it converts a digital signal into an analog signal.

## Explanation

An ADC converts a continuous-time and continuous-amplitude analog signal to a discrete-time and discrete amplitude digital signal. The conversion involves quantization of the input, so it necessarily introduces a small amount of error or noise. Furthermore, instead of continuously performing the conversion, an ADC does the conversion periodically, sampling the input, limiting the allowable bandwidth of the input signal.

The performance of an ADC is primarily characterized by its bandwidth and signal-to-noise ratio (SNR). The bandwidth of an ADC is characterized primarily by its sampling rate. The SNR of an ADC is influenced by many factors, including the resolution, linearity and accuracy (how well the quantization levels match the true analog signal), aliasing and jitter. The SNR of an ADC is often summarized in terms of its effective number of bits (ENOB), the number of bits of each measure it returns that are on average not noise. An ideal ADC has an ENOB equal to its resolution. ADCs are chosen to match the bandwidth and required SNR of the signal to be digitalized. If an ADC operates at a sampling rate greater than twice the bandwidth of the signal, then according to the Nyquist-Shannon sampling theorem, near perfect reconstruction is possible. The presence of quantization error limits the SNR of an even ideal ADC. However, if the SNR of the ADC exceeds that of the input signal, its effects may be neglected resulting in an essentially perfect digital representation of the band-limited analog signal.