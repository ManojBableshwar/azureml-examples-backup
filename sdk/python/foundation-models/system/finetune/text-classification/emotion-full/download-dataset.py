# import library to parse command line arguments
import argparse, os

parser = argparse.ArgumentParser()
# add an argument to specify a dataset name to download
parser.add_argument("--dataset", type=str, default="emotion", help="dataset name")
# add an argument to specify the directory to download the dataset to
parser.add_argument(
    "--download_dir",
    type=str,
    default="./",
    help="directory to download the dataset to",
)
args = parser.parse_args()

# create the download directory if it does not exist
if not os.path.exists(args.download_dir):
    os.makedirs(args.download_dir)



# import hugging face datasets library
from datasets import load_dataset, get_dataset_split_names
from functools import partial

for split in get_dataset_split_names(args.dataset, "unsplit"):
    print(f"Loading {split} split of {args.dataset} dataset...")
    # load the split of the dataset
    dataset = load_dataset(args.dataset, "unsplit", split=split)
    # save the split of the dataset to the download directory as json lines file
    print(dataset)
    dataset.to_json(os.path.join(args.download_dir, f"emotion.jsonl"))
    # print dataset features
