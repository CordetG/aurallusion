# Test Cases

## Audio Testing

+ Sine equation returns 0
+ Sine equation returns expected value
+ Generate test samples

## Decision Tree Testing

Note: ML algorithms are not easily tested with unit tests due to the nature
of how ML processes data.

+ Issues with csv line numbers showing up in data. After trying methods in the pandas library to resolve -- without any success, I decided to take a less efficient approach by adding a "fake index" column to see if it removes the line numbers from the data.

  ```python
    df = pd.read_csv('utils/core_data/audio_color_data.csv')
    output_file = 'utils/core_data/updated_audio_color_data.csv'
    
    df.insert(0, 'index', range(len(df)))
    
    df.to_csv(output_file, index=False)

    print(f"Index column added and saved to {output_file}")

  ```
