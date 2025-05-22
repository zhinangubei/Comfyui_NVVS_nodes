from .nodes.MaskAnalyzer import MaskAnalyzer

NODE_CLASS_MAPPINGS = {
    "MaskAnalyzer": MaskAnalyzer
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "MaskAnalyzer": "NVVS: MaskAnalyzer"
}       

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]