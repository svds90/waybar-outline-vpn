    "custom/outline": {
        "format": "<span font-family=\"Iosevka Nerd Font Mono\" font-weight=\"bold\"> Otl</span>",
        "on-click": "python3.12 $HOME/.config/waybar/modules/outline_toggle.py",
        "signal": 8
    },
    "custom/outline-status": {
        "format": " {} ",
        "exec": "python3.12 $HOME/.config/waybar/modules/outline_status.py",
        "return-type": "json",
        "signal": 8
    },
