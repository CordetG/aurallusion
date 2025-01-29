# Goals and Planning

## Features

1. Minimum Viable Product or the primary features are the main goal for implementing the first workable version of the project. 

2. Secondary features are goals that may not be implemented in the first version due to added level of complexity, but may still be realistic to implement once the primary features are successfully implemented within the project.

3. Complex features are future hopes and ideals for the project but require significally more time and dedication to implement due to requiring development at a much larger scale. 

### Minimum Viable Product

+ Take in a sound wave as input as a .wav file
+ Through the data training, the machine learning decision tree algorithm finds the best fit visual association
+ Outputs a color and hue combination based on the frequency and pitch of the sound input

### Secondary Features

+ Outputs a specific size of the visual based on volume
+ Outputs a certain shape based on the wave type
+ The machine learning algorithm uses a decision forest to create more detailed associations

### Complex Features

+ A more complex machine learning algorithm is developed to be able to precisely handle more dynamic sound files
+ The input can include full songs with many different combinations of sounds
+ The ouput can portray an abstract visual with many combinations of sounds as many different colors and shapes
+ The program can be developed to create a visual output during musical performances which may be helpful for people who have hearing impairment to experience and enjoy musical performances.

## User Stories

+ Take in a sound wave as input as a .wav file
  + As a user, I want to be able to input sound specs to produce my own sound wave.
  + As a user, I want to be able to use the sound wave I produced as input, so I can experiment and have fun with some personalization.

+ Through the data training, the machine learning decision tree algorithm finds the best fit visual association
  + As a user, I want the program to be able successfully use my personalized input choice and create a unique output.

+ Outputs a color and hue combination based on the frequency and pitch of the sound input
  + As a visual learner, I want to see what colors are produced based off my sound specs, so I can learn about music that works best for me.

## File Hierarchy

Note: For simplicity, Python will be used for the initial design and if possible, rust-lang integration will be added in the future.

:exclamation: : This setup may be subject to change.

```text
.
├── assets/
│   └── training_data.csv
├── docs/
│   └── GOALS.md
├── utils/
│   ├── audiokit/
│   │   ├── __init__.py
│   │   └── sound.py
│   ├── chromakit/
│   │   ├── __init__.py
│   │   └── colors.py
│   ├── __init__.py
│   └── tree.py
├── tests/
│   ├── __init__.py
│   ├── test_audio.py
│   └── test_colors.py
├── LICENSE
├── requirements.txt
├── references.txt
└── README.md
```

+ ./docs/ -- Includes the setup plan and program documentation.
+ ./requirements.txt -- Python recommendation for library or other system requirements needed to run the program.
+ ./utils/ [^1] -- Holds the source code for the main program.
  + utils/audiokit/ [^2] -- Module focused on audio functionality, such as creating a .wav file for input.
  + utils/chromakit/ -- Module focused on visual functionality such as color output.
  + utils/tree.py [^3] -- Holds the decision tree learning algorithm.
+ ./tests/ [^4] -- Python testing module to run tests for the individual models making sure each feature functions properly.
+ ./references.txt [^5] -- Current file for listing references.

[^1]: Not sure if `utils` or `src` is a more appropriate name for this directory.

[^2]: The current file hierarchy is a sample example for both the `audiokit` and `chromakit` modules. Depending on development structure, there may be more files added.

[^3]: More research of the file structure may be required to determine if having the machine learning algorithm file should be at the root of the `utils` directory or in a sub-module.

[^4]: Tests will likely not be limited to colors and audio testing, but may also include a file for testing the decision tree.

[^5]: This is temporary. Following up on researching Github's `CITATION` file uses.
