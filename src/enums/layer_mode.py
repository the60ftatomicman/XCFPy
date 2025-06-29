from enum import Enum

class LAYER_MODE(Enum):
    NORMAL_LEGACY        = 0
    DISSOLVE_LEGACY      = 1
    BEHIND_LEGACY        = 2
    MULTIPLY_LEGACY      = 3
    SCREEN_LEGACY        = 4
    OLD_BROKEN_OVERLAY   = 5
    DIFFERENCE_LEGACY    = 6
    ADDITION_LEGACY      = 7
    SUBTRACT_LEGACY      = 8
    DARKEN_ONLY_LEGACY   = 9
    LIGHTEN_ONLY_LEGACY  = 10
    HUE_HSV_LEGACY       = 11
    Saturation_LEGACY    = 12
    COLOR_HSL_LEGACY     = 13
    VALUE_HSV_LEGACY     = 14
    DIVIDE_LEGACY        = 15
    DODGE_LEGACY         = 16
    BURN_LEGACY          = 17
    HARD_LIGHT_LEGACY    = 18
    SOFT_LIGHT_LEGACY    = 19
    GRAIN_EXTRACT_LEGACY = 20
    GRAIN_MERGE_LEGACY   = 21
    COLOR_ERASE_LEGACY   = 22
    OVERLAY              = 23
    HUE_LCH              = 24
    CHROMA_LCH           = 25
    COLOR_LCH            = 26
    LIGHTNESS_LCH        = 27
    NORMAL               = 28
    BEHIND               = 29
    MULTIPLY             = 30
    SCREEN               = 31
    DIFFERENCE           = 32
    ADDITION             = 33
    SUBTRACT             = 34
    DARKEN_ONLY          = 35
    LIGHTEN_ONLY         = 36
    HUE_HSV              = 37
    SATURATION_HSV       = 38
    COLOR_HSL            = 39
    VALUE_HSV            = 40
    DIVIDE               = 41
    DODGE                = 42
    BURN                 = 43
    HARD_LIGHT           = 44
    SOFT_LIGHT           = 45
    GRAIN_EXTRACT        = 46
    GRAIN_MERGE          = 47
    VIVID_LIGHT          = 48
    PIN_LIGHT            = 49
    LINEAR_LIGHT         = 50
    HARD_MIX             = 51
    EXCLUSION            = 52
    LINEAR_BURN          = 53
    LUMA_LUMINANCE_DARKEN_ONLY  = 54
    LUMA_LUMINANCE_LIGHTEN_ONLY = 55
    LUMINANCE                   = 56
    COLOR_ERASE                 = 57
    ERASE                       = 58
    MERGE                       = 59
    SPLIT                       = 60
    PASS_THROUGH                = 61