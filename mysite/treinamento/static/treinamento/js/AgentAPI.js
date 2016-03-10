/**
* @required JQuery $
*/
"use strict"

var AgentAPI = (function(){

    var url = "/rest/agent";
    var _buildAgentURL = function(agentId){
        return url + "/" + agentId;
    }

    return {
        getAllAgents : function(){
            return jQuery.ajax({
                url : url
            });
        },

        getAgent : function(agentId){
            return jQuery.ajax({
                url : _buildAgentURL(agentId)
            });
        },

        createAgent : function(name,lat,lon){
            var data = {}
            data.name = name
            if(lat != null)
                data.lat = lat
            if(lon != null)
                data.lon = lon
            return jQuery.ajax({
                url : url,
                method : "POST",
                data : data
            })
        },

        updateAgent : function(agentId,name,lat,lon){
            var data = {};
            data.name = name;
            if(lat != null)
                data.lat = lat;
            if(lon != null)
                data.lon = lon;
            return jQuery.ajax({
                url : _buildAgentURL(agentId),
                method : "PUT",
                data : data
            })
        },

        deleteAgent : function(agentId){
            return jQuery.ajax({
                method : "DELETE",
                url : _buildAgentURL(agentId)
            })
        }
    }
})();