# Upload TIFF pixel masks as prelabels

## Summary
The notebook uploads externally-generated segmentation masks into Centaur and sets them as prelabels
— the starting annotations labelers see and correct — on a `pixel_seg` task. Use it when your masks
come from outside Centaur, for example from your own inference pipeline, and you already have one
binary TIFF per label class per image frame.

It covers the whole flow: requesting upload URLs, uploading each mask, committing them, and attaching
them to their cases as prelabels. Masks are checked locally first, so size and channel problems
surface before anything is uploaded.

https://docs.centaurlabs.com/reference/post_masks-public-v1-generate-presigned-urls

### Before you start
You will need:

* An API key and API password for your Centaur account, and the key's permission to set answers on
  the target task — your Centaur contact can confirm this.
* A task of type `pixel_seg`, and its `project_id` and `task_id`.
* For each frame you are labeling: the `case_id`, the `frame_id` within that case, and the
  `content_id` of the asset backing that frame. The notebook explains where these come from and why
  the last two have to agree.
* One single-channel binary TIFF per label class per frame, matching the frame's pixel dimensions.

### Installation
No special installation steps required. Follow the virtual environment setup on
[the main repository page](../README.md#installation) and then follow the steps in the notebook.
