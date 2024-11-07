import http.client
import json

modo_json = {
  "metadata": {
      "version": "2.0"
  },
  "content": [
    {
      "elementType": "statusList",
      "listStyle": "unpadded",
      "marginBottom": "none",
      "noItemsMessage": False,
      "showAccessoryIcons": False,
      "items": [
      ]
    }
  ]
}


# default values for all the variables
direction_link = ""
menu_link = ""
status = ""
status_message = ""
title = ""
label = ""

conn = http.client.HTTPSConnection("api.dineoncampus.com")
conn.request("GET", "/v1/locations/status?site_id=5efb645cbf31720ae5755e2d&platform=0")
resp = conn.getresponse()
body_str = resp.read().decode("utf-8")
body = json.loads(body_str)

for location in body['locations']:
    title = location['name']
    label = location['status']['label']
    if label == "open":
        status = 'available'
    elif label == "closed":
        status = 'unavailable'
    status_message = location['status']['message']
    lat = location.get('address', {}).get('lat')
    lon = location.get('address', {}).get('lon')
    direction_link = f"https://maps.google.com/?daddr={lat},{lon}&travelmode=walking"
    
    # each item will be appended to the items in modo_json
    item_json = {
              "accessoryButton": {
                  "elementType": "linkButton",
                  "borderColor": "theme:form_border_color",
                  "borderStyle": "solid",
                  "icon": "directions",
                  "iconColor": "#000000",
                  "iconPosition": "iconOnly",
                  "size": "normal",
                  "title": "Button",
                  "url": {
                      "linkType": "external",
                      "external": direction_link
                  },
                  "uuid": "248e12d9-ff5e-4b76-9455-b524601f0ac0"
              },
              "image": {
                  "backgroundColor": "#1f9245",
                  "borderRadius": "full",
                  "url": "kgo://asset_cache/resource_storage/proxy/modulepage/mobile_redesign_student-_/id_dining_copy2/e8a458ed-6368-4711-8163-ed69ca9783a1_image_url_be468e972e22b0f3516d24e78cc38e4b/1024px-HD_transparent_picture.png?_kgourl_is_resource=1"
              },
              "imageHeight": "18px",
              "imageHorizontalPosition": "left",
              "imageMargin": "xloose",
              "imageStyle": "thumbnailSmall",
              "imageVerticalPosition": "middle",
              "imageWidth": "18px",
              "status": status,
              "statusDescriptor": status_message,
              "statusText": f"<strong>{label}</strong>",
              "title": title,
              "titleFontSize": "xxlarge",
              "titleFontWeight": "bold",
              "url": {
                  "targetNewWindow": True,
                  "linkType": "external",
                  "external": menu_link
              },
              "uuid": "e8a458ed-6368-4711-8163-ed69ca9783a1"
          }
    
    modo_json['content'][0]['items'].append(item_json)

with open('data.json', 'w') as json_file:
    json.dump(modo_json, json_file, indent=4)