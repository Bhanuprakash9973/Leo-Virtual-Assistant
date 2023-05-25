import cv2
import mediapipe as mp
import pyautogui


def execute_mouse():
    cap = cv2.VideoCapture(0)
    HandIndicator = mp.solutions.hands.Hands()
    MarkPoints = mp.solutions.drawing_utils
    screen_width, screen_height = pyautogui.size()
    middle_y, thumb_y = 0, 0
    middle_x, thumb_x = 0, 0
    smooth_Factor = 3
    previous_X, previous_Y, current_X, current_Y = 0, 0, 0, 0
    while True:
        _, frame = cap.read()
        frame = cv2.flip(frame, 1)
        frame_height, frame_width, _ = frame.shape
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        output = HandIndicator.process(rgb_frame)
        hands = output.multi_hand_landmarks
        if hands:
            for hand in hands:
                MarkPoints.draw_landmarks(frame, hand)
                landmarks = hand.landmark
                for id, landmark in enumerate(landmarks):
                    x = int(landmark.x * frame_width)
                    y = int(landmark.y * frame_height)
                    if id == 12:
                        cv2.circle(img=frame, center=(x, y), radius=10, color=(125, 225, 255))
                        middle_x = screen_width / frame_width * x
                        middle_y = screen_width / frame_width * y
                    if id == 4:
                        cv2.circle(img=frame, center=(x, y), radius=10, color=(125, 112, 255))
                        thumb_x = screen_width / frame_width * x
                        thumb_y = screen_height / frame_height * y
                    if id == 8:
                        cv2.circle(img=frame, center=(x, y), radius=10, color=(125, 255, 255))
                        index_x = screen_width / frame_width * x
                        index_y = screen_height / frame_height * y
                        # print(abs(middle_x - index_x), abs(middle_y - index_y))
                        if abs(middle_x - index_x) < 75 and abs(middle_y - index_y) < 100:
                            pyautogui.click()
                            # pyautogui.sleep(0.5)
                            print('will be clicked.')
                        elif 75 < abs(middle_x - index_x) < 360:
                            current_X = previous_X + (middle_x - previous_X) / smooth_Factor
                            current_Y = previous_Y + (middle_y - previous_Y) / smooth_Factor
                            pyautogui.moveTo(current_X, current_Y)
                            previous_X, previous_Y = current_X, current_Y
                    if id == 16:
                        cv2.circle(img=frame, center=(x, y), radius=10, color=(125, 112, 255))
                        ring_x = screen_width / frame_width * x
                        ring_y = screen_height / frame_height * y
                        # print(abs(ring_x - thumb_x), abs(ring_y - thumb_y))
                        if abs(ring_x - thumb_x) < 100 and abs(ring_y - thumb_y) < 50:
                            pyautogui.scroll(-200)
                    if id == 20:
                        cv2.circle(img=frame, center=(x, y), radius=10, color=(125, 112, 255))
                        little_x = screen_width / frame_width * x
                        little_y = screen_height / frame_height * y
                        # print(abs(little_x - thumb_x), abs(little_y - thumb_y))
                        if abs(little_x - thumb_x) < 100 and abs(little_y - thumb_y) < 50:
                            pyautogui.scroll(200)
        cv2.imshow('MiddleMouse', frame)
        cv2.waitKey(1)

def stop():
    exit()