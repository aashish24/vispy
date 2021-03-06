# -*- coding: utf-8 -*-
from vispy.scene.visuals import Text
from vispy.testing import (requires_application, TestingCanvas,
                           run_tests_if_main)
from vispy.testing.image_tester import assert_image_approved


@requires_application()
def test_text():
    """Test basic text support"""
    
    with TestingCanvas(bgcolor='w', size=(92, 92), dpi=92) as c:
        pos = [92 // 2] * 2
        text = Text('testing', font_size=20, color='k',
                    pos=pos, anchor_x='center', anchor_y='baseline')
        c.draw_visual(text)
        # Test image created in Illustrator CS5, 1"x1" output @ 92 DPI
        assert_image_approved("screenshot", 'visuals/text1.png')


run_tests_if_main()
