
require 'kaitai/struct/visualizer/ksy_compiler'
require 'kaitai/struct/struct'

ARGS = [ ]

module Kaitai::Struct
  class Struct
    ####################################################################
    ### This would provide a reference to the existing 'from_file'   ###
    ### function. This reference could be invoked like:              ###
    ###                                                              ###
    ###        old_from_file.bind(self).call( *args )                ###
    ###                                                              ###
    ####################################################################
    # old_from_file = singleton_class.instance_method(:from_file)
    define_singleton_method(:from_file) { |filename|
      self.new( Stream.open(filename),*ARGS.reduce([]) { |acc,hash| acc << hash['VALUE'] } )
    }
  end
end

PARSERS = { }
STRUCTS = { }

Compiler = Kaitai::Struct::Visualizer::KSYCompiler

def GET( struct, *args )
  if STRUCTS.key? struct
    STRUCTS[struct]['struct']._read unless STRUCTS[struct]['read']
    STRUCTS[struct]['read'] = true

    args.reduce( STRUCTS[struct]['struct'] ) { |acc,field|
      if acc.respond_to?(field)
        acc.send(field)
      else
        raise "#{File.basename(__FILE__)}: #{field} not found in GET"
      end
    }
  else
    raise "#{File.basename(__FILE__)}: struct '#{struct}' not available"
  end
end

newARGV = ARGV.reduce([]) { |acc,arg|
  if arg.include? "-help"
    puts <<-eos
Usage: ksv -r #{File.basename(__FILE__)} [ COMPILE:<LOADER>:<KSY-PATH> |
                           LOAD:<STRUCT>=<LOADER>:<BIN-PATH> |
                           ARG:<EXPRESSION> ... ]  ...

    COMPILE:<LOADER>:<KSY-PATH>
       load the parser specified by <KSY-PATH> and associate it with the
       <LOADER> string

    LOAD:<STRUCT>=<LOADER>:<BIN-PATH>
       use the loader associated with the <LOADER> string to read the binary
       file associated with <BIN-PATH> and associate this struct with the
       <STRUCT> string

    ARG:<EXPRESSION>
       Evaluate the <EXPRESSION> string and associate the result with an
       argument for loading a KSY file into ksv. The ordering of arguments
       is preserved. Use:

           GET( "<STRUCT>", "<FIELD-1>", "<FIELD-2>" ..., "<FIELD-N>" )

       to access <FIELD-N> within <STRUCT>. An example of this would be:

           ARG:GET("meta","desc","table","columns","column_desc")[0]

       to access the first element from an array nested within meta:

           meta.desc.table.columns.column_desc[0]

eos
  end                                           
  if arg.include? ":"
    case arg[0,arg.index(':')]
    when "COMPILE"
      action = arg[8..-1]
      if action.include? ":"
        idx = action.index(':')
        symbol = action[0,idx]
        file = action[idx+1..-1]
        if File.file?(file) && File.extname(file) == ".ksy"
          COMPILER ||= Compiler.new({ })
          main_class_name = COMPILER.compile_formats_if( [file] )
          PARSERS[symbol] = Kernel.const_get(main_class_name)
        else
          raise "#{File.basename(__FILE__)}: expected existing file with ksy extension (got #{file})"
        end
      else
        raise "#{File.basename(__FILE__)}: COMPILE arguments must be of the form COMPILE:<SYMBOL>:<FILE> (got #{arg})"
      end
    when "LOAD"
      action = arg[5..-1]
      if action.include? ":"
        idx = action.index(':')
        file = action[idx+1..-1]
        raise "{File.basename(__FILE__)}: file to be loaded does not exist (got #{file})" unless File.file?(file)
        assign = action[0,idx]
        if assign.include? "="
          idx = assign.index("=")
          symbol = assign[0,idx]
          loader = assign[idx+1..-1]
          if PARSERS.key? loader
            STRUCTS[symbol] = { "struct" => PARSERS[loader].from_file(file), "read" => false }
          else
            raise "{File.basename(__FILE__)}: the '#{loader}' loader has not yet been compiled"
          end
        else
          raise "{File.basename(__FILE__)}: load action should contain an '=' (got #{assign})"
        end
      else
        raise "#{File.basename(__FILE__)}: LOAD arguments must be of the form LOAD:<SYMBOL>=<LOADER>:<FILE> (got #{action})"
      end
    when "ARG"
      ARGS << { "ARG" => arg, "VALUE" => (eval arg[4..-1]) }
    else
      acc << arg
    end
  else
    # Not one of our arguments
    acc << arg
  end
  acc
}

###
### This silences warnings about reinitializing the ARGV constant...
### leaving verbose off gets rid of all of the constant warnings
### when importing generated Kaitai Struct parsers more than once.
### This is a problem even if it is imported indirectly.
###
original_verbose, $VERBOSE = $VERBOSE, nil
ARGV = newARGV
#$VERBOSE = original_verbose
