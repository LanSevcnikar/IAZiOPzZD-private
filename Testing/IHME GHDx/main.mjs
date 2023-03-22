import { metadata } from "./metadata.mjs";
let allCauses = metadata.data.cause;

let map_name_to_id = {};
let map_id_to_name = {};
let map_cause_to_id = {};
let map_id_to_cause = {};

// loop through all the elements of the map by key and value
for (let [key, value] of Object.entries(allCauses)) {
  map_name_to_id[value.name] = key;
  map_id_to_name[key] = value.name;
  map_cause_to_id[value.cause] = key;
  map_id_to_cause[key] = value.cause;
}

let final_map = {};

for (let [key, value] of Object.entries(allCauses)) {
  let cause = value.cause;
  let hierarchy = cause.split(".");
  if (hierarchy.length == 1) {
    final_map[cause] = {
      children: {},
    };
  } else {
    let temp_string = hierarchy[0];
    let temp_location = final_map[temp_string];
    for (let i = 1; i < hierarchy.length; i++) {
      temp_string = temp_string + "." + hierarchy[i];
      if (temp_location.children[temp_string] == undefined) {
        temp_location.children[temp_string] = {
          children: {},
        };
      }
      temp_location = temp_location.children[temp_string];
    }
  }
}

// define a recursive function to fix the map
function fixMap(map) {
    console.log("HIS");
  // if the map is empty, return
  if (Object.keys(map).length == 0) {
    return;
  }

  // loop through the map
  for (let [key, value] of Object.entries(map)) {
    // if the element is a map, check if the element has a children proprety and if so, if it is empty

    let name = map_id_to_name[map_cause_to_id[key]];
    if (name != undefined) {
      map[name] = {
        ...map[key],
        ...allCauses[map_cause_to_id[key]],
      };
      delete map[key];
    }
    if (map[name] != undefined){
      for (let [key2, value2] of Object.entries(map[name].children)) {
        fixMap(map[name].children);
      }
    }
  }

  //
}


// // call the function
fixMap(final_map);

let export_final_map = {
    ...final_map["All causes"]
}

delete final_map["All causes"]

export_final_map.children = final_map
// // dump the final map into json file
// // use import

import fs from "fs";

fs.writeFile("final_map.json", JSON.stringify(export_final_map), function (err) {
  if (err) {
    return console.log(err);
  }
  console.log("The file was saved!");
});
