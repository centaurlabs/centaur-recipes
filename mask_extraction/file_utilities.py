from typing import Union

import json
from pathlib import Path

PathLike = Union[str, Path]


def nested_dict_to_json_file(nested_dictionary: dict, destination: PathLike) -> Path:
    output_json = Path(destination).with_suffix(".json")

    with output_json.open("w", encoding="utf-8") as fp:
        json.dump(nested_dictionary, fp, ensure_ascii=False, indent=4)

    return output_json
