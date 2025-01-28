<!-- omit in toc -->
# Aurallusion

<img src="./assets/aurallusion-logo.gif" alt="Project logo" width="200" height="200">

&sung; &nbsp;Aural - Illusion by Cordet Gula &nbsp; &flat;

> ' ... children's schools, when they play [out of tune] it's perfect! It's so much more colorful than a perfectly tuned orchestra. That orchestra will usually play the same 12 colors whereas the school will play maybe 60 more colors.'
>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\- Quote from Neil Harbisson in the Interview on Hearing Colors Part 2

[[1]](https://munsell.com/color-blog/neil-harbisson-hearing-colors/)

<!-- omit in toc -->
## Table of Contents

<details>
<summary><a href="#description">1. Project Description</a></summary>

  + [Outcome](#outcome)

</details>

<details>
<summary><a href="#design">2. Design</a></summary>

+ [Project Planning](#project-planning)
+ [Dataset Model](#dataset-model)
+ [Decision Tree Model](#decision-tree-model)

</details>

[3. Languages](#languages)  
[4. LICENSE](#license)

<!-- omit in toc -->
## Description

Aurallusion is an audio visualization tool that incorporates multiple functionalites. In effort to use different components of sound data, the program has implemented methods to extract and evaluate audio data, such as pitch. Foundationally, Aurallusion is using frequency and pitch as audio components extracted from .wav files. The heart of aurallusion uses a decision tree machine learning algorithm to take in audio data.

In an attempt to keep the data as objective as possible, the data was used relative to absolutes on the visible light spectrum and common notes. Red has low frequency waves on the visible light spectrum and so red is associated most strongly with the bass range in octave 0 as the lowest frequency range. Violet, on the other hand, has the highest frequency on the visible light spectrum and is associated with the 8th ocatave in the treble range. The colors are measured using RGB values to allow the machine learning algorithm to make a decision from a spectrum.

To add more sound analysis, audio pitch plays a role relative to the luminous intensity of light. Note C has a low intensity pitch and is coorelated with low luminous intensity of light, whereas high luminous intensity is coorelated with the high intensity pitch of note of note B. In this project, black and white are not explicitely used but rather the lightest or darkest shade of a cooresponding color to represent the high or low pitch relative to the frequency.

<!-- omit in toc -->
### Outcome

Once completed, Aurallusion will take an audio input and output a visual association.

<!-- omit in toc -->
## Design

<!-- omit in toc -->
### Project Planning

For the list of goals and plan for the project, see [the Docs directory](./docs).

<!-- omit in toc -->
### Dataset Model

![Table showing color and sound association](./assets/color-sound-table.png)

<!-- omit in toc -->
### Decision Tree Model

![Decision tree logic example](./assets/decision-tree-design.png)

<!-- omit in toc -->
## Languages

![Python](https://img.shields.io/badge/python-3670A0?style=style-plastic-green&logo=python&logoColor=ffdd54) ![Rust](https://img.shields.io/badge/Rust-Language-orange)

+ Python includes useful libraries for working with visual data and machine learning algorithms
+ Rust has a great integrated module system that is useful for encapsulation.

<!-- omit in toc -->
## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Aurallusion is licensed under the MIT License. See [LICENSE](./LICENSE) for more information.

---

[Back to Top](#aurallusion)
