# USB Install Guide: Nomadic D1 / D2 monitor on a Cerbo GX

**The easy way to install the monitor: one file, one USB stick, one restart.** No computer connection to the Cerbo,
no passwords, no commands to type. About 10 minutes.

📄 **[Printable version (PDF)](docs/USB-Install-Guide.pdf)**

> The monitor only *watches* your Nomadic converter. It never sends it anything, so it can't change how your
> converter or your van behaves.

---

## Before you start (one time only)

- [ ] **The CAN cable is made and connected.** It runs from the converter's CAN_H and CAN_L wires to one of the
      Cerbo's **VE.Can 2** sockets, with the Victron terminator plug in the other VE.Can 2 socket. If you haven't
      made it yet, see steps 1–2 of the Installation Guide:
      [D1 guide (PDF)](D1-monitor/docs/installation-guide.pdf) · [D2 guide (PDF)](D2-monitor/docs/installation-guide.pdf)
- [ ] **The Cerbo's firmware is v3.80 or newer.** On the Cerbo: **Settings › General › Firmware**.
- [ ] **VE.Can 2 is set to 500 kbit/s.** **Settings › Connectivity › VE.Can port 2** (some firmware calls it
      **BMS-Can port**) › **CAN-bus profile** › **CAN-bus BMS LV (500 kbit/s)**.
- [ ] **Modifications are allowed.** **Settings › General › Modification checks**: leave modifications enabled
      (the default). If they're off, the monitor disappears the next time the Cerbo restarts.
- [ ] **You know which converter you have.** Check the label: **D1** or **D2**.

---

## Step 1. Get a USB stick ready

Any USB stick of **32 GB or smaller** works. It has to be formatted as **FAT32**.

**To check on Windows:** plug it in, open **File Explorer**, right-click the stick, choose **Properties**. It
should say *File system: FAT32*.

**To format it** (this **erases** everything on the stick): right-click the stick › **Format…** ›
File system **FAT32** › **Start**.

## Step 2. Download the file for your converter

Download **only one**, the one that matches your converter:

| Your converter | Click to download |
|---|---|
| **Nomadic D1** | [**venus-data-nomadic-d1-monitor.tar.gz**](https://github.com/CKOCI13/Nomadic-D1-and-D2-monitor-on-Victron-Cerbo-GX-MK2/raw/main/Download/venus-data-nomadic-d1-monitor.tar.gz) |
| **Nomadic D2** | [**venus-data-nomadic-d2-monitor.tar.gz**](https://github.com/CKOCI13/Nomadic-D1-and-D2-monitor-on-Victron-Cerbo-GX-MK2/raw/main/Download/venus-data-nomadic-d2-monitor.tar.gz) |

On a Mac, download with **Chrome or Firefox**. Safari unpacks the file, and the Cerbo can't use it then.

## Step 3. Copy the file to the USB stick

- Put it at the **top level** of the stick, **not inside a folder**.
- Put **only this one** `venus-data` file on the stick.
- **Check the name.** If your computer saved it as `venus-data-nomadic-d1-monitor (1).tar.gz`, rename it and
  remove the ` (1)`. The Cerbo ignores names with spaces. (Windows may hide the `.gz` part of the name.
  That's fine.)

Then **eject** the stick safely (right-click › **Eject**) and take it out.

## Step 4. Put the stick in the Cerbo and restart it

1. Plug the stick into one of the Cerbo's **USB** ports.
2. Restart the Cerbo: **Settings › General › Reboot**. (Or switch it off and on again.)

## Step 5. Wait 2 minutes, then take the stick out

The Cerbo installs the monitor by itself while it starts up. When it's done, it renames the file on the stick to
`...tar.gz.installed`, so it never installs twice, even if you forget the stick in the Cerbo.

## Step 6. Check that it worked

Look for **DC-DC D1** (or **DC-DC D2**) on the Cerbo:

- in the **Device list**,
- as an **Alternator** tile on the **Overview** page,
- as cards in the **switch pane**.

**Extra: the web page with charts.** Find the Cerbo's IP address under **Settings › Connectivity › Ethernet** (or
**Wi-Fi**), then open `http://<that address>:8088` on any tablet, phone or laptop on the van's network.
For example: `http://192.168.1.50:8088`.

**That's it.** The monitor starts by itself every time the Cerbo starts, including after Victron firmware updates.

---

## If it didn't work

| What you see | What to do |
|---|---|
| Nothing new on the Cerbo, and the file on the stick **still ends in `.tar.gz`** (not `.installed`) | The Cerbo didn't read the stick. Check that the stick is **FAT32**, the file is at the **top level**, the name has **no spaces or `(1)`**, and it's the only `venus-data` file. Then do Step 4 again. |
| The file was renamed to `.installed`, but the converter says **No communication** | The monitor is installed but hears nothing. Check that the converter has power, check the cable, the 120 Ω resistor and the terminator plug. Then try the other speed: **VE.Can (250 kbit/s)** in the CAN port setting. |
| It worked, but **disappeared after a restart** | Turn modifications back on (**Settings › General › Modification checks**), then install again with a fresh download. |
| You're on a Mac and the file ends in **`.tar`** | Safari unpacked it. Download it again with Chrome or Firefox. |

To install again, always use a **fresh download**. The old file on the stick has been renamed to `.installed`.

---

## Updating to a new version

Download the new file and do Steps 1–6 again. Your history (lowest and highest readings, kWh) is kept. Any settings
you changed are set back to the standard ones.

## Important for stock LTV vans

The monitor **shows** the converter's current but **cannot limit it**. On a stock LTV, the 12 V cable is 2 AWG on
a 150 A fuse, and the converter can draw more than that while boosting.

## Need help?

Post in the owners' Facebook group, or [open an issue on GitHub](https://github.com/CKOCI13/Nomadic-D1-and-D2-monitor-on-Victron-Cerbo-GX-MK2/issues).
A photo of the Cerbo screen helps a lot.

<sub>Free owner project, not affiliated with Victron Energy, Nomadic or Grand Design. No warranty.</sub>
