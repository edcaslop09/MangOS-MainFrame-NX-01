# MangOS MainFrame NX-01

> A modular, local-first cyberdeck operating  system written in Python.
MangOS MainFrame NX-01 is a personal cyberdeck operating environment designed around modular apps, offline-first data, local media tools, and future physical hardware expansion. 

Insted of being a single application, MangOS is built as a collection of independent apps that run inside the same environment. The project follows a -- LOCAL FIRST PHILOSOPHY -- core features are designed to work offline using local files, local media, local metadata, and local configuration.

Future modules may provide optional internet connectivity, but the sytem should not depend on external services to function. MangOS is currently under active development as the software foundation for a portable cyberdeck powered by Python. 



## Current Status 

MangOS currently includes:

- A terminal-based launcher.
- A modular app architecture.
- A reusable menu utility system.
- STATIC RECORDS, a local music workstation.
- FLAC audio playback.
- Local song metadata.
- Synced ".lrc" lyrics.
- Playlist creation and playback.
- Audio filter presets.
- Experimental work toward Vinyl Black.FM, a local virtual radio station.

This project is still in development. Some features are stable, while others are experimental or planned for future versions.



## Project Vision 

MangOS is being designed as a modular cyberdeck operating environment. MangOS is not intended to replace the Raspberry Pi operating system at the kernel or driver level. Instead, the realistic long-term goal is for MangOS to run -- ON TOP OF RASPBERRY PI OS OR ANOTHER LIGHTWEIGHT LINUX DISTRIBUTION -- as the main user-facing system layer.

In that model, Raspberry Pi OS handles the low-level responsabilities:

- Hardware drivers
- Audio devices.
- USB devices.
- GPIO access.
- I²C communication.
- File System access.
- Networking.
- System services.

The long-term goal is that a Raspberry Pi-based cyberdeck could boot direcly into MangOS, making it feel like its own operating system while still using Linux underneath for stability and hardware support.

The system should feel like this to the user:

[ POWER ON CYBERDECK ]--->[ MangOS BOOT SCREEN ]--->[ MangOS LAUNCHER ]--->[ APPS, MODULES, MEDIA TOOLS, RADIO MODES, UTILITIES, CYBERSECURITY MODES ]

The long-term stack should look like this:

[ HARDWARE ]--->[ RASPBERRY PI OS / LINUX ]--->[ MangOS MAINFRAME NX-01 ]--->[ MangOS APPS AND MODULES ]

This aprroach keeps the project realistic while still allowing MangOS to behave like a dedicated cyberdeck operating system.



## Core Idea

Static Records is the first major proof of concept. It demostrates how MangOS apps can have their own menus, data, logic, and user experience while still running inside the same system.

The long-term vision is to create a portable system tat can:

- Run local apps.
- Work offline.
- Store data locally.
- Play and manage local media.
- Use human-readable file formats like JSON and LRC.
- Support terminal-first interaction during early development.
- Expand through future physical hardware modules.
- Eventually run on a Raspberry Pi-based cyberdeck.
- Boot directly into a MangOS interface on dedicated hardware.
- Provide a retro-futuristic interface inspired by cyberdecks, old terminals, and portable field computers.



## System Model

MangOS is organized around three main software layers:

MangOS
----- CORE SYSTEM
----- APPS
----- LOCAL DATA 

In the future, a fourth layer will added conceptually:

MangOS
----- CORE SYSTEM
----- APPS
----- LOCAL DATA 
----- PHYSICAL MODULES



### Core System 

The core system is responsible for shared behavior used across MangOS

Current respinsibiities include: 

- Launching apps.
- Managing reusable menu logic.
- Providing shared utilities.
- Keeping the system modular.
- Separating system-level behavior from app-specific behavior.

Current core files include:

core/
----- Launcher.py
----- menu_utils.py


Future core responsibilities may include:

- Module detection.
- System status.
- Boot behavior.
- Theme management.
- Hardware capability management.
- Raspberry Pi service integration.



## Apps

Apps are independent modules inside MangOS. Each app should have its own logic, menus, files, and data.

the FIRST major app is...

 ------------------------------
        STATIC RECORDS 
 ------------------------------

STATIC RECORDS currently handles local music playback, FLAC audio, synced lyrics, playlists, audio filters, and experimental radio-style playback.

Future apps could include:

- Module Bay/ IoT.
- File manager.
- Notes/List
- System monitor.
- Radio tools.
- Cybersecurity tools.
- Sensor dashboard.
- Local AI tools.
- Boot screen manager.
- Theme  manager.  

The goal is for each app to feel like a specialized tool inside the cyberdeck, not just a disconnected script.



### Local Data

MangOS stores important data locally using simple, human readable formats.

Examples:

- Song metadata in JSON.
- Playlists in JSON.
- Synced lyrics in LRC.
- Future module mainfests in JSON.

Current local data is stored mainly in:

data/static_records/

Example song folder:

data/static_records/demo_song/
----- original.flac
----- lyrics.lrc
----- metadata.json
----- colors.json

This local-first design makes the system easier to inspect, backup, modify, and eventually move into a Raspberry Pi cyberdeck.

### Physical Modules

Physical modules are part of the long-term hardware vision for MangOS.

A physical module would be an interchangeable device connected to the cyberdeck to add a specific capability, such as audio processing, radio communiction, storage, sensors, cameras, or AI acceleration.

In the future, MangOS could detect these modules throught Raspberry Pi OS / Linux interfaces such as:

- USB.
- GPIO.
- I²C.
- Serial communication.
- NFC.
- Other hardware protocols.

