# ddf_schedule
Tools for checking the planned observations of Deep Drilling Fields


# About Deep Drilling Field Scheduling

For the LSST Deep Drilling Fields, we pre-compute desirable times to schedule the observations. These pre-scheduled times account for field airmass, lunar phase, desired cadence, season length, etc.  The resulting schedule is stored as a numpy array. Some fields of note in the array

* mjd : This is the Modified Julian Date when the observation should be taken. Things like weather and downtime may can result in the observation being taken at a different time.
* mjd_tol : A tolerance factor for the MJD. If the current MJD is within mjd +/- mdj_tol, the scheduler will attempt the observation. This term is essentially here so if the desired MJD is only 2 minutes away, we go ahead and execute the DDF slightly early, rather than risk waiting an hour for a longer set of observations to compete. 
* RA, dec : The Right Ascension and Declination of the pointing. Note these values are stored as radians and may be shifted by the scheduler on-the-fly to ensure adequate spatial dithering of the DDF. Spatial dithers are typically of order 0.2 degrees. 
* rotSkyPos. rotTelPos : The rotation angle of the camera. Like the final RA,dec position, this is often set on-the-fly by the scheduler. 
* band : The bandpass for the observation.
* HA_min, HA_max : Hour angle limits for the observation. The scheduler will not attempt the observations if they are outside the HA limits.
* flush_by_mjd : This is the Modified Julian Date beyond which the scheduler will stop attempting to complete an observation. This is typically ~2 days after the mjd value.


Along with dynamically adjusting spatial and rotational dither positions, the scheduler may re-order observations while executing them, e.g., executing r-band observations in multiple DDF fields then executing z-band to decrease the total number of filter changes. 

