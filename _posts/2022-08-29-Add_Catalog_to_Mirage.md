---
layout: post
title:  "Add Catalog to Mirage"
date:   2022-08-29
categories: cosmos_web
---

I went through how to <a href="https://ndrakos.github.io/blog/cosmos_web/Mirage/">create an image in Mirage</a>, and how to feed this through the <a href="https://ndrakos.github.io/blog/cosmos_web/JWST_Pipeline/">JWST pipeline</a>. In the current post, I'm going to add the DREaM catalog to Mirage.

## The catalog

Rather than work with the full catalog, I'm going to get this working with a truncated test catalog. I'll take all galaxies that are brighter than 20 AB mag in at least one COSMOS-Web band. This cuts the catalog down from 3e7 to 1e4 objects.

### Position

Right now the catalog is centred at (0,0). I'm going to shift the RA and Dec to be centred in the COSMOS-Web field (as described below). The field should be a small enough angle that I don't have to worry about any geometric effects, and will just simply shift the coordinates.


The COSMOS survey is centered at (J2000):
  RA +150.11916667 (10:00:28.600)
  DEC +2.20583333 (+02:12:21.00)

The COSMOS-Web field is roughly centred on this field, but tilted:

<img src="{{ site.baseurl }}/assets/plots/20220829_COSMOS-Web.png">


The DREaM catalog is 1 deg^2, where the COSMOS field is 2 deg^2, and the COSMOS-Web field is 0.6 deg^2. The lines in the plot above should be about 0.26 degs apart.

Therefore it looks like it will be fine just to centre the DREaM catalog on the centre of the COSMOS field. It should be big enough to cover the whole COSMOS-Web field.

### Saving the catalog

After reading in the DREaM catalog, I then could generate and save a catalog similar to what I outlined <a href="https://ndrakos.github.io/blog/cosmos_web/Mirage/">here</a>.

One thing to note is that the DREaM catalog has the half-light radius stored as the half-light radius in the semi-major radius, in kpc. I converted this to the circularized half-light radius, and then converted to arcsecs (based on the redshift of the galaxy).  


## Run through Mirage and JWST pipeline

Here is the same pointing as shown in the previous post, but with the bright DREaM galaxies added.

<img src="{{ site.baseurl }}/assets/plots/20220829_pipeline.png">

If I want to get it for more than one, need to loop through them (this can be easily parallelized though, if needed).

To test the final step (which really adds together different pointings), I tried running the code on the first 3 yaml files in the folder. This is slowest when it is downloading files for the cache, but much faster on subsequent runs.


For step 3 this involved creating a .asn file:

```
from jwst.pipeline import calwebb_image3
from jwst.associations import asn_from_list
from jwst.associations.lib.rules_level3_base import DMS_Level3_Base

#Make Association file
cal_files = glob(pipeline_output_dir+'/*_cal.fits')
product_name = 'cw'
myasn_object = asn_from_list.asn_from_list(cal_files, rule=DMS_Level3_Base, product_name=product_name)
filename = pipeline_output_dir+'cw_asn.json'
with open(filename, 'w') as outfile:
    name, serialized = myasn_object.dump(format='json')
    outfile.write(serialized)
```

## Final Image

Here is the image I got with the APT file I was given for one visit, and the default pipeline parameters.


<img src="{{ site.baseurl }}/assets/plots/20220829_cw-dream-1visit.png">

It seems like it only created one file, when there should have been F115W and F150W images. Maybe it combined them all together? I'll run this by the others and see what they think



## Next steps

Right now I seem to have this working! I don't really want to bother optimizing the jwst pipeline, hopefully this is enough to check and see if my generated images look reasonable.

My next steps:

1. Run Mirage on the full catalog (maybe do this on lux?)
2. Get this parallelized so I can run imaging on the whole catalog
3. Go through some of the optional arguments in Mirage, think about what I want set to these too
4. Get a star catalog and add it to the images
5. Pass along to others, see if there is any input
