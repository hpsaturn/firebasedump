"""
trackdata2geojson -- utility for dump track_data to geojson format

usage:
  trackdata2geojson  <trackdata> 

"""

import json
import sys
from docopt import docopt

if __name__ == '__main__':
  arguments = docopt(__doc__, version='0.0.1')
  target = arguments["<trackdata>"]
  tracks_data = json.load(open(target, "r", encoding="utf-8"))
  print("tracks data keys: %i" % len(tracks_data))
  count = 0
  tracks = [v.get('data') for k,v in tracks_data.items()]
  points = []
  for track in tracks:
    if track != None:
      for point in track:
        if point != None:
          points.append(point)
  print("points: %i" % len(points))
  geojs={
    "type": "featurecollection",
    "features":[
        {
            "type":"feature",
            "geometry": {
                "type":"point",
                "coordinates":[d['lon'],d['lat']]
                },
            "properties":d,
            } for d in points
        ]
    }
  output_file=open("geo"+target, "w", encoding="utf-8")
  # json.dump(geojs, output_file)
  json.dump(geojs, output_file)
  output_file.close()
  