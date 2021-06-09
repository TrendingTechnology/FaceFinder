[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<br />
<p align="center">
  <a href="https://github.com/BleepLogger/FaceFinder">
    <img src="https://i.imgur.com/pSQUDs9.png" alt="Logo" width="500" height="400">
  </a>

  <h1 align="center">FaceFinder</h1>

  <h4 align="center">
    Use a powerful CNN to identify faces in images!
    <br /><br />
  </h4>
</p>

<details open="open">
  <summary>TABLE OF CONTENTS
  
  </summary>
  <br />
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
<img src="https://i.imgur.com/7iPl4V3.jpg" alt="screenshot" width="325" height="200" border-width=2px>

There is lots of face recognition software out there on github, but most of it focuses on speed over accuracy and uses models such as 'hog'. However, **FaceFinder is one of the most powerful face recognition programs** which uses a very large CNN to make accurate predictions.

Here's why:
* Several modern technologies make use of face recognition and its importance in the world is constantly increasing.
* You shouldn't have to train a full neural net of your own every time you want to perform face recognition.
* FaceFinder contains code which runs approximately 3.7 times faster than average.

**If you're making an app of your own and want it to perform face recognition, this is your go-to option.**

A list of commonly used resources that I find helpful are listed in the acknowledgements.

### Built With

* [Python3](https://www.python.org/downloads/release/python-388/)
* [OpenCV](https://opencv.org/)
* [Adam Geitgey's face_recognition module](https://pypi.org/project/face-recognition/)



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

* Latest versions of pip and setuptools
  ```sh
  pip install --upgrade pip setuptools
  ```
* Conda
  ```sh
  pip install conda
  ```
* Dlib
  ```sh
  python -m conda install dlib
  ```
* Required packages
  ```sh
  pip install -r requirements.txt
  ```

### Installation

1. Ensure you're in your home directory:
   ```sh
   cd ~
   ```
   When you clone the repository it should show up as a subfolder in your home folder. You can change its location whenever you want.
   
2. Clone the repo:
   ```sh
   git clone https://github.com/BleepLogger/FaceFinder
   ```
   Clone the repository by its URL.
   
3. Navigate to cloned repository:
   ```sh
   cd FaceFinder
   ```
   Commands that you run should be run within the cloned repository.
   
4. To run the program, execute tasks.py with command line arguments:
   ```sh
   python tasks.py --data-dir '<data folder path>' --input_image '<path to image>'
   ```
   Replace the <data folder path> and <path to image> with the real paths. They're just placeholders.



<!-- USAGE EXAMPLES -->
## Usage

To run it from the command line, you will need to pass two arguments.
   ```sh
   python tasks.py --data-dir '<data folder path>' --input_image '<path to image>'
   ```
   Replace the <data folder path> and <path to image> with the real paths.

This program needs one directory containing different images labelled with whose face is present in the image. And then, you need an input image which will be classified.
  
  So if you want to check whether an image is an image of your mom or your dad, then this is how you could do it:
  
  1. Create a directory called ```dataset/``` in the FaceFinder directory in ~.
  2. Create two subdirectories, ```dataset/mom``` and ```dataset/dad```.
  3. Add images of your mother to the mom subdir and your father to your dad subdir.
  4. Click an image of either your mom or your dad, the one you want to classify. Title it ```2bclassified.jpg``` and put it in the FaceFinder directory.
  5. Run this command:
     ```sh
     python tasks.py --data-dir 'dataset/' --input_image '2bclassified.jpg'
     ```
  Then, after about 20 minutes of processing (6-7 if you have a GPU), a window will open up displaying your image, with a box highlighting the detected face and a box of text saying either "Mom" or saying "Dad".
  
  You will have to install dlib from source if you want your GPU to be utilized. Look up the instructions to do that.



<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/BleepLogger/FaceFinder/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Kanav Bhasin - [@kanav_bhasin](https://twitter.com/kanav_bhasin) - kanbhasin@gmail.com

Project Link: [https://github.com/BleepLogger/FaceFinder](https://github.com/BleepLogger/FaceFinder)


  
  
  <br>
# Thank you!



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/BleepLogger/FaceFinder.svg?style=for-the-badge
[contributors-url]: https://github.com/BleepLogger/FaceFinder/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/BleepLogger/FaceFinder.svg?style=for-the-badge
[forks-url]: https://github.com/BleepLogger/FaceFinder/network/members
[stars-shield]: https://img.shields.io/github/stars/BleepLogger/FaceFinder.svg?style=for-the-badge
[stars-url]: https://github.com/BleepLogger/FaceFinder/stargazers
[issues-shield]: https://img.shields.io/github/issues/BleepLogger/FaceFinder.svg?style=for-the-badge
[issues-url]: https://github.com/BleepLogger/FaceFinder/issues
[license-shield]: https://img.shields.io/github/license/BleepLogger/FaceFinder.svg?style=for-the-badge
[license-url]: https://github.com/BleepLogger/FaceFinder/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/
