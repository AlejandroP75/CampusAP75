package com.campuslands.ADN.controllers;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.campuslands.ADN.repositories.entities.Persona;
import com.campuslands.ADN.services.PersonaService;

import lombok.AllArgsConstructor;

import java.util.List;

import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;


@RestController
@RequestMapping("/personas")
@AllArgsConstructor
public class PersonaController {
    
    private final PersonaService personaService;

    @GetMapping("/")
    public ResponseEntity<List<Persona>> findAll() {
        return ResponseEntity.ok(personaService.findAll());
    }
    
    @GetMapping("/{id}")
    public ResponseEntity<Object> findById(@PathVariable Long id) {
        try {
            return ResponseEntity.ok(personaService.findById(id));
        } catch (Exception e){
            return ResponseEntity.badRequest().body(e.getMessage());
        }  
    }

    @PostMapping("/")
    public ResponseEntity<Object> save(@RequestBody Persona persona){
        try{
            if (persona.getCromosoma().length() != 20){
                return ResponseEntity.badRequest().body("El cromosoma no tiene 20 caracteres");
            } else {
                return ResponseEntity.ok(personaService.save(persona));
            }
        } catch (Exception e) {
            return ResponseEntity.badRequest().body(e.getMessage());
        }
    }

    @PutMapping("/{id}")
    public ResponseEntity<Object> update(@PathVariable Long id, @RequestBody Persona persona){
        try {
            if (persona.getCromosoma().length() != 20){
                return ResponseEntity.badRequest().body("El cromosoma no tiene 20 caracteres");
            }else{
                return ResponseEntity.ok(personaService.update(id, persona));
            }
        } catch (Exception e) {
            return ResponseEntity.badRequest().body(e.getMessage());
        }
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<Object> delete(@PathVariable Long id){
        try {
            return ResponseEntity.ok().build();
        } catch (Exception e) {
            return ResponseEntity.badRequest().body(e.getMessage());
        }
    }

    @GetMapping("/buscarCoincidencias/{cromosoma}")
    public String busqueda(@PathVariable String cromosoma){
        if(cromosoma.length() != 20){
            return "El cromosoma tiene que tener 20 caracteres";
        }else{
            return personaService.sospechoso(cromosoma);
        }

    }
}
