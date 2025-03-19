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

### Updates

+ I misunderstood what was happening. There was no issue with the csv file index or data reading. Trying to fix the csv data ended up causing many more issues -- because it was correct to begin with. 
  + I was thinking that because the MSE result was so high -- approx. 1800+, that the indices were causing issues. This was not the case.
  + Decision trees are not all that reliable to begin with because they are a basic ml-algorithm. 
  + To see if I could improve the MSE, I tried running epochs -- but this made no difference because decision tree algorithms don't store data and update themselves like more complex algorithms.
  + However, I did find that adjusting the 'random-state' value in the training did impact the results a bit. the random-state = 93 had the best results reducing the MSE to approx. 1042 whereas over 100 greater increased the MSE and below 93 also significantly increased the MSE.
+ Adjusting the max-depth of the tree model significantly improved the MSE as well. So I changed the max-depth from a depth of 3 to None (i.e., no set cutoff). The MSE is now approx. 126.

## UI Testing

+ creating tkinker input window is successful
+ 
