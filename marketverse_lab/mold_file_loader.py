from pathlib import Path


class MoldFileLoader:

    SUPPORTED_TYPES = {
        ".stl",
        ".step",
        ".stp",
        ".iges",
        ".igs",
        ".obj",
        ".dxf"
    }

    def load(self, file_path):

        path = Path(file_path)

        if not path.exists():
            return {
                "success": False,
                "message": "File not found."
            }

        ext = path.suffix.lower()

        if ext not in self.SUPPORTED_TYPES:
            return {
                "success": False,
                "message": f"Unsupported file type: {ext}"
            }

        return {
            "success": True,
            "file_name": path.name,
            "extension": ext,
            "size": path.stat().st_size,
            "absolute_path": str(path.resolve())
        }

    def supported_formats(self):

        return sorted(self.SUPPORTED_TYPES)

    def report(self):

        return {
            "ready": True,
            "supported_formats": self.supported_formats()
        }

    def is_ready(self):

        return True
