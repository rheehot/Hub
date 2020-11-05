import numpy as np
import hub
from hub.features import Tensor


def create_large_dataset():
    sample_count = 30  # change this to big number to test

    # Decide schema of the dataset
    schema = {
        "image": Tensor((1920, 1080, 3), chunks=(2, 1920, 1080, 3), dtype="float64")
    }
    array = np.random.random((10, 1920, 1080, 3))

    # Write the dataset
    with hub.Dataset(
        "./data/examples/large_dataset_build",
        shape=(sample_count,),
        schema=schema,
    ) as ds:
        for i in range(len(ds) // 10):
            ds["image", i * 10 : i * 10 + 10] = i * array

    # Read the dataset
    with hub.Dataset("./data/examples/large_dataset_build") as ds:
        for i in range(len(ds) // 10):
            assert (ds["image", i * 10, 0, 0, 0].compute() / array[0, 0, 0, 0]) == i


if __name__ == "__main__":
    create_large_dataset()