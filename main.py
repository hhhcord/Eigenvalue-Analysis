import numpy as np
from ClassFiles.AudioLoader import AudioLoader  # Import the AudioLoader class
from ClassFiles.FrequencyResponseAnalyzer import FrequencyResponseAnalyzer  # Import the FrequencyResponseAnalyzer class
from ClassFiles.ControlSystemSimulation import ControlSystemSimulation

def main():
    # Create an instance of AudioLoader
    al = AudioLoader()

    time = 30  # Specify the duration in seconds to read

    # Use the load_audio method to read the input audio data for 30 seconds
    print("\nPlease select the .wav file for the input audio signal")
    input_data, sampling_rate = al.load_audio(time)

    # Similarly, load the output audio data for 30 seconds
    print("\nPlease select the .wav file for the output audio signal")
    output_data, sampling_rate = al.load_audio(time)

    # Create an instance of FrequencyResponseAnalyzer. Pass the input data, output data, and sampling rate
    fra = FrequencyResponseAnalyzer(input_signal=input_data, output_signal=output_data, sampling_rate=sampling_rate, time_duration=time)

    # Calculate the frequency response function
    fra.analyze_and_save_bode_plot()

    # Specify the order of the system
    system_order = 90

    # Set up the simulation
    simulation = ControlSystemSimulation(n=system_order, t_end=time, num_points=len(input_data))

    # Plot the input and output signals
    simulation.plot_input_output(input_data, output_data)

    # Identify the system using SRIM
    SRIM_system = simulation.identify_system_SRIM(input_data, output_data)

    # Plot the step response for the SRIM-identified system
    simulation.plot_step_response_SRIM(SRIM_system)

    # Plot the eigenvalues for the SRIM-identified system
    simulation.plot_eigenvalues_SRIM(SRIM_system)

    # Plot the Bode plot for the SRIM-identified system
    simulation.plot_bode_SRIM(SRIM_system)

    # Create a list of natural frequencies
    simulation.process_matrix_and_save(SRIM_system.A)

if __name__ == "__main__":
    main()
