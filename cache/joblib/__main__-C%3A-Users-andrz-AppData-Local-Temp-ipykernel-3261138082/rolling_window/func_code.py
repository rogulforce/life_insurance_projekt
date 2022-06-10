# first line: 1
def rolling_window(matrix, column: str = 'Female_l', age = 65, start_of_test = 53, end_of_test = 62, window_length = 41):
    fm = matrix.pivot(index="Age", columns="Year", values=column)
    rolling_window_forecasts = np.ones(end_of_test - start_of_test)*-999
    for i in tqdm(range(start_of_test, end_of_test)):
        fm_train = fm.iloc[:, i - window_length:i]
        rolling_window_forecasts[i - start_of_test] = predict_rolling(fm_train, age = age, steps=1)
    return rolling_window_forecasts
