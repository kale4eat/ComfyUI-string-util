NODE_CATEGORY = "string-util"


class Str:
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {}, "optional": {"object": ("*", {})}}

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("string",)
    FUNCTION = "run"
    CATEGORY = NODE_CATEGORY

    def run(self, object=None):
        return (str(object),)


class StrConcat:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "s1": ("STRING", {"default": ""}),
                "s2": ("STRING", {"default": ""}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("string",)
    FUNCTION = "run"
    CATEGORY = NODE_CATEGORY

    def run(self, s1: str, s2: str):
        return (s1 + s2,)


class StrEqual:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "s1": ("STRING", {"default": ""}),
                "s2": ("STRING", {"default": ""}),
            }
        }

    RETURN_TYPES = ("BOOLEAN",)
    RETURN_NAMES = ("bool",)
    FUNCTION = "run"
    CATEGORY = NODE_CATEGORY

    def run(self, s1: str, s2: str):
        return (s1 == s2,)


class StrNotEqual:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "s1": ("STRING", {"default": ""}),
                "s2": ("STRING", {"default": ""}),
            }
        }

    RETURN_TYPES = ("BOOLEAN",)
    RETURN_NAMES = ("bool",)
    FUNCTION = "run"
    CATEGORY = NODE_CATEGORY

    def run(self, s1: str, s2: str):
        return (s1 != s2,)


class StrLen:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "s": ("STRING", {"default": ""}),
            }
        }

    RETURN_TYPES = ("INT",)
    RETURN_NAMES = ("length",)
    FUNCTION = "run"
    CATEGORY = NODE_CATEGORY

    def run(self, s: str):
        return (len(s),)


class StrLower:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "s": ("STRING", {"default": ""}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("string",)
    FUNCTION = "run"
    CATEGORY = NODE_CATEGORY

    def run(self, s: str):
        return (s.lower(),)


class StrUpper:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "s": ("STRING", {"default": ""}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("string",)
    FUNCTION = "run"
    CATEGORY = NODE_CATEGORY

    def run(self, s: str):
        return (s.upper(),)


class StrStrip:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {"s": ("STRING", {"default": ""})},
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("string",)
    FUNCTION = "run"
    CATEGORY = NODE_CATEGORY

    def run(self, s: str):
        return (s.strip(),)


class StrLstrip:
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"s": ("STRING", {"default": ""})}}

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("string",)
    FUNCTION = "run"
    CATEGORY = NODE_CATEGORY

    def run(self, s: str):
        return (s.lstrip(),)


class StrRstrip:
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"s": ("STRING", {"default": ""})}}

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("string",)
    FUNCTION = "run"
    CATEGORY = NODE_CATEGORY

    def run(self, s: str):
        return (s.rstrip(),)


class StrStartsWith:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "s": ("STRING", {"default": ""}),
                "prefix": ("STRING", {"default": ""}),
            }
        }

    RETURN_TYPES = ("BOOLEAN",)
    RETURN_NAMES = ("bool",)
    FUNCTION = "run"
    CATEGORY = NODE_CATEGORY

    def run(self, s: str, prefix: str):
        return (s.startswith(prefix),)


class StrEndsWith:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "s": ("STRING", {"default": ""}),
                "suffix": ("STRING", {"default": ""}),
            }
        }

    RETURN_TYPES = ("BOOLEAN",)
    RETURN_NAMES = ("bool",)
    FUNCTION = "run"
    CATEGORY = NODE_CATEGORY

    def run(self, s: str, suffix: str):
        return (s.endswith(suffix),)


class StrFind:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "s": ("STRING", {"default": ""}),
                "value": ("STRING", {"default": ""}),
            }
        }

    RETURN_TYPES = ("INT", "BOOLEAN")
    RETURN_NAMES = ("index", "found")
    FUNCTION = "run"
    CATEGORY = NODE_CATEGORY

    def run(self, s: str, value: str):
        index = s.find(value)
        return (index, index > 0)


