in_linux = False

LARGE_FONT= ("Verdana", 12)

FONT = ('Helvetica', 14)

ESP_PORT = '/dev/ttyUSB0'

# Define button functions
def reset_password(controller):
    controller.show_frame(ResetPassword)
    return
