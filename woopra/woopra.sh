#/bin/bash
function track() {
    ctime=`date +%s`
    duration=$((ctime - SESSION_ID))
    duration=200
    url="http://www.woopra.com/track/ce?project=osm.etsi.org&cookie=${SESSION_ID}&ce_campaign_name=${CAMPAIGN_NAME}"
    [ "$1" == "install_start" ] && url="${url}&event=install_start"
    [ "$1" == "install_end" ] && url="${url}&event=install_end&ce_duration=${duration}"
    echo "Session id: $SESSION_ID"
    echo "Duration: $duration"
    echo "URL: $url"
    wget -q -O /dev/null $url
}

function identify() {
    id=`cat /var/lib/dbus/machine-id`
    id="fdasfads"
    [ -n "$id" ] || id="Null"
    url="http://www.woopra.com/track/identify?project=osm.etsi.org&cv_id=${id}&cookie=${SESSION_ID}"
    echo "Session id: $SESSION_ID"
    echo "Visitor id: $id"
    echo "URL: $url"
    wget -q -O /dev/null $url
}

SESSION_ID=`date +%s`
CAMPAIGN_NAME="v3.0"
identify
track install_start
sleep 1
track install_end
sleep 1
SESSION_ID=`date +%s`
identify
track install_start


