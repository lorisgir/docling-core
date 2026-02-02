class _PictureClassificationToken(str, Enum):
    """PictureClassificationToken."""

    OTHER = "<other>"

    # If more than one picture is grouped together, it
    # is generally not possible to assign a label
    PICTURE_GROUP = "<picture_group>"

    # General
    CHART = "<chart>"
    PIE_CHART = "<pie_chart>"
    BAR_CHART = "<bar_chart>"
    STACKED_BAR_CHART = "<stacked_bar_chart>"
    LINE_CHART = "<line_chart>"
    FLOW_CHART = "<flow_chart>"
    SCATTER_CHART = "<scatter_chart>"
    HEATMAP = "<heatmap>"
    REMOTE_SENSING = "<remote_sensing>"
    INFOGRAPHIC = "<infographic>"
    DECORATION = "<decoration>"
    ILLUSTRATION = "<illustration>"

    NATURAL_IMAGE = "<natural_image>"
    PERSON = "<person>"

    # --- NEW: explicit tags requested ---
    PHOTOGRAPH = "<photograph>"
    PAGE_THUMBNAIL = "<page_thumbnail>"
    FULL_PAGE_IMAGE = "<full_page_image>"
    UI_ELEMENT = "<ui_element>"  # already present below in Company; keep one definition only

    # Chemistry
    MOLECULAR_STRUCTURE = "<chemistry_molecular_structure>"
    MARKUSH_STRUCTURE = "<chemistry_markush_structure>"

    # --- NEW: requested generic chemistry tag ---
    CHEMISTRY_STRUCTURE = "<chemistry_structure>"

    # Company
    ICON = "<icon>"
    LOGO = "<logo>"
    SIGNATURE = "<signature>"
    STAMP = "<stamp>"
    QR_CODE = "<qr_code>"
    BAR_CODE = "<bar_code>"
    SCREENSHOT = "<screenshot>"

    # --- NEW: requested screenshot subtypes ---
    SCREENSHOT_FROM_COMPUTER = "<screenshot_from_computer>"
    SCREENSHOT_FROM_MANUAL = "<screenshot_from_manual>"

    # --- NEW: requested misc icon-like classes ---
    MUSIC = "<music>"
    CALENDAR = "<calendar>"

    # Geology/Geography
    GEOGRAPHIC_MAP = "<map>"
    STRATIGRAPHIC_CHART = "<stratigraphic_chart>"

    # --- NEW: requested map variants ---
    GEOGRAPHICAL_MAP = "<geographical_map>"
    TOPOGRAPHICAL_MAP = "<topographical_map>"

    # Engineering
    CAD_DRAWING = "<cad_drawing>"
    ELECTRICAL_DIAGRAM = "<electrical_diagram>"

    # --- NEW: requested engineering generic ---
    ENGINEERING_DRAWING = "<engineering_drawing>"

    # --- NEW: requested chart variants ---
    SCATTER_PLOT = "<scatter_plot>"
    BOX_PLOT = "<box_plot>"

    # --- NEW: requested puzzle ---
    CROSSWORD_PUZZLE = "<crossword_puzzle>"
