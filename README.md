# FaceRank
A project can extract facial landmark and evaluate the beauty of face, which is inspired by a book [Computer Models for Facial Beauty Analysis](http://www.springer.com/gp/book/9783319325965). 

This project use [The Vertical Thirds and Horizontal Fifths](https://www.hindawi.com/journals/tswj/2014/428250/)  algorithm to evaluate the beauty of the photos

[Demo Link](https://face.wenfeng.me/)  

## Install

### Step 1 (depends on OS)
Clone Repo

```
git clone https://github.com/pwfee/FaceRank.git
cd FaceRank
```

Linux Requirements (Deploy successfully on Debian 9 x64)

```
sudo apt-get install redis-server
sudo apt-get install build-essential cmake
sudo apt-get install libgtk-3-dev
sudo apt-get install libboost-all-dev
sudo apt-get install libopenblas-dev liblapack-dev   
```

OR

macOS Requirements (Deploy successfully on macOS 10.13.5)

```
brew install redis
brew install dlib
brew install cmake
```

### Step 2
Python Requirements

```pip install -r requirements.txt```

## Run

```
celery -A FaceRank worker -l info
python manage.py runserver
```
Then Visit http://127.0.0.1:8000/

## Screenshots

![](https://cdn.pwfee.com/ext/upload-img.png)

![](https://cdn.pwfee.com/ext/img-detail.png)

![](https://cdn.pwfee.com/ext/rank-list.png)



