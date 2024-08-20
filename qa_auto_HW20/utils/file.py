def abs_path_from_project(relative_path: str):
    import qa_auto_HW20
    from pathlib import Path

    return (
        Path(qa_auto_HW20.__file__)
        .parent.parent.joinpath(relative_path)
        .absolute()
        .__str__()
    )
