# cvismon

cvismo provides a terminal graph of the container images in the system.
For Docker the daemon does not even need to run as it retrieves the info from the git tree in filesystem

For instance, */var/lib/docker/image/btrfs/repositories.json* is the default location where the existing images are located, when the btrfs is used. From there it will match the hash256 with the one in */var/lib/docker/image/btrfs/imagedb/content/sha256/* to grub the value of *diff_ids*, which in turn can be found in */var/lib/docker/image/btrfs/layerdb/sha256/*. This should include the **size** file. 

## Configuration
TBD

## Usage
Need to run as root
