# MIC-Object-Detection-Workshop
Welcome to the Object Detection Workshop hosted by Microsoft Innovations Club, VIT Chennai!

This repository contains the trained **YOLOv8 model**, the required **files** and the **dataset** used to train the model.

We have included drive links to sample video footages to test your predictions too!
## Run Locally

1. Clone the project

```bash
  git clone https://github.com/lilNewbie/MIC-Object-Detection-Workshop.git
```
2. If you don't have poetry, install poetry using pip

```bash
  pip install poetry
```

3. Go to the project directory

```bash
  cd my-project
```

4. Activate the virtual environment

```bash
  poetry shell
```

5. Install dependencies

```bash
  poetry install
```

6. Install ultralytics using pip

```bash
  pip install ultralytics
```

7. Run the base.py file

```bash
  py base.py
```
8. Upload your video file (for example, download the file in this link and test it out) and click Upload


9. Results will be displayed and the output video will be stored in the static/output folder 

# LINKS
- Link to the [dataset](https://drive.google.com/drive/folders/1eE0SwaHKCFt6naJn1QNnviAhz7QgVpS4?usp=sharing)
- Link to the actual dataset from [Roboflow](https://universe.roboflow.com/kolaman/cesas/dataset/1)
- Link to [videos](https://drive.google.com/drive/folders/1tUCNzVOf8pc1PibwR7UfOdpmTyiXIW3i?usp=sharing) for testing (download and and then upload them)

## IMPORTANT
If you are using poetry for the first time, you may face a Set-ExecutionPolicy (Running scripts is disabled) error. Try [these](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.security/set-executionpolicy?view=powershell-7.3) and [these](https://youtu.be/yNZMUdpkuBE) fixes.
