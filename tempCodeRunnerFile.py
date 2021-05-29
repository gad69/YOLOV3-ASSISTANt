# # Check point
# # Showing blob image in OpenCV window
# # Slicing blob image and transposing to make channels come at the end
# blob_to_show = blob[0, :, :, :].transpose(1, 2, 0)
# print(blob_to_show.shape)  # (416, 416, 3)
#
# # Showing Blob Image
# # Giving name to the window with Blob Image
# # And specifying that window is resizable
# cv2.namedWindow('Blob Image', cv2.WINDOW_NORMAL)
# # Pay attention! 'cv2.imshow' takes images in BGR format
# # Consequently, we DO need to convert image from RGB to BGR firstly
# # Because we have our blob in RGB format
# cv2.imshow('Blob Image', cv2.cvtColor(blob_to_show, cv2.COLOR_RGB2BGR))
# # Waiting for any key being pressed
# cv2.waitKey(0)
# # Destroying opened window with name 'Blob Image'
# cv2.destroyWindow('Blob Image')