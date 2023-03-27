import pandas
import numpy
import matplotlib.pyplot as plt

# Read the data
data = pandas.read_csv('data.csv')

def convert_csv_to_json(data):
    # Convert the data to json
    data_json = data.to_json(orient='records')  # Convert the data to json

    # Write the data to a file
    with open('data.json', 'w') as file:
        file.write(data_json)

def plot_data(data):
    # Plot the data
    plt.plot(data['x'], data['y'])
    plt.show()

def main():
    # Convert the data to json
    convert_csv_to_json(data)

    # Plot the data
    plot_data(data)

if __name__ == '__main__':
    main()  # Run the main function
