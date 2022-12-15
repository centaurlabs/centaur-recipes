# Mel Spectrogram Generation

<video>
  <source src="example/output/example_heart_beat.mp4" type="video/mp4">
</video>

## Summary
The code snippet in the notebook can be used to create a video with the supplied audio file. A still background image may be optionally provided. You may combine this recipe with the [audio_to_mel_spectrogram](../audio_to_mel_spectrogram) recipe to create a video with the audio over an image of the audio's mell spectrogram. Most audio, video, and image file formats are supported.

### Installation
No special installation steps required. Follow the virtual environment setup on
[the main repository page](../README.md#installation) and then follow the steps in the notebook.

### References
The example data is the phonocardiogram of a pregnant woman sourced from the following publication. The original file name was m42.wav.  
* Sameni, R., & Samieinasab, M. (2021). Shiraz University Fetal Heart Sounds Database (version 1.0.1). PhysioNet. https://doi.org/10.13026/42eg-8e59.

The original publication:
* M. Samieinasab and R. Sameni, Fetal phonocardiogram extraction using single channel blind source separation, 2015 23rd Iranian Conference on Electrical Engineering, Tehran, 2015, pp. 78-83. doi: 10.1109/IranianCEE.2015.7146186

PhysioNet Citation:  
* Goldberger, A., Amaral, L., Glass, L., Hausdorff, J., Ivanov, P. C., Mark, R., ... & Stanley, H. E. (2000). PhysioBank, PhysioToolkit, and PhysioNet: Components of a new research resource for complex physiologic signals. Circulation [Online]. 101 (23), pp. e215–e220.