The module would provide it's identity, type, version, and capabilities to MangOS. MangOS could then enable the correct app, driver behaivor, or interface mode.

This is a future goal. The current project is software-first, but the architecture is being planned with hardware expansion in mind.



## Installation 

MangOS MainFrame NX-01 currently runs as a Python project on top of a regular operating system.

Durring devekopment, it can be run on a normal computer using Windows, macOS, or Linux. The long-term goal is to run it on a Raspberry Pi-based cyberdeck as the main user-facing interface.

### Requierments

Recommended setup:

- Python 3.10 or newer.
- Git.
- A terminal such as PowerShell, Windows Terminal, VS Code terminal, or a Linux/macOS terminal.
- An audio output device for STATIC RECORDS playback.

The project is currently developed mainly on Windows, but the architecture is intended to remain portable.

### Clone or download the project

Using Git:
git clone <repository-url>
cd LYRICS_PY


### Install dependencies 
pip install -r requirements.txt

Current dependecies:
numpy
sounddevice
soundfile
mutagen
keyboard

These packages are used for audio playback, FLAC file loading, metadata handling, keyboard controls, and audio processing.

Windows: 

python -m venv .venv
.venv\Scripts\activate

macOS/Linux: 
Python3 -m venv .venv 
source .venv\bin\activate

## How to run the project 

Run from the project root: 

python main.py

Do not run internla files directly from inside subfolders, because some modules use relative imports.

## Configuration

### Statiic records Configuration 

Songs are stored in: data/static_records/

Each song must have it's own folder:
data/static_records/demo_song/
----- original.flac
----- lyrics.lrc
----- metatdata.json
----- colors.json

Each song folder should include thee required files:
- "metadata.json"
- "lyrics.lrc"
- "colors.json"
- One supported audio file, preferably "original.flac"

Supported audio filename:

Original.flac
song.flac
song.wav
song.mp3


## Metadata

### metadata.json

Example format

---json
 {
  "titulo": "Rich FLAC Test",
  "artistas": ["MangOS"],
  "album": "Static Records Lab",
  "genero": "Test Audio",
  "favorita": false,
  "veces_reproducida": 0
}

## Lyrics

### lyrics.lrc

Example format

[00:00.00] MangOS FLAC audio test
[00:03.00] Static Records high fidelity probe
[00:06.00] Vinyl Black FM audio engine ready

## SOng Colors 

Each song folder includes a "color.json" file.

Example format

---json 
{
  "primary": "yellow",
  "secondary": "magenta",
  "background": "black"
}

## Playlists 

Playlists are stored in: data/static_records/playlists/

Example

{
  "nombre": "Test",
  "canciones": [
    "data/static_records/demo_song"
  ]
}

## Audio Filters 

Static Records includes audio filter presets handled by: apps/static_records/audio_filters.py

Current dilter concepts includes:
- Flat
- Old radio
- Phone speaker
- Vinyl warm
- Cassette tape
- Night drive 
- Vinyl Black classic

Current limitation: Filters are applied when playback starts. Fully real-time filter changes are planned for future audio engine.

## Vinyl Black.FM

Vinyl Black.Fm is an experimental radio-style mode for Static Records.

The goal is to simulate a local virtual radio station that can:

- Use a playlist as the station source.
- Play songs continuously.
- Use the Vinyl Black audio filter.
- Allow radio-style controls such as next song, status, and stop.

Current status: experimental / in development.

## Project Structure 

LYRICS_PY/
----- main.py
----- README.md
----- requirements.txt
----- core/
      ----- launcher.py
      ----- menu_utils.py
----- apps/
      ----- static_records/
            ----- static_records_core.py
            ----- static_records_menu.py
            ----- audio_engine.py
            ----- audio_filters.py
            ----- playlist.py
            ----- playlist_manager.py
            ----- playlist_menu.py
----- data/
      ----- static_records/
            ----- demo_song/
            ----- playlists/



## Long-Term Raspberry Pi Deployment

MangOS is designed to eventually run on a Raspberry Pi-based cyberdeck.

MangOS will not replace Raspberry Pi OS at the kernel or driver level. Instead, MangOS is not a replacement for Raspberry Pi OS, It's intended to run on top of Raspberry Pi OS or another lightweight Linux distribution as the main user-facing interface.

Future deployment goal:

[ Power on cyberdeck ]--->[ Raspberry Pi OS / Linux starts ]--->[ MangOS launches automatically ]--->[ MangOS launcher ]



## Physical Expansion Modules

Physical modules are part of the long-term hardware vision for MangOS.

A module could connect to cyberdeck and add a specific capability, such as audio, radio, storage, sensors, networking, cameras, or AI acceleration.

Future examples:

- Audio Module
- Radio Module
- Storage Module
- Sensor Module
- Network Module 
- Cybersecurity Module 
- AI Module

Current status: conceptual / planned.



## Roadmap

Short-term:

- Improve steup documentation.
- Stabilize Static Records menus.
- Finish Vinyl Black.FM integration.
- Improve playlist UX.
- Add better back/cancel navigation.

Medium-term:

- Add equalizer presets.
- Improve audio engine controls.
- Add Module Bay simulation.
- Add Raspberry Pi deployment note.

Long-term:

- Raspberry Pi cyberdeck integration.
- Physical module detection.
- Boot directly into MangOS interface.
- More MangOS apps.



## Known Limitations

- Terminal-based interface.
- Audio filters are not fully real-time yet.
- Pause/resume support still limited.
- Physical module are not implemented yet.
- Raspberry Pi deployment is planned, not finished. 

Some local data files may change during testing, such as playback counters in "metadata.json" or generated playlist files. These files should be revieed before committing changes.










