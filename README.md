# xMusicWeb

[![Build Status](https://travis-ci.org/comwrg/xMusicWeb.svg?branch=master)](https://travis-ci.org/comwrg/xMusicWeb)

A simple web tool to convert QQ Music playlists to NetEase Cloud Music playlists (as `.kwl` files).

## Preview
[网易云歌单转换](http://144.48.7.239:5000/)

## Features
- **Convert**: Input a QQ Music playlist URL and download a `.kwl` file compatible with NetEase Cloud Music import.
- **Diff**: Compare playlists between QQ Music and NetEase Cloud Music to find missing songs.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/comwrg/xMusicWeb.git
   cd xMusicWeb
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Start the server:
   ```bash
   python run.py
   ```
   The application will be available at `http://127.0.0.1:5000/`.

2. Open the converter page in your browser.

3. **To Convert a Playlist:**
   - Open your QQ Music playlist page (e.g., `https://y.qq.com/n/yqq/playlist/xxxxxxxxxx.html`).
   - Copy the URL and paste it into the input box.
   - Click "DO IT". A `.kwl` file (e.g., `guys.kwl`) will be downloaded.
   - Open NetEase Cloud Music PC client.
   - Click on your avatar/nickname -> Import Playlist (导入歌单) -> Select Kuwo Music (酷我音乐).
   - Upload the downloaded `.kwl` file.
   - Wait for the import to complete.

4. **To Compare Playlists:**
   - Go to the "Diff" page.
   - Enter the URLs of two playlists to see the differences.

## License
MIT
