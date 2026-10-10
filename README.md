# How Do I Know?

A mind-reading magic show that runs in your web browser.

- **Try it online:** https://hu-yaqi.github.io/how-do-i-know/
- **Download it:** https://github.com/Hu-Yaqi/how-do-i-know/releases/latest/download/how-do-i-know.zip

## What you need

- A laptop or desktop computer with a webcam.
- Chrome or Edge works best. Firefox also works.

## Run it from the download

1. Unzip the file first. Don't open the page from inside the zip.
2. Double-click `index.html`. It opens in your browser.
3. Click **Begin the show** and allow the camera.

This needs an internet connection when the page loads. No internet? On Windows, double-click `start-demo.bat`. On a Mac or Linux, open a Terminal in this folder and type `python3 serve.py`. Both need Python 3.

## How to play

- Sit in the middle, about an arm's length from the screen, with light on your face.
- Follow the magician: breathe, watch the smoke, choose a ball in your mind, then stare into it.
- After a round, click **Reveal the secret** to see how the trick works.
- No webcam? Click **Rehearse with the mouse**.

Keys: Space presses the main button. F is full screen. M turns sound on or off. V is the secret view, which shows what the camera sees (keep it off while you perform).

## Privacy

The camera video never leaves your computer. All the work happens inside your browser. Nothing is uploaded or saved.

## How it works (spoiler)

The page uses the webcam to track where your eyes point. The breathing and the smoke are a disguised calibration: the smoke tells your eyes which ball to look at, so the page can learn what your eyes look like for each ball. When you "send" your ball, you stare at it, and the page picks the ball you looked at longest. **Reveal the secret** explains each step.

## Credits

Face tracking: MediaPipe Face Landmarker by Google (Apache License 2.0). The copy in `vendor/` is unchanged.
