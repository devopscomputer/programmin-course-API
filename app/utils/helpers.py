from typing import Any, Dict

def response_success(data: Any, message: str = "Success") -> Dict[str, Any]:
    return {
        "status": "success",
        "message": message,
        "data": data,
    }

def response_error(message: str, status_code: int = 400) -> Dict[str, Any]:
    return {
        "status": "error",
        "message": message,
        "status_code": status_code,
    }