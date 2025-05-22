import torch
from server import PromptServer
from aiohttp import web
class MaskAnalyzer:
    @classmethod
    # def __init__(self):
    #     self.NODE_NAME = 'MaskAnalyzer'
    def INPUT_TYPES(cls):
        return {
            "required": {
                "mask": ("MASK",),
            }
        }

    RETURN_TYPES = ("STRING", "BOOLEAN")
    RETURN_NAMES = ("shape_info", "is_all_black")
    FUNCTION = "analyze_mask"
    CATEGORY = "mask preprocessing"

    def analyze_mask(self, mask):
        # 获取输入mask的形状
        shape_info = f"Shape: {tuple(mask.shape)}"
        
        # 检查是否全黑（假设mask是单通道的）
        is_all_black = torch.all(mask == 0).item()
        
        # 如果mask是多通道的（非常用情况），改用：
        # is_all_black = torch.all(mask == 0, dim=[-1,-2]).all().item()
        
        return (shape_info, is_all_black)

# Set up the node mappings
NODE_CLASS_MAPPINGS = {
    "MaskAnalyzer": MaskAnalyzer
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "MaskAnalyzer": "NVVS MaskAnalyzer"
}
# Example of adding a custom API route
@PromptServer.instance.routes.get("/custom_endpoint")
async def custom_endpoint(request):
    return web.json_response({"message": "This is a custom endpoint"})