class StrReplace:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "s": ("STRING", {"default": ""}),
                "to_replace": ("STRING", {"default": ""}),
                "replace_with": ("STRING", {"default": ""}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("string",)
    FUNCTION = "run"
    CATEGORY = NODE_CATEGORY

    def run(self, s: str, to_replace: str, replace_with: str):
        return (s.replace(to_replace, replace_with),)


class StrCount:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "s": ("STRING", {"default": ""}),
                "value": ("STRING", {"default": ""}),
            }
        }

    RETURN_TYPES = ("INT",)
    RETURN_NAMES = ("count",)
    FUNCTION = "run"
    CATEGORY = NODE_CATEGORY

    def run(self, s: str, value: str):
        return (s.count(value),)


class StrJoin:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "strings": ("STRING", {"forceInput": True}),
                "sep": ("STRING", {"default": ""}),
            }
        }

    INPUT_IS_LIST = True
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("string",)
    FUNCTION = "run"
    CATEGORY = NODE_CATEGORY

    def run(self, strings: list[str], sep: list[str]):
        return (sep[0].join(strings),)


class StrSplit:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "s": ("STRING", {"default": ""}),
                "sep": ("STRING", {"default": ""}),
            }
        }

    OUTPUT_IS_LIST = (True,)
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("strings",)
    FUNCTION = "run"
    CATEGORY = NODE_CATEGORY

    def run(self, s: str, sep: str):
        return (s.split(sep),)


class StrSlice:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "s": ("STRING", {"default": ""}),
                "start": ("INT", {"default": 0}),
                "end": ("INT", {"default": 0}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("string",)
    FUNCTION = "run"
    CATEGORY = NODE_CATEGORY

    def run(self, s: str, start: int, end: int):
        return (s[start:end],)


class StrFormat:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "optional": {
                "object": ("*", {}),
            },
            "required": {
                "format": ("STRING", {"default": ""}),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("string",)
    FUNCTION = "run"
    CATEGORY = NODE_CATEGORY

    def run(self, object=None, format: str = ""):
        return (format.format(object),)


NODE_CLASS_MAPPINGS = {
    "string_util_Str": Str,
    "string_util_StrConcat": StrConcat,
    "string_util_StrEqual": StrEqual,
    "string_util_StrNotEqual": StrNotEqual,
    "string_util_StrLen": StrLen,
    "string_util_StrLower": StrLower,
    "string_util_StrUpper": StrUpper,
    "string_util_StrStrip": StrStrip,
    "string_util_StrLstrip": StrLstrip,
    "string_util_StrRstrip": StrRstrip,
    "string_util_StrStartsWith": StrStartsWith,
    "string_util_StrEndsWith": StrEndsWith,
    "string_util_StrFind": StrFind,
    "string_util_StrReplace": StrReplace,
    "string_util_StrCount": StrCount,
    "string_util_StrJoin": StrJoin,
    "string_util_StrSplit": StrSplit,
    "string_util_StrSlice": StrSlice,
    "string_util_StrFormat": StrFormat,
}
NODE_DISPLAY_NAME_MAPPINGS = {
    "string_util_Str": "String Str",
    "string_util_StrConcat": "String Concat",
    "string_util_StrEqual": "String Equal",
    "string_util_StrNotEqual": "String Not Equal",
    "string_util_StrLen": "String Length",
    "string_util_StrLower": "String Lower",
    "string_util_StrUpper": "String Upper",
    "string_util_StrStrip": "String Strip",
    "string_util_StrLstrip": "String Lstrip",
    "string_util_StrRstrip": "String Rstrip",
    "string_util_StrStartsWith": "String StartsWith",
    "string_util_StrEndsWith": "String EndsWith",
    "string_util_StrFind": "String Find",
    "string_util_StrReplace": "String Replace",
    "string_util_StrCount": "String Count",
    "string_util_StrJoin": "String Join",
    "string_util_StrSplit": "String Split",
    "string_util_StrSlice": "String Slice",
    "string_util_StrFormat": "String Format",
}
