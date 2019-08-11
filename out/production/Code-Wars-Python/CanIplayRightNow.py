import unittest

def can_i_play(now_hour, start_hour, end_hour):
    # check if prime time is between midnight
    new_now_hour = new_start_hour = new_end_hour = 0
    isMidnight = False
    if start_hour > end_hour:
        isMidnight = True
        if now_hour == 0:
            now_hour = 24
        new_start_hour = start_hour - 12
        new_end_hour = end_hour + 12
        if now_hour > 12:
            new_now_hour = now_hour - 12
        elif now_hour < 12:
            new_now_hour = now_hour

    if now_hour >= start_hour and now_hour < end_hour:
        return True
    elif isMidnight and new_now_hour >= new_start_hour and new_now_hour < new_end_hour:
        return True
    else:
        return False

def can_i_play2(now_hour, start_hour, end_hour):
    if start_hour < end_hour:
        return start_hour <= now_hour < end_hour
    return start_hour <= now_hour or now_hour < end_hour

class CanIPlayTests(unittest.TestCase):
    def test(self):
        # self.assertEqual(can_i_play2(12, 10, 14), True)
        # self.assertEqual(can_i_play2(12, 13, 14), False)
        # self.assertEqual(can_i_play2(15, 12, 15), False)
        self.assertEqual(can_i_play2(20, 21, 1), False)
        self.assertEqual(can_i_play2(9, 20, 11), True)
        self.assertEqual(can_i_play2(8, 21, 7), False)
        self.assertEqual(can_i_play2(10, 21, 13), True)
        self.assertEqual(can_i_play2(16, 20, 15), False)
        self.assertEqual(can_i_play2(21, 21, 6), True)