class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _keyboard_service (KeyboardService): For getting directional input.
        _video_service (VideoService): For providing video output.
    """

    def __init__(self, keyboard_service, video_service):
        """Constructs a new Director using the specified keyboard and video services.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
            video_service (VideoService): An instance of VideoService.
        """
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        self.score = 0
        
    def start_game(self, cast):
        """Starts the game using the given cast. Runs the main game loop.

        Args:
            cast (Cast): The cast of items.
        """
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._get_inputs(cast)
            self._do_updates(cast)
            self._do_outputs(cast)
        
        self._video_service.close_window()

    def _get_inputs(self, cast):
        """Gets directional input from the keyboard and applies it to the player.
        
        Args:
            cast (Cast): The cast of items.
        """
        player = cast.get_first_item("players")
        velocity = self._keyboard_service.get_direction()
        player.set_velocity(velocity)        

    def _do_updates(self, cast):
        """Updates the player's position and resolves any collisions with artifacts.
        
        Args:
            cast (Cast): The cast of items.
        """
        banner = cast.get_first_item("banners")
        player = cast.get_first_item("players")
        gemrocks = cast.get_items("gemrocks")

        banner.set_text("")
        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        player.move_next(max_x, max_y)
        
        #update points
        for gemrock in gemrocks:
            gemrock.move_next(max_x, max_y)
            if player.get_position().equals(gemrock.get_position()):
                self.score = self.score + gemrock.get_points()
                cast.reset_item(gemrock)
            banner.set_text(f"Score: {self.score}")
        
    def _do_outputs(self, cast):
        """Draws the items on the screen.
        
        Args:
            cast (Cast): The cast of items.
        """
        self._video_service.clear_buffer()
        items = cast.get_all_items()
        self._video_service.draw_items(items)
        self._video_service.flush_buffer()