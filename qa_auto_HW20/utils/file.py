from pathlib import Path
import qa_auto_HW20


def abs_path_from_project(relative_path: str):
    return (
        Path(qa_auto_HW20.__file__)
        .parent.parent.joinpath(relative_path)
        .absolute()
        .__str__()
    )
