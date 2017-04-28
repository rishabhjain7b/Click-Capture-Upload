from subprocess import call
try:
    import picamera
    import datetime
    timestamp=datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    camera = picamera.PiCamera()
    try:
        camera.resolution=(1280,720)
        camera.rotation=180
        camera.start_preview()
        camera.capture(timestamp+".jpg")
    except:
        pass
    finally:
        camera.close()
 
    photofile = "/home/pi/Dropbox-Uploader/dropbox_uploader.sh upload /home/pi/"+timestamp+".jpg "+timestamp+".jpg "
    call([photofile], shell=True)
except:
    pass
